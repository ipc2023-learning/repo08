import logging
import dlplan

from termcolor import colored
from typing import List

from learner.src.asp.asp_factory import ASPFactory
from learner.src.asp.returncodes import ClingoExitCode
from learner.src.instance_data.instance_data import InstanceData
from learner.src.instance_data.instance_information import InstanceInformation
from learner.src.iteration_data.domain_feature_data_factory import DomainFeatureDataFactory
from learner.src.iteration_data.feature_valuations_factory import FeatureValuationsFactory
from learner.src.util.timer import CountDownTimer
from learner.src.util.command import create_experiment_workspace
from learner.src.util.clock import Clock
from learner.src.domain_data.domain_data import DomainData


def compute_state_b_values(booleans: List[dlplan.Boolean], numericals: List[dlplan.Numerical], instance_data: InstanceData, state: dlplan.State):
    return tuple([boolean.evaluate(state, instance_data.denotations_caches) for boolean in booleans] + [numerical.evaluate(state, instance_data.denotations_caches) > 0 for numerical in numericals])


def compute_smallest_unsolved_instance(booleans: List[dlplan.Boolean], numericals: List[dlplan.Numerical], instance_datas: List[InstanceData]):
    goal_b_values = set()
    nongoal_b_values = set()
    for instance_data in instance_datas:
        for s_idx, state in instance_data.state_space.get_states().items():
            b_values = compute_state_b_values(booleans, numericals, instance_data, state)
            separating = True
            if instance_data.is_goal(s_idx):
                goal_b_values.add(b_values)
                if b_values in nongoal_b_values:
                    separating = False
            else:
                nongoal_b_values.add(b_values)
                if b_values in goal_b_values:
                    separating = False
            if not separating:
                print("Features do not separate goals from non goals")
                print("Booleans:")
                print("State:", str(state))
                print("b_values:", b_values)
                return instance_data
    return None


def parse_features_from_answer_set(symbols, domain_data: DomainData):
    booleans = []
    numericals = []
    for symbol in symbols:
        if symbol.name == "select":
            f_idx = symbol.arguments[0].number
            if f_idx < len(domain_data.domain_feature_data.boolean_features.features_by_index):
                booleans.append(domain_data.domain_feature_data.boolean_features.features_by_index[f_idx].dlplan_feature)
            else:
                numericals.append(domain_data.domain_feature_data.numerical_features.features_by_index[f_idx - len(domain_data.domain_feature_data.boolean_features.features_by_index)].dlplan_feature)
    return booleans, numericals


def learn_goal_separating_features(config, domain_data, instance_datas, zero_cost_domain_feature_data, workspace):
    """ Learns goal separating features
    """
    clock = Clock("LEARNING")
    clock.set_start()

    booleans = []
    numericals = []
    i = 0
    selected_instance_idxs = [0]
    timer = CountDownTimer(config.timeout)
    create_experiment_workspace(workspace, rm_if_existed=False)
    while not timer.is_expired():
        logging.info(colored(f"Iteration: {i}", "red", "on_grey"))

        selected_instance_datas = [instance_datas[subproblem_idx] for subproblem_idx in selected_instance_idxs]
        for instance_data in selected_instance_datas:
            instance_data.instance_information = InstanceInformation(
                instance_data.instance_information.name,
                instance_data.instance_information.filename,
                workspace / f"iteration_{i}")
            instance_data.set_state_space(instance_data.state_space, True)
            print("     id:", instance_data.id, "name:", instance_data.instance_information.name)

        logging.info(colored("Initializing DomainFeatureData...", "blue", "on_grey"))
        domain_feature_data_factory = DomainFeatureDataFactory()
        domain_feature_data_factory.make_domain_feature_data_from_instance_datas(config, domain_data, selected_instance_datas)
        domain_feature_data_factory.statistics.print()
        #for boolean_feature in domain_data.domain_feature_data.boolean_features.features_by_index:
        #    print(boolean_feature.dlplan_feature.compute_repr())
        for zero_cost_boolean_feature in zero_cost_domain_feature_data.boolean_features.features_by_index:
            domain_data.domain_feature_data.boolean_features.add_feature(zero_cost_boolean_feature)
        for zero_cost_numerical_feature in zero_cost_domain_feature_data.numerical_features.features_by_index:
            domain_data.domain_feature_data.numerical_features.add_feature(zero_cost_numerical_feature)
        logging.info(colored("..done", "blue", "on_grey"))

        logging.info(colored("Initializing InstanceFeatureDatas...", "blue", "on_grey"))
        for instance_data in selected_instance_datas:
            instance_data.set_feature_valuations(FeatureValuationsFactory().make_feature_valuations(instance_data))
        logging.info(colored("..done", "blue", "on_grey"))

        asp_factory = ASPFactory()
        asp_factory.load_problem_file(config.asp_location / "goal-separating.lp")
        facts = []
        facts.extend(asp_factory.make_state_space_facts(domain_data, selected_instance_datas))
        facts.extend(asp_factory.make_domain_feature_data_facts(domain_data, selected_instance_datas))
        facts.extend(asp_factory.make_instance_feature_data_facts(domain_data, selected_instance_datas))

        logging.info(colored("Grounding Logic Program...", "blue", "on_grey"))
        asp_factory.ground(facts)
        logging.info(colored("..done", "blue", "on_grey"))

        logging.info(colored("Solving Logic Program...", "blue", "on_grey"))
        symbols, returncode = asp_factory.solve()
        if returncode == ClingoExitCode.UNSATISFIABLE:
            print("UNSAT")
            exit(1)
        asp_factory.print_statistics()
        logging.info(colored("..done", "blue", "on_grey"))

        logging.info("Learned the following goal separating features:")
        booleans, numericals = parse_features_from_answer_set(symbols, domain_data)
        print("\n".join([boolean.compute_repr() for boolean in booleans]))
        print("\n".join([numerical.compute_repr() for numerical in numericals]))
        assert compute_smallest_unsolved_instance(booleans, numericals, selected_instance_datas) is None

        logging.info(colored("Verifying goal separating features...", "blue", "on_grey"))
        smallest_unsolved_instance = compute_smallest_unsolved_instance(booleans, numericals, instance_datas)
        logging.info(colored("..done", "blue", "on_grey"))

        if smallest_unsolved_instance is None:
            print(colored("Features separate all goal from non-goal states!", "red", "on_grey"))
            break
        else:
            if smallest_unsolved_instance.id > max(selected_instance_idxs):
                selected_instance_idxs = [smallest_unsolved_instance.id]
            else:
                selected_instance_idxs.append(smallest_unsolved_instance.id)
            print("Smallest unsolved instance:", smallest_unsolved_instance.id)
            print("Selected instances:", selected_instance_idxs)
        i += 1
    clock.set_accumulate()
    return booleans, numericals

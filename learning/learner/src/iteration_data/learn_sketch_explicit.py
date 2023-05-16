import logging
import dlplan

from termcolor import colored
from typing import List

from learner.src.asp.asp_factory import ASPFactory
from learner.src.asp.returncodes import ClingoExitCode
from learner.src.instance_data.instance_data import InstanceData
from learner.src.instance_data.instance_information import InstanceInformation
from learner.src.instance_data.tuple_graph_factory import TupleGraphFactory
from learner.src.iteration_data.domain_feature_data import DomainFeatureData
from learner.src.iteration_data.domain_feature_data_factory import DomainFeatureDataFactory
from learner.src.iteration_data.feature_valuations_factory import FeatureValuationsFactory
from learner.src.iteration_data.dlplan_policy_factory import ExplicitDlplanPolicyFactory
from learner.src.iteration_data.sketch import Sketch
from learner.src.iteration_data.state_pair_equivalence_factory import StatePairEquivalenceFactory
from learner.src.iteration_data.tuple_graph_equivalence_factory import TupleGraphEquivalenceFactory
from learner.src.iteration_data.tuple_graph_equivalence_minimizer import TupleGraphEquivalenceMinimizer
from learner.src.util.timer import CountDownTimer
from learner.src.util.command import create_experiment_workspace
from learner.src.util.clock import Clock
from learner.src.iteration_data.learning_statistics import LearningStatistics


def compute_smallest_unsolved_instance(config, sketch: Sketch, instance_datas: List[InstanceData]):
    for instance_data in instance_datas:
        if not sketch.solves(config, instance_data):
            return instance_data
    return None


def learn_sketch(config, domain_data, instance_datas, zero_cost_domain_feature_data: DomainFeatureData, workspace, width: int):
    """ Learns a sketch that solves all given instances while first computing required data.
    """
    clock = Clock("LEARNING")
    clock.set_start()

    logging.info(colored("Initializing TupleGraphs...", "blue", "on_grey"))
    tuple_graph_factory = TupleGraphFactory(width)
    for instance_data in instance_datas:
        instance_data.set_tuple_graphs(tuple_graph_factory.make_tuple_graphs(instance_data))
    logging.info(colored("..done", "blue", "on_grey"))

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
            print("     id:", instance_data.id, "name:", instance_data.instance_information.name, "initial_states:", instance_data.initial_s_idxs)

        logging.info(colored("Initializing DomainFeatureData...", "blue", "on_grey"))
        domain_feature_data_factory = DomainFeatureDataFactory()
        domain_feature_data_factory.make_domain_feature_data_from_instance_datas(config, domain_data, selected_instance_datas)
        domain_feature_data_factory.statistics.print()
        for zero_cost_boolean_feature in zero_cost_domain_feature_data.boolean_features.f_idx_to_feature.values():
            domain_data.domain_feature_data.boolean_features.add_feature(zero_cost_boolean_feature)
        for zero_cost_numerical_feature in zero_cost_domain_feature_data.numerical_features.f_idx_to_feature.values():
            domain_data.domain_feature_data.numerical_features.add_feature(zero_cost_numerical_feature)
        logging.info(colored("..done", "blue", "on_grey"))

        logging.info(colored("Initializing InstanceFeatureDatas...", "blue", "on_grey"))
        for instance_data in selected_instance_datas:
            state_feature_valuations, boolean_feature_valuations, numerical_feature_valuations = FeatureValuationsFactory().make_feature_valuations(instance_data)
            instance_data.set_feature_valuations(state_feature_valuations)
            instance_data.boolean_feature_valuations = boolean_feature_valuations
            instance_data.numerical_feature_valuations = numerical_feature_valuations
        logging.info(colored("..done", "blue", "on_grey"))

        logging.info(colored("Initializing StatePairEquivalenceDatas...", "blue", "on_grey"))
        state_pair_equivalence_factory = StatePairEquivalenceFactory()
        state_pair_equivalence_factory.make_state_pair_equivalences(domain_data, selected_instance_datas)
        logging.info(colored("..done", "blue", "on_grey"))

        logging.info(colored("Initializing TupleGraphEquivalences...", "blue", "on_grey"))
        tuple_graph_equivalence_factory = TupleGraphEquivalenceFactory()
        tuple_graph_equivalence_factory.make_tuple_graph_equivalences(domain_data, selected_instance_datas)
        tuple_graph_equivalence_factory.statistics.print()
        logging.info(colored("..done", "blue", "on_grey"))

        logging.info(colored("Initializing TupleGraphEquivalenceMinimizer...", "blue", "on_grey"))
        tuple_graph_equivalence_minimizer = TupleGraphEquivalenceMinimizer()
        for instance_data in selected_instance_datas:
            tuple_graph_equivalence_minimizer.minimize(instance_data)
        logging.info(colored("..done", "blue", "on_grey"))

        logging.info(colored("Iteration data preprocessing summary:", "yellow", "on_grey"))
        domain_feature_data_factory.statistics.print()
        state_pair_equivalence_factory.statistics.print()
        tuple_graph_equivalence_factory.statistics.print()
        tuple_graph_equivalence_minimizer.statistics.print()

        asp_factory = ASPFactory(max_num_rules=config.max_num_rules)
        asp_factory.load_problem_file(config.asp_location / config.asp_name)
        facts = asp_factory.make_facts(domain_data, selected_instance_datas)
        logging.info(colored("Grounding Logic Program...", "blue", "on_grey"))
        asp_factory.ground(facts)
        logging.info(colored("..done", "blue", "on_grey"))

        logging.info(colored("Solving Logic Program...", "blue", "on_grey"))
        symbols, returncode = asp_factory.solve()
        if returncode == ClingoExitCode.UNSATISFIABLE:
            print("UNSAT")
            return None, None, None
        asp_factory.print_statistics()
        logging.info(colored("..done", "blue", "on_grey"))

        dlplan_policy = ExplicitDlplanPolicyFactory().make_dlplan_policy_from_answer_set(symbols, domain_data)
        sketch = Sketch(dlplan_policy, width)
        logging.info("Learned the following sketch:")
        sketch.print()
        assert compute_smallest_unsolved_instance(config, sketch, selected_instance_datas) is None

        logging.info(colored("Verifying learned sketch...", "blue", "on_grey"))
        smallest_unsolved_instance = compute_smallest_unsolved_instance(config, sketch, instance_datas)
        logging.info(colored("..done", "blue", "on_grey"))

        if smallest_unsolved_instance is None:
            print(colored("Sketch solves all instances!", "red", "on_grey"))
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

    logging.info(colored("Summary:", "green", "on_grey"))
    learning_statistics = LearningStatistics(
        num_training_instances=len(instance_datas),
        num_selected_training_instances=len(selected_instance_datas),
        num_states_in_selected_training_instances=sum([len(instance_data.state_space.get_states()) for instance_data in selected_instance_datas]),
        num_features_in_pool=len(domain_data.domain_feature_data.boolean_features.f_idx_to_feature) + len(domain_data.domain_feature_data.numerical_features.f_idx_to_feature),
        num_cpu_seconds=clock.accumulated,
        num_peak_memory_mb=clock.used_memory())
    learning_statistics.print()
    print("Resulting sketch:")
    sketch.print()
    print("Resulting sketch minimized:")
    sketch_minimized = Sketch(dlplan.PolicyMinimizer().minimize(sketch.dlplan_policy, domain_data.policy_builder), sketch.width)
    sketch_minimized.print()
    return sketch, sketch_minimized, learning_statistics

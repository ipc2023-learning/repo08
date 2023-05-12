import dlplan
import math

from collections import defaultdict, deque
from typing import  List, Dict

from learner.src.instance_data.instance_information import InstanceInformation
from learner.src.instance_data.instance_data import InstanceData
from learner.src.instance_data.tuple_graph_factory import TupleGraphFactory
from learner.src.iteration_data.sketch import Sketch


class SubproblemInstanceDataFactory:
    def make_subproblems(self, config, instance_datas: List[InstanceData], sketch: Sketch, rule: dlplan.Rule, width: int):
        features = list(sketch.booleans) + list(sketch.numericals)
        subproblem_instance_datas = []
        for instance_data in instance_datas:
            state_space = instance_data.state_space
            covered_relevant_s_idxs = set()
            # 1. Group relevant states with same feature valuation together
            feature_valuation_to_relevant_s_idxs = defaultdict(set)
            for s_idx in sketch.compute_r_reachable_states(instance_data):
                if instance_data.is_goal(s_idx):
                    # Definition of relevant states: state must be nongoal.
                    continue
                if not rule.evaluate_conditions(state_space.get_states()[s_idx], instance_data.denotations_caches):
                    # Definition of relevant states: state must satisfy condition of rule
                    continue
                state = state_space.get_states()[s_idx]
                feature_valuation = tuple([feature.evaluate(state) for feature in features])
                feature_valuation_to_relevant_s_idxs[feature_valuation].add(s_idx)
            # 2. Group subgoal states with same feature valuation together
            feature_valuation_to_target_s_idxs = defaultdict(set)
            for s_idx, state in instance_data.state_space.get_states().items():
                feature_valuation = tuple([feature.evaluate(state) for feature in features])
                feature_valuation_to_target_s_idxs[feature_valuation].add(s_idx)
            # 3. Compute goals for each group.
            for _, relevant_s_idxs in feature_valuation_to_relevant_s_idxs.items():
                # 3.2. Compute set of goal states, i.e., all s' such that (f(s), f(s')) satisfies E.
                goal_s_idxs = set()
                for _, target_s_idxs in feature_valuation_to_target_s_idxs.items():
                    if not rule.evaluate_effects(state_space.get_states()[next(iter(relevant_s_idxs))], state_space.get_states()[next(iter(target_s_idxs))], instance_data.denotations_caches):
                        continue
                    goal_s_idxs.update(target_s_idxs)
                if not goal_s_idxs:
                    continue

                # 4. Compute goal distances of all relevant states.
                old_goal_distances = instance_data.goal_distances
                old_goal_state_indices = instance_data.state_space.get_goal_state_indices()
                instance_data.state_space.set_goal_state_indices(goal_s_idxs)
                instance_data.goal_distances = instance_data.state_space.compute_goal_distances()
                # 4. Sort relevant states by distance and then instantiate the subproblem
                sorted_relevant_s_idxs = sorted(relevant_s_idxs, key=lambda x : -instance_data.goal_distances.get(x, math.inf))
                for initial_s_idx in sorted_relevant_s_idxs:
                    if initial_s_idx in covered_relevant_s_idxs:
                        continue
                    name = f"{instance_data.instance_information.name}-{initial_s_idx}"

                    # 5. Compute states and initial states covered by these states.
                    initial_state_distances = instance_data.state_space.compute_distances({initial_s_idx}, True, True)
                    # All I-reachable states make it into the instance
                    state_indices = set(initial_state_distances.keys())
                    # Extend initial states by uncovered initial states
                    subproblem_initial_s_idxs = {initial_s_idx,}
                    covered_relevant_s_idxs.add(initial_s_idx)
                    for initial_s_prime_idx in relevant_s_idxs:
                        if initial_s_prime_idx not in state_indices:
                            # State is not part of the subproblem
                            continue
                        elif initial_s_prime_idx in covered_relevant_s_idxs:
                            # Dont cover initial states multiple times
                            continue
                        subproblem_initial_s_idxs.add(initial_s_prime_idx)
                        covered_relevant_s_idxs.add(initial_s_prime_idx)

                    # 6. Instantiate subproblem for initial state and subgoals.
                    subproblem_state_space = dlplan.StateSpace(
                        instance_data.state_space,
                        state_indices)
                    subproblem_state_space.set_initial_state_index(initial_s_idx)
                    # Goal states were overapproximated and must be restricted to those that are I-reachable
                    subproblem_state_space.set_goal_state_indices(goal_s_idxs.intersection(state_indices))
                    subproblem_goal_distances = subproblem_state_space.compute_goal_distances()
                    subproblem_instance_information = InstanceInformation(
                        name,
                        instance_data.instance_information.filename,
                        instance_data.instance_information.workspace / f"rule_{rule.get_index()}" / name)
                    subproblem_instance_data = InstanceData(
                        len(subproblem_instance_datas),
                        instance_data.domain_data,
                        instance_data.denotations_caches,
                        subproblem_instance_information)
                    subproblem_instance_data.set_state_space(subproblem_state_space)
                    subproblem_instance_data.set_goal_distances(subproblem_goal_distances)
                    subproblem_instance_data.initial_s_idxs = subproblem_initial_s_idxs
                    if not subproblem_instance_data.is_alive(initial_s_idx):
                        continue
                    assert all([subproblem_instance_data.is_alive(initial_s_idx) for initial_s_idx in subproblem_instance_data.initial_s_idxs])
                    # 2.2.1. Recompute tuple graph for restricted state space
                    subproblem_instance_data.set_tuple_graphs(TupleGraphFactory(width).make_tuple_graphs(subproblem_instance_data))
                    subproblem_instance_datas.append(subproblem_instance_data)
                instance_data.state_space.set_goal_state_indices(old_goal_state_indices)
                instance_data.goal_distances = old_goal_distances
        subproblem_instance_datas = sorted(subproblem_instance_datas, key=lambda x : len(x.state_space.get_states()))
        for instance_idx, instance_data in enumerate(subproblem_instance_datas):
            instance_data.id = instance_idx
            instance_data.state_space.get_instance_info().set_index(instance_idx)
        print("Number of problems:", len(instance_datas))
        print("Number of subproblems:", len(subproblem_instance_datas))
        print("Highest number of states in problem:", max([len(instance_data.state_space.get_states()) for instance_data in instance_datas]))
        print("Highest number of states in subproblem:", max([len(instance_data.state_space.get_states()) for instance_data in subproblem_instance_datas]))
        return subproblem_instance_datas


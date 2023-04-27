#! /usr/bin/env python3
import re
import argparse
import subprocess
import os
from pathlib import Path

"""Example callstring

inner_node_search(child_searches=[
    inner_node_search(child_searches=[
        inner_node_search(child_searches=[
            leaf_node_search(goal_test=sketch_subgoal(filename=/home/dominik/projects/code/h-policy-learner/learning/learner/workspace_default/output/hierarchical_sketch/rule_0/rule_1/rule_1/rule.txt)),
            leaf_node_search(goal_test=sketch_subgoal(filename=/home/dominik/projects/code/h-policy-learner/learning/learner/workspace_default/output/hierarchical_sketch/rule_0/rule_1/rule_0/rule.txt)),
        ], goal_test=sketch_subgoal(filename=/home/dominik/projects/code/h-policy-learner/learning/learner/workspace_default/output/hierarchical_sketch/rule_0/rule_1/rule.txt)),
        inner_node_search(child_searches=[
            leaf_node_search(goal_test=sketch_subgoal(filename=/home/dominik/projects/code/h-policy-learner/learning/learner/workspace_default/output/hierarchical_sketch/rule_0/rule_0/rule_1/rule.txt)),
            leaf_node_search(goal_test=sketch_subgoal(filename=/home/dominik/projects/code/h-policy-learner/learning/learner/workspace_default/output/hierarchical_sketch/rule_0/rule_0/rule_0/rule.txt)),
        ], goal_test=sketch_subgoal(filename=/home/dominik/projects/code/h-policy-learner/learning/learner/workspace_default/output/hierarchical_sketch/rule_0/rule_0/rule.txt)),
    ], goal_test=sketch_subgoal(filename=/home/dominik/projects/code/h-policy-learner/learning/learner/workspace_default/output/hierarchical_sketch/rule_0/rule.txt)),
], goal_test=top_goal())
"""

def make_callstring(path: Path):
    subpaths = []
    for subpath in path.iterdir():
        if subpath.is_dir():
            subpaths.append(subpath)

    ss = "inner_node_search(child_searches=["
    for subpath in subpaths:
        ss += make_callstring_rec(subpath) + ","
    ss += f"], goal_test=top_goal())"
    return ss


def make_callstring_rec(path: Path):
    subpaths = []
    rule_file = None
    for subpath in path.iterdir():
        if subpath.is_dir():
            subpaths.append(subpath)
        elif subpath.is_file():
            if subpath.name == "rule.txt":
                rule_file = subpath.name
    # Inductive case: apply children until reaching goal
    if subpaths:
        ss = "inner_node_search(child_searches=["
        for subpath in subpaths:
            ss += make_callstring_rec(subpath) + ","
        ss += f"], goal_test=sketch_subgoal(filename={str(path / rule_file)}))"
        return ss
    # Base case: apply single action
    elif rule_file is not None:
        return f"leaf_node_search(goal_test=sketch_subgoal(filename={str(path / rule_file)}))"
    else:
        raise Exception()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Hierarchical Serialized Iterated Width With Sketches (HSIWR) Algorithm')
    parser.add_argument("--fd_file", type=str, default="./fast-downward.py")
    parser.add_argument("--domain_file", type=str, required=True)
    parser.add_argument("--instance_file", type=str, required=True)
    parser.add_argument("--hierarchical_sketch_dir", type=str, required=True)
    parser.add_argument("--plan_file", type=str, required=True)
    args = parser.parse_args()
    search_string = make_callstring(Path(args.hierarchical_sketch_dir).resolve())
    print(search_string)
    command = [
        Path(args.fd_file).resolve(),
        "--keep-sas-file",
        "--plan-file",
        Path(args.plan_file).resolve(),
        Path(args.domain_file).resolve(),
        Path(args.instance_file).resolve(),
        "--translate-options",
        "--dump-static-predicates",
        "--dump-predicates",
        "--dump-constants",
        "--dump-static-atoms",
        "--dump-goal-atoms",
        "--search-options",
        "--search",
        search_string]
    print(f'Executing "{" ".join(map(str, command))}"')
    subprocess.run(command)

# ./hsiwr.py --domain_file ../../../h-policy-learner/learning/benchmarks/gripper/domain.pddl --instance_file ../../../h-policy-learner/learning/benchmarks/gripper/instances/p-5-0.pddl --hierarchical_sketch_dir ../../../h-policy-learner/learning/learner/workspace_default/output/hierarchical_sketch/ --plan_file plan.txt
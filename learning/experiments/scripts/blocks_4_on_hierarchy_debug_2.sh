#!/bin/bash
#
#SBATCH -J blocks_4_on_hierarchy_2
#SBATCH -t 7-00:00:00
#SBATCH -C thin --exclusive
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=dominik.drexler@liu.se

DOMAIN="${PWD}/../../benchmarks/blocks_4_on/domain.pddl"
TASK_DIR="${PWD}/../../benchmarks/blocks_4_on/instances"
PIPELINE=hierarchy
WIDTH=2
CONCEPT_COMPLEXITY=9
ROLE_COMPLEXITY=9
BOOLEAN_COMPLEXITY=9
COUNT_NUMERICAL_COMPLEXITY=9
DISTANCE_NUMERICAL_COMPLEXITY=9
WORKSPACE="${PWD}/workspace/blocks_4_on_hierarchy_debug_${WIDTH}_${CONCEPT_COMPLEXITY}_${ROLE_COMPLEXITY}_${BOOLEAN_COMPLEXITY}_${COUNT_NUMERICAL_COMPLEXITY}_${DISTANCE_NUMERICAL_COMPLEXITY}"
RUN_ERR="${WORKSPACE}/run.err"
RUN_LOG="${WORKSPACE}/run.log"

# Run a single task in the foreground.
rm -rf ${WORKSPACE}
mkdir -p ${WORKSPACE}
./../../learner/main.py --domain ${DOMAIN} --task_dir ${TASK_DIR} --workspace ${WORKSPACE} --pipeline ${PIPELINE} -w ${WIDTH} -cc ${CONCEPT_COMPLEXITY} -rc ${ROLE_COMPLEXITY} -bc ${BOOLEAN_COMPLEXITY} -ncc ${COUNT_NUMERICAL_COMPLEXITY} -ndc ${DISTANCE_NUMERICAL_COMPLEXITY} --exp_id blocks_4:hierarchy_on_debug 2> ${RUN_ERR} 1> ${RUN_LOG}

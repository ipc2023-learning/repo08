#!/bin/bash

DOMAIN="${PWD}/../../benchmarks/miconic/domain-with-fix.pddl"
TASK_DIR="${PWD}/../../benchmarks/miconic/instances"
PIPELINE=$1
WIDTH=$2
CONCEPT_COMPLEXITY=9
ROLE_COMPLEXITY=9
BOOLEAN_COMPLEXITY=9
COUNT_NUMERICAL_COMPLEXITY=9
DISTANCE_NUMERICAL_COMPLEXITY=9
WORKSPACE="${PWD}/workspace/miconic_${PIPELINE}_${WIDTH}_${CONCEPT_COMPLEXITY}_${ROLE_COMPLEXITY}_${BOOLEAN_COMPLEXITY}_${COUNT_NUMERICAL_COMPLEXITY}_${DISTANCE_NUMERICAL_COMPLEXITY}"

./runner.sh $DOMAIN $TASK_DIR $WORKSPACE $PIPELINE $WIDTH $CONCEPT_COMPLEXITY $ROLE_COMPLEXITY $BOOLEAN_COMPLEXITY $COUNT_NUMERICAL_COMPLEXITY $DISTANCE_NUMERICAL_COMPLEXITY

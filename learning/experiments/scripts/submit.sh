#!/bin/bash

# e.g. dfsplan=${PARTITION}
PARTITION=$1
PIPELINE=$2

# We timeout in blocks_3_general
# sbatch -A ${PARTITION} blocks_3_general_${PIPELINE}_0.sh
# sbatch -A ${PARTITION} blocks_3_general_${PIPELINE}_1.sh
# sbatch -A ${PARTITION} blocks_3_general_${PIPELINE}_2.sh

# We timout in blocks_4_general
# sbatch -A ${PARTITION} blocks_4_general_${PIPELINE}_0.sh
# sbatch -A ${PARTITION} blocks_4_general_${PIPELINE}_1.sh
# sbatch -A ${PARTITION} blocks_4_general_${PIPELINE}_2.sh

sbatch -A ${PARTITION} blocks_4_clear_${PIPELINE}_0.sh
sbatch -A ${PARTITION} blocks_4_clear_${PIPELINE}_1.sh
sbatch -A ${PARTITION} blocks_4_clear_${PIPELINE}_2.sh

sbatch -A ${PARTITION} blocks_4_on_${PIPELINE}_0.sh
sbatch -A ${PARTITION} blocks_4_on_${PIPELINE}_1.sh
sbatch -A ${PARTITION} blocks_4_on_${PIPELINE}_2.sh

# We timout in childsnack
# sbatch -A ${PARTITION} childsnack_${PIPELINE}_0.sh  does not exist over C2 features
# sbatch -A ${PARTITION} childsnack_${PIPELINE}_1.sh
# sbatch -A ${PARTITION} childsnack_${PIPELINE}_2.sh

sbatch -A ${PARTITION} delivery_${PIPELINE}_0.sh
sbatch -A ${PARTITION} delivery_${PIPELINE}_1.sh
sbatch -A ${PARTITION} delivery_${PIPELINE}_2.sh

# We timeout on grid
# sbatch -A ${PARTITION} grid_${PIPELINE}_0.sh
# sbatch -A ${PARTITION} grid_${PIPELINE}_1.sh
# sbatch -A ${PARTITION} grid_${PIPELINE}_2.sh

sbatch -A ${PARTITION} gripper_${PIPELINE}_0.sh
sbatch -A ${PARTITION} gripper_${PIPELINE}_1.sh
sbatch -A ${PARTITION} gripper_${PIPELINE}_2.sh

sbatch -A ${PARTITION} miconic_${PIPELINE}_0.sh
sbatch -A ${PARTITION} miconic_${PIPELINE}_1.sh
sbatch -A ${PARTITION} miconic_${PIPELINE}_2.sh

sbatch -A ${PARTITION} reward_${PIPELINE}_0.sh
sbatch -A ${PARTITION} reward_${PIPELINE}_1.sh
sbatch -A ${PARTITION} reward_${PIPELINE}_2.sh

sbatch -A ${PARTITION} spanner_${PIPELINE}_0.sh
sbatch -A ${PARTITION} spanner_${PIPELINE}_1.sh
sbatch -A ${PARTITION} spanner_${PIPELINE}_2.sh

sbatch -A ${PARTITION} visitall_${PIPELINE}_0.sh
sbatch -A ${PARTITION} visitall_${PIPELINE}_1.sh
sbatch -A ${PARTITION} visitall_${PIPELINE}_2.sh

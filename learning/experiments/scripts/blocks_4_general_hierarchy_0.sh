#!/bin/bash
#
#SBATCH -J blocks_4_general_hierarchy_0
#SBATCH -t 7-00:00:00
#SBATCH -C thin --exclusive
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=dominik.drexler@liu.se

bash ./blocks_4_general.sh hierarchy 0

#!/bin/bash
#
#SBATCH -J blocks_4_on_hierarchy_2
#SBATCH -t 7-00:00:00
#SBATCH -C thin --exclusive
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=dominik.drexler@liu.se

bash ./blocks_4_on.sh hierarchy 2

#!/bin/bash
#
#SBATCH -J grid_hierarchy_1
#SBATCH -t 7-00:00:00
#SBATCH -C thin --exclusive
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=dominik.drexler@liu.se

bash ./grid.sh hierarchy 1

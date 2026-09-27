#!/bin/bash
#SBATCH --job-name=marta_xrepo_prep
#SBATCH --account=f202407648iacdcf2x
#SBATCH --partition=dev-x86
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=04:00:00
#SBATCH --output=logs/xrepo_prepare_%j.out
set -euo pipefail
BASE=${MARTA_CLUSTER_BASE:-/projects/F202407648IACDCF2/mario}
bash "$BASE/MARTA/deucalion/setup_xrepotest.sh"

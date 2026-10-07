#!/bin/bash
#SBATCH --job-name=xrepo_mut_diag
#SBATCH --account=f202407648iacdcf2x
#SBATCH --partition=dev-x86
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=02:00:00
#SBATCH --output=logs/xrepo_mutation_diag_%j.out
set -euo pipefail
BASE=${MARTA_CLUSTER_BASE:-/projects/F202407648IACDCF2/mario}
CODE=${MARTA_CLUSTER_CODE:-$BASE/MARTA-evaluation}
XROOT="$BASE/xrepotest"
: "${XREPO_RUN:?Set the frozen source experiment}"
[[ "$XREPO_RUN" =~ ^[a-zA-Z0-9][a-zA-Z0-9_-]*$ ]] || exit 2
RUN="$XROOT/runs/$XREPO_RUN"
OUT="$RUN/diagnostics/mutation_$SLURM_JOB_ID"
mkdir -p "$OUT/home"
GOMAXPROCS=4 singularity exec --cleanenv --home "$OUT/home:/home/marta"     --bind "$CODE:/opt/marta:ro" --bind "$XROOT:/data/xrepo"     --env PYTHONPATH=/app:/opt/marta --env PYTHONUNBUFFERED=1 --env GOMAXPROCS=4     "$XROOT/repaired-v2.sif" python3 -B /opt/marta/deucalion/xrepotest_mutation_diagnostic.py     --generation "/data/xrepo/runs/$XREPO_RUN/generation"     --output "/data/xrepo/runs/$XREPO_RUN/diagnostics/mutation_$SLURM_JOB_ID/results"     --ids 155 220 4 416

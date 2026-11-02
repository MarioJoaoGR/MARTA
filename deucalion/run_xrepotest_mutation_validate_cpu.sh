#!/bin/bash
#SBATCH --job-name=xrepo_mut_validate
#SBATCH --account=f202407648iacdcf2x
#SBATCH --partition=dev-x86
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=02:00:00
#SBATCH --output=logs/xrepo_mutation_validate_%j.out
set -euo pipefail
BASE=${MARTA_CLUSTER_BASE:-/projects/F202407648IACDCF2/mario}
CODE=${MARTA_CLUSTER_CODE:-$BASE/MARTA-evaluation}
XROOT="$BASE/xrepotest"
RUN="$XROOT/runs/qwen36_35b_thinking_bundle_loading_v4"
OUT="$RUN/diagnostics/mutation_validate_$SLURM_JOB_ID"
mkdir -p "$OUT/home"
# Freeze all benchmark inputs read-only. Only diagnostic copies/output are writable.
GOMAXPROCS=4 singularity exec --cleanenv \
    --home "$OUT/home:/home/marta" \
    --bind "$CODE:/opt/marta:ro" --bind "$XROOT:/data/xrepo:ro" \
    --bind "$OUT:/data/diagnostic" \
    --env PYTHONPATH=/app:/opt/marta --env PYTHONUNBUFFERED=1 --env GOMAXPROCS=4 \
    "$XROOT/repaired-v2.sif" python3 -B -m deucalion.xrepotest_mutation_validate \
    --output /data/diagnostic/results \
    --generation /data/xrepo/runs/qwen36_35b_thinking_bundle_loading_v4/generation \
    --core /data/xrepo/runs/qwen36_35b_thinking_bundle_loading_v4/evaluation

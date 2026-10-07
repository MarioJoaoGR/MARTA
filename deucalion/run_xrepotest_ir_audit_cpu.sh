#!/bin/bash
#SBATCH --job-name=xrepo_ir_audit
#SBATCH --account=f202407648iacdcf2x
#SBATCH --partition=dev-x86
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --time=00:30:00
#SBATCH --output=logs/xrepo_ir_audit_%j.out
set -euo pipefail
BASE=${MARTA_CLUSTER_BASE:-/projects/F202407648IACDCF2/mario}
CODE=${MARTA_CLUSTER_CODE:-$BASE/MARTA-evaluation}
XROOT="$BASE/xrepotest"
: "${XREPO_RUN:?Set the completed source experiment}"
[[ "$XREPO_RUN" =~ ^[a-zA-Z0-9][a-zA-Z0-9_-]*$ ]] || exit 2
OUT="$XROOT/runs/$XREPO_RUN/diagnostics/ir_$SLURM_JOB_ID"
mkdir -p "$OUT/home"
GOMAXPROCS=2 singularity exec --cleanenv \
  --home "$OUT/home:/home/marta" \
  --bind "$CODE:/opt/marta:ro" --bind "$XROOT:/data/xrepo:ro" \
  --bind "$OUT:/data/ir-audit" \
  --env PYTHONPATH=/app:/opt/marta --env PYTHONUNBUFFERED=1 --env GOMAXPROCS=2 \
  "$XROOT/repaired-v2.sif" python3 -B /opt/marta/deucalion/xrepotest_ir_audit.py \
  --generation "/data/xrepo/runs/$XREPO_RUN/generation" \
  --evaluation "/data/xrepo/runs/$XREPO_RUN/evaluation" \
  --output /data/ir-audit/report.json

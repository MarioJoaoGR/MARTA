#!/bin/bash
#SBATCH --job-name=marta_xrepo_load
#SBATCH --account=f202407648iacdcf2x
#SBATCH --partition=dev-x86
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=02:00:00
#SBATCH --output=logs/xrepo_loading_%j.out
set -euo pipefail
BASE=${MARTA_CLUSTER_BASE:-/projects/F202407648IACDCF2/mario}
XROOT="$BASE/xrepotest"
mkdir -p "$XROOT/reports" "$XROOT/home"
GOMAXPROCS=4 singularity exec --cleanenv --home "$XROOT/home:/home/marta" \
    --bind "$BASE/MARTA:/opt/marta:ro" --bind "$XROOT:/data/xrepo" \
    --env PYTHONPATH=/opt/marta --env PYTHONUNBUFFERED=1 --env GOMAXPROCS=4 \
    "$XROOT/repaired-v2.sif" python3 -B -m benchmark.xrepotest.environment.verify_loading \
    --report /data/xrepo/reports/loading-diagnostics.json
singularity exec --cleanenv --home "$XROOT/home:/home/marta" \
    --bind "$BASE/MARTA:/opt/marta:ro" --bind "$XROOT:/data/xrepo" \
    --env PYTHONPATH=/opt/marta "$XROOT/repaired-v2.sif" \
    python3 -B -m benchmark.xrepotest.cluster --root /data/xrepo --require-loading

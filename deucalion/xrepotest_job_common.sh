#!/bin/bash
# Sourced by the two Slurm jobs. All writable state stays in mario/xrepotest.
set -euo pipefail
BASE=${MARTA_CLUSTER_BASE:-/projects/F202407648IACDCF2/mario}
CODE="$BASE/MARTA"
XROOT="$BASE/xrepotest"
IMAGE="$XROOT/repaired-v2.sif"
: "${XREPO_RUN:?Set an explicit new experiment name in XREPO_RUN}"
[[ "$XREPO_RUN" =~ ^[a-zA-Z0-9][a-zA-Z0-9_-]*$ ]] || { echo "Invalid XREPO_RUN"; exit 2; }
RUN="$XROOT/runs/$XREPO_RUN"
mkdir -p "$RUN/logs" "$RUN/home" "$RUN/work" "$RUN/metadata"
export GOMAXPROCS=4
export SINGULARITY_CACHEDIR="$XROOT/downloads/cache"
export SINGULARITY_TMPDIR="$XROOT/tmp"
export PYTHONUNBUFFERED=1
CONTAINER=(singularity exec --cleanenv --home "$RUN/home:/home/marta"
    --bind "$CODE:/opt/marta:ro" --bind "$XROOT:/data/xrepo"
    --env PYTHONPATH=/app:/opt/marta --env PYTHONUNBUFFERED=1
    --env "SLURM_JOB_ID=$SLURM_JOB_ID"
    --env OMP_NUM_THREADS=4 --env OPENBLAS_NUM_THREADS=4)
# No legacy results or prepared projects are mounted.
"${CONTAINER[@]}" "$IMAGE" python3 -B -m benchmark.xrepotest.cluster --root /data/xrepo
STEP_PID=""
OLLAMA_PID=""
cleanup() {
    if [ -n "$STEP_PID" ]; then kill "$STEP_PID" 2>/dev/null || true; fi
    if [ -n "$OLLAMA_PID" ]; then kill "$OLLAMA_PID" 2>/dev/null || true; fi
}
trap cleanup EXIT
trap 'exit 143' TERM INT
# Only the Slurm advance walltime signal chains; cancellation does not resubmit.
continue_at_walltime() {
    trap '' USR1
    sbatch --parsable --dependency="afterany:$SLURM_JOB_ID" --export=ALL "$CONTINUATION"
    exit 143
}
trap continue_at_walltime USR1

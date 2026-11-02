#!/bin/bash
#SBATCH --job-name=xrepo_core_eval
#SBATCH --account=f202407648iacdcf2x
#SBATCH --partition=dev-x86
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=02:00:00
#SBATCH --output=logs/xrepo_core_evaluate_%j.out
#SBATCH --signal=B:USR1@120
set -euo pipefail
BASE=${MARTA_CLUSTER_BASE:-/projects/F202407648IACDCF2/mario}
export MARTA_CLUSTER_CODE=${MARTA_CLUSTER_CODE:-$BASE/MARTA-evaluation}
export XREPO_RUN
source "$MARTA_CLUSTER_CODE/deucalion/xrepotest_job_common.sh"
CONTINUATION="$CODE/deucalion/run_xrepotest_core_evaluate_cpu.sh"
test -s "$RUN/generation/processed.jsonl" || { echo "Generation export is not complete"; exit 2; }
EXTRA=()
if [[ -n "${XREPO_TASK_IDS:-}" ]]; then
    [[ "$XREPO_TASK_IDS" == /data/xrepo/* && -f "$XROOT/${XREPO_TASK_IDS#/data/xrepo/}" ]] || exit 2
    EXTRA+=(--task-ids "$XREPO_TASK_IDS")
fi
export XREPO_TASK_IDS
# Separate checkpoints: never replace a previous mutation-enabled evaluation.
"${CONTAINER[@]}" --pwd /home/marta "$IMAGE" python3 -B \
    -m benchmark.xrepotest.evaluate --dataset /app/xrepotest/ruby_functions.jsonl \
    --processed "/data/xrepo/runs/$XREPO_RUN/generation/processed.jsonl" \
    --output "/data/xrepo/runs/$XREPO_RUN/evaluation_core_v1" \
    --work "/data/xrepo/runs/$XREPO_RUN/work/evaluation_core_v1" "${EXTRA[@]}" &
STEP_PID=$!
wait "$STEP_PID"
STEP_PID=""
echo "Core evaluation complete: $RUN/evaluation_core_v1/summary.json"

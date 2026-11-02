#!/bin/bash
#SBATCH --job-name=xrepo_off_eval
#SBATCH --account=f202407648iacdcf2x
#SBATCH --partition=dev-x86
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=02:00:00
#SBATCH --output=logs/xrepo_official_evaluate_%j.out
#SBATCH --signal=B:USR1@120
set -euo pipefail
BASE=${MARTA_CLUSTER_BASE:-/projects/F202407648IACDCF2/mario}
export MARTA_CLUSTER_CODE=${MARTA_CLUSTER_CODE:-$BASE/MARTA-evaluation}
source "$MARTA_CLUSTER_CODE/deucalion/xrepotest_job_common.sh"
[[ "$XREPO_RUN" == qwen36_35b_xrepotest_contexts_thinking_v1 ||
   "$XREPO_RUN" == qwen36_35b_xrepotest_contexts_thinking_cpu_v1 ||
   "$XREPO_RUN" == qwen36_35b_xrepotest_contexts_thinking_cpu_threads8_v2 ]] || exit 2
CONTINUATION="$CODE/deucalion/run_xrepotest_official_evaluate_cpu.sh"
export XREPO_EVALUATE_MODE=${XREPO_EVALUATE_MODE:-all}
case "$XREPO_EVALUATE_MODE" in
    all) MODES=(standard lsp_context file_context rag_bm25 rag_dense) ;;
    standard|lsp_context|file_context|rag_bm25|rag_dense) MODES=("$XREPO_EVALUATE_MODE") ;;
    *) echo "Unknown evaluation context mode: $XREPO_EVALUATE_MODE"; exit 2 ;;
esac
exec 9>"$RUN/evaluation-job.lock"
if [[ "$XREPO_EVALUATE_MODE" == all ]]; then
    flock -n 9 || { echo "Official evaluation already running"; exit 2; }
else
    flock -sn 9 || { echo "All-mode evaluation already running"; exit 2; }
    exec 8>"$RUN/evaluation-$XREPO_EVALUATE_MODE-job.lock"
    flock -n 8 || { echo "Evaluation already running: $XREPO_EVALUATE_MODE"; exit 2; }
fi
for mode in "${MODES[@]}"; do
    test -s "$RUN/modes/$mode/generation/complete.json" || { echo "Generation incomplete: $mode"; exit 2; }
done
for mode in "${MODES[@]}"; do
    echo "=== Evaluate official mode: $mode; all 675 tasks ==="
    "${CONTAINER[@]}" --pwd /home/marta "$IMAGE" python3 -B \
        -m benchmark.xrepotest.evaluate --dataset /app/xrepotest/ruby_functions.jsonl \
        --processed "/data/xrepo/runs/$XREPO_RUN/modes/$mode/generation/processed.jsonl" \
        --output "/data/xrepo/runs/$XREPO_RUN/modes/$mode/evaluation_core_v1" \
        --work "/data/xrepo/runs/$XREPO_RUN/work/evaluation/$mode" &
    STEP_PID=$!
    wait "$STEP_PID"
    STEP_PID=""
done
echo "Official mode(s) evaluated: ${MODES[*]}; $RUN/modes"

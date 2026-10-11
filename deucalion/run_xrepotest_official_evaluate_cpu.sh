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
[[ "$XREPO_RUN" == qwen36_35b_xrepotest_contexts_thinking_v1 ]] || exit 2
CONTINUATION="$CODE/deucalion/run_xrepotest_official_evaluate_cpu.sh"
for mode in standard lsp_context file_context rag_bm25 rag_dense; do
    test -s "$RUN/modes/$mode/generation/complete.json" || { echo "Generation incomplete: $mode"; exit 2; }
done
for mode in standard lsp_context file_context rag_bm25 rag_dense; do
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
echo "All five official modes evaluated: $RUN/modes"

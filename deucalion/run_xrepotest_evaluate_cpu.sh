#!/bin/bash
#SBATCH --job-name=marta_xrepo_eval
#SBATCH --account=f202407648iacdcf2x
#SBATCH --partition=dev-x86
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=04:00:00
#SBATCH --output=logs/xrepo_evaluate_%j.out
#SBATCH --signal=B:USR1@120
set -euo pipefail
BASE=${MARTA_CLUSTER_BASE:-/projects/F202407648IACDCF2/mario}
export XREPO_RUN
source "$BASE/MARTA/deucalion/xrepotest_job_common.sh"
CONTINUATION="$CODE/deucalion/run_xrepotest_evaluate_cpu.sh"
test -s "$RUN/generation/processed.jsonl" || { echo "Generation export is not complete"; exit 2; }
"${CONTAINER[@]}" --pwd /home/marta "$IMAGE" python3 -B \
    -m benchmark.xrepotest.evaluate --dataset /app/xrepotest/ruby_functions.jsonl \
    --processed "/data/xrepo/runs/$XREPO_RUN/generation/processed.jsonl" \
    --output "/data/xrepo/runs/$XREPO_RUN/evaluation" \
    --work "/data/xrepo/runs/$XREPO_RUN/work/evaluation" --enable-mutation &
STEP_PID=$!
wait "$STEP_PID"
STEP_PID=""
echo "Evaluation complete: $RUN/evaluation/summary.json"

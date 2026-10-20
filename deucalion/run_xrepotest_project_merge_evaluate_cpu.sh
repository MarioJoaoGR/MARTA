#!/bin/bash
#SBATCH --job-name=xrepo_ablation_eval
#SBATCH --account=f202407648iacdcf2x
#SBATCH --partition=dev-x86
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=02:00:00
#SBATCH --output=logs/xrepo_project_evaluate_%j.out
#SBATCH --signal=B:USR1@120
set -euo pipefail
BASE=${MARTA_CLUSTER_BASE:-/projects/F202407648IACDCF2/mario}
export MARTA_CLUSTER_CODE=${MARTA_CLUSTER_CODE:-$BASE/MARTA-ablation}
export XREPO_RUN=${XREPO_RUN:-qwen36_35b_ablation97_no_graph_v1}
[[ "$XREPO_RUN" == qwen36_35b_ablation97_no_graph_v1 ]] || exit 2
source "$MARTA_CLUSTER_CODE/deucalion/xrepotest_job_common.sh"
CONTINUATION="$CODE/deucalion/run_xrepotest_project_merge_evaluate_cpu.sh"
exec 9>"$RUN/evaluation-job.lock"
flock -n 9 || { echo "Project merge/evaluation already running"; exit 2; }
"${CONTAINER[@]}" "$IMAGE" python3 -B /opt/marta/deucalion/xrepotest_project_split.py merge &
STEP_PID=$!
wait "$STEP_PID"
STEP_PID=""
test -s "$RUN/project_parallel/merged/processed.jsonl"
"${CONTAINER[@]}" --pwd /home/marta "$IMAGE" python3 -B \
    -m benchmark.xrepotest.evaluate --dataset /app/xrepotest/ruby_functions.jsonl \
    --processed "/data/xrepo/runs/$XREPO_RUN/project_parallel/merged/processed.jsonl" \
    --task-ids /data/xrepo/selections/xrepotest_ablation97_v1.json \
    --output "/data/xrepo/runs/$XREPO_RUN/evaluation_core_v1" \
    --work "/data/xrepo/runs/$XREPO_RUN/work/evaluation_core_v1" &
STEP_PID=$!
wait "$STEP_PID"
STEP_PID=""
echo "Merged 97-task core evaluation complete: $RUN/evaluation_core_v1/summary.json"

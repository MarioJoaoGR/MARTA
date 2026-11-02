#!/bin/bash
#SBATCH --job-name=xrepo_cpu_request
#SBATCH --account=f202407648iacdcf2x
#SBATCH --partition=dev-x86
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=64G
#SBATCH --time=00:40:00
#SBATCH --output=logs/xrepo_cpu_request_%j.out
set -euo pipefail
BASE=${MARTA_CLUSTER_BASE:-/projects/F202407648IACDCF2/mario}
export MARTA_CLUSTER_CODE=${MARTA_CLUSTER_CODE:-$BASE/MARTA-evaluation}
export XREPO_RUN=qwen36_35b_xrepotest_contexts_thinking_cpu_v1
source "$MARTA_CLUSTER_CODE/deucalion/xrepotest_job_common.sh"
trap 'exit 143' USR1
[[ -z "${SLURM_JOB_GPUS:-}" && "${SLURM_GPUS_ON_NODE:-0}" == 0 ]] || exit 2
exec 9>"$RUN/generation-job.lock"
flock -n 9 || { echo "CPU benchmark still running; cancel it first"; exit 2; }
PORT=$((20000 + SLURM_JOB_ID % 20000))
HOST="127.0.0.1:$PORT"
LOG="$RUN/logs/ollama_cpu_request_$SLURM_JOB_ID.log"
scontrol show job "$SLURM_JOB_ID" > "$RUN/metadata/slurm_cpu_request_$SLURM_JOB_ID.txt"
lscpu > "$RUN/metadata/cpu_request_$SLURM_JOB_ID.txt"
singularity exec --cleanenv --home "$RUN/home:/home/marta" \
    --bind "$BASE/ollama_models:/data/ollama:ro" \
    --env GOMAXPROCS=4 --env OMP_NUM_THREADS=32 --env LLAMA_ARG_THREADS=8 --env "OLLAMA_HOST=$HOST" \
    --env CUDA_VISIBLE_DEVICES=-1 --env ROCR_VISIBLE_DEVICES=-1 \
    --env GGML_VK_VISIBLE_DEVICES=-1 --env OLLAMA_VULKAN=0 \
    --env OLLAMA_MODELS=/data/ollama --env OLLAMA_CONTEXT_LENGTH=32768 \
    --env OLLAMA_KEEP_ALIVE=-1 --env OLLAMA_NUM_PARALLEL=1 --env OLLAMA_FLASH_ATTENTION=0 \
    "$BASE/containers/marta_benchmark.sif" ollama serve > "$LOG" 2>&1 &
OLLAMA_PID=$!
for ((i=0; i<60; i++)); do
    kill -0 "$OLLAMA_PID" 2>/dev/null || exit 2
    if curl --fail --silent "http://$HOST/api/version" >/dev/null; then break; fi
    sleep 2
done
curl --fail --silent "http://$HOST/api/version" || exit 2
"${CONTAINER[@]}" "$IMAGE" python3 -B /opt/marta/deucalion/xrepotest_cpu_request_probe.py \
    --host "http://$HOST" \
    --sdk-source "/data/xrepo/runs/$XREPO_RUN/modes/standard/generation/api_requests.jsonl" \
    --http-source "/data/xrepo/runs/$XREPO_RUN/modes/standard/generation/http_requests.jsonl" \
    --server-log "/data/xrepo/runs/$XREPO_RUN/logs/ollama_cpu_request_$SLURM_JOB_ID.log" \
    --output "/data/xrepo/runs/$XREPO_RUN/diagnostics/cpu_request_threads8_$SLURM_JOB_ID" &
STEP_PID=$!
wait "$STEP_PID"
STEP_PID=""

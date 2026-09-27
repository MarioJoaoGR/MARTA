#!/bin/bash
#SBATCH --job-name=marta_xrepo_gen
#SBATCH --account=f202407648iacdcf2g
#SBATCH --partition=normal-a100-40
#SBATCH --nodes=1
#SBATCH --gpus=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --time=47:30:00
#SBATCH --output=logs/xrepo_generate_%j.out
#SBATCH --signal=B:USR1@120
set -euo pipefail
BASE=${MARTA_CLUSTER_BASE:-/projects/F202407648IACDCF2/mario}
: "${MODEL:?Set MODEL explicitly}"
: "${XREPO_THINKING:?Set XREPO_THINKING to off or on}"
[[ "$XREPO_THINKING" == off || "$XREPO_THINKING" == on ]] || exit 2
export MODEL XREPO_THINKING XREPO_RUN
export OLLAMA_CTX=${OLLAMA_CTX:-32768}
export XREPO_MAX_TOKENS=${XREPO_MAX_TOKENS:-16384}
export XREPO_TEMPERATURE=${XREPO_TEMPERATURE:-0.6}
export XREPO_TOP_P=${XREPO_TOP_P:-0.95}
export XREPO_PRESENCE_PENALTY=${XREPO_PRESENCE_PENALTY:-0}
export XREPO_REQUEST_TIMEOUT=${XREPO_REQUEST_TIMEOUT:-1800}
export XREPO_NO_GRAPH=${XREPO_NO_GRAPH:-0}
[[ "$XREPO_NO_GRAPH" == 0 || "$XREPO_NO_GRAPH" == 1 ]] || exit 2
source "$BASE/MARTA/deucalion/xrepotest_job_common.sh"
CONTINUATION="$CODE/deucalion/run_xrepotest_generate_gpu.sh"
# A duplicate job exits before loading the GPU/model.
exec 9>"$RUN/generation-job.lock"
flock -n 9 || { echo "Generation already running for $XREPO_RUN"; exit 2; }
PORT=$((20000 + SLURM_JOB_ID % 20000))
HOST="127.0.0.1:$PORT"
ml OpenMPI/5.0.3-GCC-13.3.0 CUDA/11.8.0 NCCL/2.20.5-GCCcore-13.3.0-CUDA-12.4.0
singularity exec --cleanenv --nv --home "$RUN/home:/home/marta" \
    --bind "$BASE/ollama_models:/data/ollama:ro" \
    --env GOMAXPROCS=4 --env "OLLAMA_HOST=$HOST" \
    --env OLLAMA_MODELS=/data/ollama --env "OLLAMA_CONTEXT_LENGTH=$OLLAMA_CTX" \
    --env OLLAMA_KEEP_ALIVE=-1 --env OLLAMA_NUM_PARALLEL=1 \
    --env OLLAMA_FLASH_ATTENTION=0 \
    "$BASE/containers/marta_benchmark.sif" ollama serve \
    > "$RUN/logs/ollama_$SLURM_JOB_ID.log" 2>&1 &
OLLAMA_PID=$!
for ((i=0; i<60; i++)); do
    kill -0 "$OLLAMA_PID" 2>/dev/null || { tail -40 "$RUN/logs/ollama_$SLURM_JOB_ID.log"; exit 2; }
    if curl --fail --silent "http://$HOST/api/version" >/dev/null; then break; fi
    sleep 2
done
curl --fail --silent "http://$HOST/api/version" || exit 2
DIGEST=$("${CONTAINER[@]}" "$IMAGE" python3 -B -m benchmark.xrepotest.cluster \
    --root /data/xrepo --model "$MODEL" --host "http://$HOST" \
    --metadata "/data/xrepo/runs/$XREPO_RUN/metadata/model_$SLURM_JOB_ID.json")
EXTRA=(--rounds 3 --attempts 3)
if [ "$XREPO_NO_GRAPH" == 1 ]; then EXTRA+=(--no-graph); fi
echo "XRepoTest: $MODEL ($DIGEST); thinking=$XREPO_THINKING; run=$XREPO_RUN"
"${CONTAINER[@]}" \
    --bind "$XROOT/python:/opt/conda/envs/test4py_env:ro" \
    --bind "$BASE/pydeps/marta:/data/pydeps/marta:ro" \
    --bind "$BASE/hf_cache:/data/hf_cache:ro" \
    --env PYTHONPATH=/data/pydeps/marta:/opt/marta \
    --env "OPENAI_API_BASE=http://$HOST/v1" --env OPENAI_API_KEY=ollama \
    --env "OLLAMA_CTX=$OLLAMA_CTX" --env HF_HOME=/data/hf_cache \
    --env HF_HUB_OFFLINE=1 --env TRANSFORMERS_OFFLINE=1 --env EMBED_DEVICE=cpu \
    --env TRANSFORMER_PATH=BAAI/bge-large-en-v1.5 \
    --pwd /home/marta "$IMAGE" /opt/conda/envs/test4py_env/bin/python -B \
    -m benchmark.xrepotest.run --dataset /app/xrepotest/ruby_functions.jsonl \
    --preflight /data/xrepo/reports/preflight.json \
    --output "/data/xrepo/runs/$XREPO_RUN/generation" \
    --work "/data/xrepo/runs/$XREPO_RUN/work/generation" \
    --model "$MODEL" --model-digest "$DIGEST" --thinking "$XREPO_THINKING" \
    --max-tokens "$XREPO_MAX_TOKENS" \
    --temperature "$XREPO_TEMPERATURE" --top-p "$XREPO_TOP_P" \
    --presence-penalty "$XREPO_PRESENCE_PENALTY" \
    --request-timeout "$XREPO_REQUEST_TIMEOUT" "${EXTRA[@]}" &
STEP_PID=$!
wait "$STEP_PID"
STEP_PID=""
echo "Generation complete: $RUN/generation/processed.jsonl"

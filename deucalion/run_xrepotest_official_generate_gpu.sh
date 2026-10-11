#!/bin/bash
#SBATCH --job-name=xrepo_off_gen
#SBATCH --account=f202407648iacdcf2g
#SBATCH --partition=normal-a100-40
#SBATCH --nodes=1
#SBATCH --gpus=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --time=08:00:00
#SBATCH --output=logs/xrepo_official_generate_%j.out
#SBATCH --signal=B:USR1@120
set -euo pipefail
BASE=${MARTA_CLUSTER_BASE:-/projects/F202407648IACDCF2/mario}
export MARTA_CLUSTER_CODE=${MARTA_CLUSTER_CODE:-$BASE/MARTA-evaluation}
export MODEL=qwen3.6:35b XREPO_THINKING=on OLLAMA_CTX=32768
source "$MARTA_CLUSTER_CODE/deucalion/xrepotest_job_common.sh"
[[ "$XREPO_RUN" == qwen36_35b_xrepotest_standard_thinking_v1 ]] || exit 2
CONTINUATION="$CODE/deucalion/run_xrepotest_official_generate_gpu.sh"
exec 9>"$RUN/generation-job.lock"
flock -n 9 || { echo "Official generation already running"; exit 2; }
test -s "$RUN/metadata/official_preflight.json" || { echo "Run the official CPU preparation first"; exit 2; }
PYTHON_CONTAINER=("${CONTAINER[@]}"
    --bind "$XROOT/python:/opt/conda/envs/test4py_env:ro"
    --bind "$BASE/pydeps/marta:/data/pydeps/marta:ro"
    --env PYTHONPATH=/data/pydeps/marta:/opt/marta --env OLLAMA_CTX=32768)
ARGS=(--assets-dir /data/xrepo/assets/official-standard-39fb6ab
    --dataset /app/xrepotest/ruby_functions.jsonl
    --reference /data/xrepo/runs/qwen36_35b_thinking_bundle_loading_v4/generation)
# Verify offline imports and reference again before starting Ollama.
"${PYTHON_CONTAINER[@]}" "$IMAGE" /opt/conda/envs/test4py_env/bin/python -B \
    /opt/marta/deucalion/xrepotest_official_generate.py "${ARGS[@]}"
scontrol show job "$SLURM_JOB_ID" > "$RUN/metadata/slurm_$SLURM_JOB_ID.txt" 2>&1 || true
python3 -B "$CODE/deucalion/monitor_memory.py" \
    --job-id "$SLURM_JOB_ID" --root-pid "$$" \
    --output "$RUN/metadata/memory_$SLURM_JOB_ID.jsonl" \
    > "$RUN/logs/memory_$SLURM_JOB_ID.log" 2>&1 &
MONITOR_PID=$!
PORT=$((20000 + SLURM_JOB_ID % 20000))
HOST="127.0.0.1:$PORT"
ml OpenMPI/5.0.3-GCC-13.3.0 CUDA/11.8.0 NCCL/2.20.5-GCCcore-13.3.0-CUDA-12.4.0
singularity exec --cleanenv --nv --home "$RUN/home:/home/marta" \
    --bind "$BASE/ollama_models:/data/ollama:ro" \
    --env GOMAXPROCS=4 --env "OLLAMA_HOST=$HOST" \
    --env OLLAMA_MODELS=/data/ollama --env OLLAMA_CONTEXT_LENGTH=32768 \
    --env OLLAMA_KEEP_ALIVE=-1 --env OLLAMA_NUM_PARALLEL=1 \
    --env OLLAMA_FLASH_ATTENTION=0 \
    "$BASE/containers/marta_benchmark.sif" ollama serve \
    > "$RUN/logs/ollama_$SLURM_JOB_ID.log" 2>&1 &
OLLAMA_PID=$!
for ((i=0; i<60; i++)); do
    kill -0 "$OLLAMA_PID" 2>/dev/null || exit 2
    if curl --fail --silent "http://$HOST/api/version" >/dev/null; then break; fi
    sleep 2
done
curl --fail --silent "http://$HOST/api/version" || exit 2
"${CONTAINER[@]}" "$IMAGE" python3 -B -m benchmark.xrepotest.cluster \
    --root /data/xrepo --model "$MODEL" --host "http://$HOST" \
    --metadata "/data/xrepo/runs/$XREPO_RUN/metadata/model_$SLURM_JOB_ID.json"
"${PYTHON_CONTAINER[@]}" "$IMAGE" /opt/conda/envs/test4py_env/bin/python -B \
    /opt/marta/deucalion/xrepotest_official_generate.py "${ARGS[@]}" \
    --output "/data/xrepo/runs/$XREPO_RUN/generation" \
    --api-base "http://$HOST/v1" \
    --model-metadata "/data/xrepo/runs/$XREPO_RUN/metadata/model_$SLURM_JOB_ID.json" &
STEP_PID=$!
wait "$STEP_PID"
STEP_PID=""
echo "Official generation complete: $RUN/generation/processed.jsonl"

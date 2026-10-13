#!/bin/bash
#SBATCH --job-name=xrepo_off_cpu
#SBATCH --account=f202407648iacdcf2x
#SBATCH --partition=normal-x86
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=64G
#SBATCH --time=24:00:00
#SBATCH --output=logs/xrepo_official_generate_cpu_%j.out
#SBATCH --signal=B:USR1@120
set -euo pipefail
BASE=${MARTA_CLUSTER_BASE:-/projects/F202407648IACDCF2/mario}
export MARTA_CLUSTER_CODE=${MARTA_CLUSTER_CODE:-$BASE/MARTA-evaluation}
export MODEL=qwen3.6:35b XREPO_THINKING=on
export XREPO_OFFICIAL_CTX=${XREPO_OFFICIAL_CTX:-32768}
[[ "$XREPO_OFFICIAL_CTX" == 32768 ]] || { echo "Context must match MARTA: 32768"; exit 2; }
export OLLAMA_CTX="$XREPO_OFFICIAL_CTX"
export XREPO_OFFICIAL_MODE=${XREPO_OFFICIAL_MODE:-all}
case "$XREPO_OFFICIAL_MODE" in
    all) MODES=(standard lsp_context file_context rag_bm25 rag_dense) ;;
    standard|lsp_context|file_context|rag_bm25|rag_dense) MODES=("$XREPO_OFFICIAL_MODE") ;;
    *) echo "Unknown official context mode: $XREPO_OFFICIAL_MODE"; exit 2 ;;
esac
source "$MARTA_CLUSTER_CODE/deucalion/xrepotest_job_common.sh"
[[ "$XREPO_RUN" == qwen36_35b_xrepotest_contexts_thinking_cpu_threads8_v2 ]] || {
    echo "Use the fresh CPU threads8 v2 run; v1 is preserved as a failed runtime trial"
    exit 2
}
CONTINUATION="$CODE/deucalion/run_xrepotest_official_generate_cpu.sh"
# CPU quota is separate. No chain unless explicitly enabled after billing check.
export XREPO_CPU_CHAIN=${XREPO_CPU_CHAIN:-0}
[[ "$XREPO_CPU_CHAIN" == 0 || "$XREPO_CPU_CHAIN" == 1 ]] || exit 2
if [[ "$XREPO_CPU_CHAIN" == 0 ]]; then
    trap 'echo "CPU walltime approaching; checkpoints kept, no automatic resubmission"; exit 143' USR1
fi
[[ -z "${SLURM_JOB_GPUS:-}" && "${SLURM_GPUS_ON_NODE:-0}" == 0 ]] || { echo "CPU generation must not allocate a GPU"; exit 2; }
exec 9>"$RUN/generation-job.lock"
if [[ "$XREPO_OFFICIAL_MODE" == all ]]; then
    flock -n 9 || { echo "Official generation already running"; exit 2; }
else
    # Different modes can run together; reject duplicates and an all-mode job.
    flock -sn 9 || { echo "All-mode generation already running"; exit 2; }
    exec 8>"$RUN/generation-$XREPO_OFFICIAL_MODE-job.lock"
    flock -n 8 || { echo "Generation already running: $XREPO_OFFICIAL_MODE"; exit 2; }
fi
for mode in "${MODES[@]}"; do
    test -s "$RUN/modes/$mode/metadata/official_preflight.json" || { echo "Run the five-mode CPU preparation first"; exit 2; }
done
PYTHON_CONTAINER=("${CONTAINER[@]}"
    --bind "$XROOT/python:/opt/conda/envs/test4py_env:ro"
    --bind "$BASE/pydeps/marta:/data/pydeps/marta:ro"
    --env PYTHONPATH=/data/pydeps/marta:/opt/marta --env "OLLAMA_CTX=$XREPO_OFFICIAL_CTX")
ARGS=(--context-length "$XREPO_OFFICIAL_CTX" --assets-dir /data/xrepo/assets/official-contexts-39fb6ab
    --dataset /app/xrepotest/ruby_functions.jsonl
    --reference /data/xrepo/runs/qwen36_35b_thinking_bundle_loading_v4/generation)
# Verify offline imports and reference again before starting Ollama.
for mode in "${MODES[@]}"; do
"${PYTHON_CONTAINER[@]}" "$IMAGE" /opt/conda/envs/test4py_env/bin/python -B \
    /opt/marta/deucalion/xrepotest_official_generate.py --mode "$mode" --backend cpu "${ARGS[@]}"
done
scontrol show job "$SLURM_JOB_ID" > "$RUN/metadata/slurm_$SLURM_JOB_ID.txt" 2>&1 || true
python3 -B "$CODE/deucalion/monitor_memory.py" \
    --job-id "$SLURM_JOB_ID" --root-pid "$$" \
    --output "$RUN/metadata/memory_$SLURM_JOB_ID.jsonl" \
    > "$RUN/logs/memory_$SLURM_JOB_ID.log" 2>&1 &
MONITOR_PID=$!
PORT=$((20000 + SLURM_JOB_ID % 20000))
HOST="127.0.0.1:$PORT"
lscpu > "$RUN/metadata/cpu_$SLURM_JOB_ID.txt" 2>&1 || true
SERVER_HOME="$RUN/ollama_home_$XREPO_OFFICIAL_MODE"
mkdir -p "$SERVER_HOME"
singularity exec --cleanenv --home "$SERVER_HOME:/home/marta" \
    --bind "$BASE/ollama_models:/data/ollama:ro" \
    --env GOMAXPROCS=4 --env LLAMA_ARG_THREADS=8 --env "OLLAMA_HOST=$HOST" \
    --env CUDA_VISIBLE_DEVICES=-1 --env ROCR_VISIBLE_DEVICES=-1 \
    --env GGML_VK_VISIBLE_DEVICES=-1 --env OLLAMA_VULKAN=0 \
    --env "OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-32}" \
    --env OLLAMA_MODELS=/data/ollama --env "OLLAMA_CONTEXT_LENGTH=$XREPO_OFFICIAL_CTX" \
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
"${CONTAINER[@]}" "$IMAGE" python3 -B /opt/marta/deucalion/verify_ollama_cpu.py \
    --host "http://$HOST" --model "$MODEL" --context 32768 --threads 8 \
    --server-log "/data/xrepo/runs/$XREPO_RUN/logs/ollama_$SLURM_JOB_ID.log" \
    --output "/data/xrepo/runs/$XREPO_RUN/metadata/cpu_proof_$SLURM_JOB_ID.json"
for mode in "${MODES[@]}"; do
    echo "=== Official XRepoTest CPU mode: $mode; 675 tasks ==="
    "${PYTHON_CONTAINER[@]}" "$IMAGE" /opt/conda/envs/test4py_env/bin/python -B \
        /opt/marta/deucalion/xrepotest_official_generate.py --mode "$mode" --backend cpu "${ARGS[@]}" \
        --cpu-proof "/data/xrepo/runs/$XREPO_RUN/metadata/cpu_proof_$SLURM_JOB_ID.json" \
        --output "/data/xrepo/runs/$XREPO_RUN/modes/$mode/generation" \
        --api-base "http://$HOST/v1" \
        --model-metadata "/data/xrepo/runs/$XREPO_RUN/metadata/model_$SLURM_JOB_ID.json" &
    STEP_PID=$!
    wait "$STEP_PID"
    STEP_PID=""
done
echo "Official CPU mode(s) complete: ${MODES[*]}; $RUN/modes"

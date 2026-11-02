#!/bin/bash
#SBATCH --job-name=marta_xrepo_cpu
#SBATCH --account=f202407648iacdcf2x
#SBATCH --partition=normal-x86
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=64G
#SBATCH --time=48:00:00
#SBATCH --output=logs/xrepo_generate_cpu_%j.out
#SBATCH --signal=B:USR1@120
set -euo pipefail
BASE=${MARTA_CLUSTER_BASE:-/projects/F202407648IACDCF2/mario}
export MARTA_CLUSTER_CODE=${MARTA_CLUSTER_CODE:-$BASE/MARTA-ablation}
: "${XREPO_RUN:?Set the existing no-graph cohort}"
export XREPO_PROJECT_SHARD=${XREPO_PROJECT_SHARD:-}
PARENT_COHORT=qwen36_35b_ablation97_no_graph_v1
RESUME_HELPER=(python3 -B /opt/marta/deucalion/xrepotest_cpu_resume.py)
if [[ -z "$XREPO_PROJECT_SHARD" ]]; then
    [[ "$XREPO_RUN" == "$PARENT_COHORT" ]] || exit 2
else
    case "$XREPO_PROJECT_SHARD" in
        capybara|dotenv|grape|hanami|hashie|httparty|pundit|rom|rspec-core|shoryuken) ;;
        *) exit 2 ;;
    esac
    [[ "$XREPO_RUN" == "${PARENT_COHORT}_cpu_${XREPO_PROJECT_SHARD//-/_}" ]] || exit 2
    RESUME_HELPER=(python3 -B /opt/marta/deucalion/xrepotest_project_split.py --project "$XREPO_PROJECT_SHARD")
fi
source "$MARTA_CLUSTER_CODE/deucalion/xrepotest_job_common.sh"
PARENT_RUN="$XROOT/runs/$PARENT_COHORT"
if [[ -n "$XREPO_PROJECT_SHARD" ]]; then
    test -s "$PARENT_RUN/metadata/project_split.json" || { echo "Project split has not been prepared"; exit 2; }
    # Different projects share a read lock on the frozen parent. Serial jobs require exclusive access.
    exec 8>"$PARENT_RUN/generation-job.lock"
    flock -sn 8 || { echo "Serial parent generation is still running"; exit 2; }
elif [[ -e "$PARENT_RUN/metadata/project_split.json" ]]; then
    echo "Serial cohort is frozen for project-parallel continuation"; exit 2
fi
[[ -z "${SLURM_JOB_GPUS:-}" && "${SLURM_GPUS_ON_NODE:-0}" == 0 ]] || exit 2
CONTINUATION="$CODE/deucalion/run_xrepotest_generate_cpu.sh"
exec 9>"$RUN/generation-job.lock"
flock -n 9 || { echo "Generation already running for $XREPO_RUN"; exit 2; }
"${CONTAINER[@]}" "$IMAGE" "${RESUME_HELPER[@]}" env \
    --generation "/data/xrepo/runs/$XREPO_RUN/generation" --job-id "$SLURM_JOB_ID" \
    --env-file "/data/xrepo/runs/$XREPO_RUN/metadata/cpu_env_$SLURM_JOB_ID.sh"
source "$RUN/metadata/cpu_env_$SLURM_JOB_ID.sh"
export XREPO_CPU_CHAIN=${XREPO_CPU_CHAIN:-1}
[[ "$XREPO_CPU_CHAIN" == 0 || "$XREPO_CPU_CHAIN" == 1 ]] || exit 2
if [[ "$XREPO_CPU_CHAIN" == 0 ]]; then trap 'exit 143' USR1; fi
AUDIT_STARTED=0
cpu_cleanup() {
    status=$?
    trap - EXIT
    cleanup
    if [[ -n "$STEP_PID" ]]; then wait "$STEP_PID" 2>/dev/null || true; fi
    if [[ "$AUDIT_STARTED" == 1 ]]; then
        "${CONTAINER[@]}" "$IMAGE" "${RESUME_HELPER[@]}" finish \
            --generation "/data/xrepo/runs/$XREPO_RUN/generation" --job-id "$SLURM_JOB_ID" \
            --exit-code "$status" || status=1
    fi
    exit "$status"
}
trap cpu_cleanup EXIT
EXTRA=(--rounds "${XREPO_ROUNDS:-3}" --attempts "${XREPO_ATTEMPTS:-3}")
for pair in "XREPO_NO_TYPE_HINTS:no-type-hints" "XREPO_NO_METHOD_RETRIEVAL:no-method-retrieval" \
            "XREPO_NO_COVERAGE_FEEDBACK:no-coverage-feedback" "XREPO_NO_REPAIR:no-repair"; do
    variable=${pair%%:*}
    value=${!variable:-0}
    [[ "$value" == 0 || "$value" == 1 ]] || { echo "Invalid $variable"; exit 2; }
    if [[ "$value" == 1 ]]; then EXTRA+=("--${pair#*:}"); fi
    export "$variable=$value"
done
if [[ -n "${XREPO_TASK_IDS:-}" ]]; then
    [[ "$XREPO_TASK_IDS" == /data/xrepo/* && -f "$XROOT/${XREPO_TASK_IDS#/data/xrepo/}" ]] || exit 2
    EXTRA+=(--task-ids "$XREPO_TASK_IDS")
fi
if [[ -n "${XREPO_REUSE_ANALYSIS_FROM:-}" ]]; then
    [[ "$XREPO_REUSE_ANALYSIS_FROM" == /data/xrepo/runs/* ]] || exit 2
    EXTRA+=(--reuse-analysis-from "$XREPO_REUSE_ANALYSIS_FROM")
fi
if [[ -n "${XREPO_REUSE_FIRST_ROUND_FROM:-}" ]]; then
    [[ "$XREPO_REUSE_FIRST_ROUND_FROM" == "${XREPO_REUSE_ANALYSIS_FROM:-}" ]] || exit 2
    [[ "${XREPO_NO_COVERAGE_FEEDBACK:-0}" == 1 && "$XREPO_NO_GRAPH" == 0 &&
       "${XREPO_NO_TYPE_HINTS:-0}" == 0 && "${XREPO_NO_METHOD_RETRIEVAL:-0}" == 0 &&
       "${XREPO_NO_REPAIR:-0}" == 0 ]] || exit 2
    EXTRA+=(--reuse-first-round-from "$XREPO_REUSE_FIRST_ROUND_FROM")
fi
export XREPO_ROUNDS XREPO_ATTEMPTS XREPO_TASK_IDS XREPO_REUSE_ANALYSIS_FROM XREPO_REUSE_FIRST_ROUND_FROM
if [ "$XREPO_NO_GRAPH" == 1 ]; then EXTRA+=(--no-graph); fi
"${CONTAINER[@]}" "$IMAGE" python3 -B -m benchmark.xrepotest.cluster \
    --root /data/xrepo --require-loading
# Retain the scheduler's effective CPU/RAM allocation, including site defaults.
# A diagnostic failure must not prevent generation.
scontrol show job "$SLURM_JOB_ID" > "$RUN/metadata/slurm_$SLURM_JOB_ID.txt" 2>&1 || true
# Host-side diagnostics: no model calls, packages or shared-account cmdlines.
python3 -B "$CODE/deucalion/monitor_memory.py" \
    --job-id "$SLURM_JOB_ID" --root-pid "$$" \
    --output "$RUN/metadata/memory_$SLURM_JOB_ID.jsonl" \
    > "$RUN/logs/memory_$SLURM_JOB_ID.log" 2>&1 &
MONITOR_PID=$!
echo "Memory diagnostics: $RUN/metadata/memory_$SLURM_JOB_ID.jsonl"
PORT=$((20000 + SLURM_JOB_ID % 20000))
HOST="127.0.0.1:$PORT"
lscpu > "$RUN/metadata/cpu_$SLURM_JOB_ID.txt" 2>&1 || true
mkdir -p "$RUN/ollama_home_cpu"
singularity exec --cleanenv --home "$RUN/ollama_home_cpu:/home/marta" \
    --bind "$BASE/ollama_models:/data/ollama:ro" \
    --env GOMAXPROCS=4 --env LLAMA_ARG_THREADS=8 --env "OLLAMA_HOST=$HOST" \
    --env CUDA_VISIBLE_DEVICES=-1 --env ROCR_VISIBLE_DEVICES=-1 \
    --env GGML_VK_VISIBLE_DEVICES=-1 --env OLLAMA_VULKAN=0 \
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
echo "XRepoTest: $MODEL ($DIGEST); thinking=$XREPO_THINKING; run=$XREPO_RUN"
"${CONTAINER[@]}" "$IMAGE" python3 -B /opt/marta/deucalion/verify_marta_ollama_cpu.py \
    --host "http://$HOST" --model "$MODEL" --context "$OLLAMA_CTX" --threads 8 \
    --server-log "/data/xrepo/runs/$XREPO_RUN/logs/ollama_$SLURM_JOB_ID.log" \
    --output "/data/xrepo/runs/$XREPO_RUN/metadata/cpu_proof_$SLURM_JOB_ID.json"
"${CONTAINER[@]}" "$IMAGE" "${RESUME_HELPER[@]}" start \
    --generation "/data/xrepo/runs/$XREPO_RUN/generation" --job-id "$SLURM_JOB_ID" \
    --proof "/data/xrepo/runs/$XREPO_RUN/metadata/cpu_proof_$SLURM_JOB_ID.json"
AUDIT_STARTED=1
RUNTIME_FLAGS=()
for variable in TRANSFORMER_PATH MARTA_MAX_CONTEXT_CHARS; do
    if [[ -n "${!variable:-}" ]]; then RUNTIME_FLAGS+=(--env "$variable=${!variable}"); fi
done
"${CONTAINER[@]}" \
    --bind "$XROOT/python:/opt/conda/envs/test4py_env:ro" \
    --bind "$BASE/pydeps/marta:/data/pydeps/marta:ro" \
    --bind "$BASE/hf_cache:/data/hf_cache:ro" \
    --env PYTHONPATH=/data/pydeps/marta:/opt/marta \
    --env "OPENAI_API_BASE=http://$HOST/v1" --env OPENAI_API_KEY=ollama \
    --env "OLLAMA_CTX=$OLLAMA_CTX" --env HF_HOME=/data/hf_cache \
    --env HF_HUB_OFFLINE=1 --env TRANSFORMERS_OFFLINE=1 --env EMBED_DEVICE=cpu \
    "${RUNTIME_FLAGS[@]}" \
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

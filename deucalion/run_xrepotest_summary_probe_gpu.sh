#!/bin/bash
#SBATCH --job-name=marta_xrepo_probe
#SBATCH --account=f202407648iacdcf2g
#SBATCH --partition=normal-a100-40
#SBATCH --nodes=1
#SBATCH --gpus=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --time=00:20:00
#SBATCH --output=logs/xrepo_probe_%j.out
set -euo pipefail
BASE=${MARTA_CLUSTER_BASE:-/projects/F202407648IACDCF2/mario}
: "${XREPO_RUN:?Set the original experiment name}"
source "$BASE/MARTA/deucalion/xrepotest_job_common.sh"
# A probe has no continuation; it makes exactly one model request.
trap - USR1
exec 9>"$RUN/generation-job.lock"
flock -n 9 || { echo "Original generation is active; probe refused"; exit 2; }
"${CONTAINER[@]}" "$IMAGE" python3 -B -m benchmark.xrepotest.cluster \
    --root /data/xrepo --require-loading
export OLLAMA_CTX=65536
OUT="/data/xrepo/runs/$XREPO_RUN/diagnostics/summary_budget_$SLURM_JOB_ID"
GEN="/data/xrepo/runs/$XREPO_RUN/generation"
# Read-only generation mount also prevents accidental checkpoint writes.
PROBE_CONTAINER=("${CONTAINER[@]}"
    --bind "$RUN/generation:$GEN:ro"
    --bind "$XROOT/python:/opt/conda/envs/test4py_env:ro"
    --bind "$BASE/pydeps/marta:/data/pydeps/marta:ro"
    --env PYTHONPATH=/data/pydeps/marta:/app:/opt/marta --env "OLLAMA_CTX=$OLLAMA_CTX")
PROBE=(/opt/conda/envs/test4py_env/bin/python -B /opt/marta/deucalion/xrepotest_summary_probe.py
    --generation "$GEN" --output "$OUT"
    --project "${XREPO_PROBE_PROJECT:-hashie}" --method "${XREPO_PROBE_METHOD:-Hashie::Hash#to_mash}")
"${PROBE_CONTAINER[@]}" "$IMAGE" "${PROBE[@]}" --capture-only
MODEL=$("${CONTAINER[@]}" "$IMAGE" python3 -B -c \
    'import json,sys; print(json.load(open(sys.argv[1]))["original_manifest"]["model"])' "$OUT/request.json")
PORT=$((20000 + SLURM_JOB_ID % 20000))
HOST="127.0.0.1:$PORT"
ml OpenMPI/5.0.3-GCC-13.3.0 CUDA/11.8.0 NCCL/2.20.5-GCCcore-13.3.0-CUDA-12.4.0
singularity exec --cleanenv --nv --home "$RUN/home:/home/marta" \
    --bind "$BASE/ollama_models:/data/ollama:ro" \
    --env GOMAXPROCS=4 --env "OLLAMA_HOST=$HOST" \
    --env OLLAMA_MODELS=/data/ollama --env "OLLAMA_CONTEXT_LENGTH=$OLLAMA_CTX" \
    --env OLLAMA_KEEP_ALIVE=-1 --env OLLAMA_NUM_PARALLEL=1 --env OLLAMA_FLASH_ATTENTION=0 \
    "$BASE/containers/marta_benchmark.sif" ollama serve \
    > "$RUN/logs/ollama_probe_$SLURM_JOB_ID.log" 2>&1 &
OLLAMA_PID=$!
for ((i=0; i<60; i++)); do
    kill -0 "$OLLAMA_PID" 2>/dev/null || exit 2
    if curl --fail --silent "http://$HOST/api/version" >/dev/null; then break; fi
    sleep 2
done
curl --fail --silent "http://$HOST/api/version" || exit 2
DIGEST=$("${CONTAINER[@]}" "$IMAGE" python3 -B -m benchmark.xrepotest.cluster \
    --root /data/xrepo --model "$MODEL" --host "http://$HOST" \
    --metadata "$OUT/model.json")
"${PROBE_CONTAINER[@]}" "$IMAGE" "${PROBE[@]}" --host "http://$HOST" --model-digest "$DIGEST" &
STEP_PID=$!
wait "$STEP_PID"
STEP_PID=""
echo "Diagnostic complete: $RUN/diagnostics/summary_budget_$SLURM_JOB_ID/result.json"

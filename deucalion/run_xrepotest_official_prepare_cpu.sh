#!/bin/bash
#SBATCH --job-name=xrepo_off_prep
#SBATCH --account=f202407648iacdcf2x
#SBATCH --partition=dev-x86
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --time=00:30:00
#SBATCH --output=logs/xrepo_official_prepare_%j.out
set -euo pipefail
BASE=${MARTA_CLUSTER_BASE:-/projects/F202407648IACDCF2/mario}
export MARTA_CLUSTER_CODE=${MARTA_CLUSTER_CODE:-$BASE/MARTA-evaluation}
source "$MARTA_CLUSTER_CODE/deucalion/xrepotest_job_common.sh"
[[ "$XREPO_RUN" == qwen36_35b_xrepotest_contexts_thinking_v1 ||
   "$XREPO_RUN" == qwen36_35b_xrepotest_contexts_thinking_cpu_v1 ||
   "$XREPO_RUN" == qwen36_35b_xrepotest_contexts_thinking_cpu_threads8_v2 ]] || exit 2
export XREPO_OFFICIAL_CTX=${XREPO_OFFICIAL_CTX:-32768}
[[ "$XREPO_OFFICIAL_CTX" == 32768 ]] || { echo "Context must match MARTA: 32768"; exit 2; }
BACKEND=gpu
if [[ "$XREPO_RUN" == qwen36_35b_xrepotest_contexts_thinking_cpu_v1 ||
   "$XREPO_RUN" == qwen36_35b_xrepotest_contexts_thinking_cpu_threads8_v2 ]]; then BACKEND=cpu; fi
for mode in standard lsp_context file_context rag_bm25 rag_dense; do
"${CONTAINER[@]}" \
    --bind "$XROOT/python:/opt/conda/envs/test4py_env:ro" \
    --bind "$BASE/pydeps/marta:/data/pydeps/marta:ro" \
    --env PYTHONPATH=/data/pydeps/marta:/opt/marta \
    "$IMAGE" /opt/conda/envs/test4py_env/bin/python -B \
    /opt/marta/deucalion/xrepotest_official_generate.py \
    --mode "$mode" --backend "$BACKEND" --context-length "$XREPO_OFFICIAL_CTX" --assets-dir /data/xrepo/assets/official-contexts-39fb6ab \
    --dataset /app/xrepotest/ruby_functions.jsonl \
    --reference /data/xrepo/runs/qwen36_35b_thinking_bundle_loading_v4/generation \
    --preflight-output "/data/xrepo/runs/$XREPO_RUN/modes/$mode/metadata/official_preflight.json"
done
echo "All five official context modes ready; no GPU or inference used."

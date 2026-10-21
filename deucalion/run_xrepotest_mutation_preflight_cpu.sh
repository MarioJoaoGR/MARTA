#!/bin/bash
#SBATCH --job-name=xrepo_mut_preflight
#SBATCH --account=f202407648iacdcf2x
#SBATCH --partition=dev-x86
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=02:00:00
#SBATCH --output=logs/xrepo_mutation_preflight_%j.out
set -euo pipefail
BASE=${MARTA_CLUSTER_BASE:-/projects/F202407648IACDCF2/mario}
CODE=${MARTA_CLUSTER_CODE:-$BASE/MARTA-evaluation}
XROOT="$BASE/xrepotest"
VALIDATION=${XREPO_MUTATION_VALIDATION:-/data/xrepo/runs/qwen36_35b_thinking_bundle_loading_v4/diagnostics/mutation_validate_2099026/results/report.json}
JOBHOME="$XROOT/tmp/mutation_preflight_$SLURM_JOB_ID"
mkdir -p "$JOBHOME"
GOMAXPROCS=4 singularity exec --cleanenv \
    --home "$JOBHOME:/home/marta" \
    --bind "$CODE:/opt/marta:ro" --bind "$XROOT:/data/xrepo:ro" \
    --env PYTHONPATH=/app:/opt/marta --env PYTHONUNBUFFERED=1 --env GOMAXPROCS=4 \
    "$XROOT/repaired-v2.sif" bash -c '
        set -e
        for cohort in marta no_coverage no_repair no_method_retrieval no_type_hints no_graph standard lsp_context file_context rag_bm25 rag_dense; do
            python3 -B -m deucalion.xrepotest_mutation_evaluate \
                --cohort "$cohort" --validation "$1" --preflight-only
        done
    ' preflight "$VALIDATION"
echo "All 11 cohorts ready: immutable core/suites, same validated mutation executor. No measurements or LLM calls."

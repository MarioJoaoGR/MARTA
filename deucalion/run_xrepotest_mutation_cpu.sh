#!/bin/bash
#SBATCH --job-name=xrepo_mutation
#SBATCH --account=f202407648iacdcf2x
#SBATCH --partition=normal-x86
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=24:00:00
#SBATCH --output=logs/xrepo_mutation_%A_%a.out
#SBATCH --signal=B:USR1@120
set -euo pipefail
BASE=${MARTA_CLUSTER_BASE:-/projects/F202407648IACDCF2/mario}
CODE=${MARTA_CLUSTER_CODE:-$BASE/MARTA-evaluation}
XROOT="$BASE/xrepotest"
VALIDATION=${XREPO_MUTATION_VALIDATION:-/data/xrepo/runs/qwen36_35b_thinking_bundle_loading_v4/diagnostics/mutation_validate_2099026/results/report.json}
COHORTS=(marta no_coverage no_repair no_method_retrieval no_type_hints no_graph standard lsp_context file_context rag_bm25 rag_dense)
INDEX=${SLURM_ARRAY_TASK_ID:?Submit with --array=0-10}
[[ "$INDEX" =~ ^[0-9]+$ ]] && (( INDEX < ${#COHORTS[@]} )) || exit 2
COHORT=${COHORTS[$INDEX]}
case "$COHORT" in
    marta) REL=runs/qwen36_35b_thinking_bundle_loading_v4 ;;
    standard|lsp_context|file_context|rag_bm25|rag_dense)
        REL=runs/qwen36_35b_xrepotest_contexts_thinking_cpu_threads8_v2/modes/$COHORT ;;
    *) REL=runs/qwen36_35b_ablation97_${COHORT}_v1 ;;
esac
OUT="$XROOT/$REL/mutation_v1"
JOBHOME="$XROOT/tmp/mutation_${SLURM_JOB_ID}_$INDEX"
mkdir -p "$OUT" "$JOBHOME"
STEP_PID=""
cleanup() {
    if [ -n "$STEP_PID" ]; then
        kill -TERM "$STEP_PID" 2>/dev/null || true
        wait "$STEP_PID" 2>/dev/null || true
        STEP_PID=""
    fi
}
trap cleanup EXIT
trap 'exit 143' TERM INT
continue_at_walltime() {
    trap '' USR1
    cleanup
    if [[ ${XREPO_MUTATION_CHAIN:-1} == 1 ]]; then
        sbatch --parsable --array="$INDEX" --export=ALL \
            --dependency="afterany:${SLURM_ARRAY_JOB_ID}_$INDEX" \
            "$CODE/deucalion/run_xrepotest_mutation_cpu.sh"
    fi
    exit 143
}
trap continue_at_walltime USR1
# Only this cohort's new mutation output is writable. Original generations,
# core evaluations, diagnostics/certificate, and code are mounted read-only.
srun --ntasks=1 --cpus-per-task=4 singularity exec --cleanenv \
    --home "$JOBHOME:/home/marta" \
    --bind "$CODE:/opt/marta:ro" --bind "$XROOT:/data/xrepo:ro" \
    --bind "$OUT:/data/xrepo/$REL/mutation_v1" \
    --env PYTHONPATH=/app:/opt/marta --env PYTHONUNBUFFERED=1 \
    --env GOMAXPROCS=4 --env OMP_NUM_THREADS=4 --env OPENBLAS_NUM_THREADS=4 \
    "$XROOT/repaired-v2.sif" python3 -B -m deucalion.xrepotest_mutation_evaluate \
    --cohort "$COHORT" --validation "$VALIDATION" &
STEP_PID=$!
wait "$STEP_PID"
STEP_PID=""
echo "Mutation finished: $COHORT; $OUT/summary.json"

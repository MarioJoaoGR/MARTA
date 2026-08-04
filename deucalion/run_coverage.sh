#!/bin/bash
#SBATCH --job-name="cov_measure"
#SBATCH --account=f202407648iacdcf2x
#SBATCH --partition=dev-x86
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=64G
#SBATCH --time=04:00:00
#SBATCH --output=logs/cov_%j.out
#SBATCH --signal=B:SIGTERM@120

# ─────────────────────────────────────────────────────────────────────────────
# Medição de cobertura dos 3 tools (measure_coverage.py), em lotes resistentes a
# crash. SÓ CPU. O script faz RESUME por coverage_measured.csv → o auto-chain
# retoma no projeto onde ficou quando bater o walltime de 4h (limite do dev-x86).
#
#   export MODEL=deepseek-coder-v2:16b; sbatch --export=ALL deucalion/run_coverage.sh
#   COV_TOOL=marta        limita a um tool (default: all)
#   ONLY_PROJECTS=a,b     limita a projetos
#   MAX_GEN=0             ABLAÇÃO do ciclo externo: mede só o 1.º ficheiro de
#                         teste de cada função (só afeta a MARTA). Escreve em
#                         coverage_measured_g0.csv e _cov_marta_g0/ — NÃO toca
#                         na medição canónica. Usar com COV_TOOL=marta.
# ─────────────────────────────────────────────────────────────────────────────

set -euo pipefail

MARTA_ROOT=/projects/F202407648IACDCF2/mario/MARTA
CONTAINER=/projects/F202407648IACDCF2/mario/containers/marta_benchmark.sif
PYDEPS=/projects/F202407648IACDCF2/mario/pydeps

export MODEL="${MODEL:-deepseek-coder-v2:16b}"
SAFE_MODEL=$(echo "$MODEL" | tr ':/' '__')
RES=/projects/F202407648IACDCF2/mario/results/$SAFE_MODEL
mkdir -p logs "$RES/_cov_scratch"

echo "=== cobertura  job=$SLURM_JOB_ID  tool=${COV_TOOL:-all}  results=$RES  max_gen=${MAX_GEN:-<todos>} ==="

_chained=0
chain() {
    if [ "$_chained" -eq 0 ]; then
        _chained=1
        echo "→ walltime: a encadear continuação (resume via coverage_measured.csv) ..."
        sbatch --parsable --dependency=afterany:"$SLURM_JOB_ID" \
            --export=ALL "$0" || echo "⚠️  sbatch da continuação falhou"
    fi
    exit 143
}
trap chain SIGTERM

srun -n1 singularity exec \
    --bind "$MARTA_ROOT:/opt/marta" \
    --bind "$RES:/data/results" \
    --bind "$PYDEPS:/data/pydeps" \
    --env "USER_PYTHON_PATH=/opt/conda/envs/test4py_env/bin/python" \
    --env "PYTHONPATH=/data/pydeps/sut:/data/pydeps/marta" \
    --env "COV_BATCH=${COV_BATCH:-50}" \
    --env "COV_SCRATCH=${COV_SCRATCH:-/data/results/_cov_scratch}" \
    --env "COV_BATCH_TIMEOUT=${COV_BATCH_TIMEOUT:-600}" \
    --env "ONLY_PROJECTS=${ONLY_PROJECTS:-}" \
    --env "PYTHONUNBUFFERED=1" \
    "$CONTAINER" /opt/conda/envs/test4py_env/bin/python \
    /opt/marta/scripts/measure_coverage.py --results /data/results \
    --tool "${COV_TOOL:-all}" ${MAX_GEN:+--max-gen $MAX_GEN} &

SRUN_PID=$!
EXIT_CODE=0
wait "$SRUN_PID" || EXIT_CODE=$?

echo "=== cobertura job $SLURM_JOB_ID terminou (exit $EXIT_CODE) ==="
if [ "$EXIT_CODE" -eq 137 ] || [ "$EXIT_CODE" -eq 9 ]; then
    R="${OOM_RETRIES:-0}"
    if [ "$R" -lt 5 ] && [ "$_chained" -eq 0 ]; then
        export OOM_RETRIES=$((R+1))
        echo "→ SIGKILL. Resubmissão automática ($OOM_RETRIES/5) ..."
        sbatch --parsable --export=ALL "$0" || echo "⚠️  falhou"
    fi
fi
exit $EXIT_CODE

#!/bin/bash
#SBATCH --job-name="mutmut"
#SBATCH --account=f202407648iacdcf2x
#SBATCH --partition=dev-x86
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=64G
#SBATCH --time=04:00:00
#SBATCH --output=logs/mutmut_%j.out
#SBATCH --signal=B:SIGTERM@120

# ─────────────────────────────────────────────────────────────────────────────
# Mutation testing (mutmut) sobre os 27 projetos × 3 tools. SÓ CPU (sem GPU/Ollama).
# O run_mutmut.py faz RESUME: salta combos já em mutmut.csv → o job sobrevive ao
# walltime e a continuação (auto-chain) retoma de onde parou. Por isso um walltime
# curto (4h, seguro em dev-x86) basta: encadeia até acabar os 81 combos.
#
# Modelo (escolhe o results dir): default 16b. Para outro modelo:
#   export MODEL=qwen2.5-coder:32b; sbatch --export=ALL deucalion/run_mutmut.sh
#
# MUTMUT_TOOL limita a um tool (marta|test4py_baseline|pynguin). ESSENCIAL para
# correr em PARALELO com uma geração: muta só o tool cujos testes estão ESTÁTICOS.
# Ex.: durante o re-run da marta → MUTMUT_TOOL=test4py_baseline.
# Este job é seguro em paralelo (não cria symlinks em /opt/marta nem toca no
# state.json do harness) — ao contrário do run_benchmark.sh/run_pynguin_cpu.sh,
# que partilham os symlinks baselines/harness e baselines/Results_*.
# ⚠️ Confirmar a partição CPU do teu cluster; dev-x86 é a que temos usado.
# ─────────────────────────────────────────────────────────────────────────────

set -euo pipefail

MARTA_ROOT=/projects/F202407648IACDCF2/mario/MARTA
CONTAINER=/projects/F202407648IACDCF2/mario/containers/marta_benchmark.sif
PYDEPS=/projects/F202407648IACDCF2/mario/pydeps

export MODEL="${MODEL:-deepseek-coder-v2:16b}"
SAFE_MODEL=$(echo "$MODEL" | tr ':/' '__')
RES=/projects/F202407648IACDCF2/mario/results/$SAFE_MODEL
mkdir -p logs

echo "=== mutmut  job=$SLURM_JOB_ID  model=$MODEL  results=$RES ==="

# Auto-chain via trap SIGTERM (120s antes do walltime). A continuação usa RESUME
# (salta o que já está em mutmut.csv). srun em background + wait p/ o trap disparar.
_chained=0
chain() {
    if [ "$_chained" -eq 0 ]; then
        _chained=1
        echo "→ walltime: a encadear continuação (resume via mutmut.csv) ..."
        sbatch --parsable --dependency=afterany:"$SLURM_JOB_ID" \
            --export=ALL "${CHAIN_SCRIPT:-$0}" || echo "⚠️  sbatch da continuação falhou"
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
    --env "MUTMUT_TIMEOUT=${MUTMUT_TIMEOUT:-1800}" \
    --env "MUTMUT_GREEN_TIMEOUT=${MUTMUT_GREEN_TIMEOUT:-90}" \
    --env "MUTMUT_SCRATCH=/data/results/_mutmut_scratch" \
    --env "PYTHONUNBUFFERED=1" \
    "$CONTAINER" /opt/conda/envs/test4py_env/bin/python \
    /opt/marta/scripts/run_mutmut.py --results /data/results ${MUTMUT_TOOL:+--tool "$MUTMUT_TOOL"} ${MUTMUT_PROJECT:+--project "$MUTMUT_PROJECT"} &

SRUN_PID=$!
EXIT_CODE=0
wait "$SRUN_PID" || EXIT_CODE=$?

echo "=== mutmut job $SLURM_JOB_ID terminou (exit $EXIT_CODE) ==="
# saída: $RES/mutmut.csv  (tool,project,status,score,killed,survived,...)
exit $EXIT_CODE

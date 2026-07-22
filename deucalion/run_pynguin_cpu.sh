#!/bin/bash
#SBATCH --job-name="pynguin_cpu"
#SBATCH --account=f202407648iacdcf2x
#SBATCH --partition=dev-x86
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=64G
#SBATCH --time=04:00:00
#SBATCH --output=logs/pynguin_cpu_%j.out
#SBATCH --signal=B:SIGTERM@120

# ─────────────────────────────────────────────────────────────────────────────
# PYNGUIN SEM GPU — o Pynguin é SBST puro (nenhuma chamada a LLM), por isso não
# precisa de GPU nem de Ollama. Corria no run_benchmark.sh (conta GPU ...cf2g,
# 455h restantes) a gastar orçamento à toa; aqui vai para a conta CPU (...cf2x,
# 3M horas, <1% usado) = essencialmente gratuito.
#
# Walltime curto (4h, seguro em dev-x86) + auto-chain: o harness tem resume
# POR-MÓDULO no state.json (chave pynguin/<proj>/<mod>), por isso encadeia até
# terminar os 486 módulos. A 600s/módulo são ~81h de busca → ~20 continuações.
#
# ⚠️ NUNCA correr ao mesmo tempo que um job que escreva o MESMO state.json
#    (race). Se o baseline/marta estiverem a correr no results dir do 16b, espera.
# ─────────────────────────────────────────────────────────────────────────────

set -euo pipefail

MARTA_ROOT=/projects/F202407648IACDCF2/mario/MARTA
CONTAINER=/projects/F202407648IACDCF2/mario/containers/marta_benchmark.sif
PYDEPS_DIR=/projects/F202407648IACDCF2/mario/pydeps
RESULTS_DIR=/projects/F202407648IACDCF2/mario/results

# MODEL só define a pasta de resultados (o Pynguin é independente do modelo).
export MODEL="${MODEL:-deepseek-coder-v2:16b}"
export TOOLS=pynguin
export PROJECTS="${PROJECTS:-}"
SAFE_MODEL=$(echo "$MODEL" | tr ':/' '__')
RUN_RESULTS="$RESULTS_DIR/$SAFE_MODEL"
mkdir -p "$RUN_RESULTS/harness" "$RUN_RESULTS/Results_Pynguin" logs

echo "=== Pynguin (CPU, sem GPU)  job=$SLURM_JOB_ID  results=$RUN_RESULTS ==="
echo "    search-time=${PYNGUIN_SEARCH_TIME:-600}s  algoritmo=${PYNGUIN_ALGORITHM:-default (DynaMOSA)}"

_chained=0
chain() {
    if [ "$_chained" -eq 0 ]; then
        _chained=1
        echo "→ walltime: a encadear continuação (resume por-módulo via state.json) ..."
        sbatch --parsable --dependency=afterany:"${SLURM_JOB_ID}" \
            --export=ALL "${CHAIN_SCRIPT:-$0}" || echo "⚠️  sbatch da continuação falhou"
    fi
    exit 143
}
trap chain SIGTERM

srun -n1 singularity exec \
    --bind "$MARTA_ROOT:/opt/marta" \
    --bind "$RUN_RESULTS:/data/results" \
    --bind "$PYDEPS_DIR:/data/pydeps" \
    --env "SAFE_MODEL=$SAFE_MODEL" \
    --env "ENV_PYNGUIN=/opt/conda/envs/pynguin_env" \
    --env "PYDEPS_SUT=/data/pydeps/sut" \
    --env "PYNGUIN_SEARCH_TIME=${PYNGUIN_SEARCH_TIME:-600}" \
    --env "PYNGUIN_ALGORITHM=${PYNGUIN_ALGORITHM:-}" \
    --env "PYTHONUNBUFFERED=1" \
    "$CONTAINER" bash -c '
        set -e
        cd /opt/marta
        ln -sfn /data/results/harness baselines/harness
        mkdir -p /data/results/Results_Pynguin
        ln -sfn /data/results/Results_Pynguin baselines/Results_Pynguin
        EXTRA=""
        [ -n "'"$PROJECTS"'" ] && EXTRA="$EXTRA --projects '"$PROJECTS"'"
        # timeout-pynguin alto: o kill timeout tem de exceder a busca (600s) +
        # overhead; o run_benchmark.py já faz max(timeout, busca+300).
        /opt/conda/envs/test4py_env/bin/python scripts/run_benchmark.py \
            --tools pynguin --timeout-pynguin 900 $EXTRA
    ' &

SRUN_PID=$!
EXIT_CODE=0
wait "$SRUN_PID" || EXIT_CODE=$?

echo "=== Pynguin CPU job $SLURM_JOB_ID terminou (exit $EXIT_CODE) ==="
# Mesmo tratamento de SIGKILL (kill externo em nó partilhado) que o run_benchmark.sh
if [ "$EXIT_CODE" -eq 137 ] || [ "$EXIT_CODE" -eq 9 ]; then
    OOM_RETRIES="${OOM_RETRIES:-0}"
    if [ "$OOM_RETRIES" -lt 5 ] && [ "$_chained" -eq 0 ]; then
        export OOM_RETRIES=$((OOM_RETRIES+1))
        echo "→ SIGKILL. Resubmissão automática ($OOM_RETRIES/5) ..."
        sbatch --parsable --export=ALL "${CHAIN_SCRIPT:-$0}" || echo "⚠️  falhou"
    fi
fi
exit $EXIT_CODE

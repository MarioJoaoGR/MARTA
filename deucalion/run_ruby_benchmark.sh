#!/bin/bash
#SBATCH --job-name="marta_ruby"
#SBATCH --account=f202407648iacdcf2g
#SBATCH --partition=normal-a100-40
#SBATCH --nodes=1
#SBATCH --gpus=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=200G
#SBATCH --time=47:30:00
#SBATCH --output=logs/ruby_%j.out
#SBATCH --signal=B:SIGTERM@120
# ─────────────────────────────────────────────────────────────────────
# Benchmark MARTA-Ruby sobre o corpus da camada 7 (tamanho por decidir).
# Os alvos e o ambiente de cada gem vêm do projetos.json (camada 7); o harness
# recusa-se a correr gems que não estejam lá E preparadas, para nunca acontecer
# tomar a gem inteira como alvo (dezenas de milhares de métodos em vez dos do corpus).
#
# Mesma engenharia do lado Python: auto-chain no SIGTERM, resume via state.json,
# retry em OOM.
#
# MODELO POR DECIDIR (16B vs 32B). Medido nos mesmos 10 projetos do lado Python:
# o 32B é 3,4x mais lento na geração, e o corpus inteiro a 32B (~340 GPU-h) não
# cabe nas horas disponíveis. O 236B está fora (4 GPUs e muito mais lento).
#   16B:  sbatch deucalion/run_ruby_benchmark.sh
#   32B:  MODEL=qwen2.5-coder:32b sbatch --export=ALL deucalion/run_ruby_benchmark.sh
#
# FASES: `generate` precisa de GPU, `measure` não. Para não gastar horas de GPU a
# medir cobertura, correr PHASE=generate aqui e PHASE=measure na conta de CPU.
# ─────────────────────────────────────────────────────────────────────

set -euo pipefail

# ============================================================================
# CONFIGURAÇÃO
# ============================================================================
MARTA_ROOT="/projects/F202407648IACDCF2/mario/MARTA"
CONTAINER="/projects/F202407648IACDCF2/mario/containers/marta_benchmark.sif"
OLLAMA_DIR="/projects/F202407648IACDCF2/mario/ollama_models"
RESULTS_DIR="/projects/F202407648IACDCF2/mario/results_ruby"
PYDEPS_DIR="/projects/F202407648IACDCF2/mario/pydeps"
HF_CACHE_DIR="/projects/F202407648IACDCF2/mario/hf_cache"
# Projetos preparados COM REDE no nó de login (ver prepare_ruby_projects.py), e
# depois VERIFICADOS (verifica_ambiente.py) — sem a verificação não se sabe se os
# módulos carregam pela ferramenta neste ambiente.
RUBY_PROJECTS="/projects/F202407648IACDCF2/mario/ruby_projects"
# Toolchain Ruby (>=3.3 p/ Prism) — no container ou instalada em /projects.
RUBY_ROOT="${RUBY_ROOT:-/projects/F202407648IACDCF2/mario/ruby-3.4.10}"

export MODEL="${MODEL:-deepseek-coder-v2:16b}"
export PROJECTS="${PROJECTS:-}"     # vazio = todas as gems do corpus preparadas
export NUM_ROUNDS="${NUM_ROUNDS:-3}"
export LIMIT="${LIMIT:-}"           # p/ smoke run (ex.: LIMIT=5)
export PHASE="${PHASE:-all}"        # all | generate | measure
export MARTA_SEM_GRAFO="${MARTA_SEM_GRAFO:-0}"   # 1 = braço da ablação do grafo
# Janela de contexto do Ollama. SEM ISTO fica a do modelo por omissão e um prompt
# maior é cortado EM SILÊNCIO — o modelo responde a um prompt truncado e nada no
# log o diz. A telemetria por chamada mostra se algum prompt se aproxima daqui.
export OLLAMA_CTX="${OLLAMA_CTX:-16384}"

mkdir -p "$OLLAMA_DIR" logs

SAFE_MODEL=$(echo "$MODEL" | tr ':/' '__')
RUN_RESULTS="$RESULTS_DIR/$SAFE_MODEL"
mkdir -p "$RUN_RESULTS/harness" "$RUN_RESULTS/run_results"

PORT_SUFFIX="${SLURM_JOB_ID: -4}"
OLLAMA_PORT="1${PORT_SUFFIX}"

echo "================================================================="
echo " MARTA-Ruby Benchmark — corpus de 500 módulos (camada 7)"
echo "  Job ID:    $SLURM_JOB_ID"
echo "  Model:     $MODEL   (contexto $OLLAMA_CTX)"
echo "  Fase:      $PHASE   Ablação (sem grafo): $MARTA_SEM_GRAFO"
echo "  Projects:  ${PROJECTS:-(todas as preparadas)}"
echo "  Rondas:    $NUM_ROUNDS   Limite métodos: ${LIMIT:-(sem limite)}"
echo "  Ruby proj: $RUBY_PROJECTS"
echo "  Output:    $RUN_RESULTS"
echo "  Ollama:    127.0.0.1:$OLLAMA_PORT"
echo "================================================================="

if [ ! -f "$RUBY_PROJECTS/manifest.json" ]; then
    echo "❌ $RUBY_PROJECTS/manifest.json não existe. No nó de LOGIN (tem rede):"
    echo "   python -m benchmark.prepare_ruby_projects --out $RUBY_PROJECTS"
    echo "   python -m benchmark.verifica_ambiente   --projects-dir $RUBY_PROJECTS"
    exit 2
fi

ml OpenMPI/5.0.3-GCC-13.3.0 CUDA/11.8.0 NCCL/2.20.5-GCCcore-13.3.0-CUDA-12.4.0

# ============================================================================
# AUTO-CHAIN via trap SIGTERM (idêntico ao harness Python)
# O harness Ruby apanha SIGTERM, grava state.json e sai 143; a continuação
# retoma (salta os projetos já "ok"). srun em background + wait para o trap
# disparar de imediato.
# ============================================================================
_chained=0
chain_continuation() {
    if [ "$_chained" -eq 0 ]; then
        _chained=1
        echo "→ SIGTERM (walltime). A submeter continuação ..."
        sbatch --parsable --dependency=afterany:"${SLURM_JOB_ID}" \
            --export=ALL "${CHAIN_SCRIPT:-$0}" || echo "⚠️  sbatch da continuação falhou"
    fi
    exit 143
}
trap chain_continuation SIGTERM

srun -n1 singularity exec --nv \
    --bind "$MARTA_ROOT:/opt/marta" \
    --bind "$OLLAMA_DIR:/data/ollama" \
    --bind "$RUN_RESULTS:/data/results" \
    --bind "$PYDEPS_DIR:/data/pydeps" \
    --bind "$HF_CACHE_DIR:/data/hf_cache" \
    --bind "$RUBY_PROJECTS:/data/ruby_projects" \
    --bind "$RUBY_ROOT:/opt/ruby" \
    --env "MODEL=$MODEL" \
    --env "OLLAMA_MODELS=/data/ollama" \
    --env "OLLAMA_HOST=127.0.0.1:$OLLAMA_PORT" \
    --env "OPENAI_API_BASE=http://127.0.0.1:$OLLAMA_PORT/v1" \
    --env "OPENAI_API_KEY=ollama" \
    --env "TRANSFORMER_PATH=BAAI/bge-large-en-v1.5" \
    --env "USER_PYTHON_PATH=/opt/conda/envs/test4py_env/bin/python" \
    --env "SAFE_MODEL=$SAFE_MODEL" \
    --env "MARTA_RUBY_BIN=/opt/ruby/bin/ruby" \
    --env "MARTA_RSPEC_BIN=/opt/ruby/bin/rspec" \
    --env "PYDEPS_MARTA=/data/pydeps/marta" \
    --env "EMBED_DEVICE=cpu" \
    --env "HF_HOME=/data/hf_cache" \
    --env "HF_HUB_OFFLINE=1" \
    --env "TRANSFORMERS_OFFLINE=1" \
    --env "OLLAMA_FLASH_ATTENTION=0" \
    --env "OLLAMA_CONTEXT_LENGTH=$OLLAMA_CTX" \
    --env "OLLAMA_KEEP_ALIVE=-1" \
    --env "MARTA_SEM_GRAFO=$MARTA_SEM_GRAFO" \
    --env "PYTHONUNBUFFERED=1" \
    "$CONTAINER" bash -c '
        set -e
        cd /opt/marta
        export PATH="/opt/ruby/bin:$PATH"

        echo "→ Ruby: $("$MARTA_RUBY_BIN" -v 2>&1 | head -1)"
        "$MARTA_RUBY_BIN" -e "require \"prism\"; puts \"   prism OK \" + Prism::VERSION" \
            || { echo "❌ Prism indisponível (precisa de Ruby >= 3.3)"; exit 2; }

        echo "→ A iniciar Ollama em $OLLAMA_HOST (contexto $OLLAMA_CONTEXT_LENGTH, keep_alive -1) ..."
        ollama serve > /data/results/ollama_server.log 2>&1 &
        OLLAMA_PID=$!
        # Sondagem em vez de `sleep 30`: num nó carregado 30s podem não chegar, e
        # a primeira chamada falhava sem razão visível.
        for i in $(seq 1 60); do
            ollama list >/dev/null 2>&1 && break
            sleep 2
        done
        ollama list >/dev/null 2>&1 || { echo "❌ Ollama não respondeu em 120s"; exit 2; }
        echo "→ Garantir modelo $MODEL (pull-on-miss) ..."
        ollama show "$MODEL" >/dev/null 2>&1 || ollama pull "$MODEL"

        EXTRA=""
        [ -n "'"$PROJECTS"'" ] && EXTRA="$EXTRA --projects '"$PROJECTS"'"
        [ -n "'"$LIMIT"'" ] && EXTRA="$EXTRA --limit '"$LIMIT"'"

        echo "→ Arrancar harness Ruby (resume automático via state.json) ..."
        PYTHONPATH="/data/pydeps/marta:/opt/marta:${PYTHONPATH:-}" \
        /opt/conda/envs/test4py_env/bin/python -m benchmark.run_ruby_benchmark \
            --projects-dir /data/ruby_projects \
            --out-dir /data/results \
            --phase '"$PHASE"' \
            --num '"$NUM_ROUNDS"' $EXTRA

        EXIT_CODE=$?
        echo "→ Encerrar Ollama ..."
        kill $OLLAMA_PID 2>/dev/null || true
        exit $EXIT_CODE
    ' &

SRUN_PID=$!
EXIT_CODE=0
wait "$SRUN_PID" || EXIT_CODE=$?

echo "================================================================="
echo " Job $SLURM_JOB_ID terminou (exit $EXIT_CODE)"
echo "================================================================="

# Retry em SIGKILL (OOM por spec gerado memory-bomb) — mesma lógica do Python.
if [ "$EXIT_CODE" -eq 137 ] || [ "$EXIT_CODE" -eq 9 ]; then
    OOM_RETRIES="${OOM_RETRIES:-0}"
    if [ "$OOM_RETRIES" -lt 5 ] && [ "$_chained" -eq 0 ]; then
        export OOM_RETRIES=$((OOM_RETRIES+1))
        echo "→ SIGKILL (OOM provável). Resubmissão automática ($OOM_RETRIES/5) ..."
        sbatch --parsable --export=ALL "${CHAIN_SCRIPT:-$0}" \
            || echo "⚠️  resubmissão automática falhou"
    else
        echo "⚠️  SIGKILL com OOM_RETRIES=$OOM_RETRIES — intervir manualmente"
    fi
fi
exit $EXIT_CODE

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
# Benchmark MARTA-Ruby. Mesma engenharia do run_benchmark.sh (Python):
# auto-chain no SIGTERM, resume via state.json, retry em OOM.
#
# MODELO AINDA POR DECIDIR (16B vs 236B). Parametrizado por env var:
#   16B:  sbatch deucalion/run_ruby_benchmark.sh
#   236B: export MODEL=deepseek-coder-v2:236b
#         sbatch --partition=normal-a100-80 --gpus=4 --mem=400G \
#                --export=ALL deucalion/run_ruby_benchmark.sh
#   (o wrapper 236B do lado Python é o padrão a seguir se se quiser fixar)
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
# Projetos Ruby preparados COM REDE no login node (ver prepare_ruby_projects.py):
#   python -m benchmark.prepare_ruby_projects --out $RUBY_PROJECTS
# Contêm o clone no commit fixado + .gem_home com as runtime deps (offline-ready).
RUBY_PROJECTS="/projects/F202407648IACDCF2/mario/ruby_projects"
# Toolchain Ruby (>=3.3 p/ Prism) — no container ou instalada em /projects.
RUBY_ROOT="${RUBY_ROOT:-/projects/F202407648IACDCF2/mario/ruby-3.4.10}"

export MODEL="${MODEL:-deepseek-coder-v2:16b}"
export PROJECTS="${PROJECTS:-}"     # vazio = todos os do manifest
export NUM_ROUNDS="${NUM_ROUNDS:-3}"
export LIMIT="${LIMIT:-}"           # p/ smoke run (ex.: LIMIT=5)

mkdir -p "$OLLAMA_DIR" logs

SAFE_MODEL=$(echo "$MODEL" | tr ':/' '__')
RUN_RESULTS="$RESULTS_DIR/$SAFE_MODEL"
mkdir -p "$RUN_RESULTS/harness" "$RUN_RESULTS/run_results"

PORT_SUFFIX="${SLURM_JOB_ID: -4}"
OLLAMA_PORT="1${PORT_SUFFIX}"

echo "================================================================="
echo " MARTA-Ruby Benchmark (Fase 1: repos Ruby do SWE-bench Multilingual)"
echo "  Job ID:    $SLURM_JOB_ID"
echo "  Model:     $MODEL"
echo "  Projects:  ${PROJECTS:-(todos do manifest)}"
echo "  Rondas:    $NUM_ROUNDS   Limite métodos: ${LIMIT:-(sem limite)}"
echo "  Ruby proj: $RUBY_PROJECTS"
echo "  Output:    $RUN_RESULTS"
echo "  Ollama:    127.0.0.1:$OLLAMA_PORT"
echo "================================================================="

if [ ! -d "$RUBY_PROJECTS" ]; then
    echo "❌ $RUBY_PROJECTS não existe. Correr no login node (tem rede):"
    echo "   python -m benchmark.prepare_ruby_projects --out $RUBY_PROJECTS"
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
    --env "PYTHONUNBUFFERED=1" \
    "$CONTAINER" bash -c '
        set -e
        cd /opt/marta
        export PATH="/opt/ruby/bin:$PATH"

        echo "→ Ruby: $("$MARTA_RUBY_BIN" -v 2>&1 | head -1)"
        "$MARTA_RUBY_BIN" -e "require \"prism\"; puts \"   prism OK \" + Prism::VERSION" \
            || { echo "❌ Prism indisponível (precisa de Ruby >= 3.3)"; exit 2; }

        echo "→ A iniciar Ollama em $OLLAMA_HOST ..."
        ollama serve > /data/results/ollama_server.log 2>&1 &
        OLLAMA_PID=$!
        sleep 30
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

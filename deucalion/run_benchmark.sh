#!/bin/bash
#SBATCH --job-name="marta_bench"
#SBATCH --account=f202407648iacdcf2g
#SBATCH --partition=normal-a100-40
#SBATCH --nodes=1
#SBATCH --gpus=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=64G
#SBATCH --time=47:30:00
#SBATCH --output=logs/bench_%j.out
#SBATCH --signal=B:SIGTERM@120
# ─────────────────────────────────────────────────────────────────────
# Signal SIGTERM 120s antes do walltime → SIGTERM handler do harness
# grava state.json e sai com exit 143. Job dependente faz resume.
# ─────────────────────────────────────────────────────────────────────

set -euo pipefail

# ============================================================================
# CONFIGURAÇÃO
# ============================================================================
MARTA_ROOT="/projects/F202407648IACDCF2/mario/MARTA"
CONTAINER="/projects/F202407648IACDCF2/mario/containers/marta_benchmark.sif"
OLLAMA_DIR="/projects/F202407648IACDCF2/mario/ollama_models"
RESULTS_DIR="/projects/F202407648IACDCF2/mario/results"

# Modelo via env var (default: DeepSeek-Coder-V2 16B Lite).
# Para o run de 236B: sbatch --export=MODEL=deepseek-coder-v2:236b,... run_benchmark.sh
MODEL="${MODEL:-deepseek-coder-v2:16b}"
TOOLS="${TOOLS:-pynguin,marta,test4py_baseline}"
PROJECTS="${PROJECTS:-}"          # vazio = todos os 27 projetos do CM
TIMEOUT_PYNGUIN="${TIMEOUT_PYNGUIN:-300}"

mkdir -p "$OLLAMA_DIR" logs

# Sanitizar o nome do modelo para usar em paths
SAFE_MODEL=$(echo "$MODEL" | tr ':/' '__')
RUN_RESULTS="$RESULTS_DIR/$SAFE_MODEL"
# Criar harness/ e Results_*/ ANTES de o container fazer os symlinks — caso
# contrário ln -sfn cria symlinks dangling e Python falha o mkdir(exist_ok=True).
mkdir -p "$RUN_RESULTS/harness" \
         "$RUN_RESULTS/Results_Pynguin" \
         "$RUN_RESULTS/Results_Test4PyBaseline" \
         "$RUN_RESULTS/Results_MARTA"

# Porta única por job (evita colisão entre jobs do mesmo utilizador)
PORT_SUFFIX="${SLURM_JOB_ID: -4}"
OLLAMA_PORT="1${PORT_SUFFIX}"

echo "================================================================="
echo " MARTA Benchmark CM"
echo "  Job ID:    $SLURM_JOB_ID"
echo "  Model:     $MODEL"
echo "  Tools:     $TOOLS"
echo "  Projects:  ${PROJECTS:-(all 27 CM)}"
echo "  Container: $CONTAINER"
echo "  Output:    $RUN_RESULTS"
echo "  Ollama:    127.0.0.1:$OLLAMA_PORT"
echo "================================================================="

# ============================================================================
# MÓDULOS / ENVIRONMENT
# ============================================================================
ml OpenMPI/5.0.3-GCC-13.3.0 CUDA/11.8.0 NCCL/2.20.5-GCCcore-13.3.0-CUDA-12.4.0

# ============================================================================
# EXECUÇÃO NO CONTAINER
# ============================================================================
# Bind mounts:
#   - MARTA source       → /opt/marta  (read+write para state.json, logs)
#   - Ollama models      → /data/ollama
#   - Results            → /data/results (output)
#
# Env vars passadas:
#   - MODEL              (para .env da MARTA)
#   - OLLAMA_MODELS      (onde Ollama persiste os modelos puxados)
#   - OPENAI_API_BASE    (aponta ao Ollama deste job)
#   - OPENAI_API_KEY     (Ollama não verifica mas a OpenAI lib exige)
#   - TRANSFORMER_PATH   (BAAI/bge-large-en-v1.5, cache pré-baked em /opt/hf_cache)
#   - USER_PYTHON_PATH   (interpretador certo do env conda da MARTA)

srun -n1 singularity exec --nv \
    --bind "$MARTA_ROOT:/opt/marta" \
    --bind "$OLLAMA_DIR:/data/ollama" \
    --bind "$RUN_RESULTS:/data/results" \
    --env "MODEL=$MODEL" \
    --env "OLLAMA_MODELS=/data/ollama" \
    --env "OLLAMA_HOST=127.0.0.1:$OLLAMA_PORT" \
    --env "OPENAI_API_BASE=http://127.0.0.1:$OLLAMA_PORT/v1" \
    --env "OPENAI_API_KEY=ollama" \
    --env "TRANSFORMER_PATH=BAAI/bge-large-en-v1.5" \
    --env "USER_PYTHON_PATH=/opt/conda/envs/test4py_env/bin/python" \
    --env "SAFE_MODEL=$SAFE_MODEL" \
    --env "ENV_PYNGUIN=/opt/conda/envs/pynguin_env" \
    --env "ENV_TEST4PY_BASELINE=/opt/conda/envs/test4py_baseline_env" \
    --env "ENV_MARTA=/opt/conda/envs/test4py_env" \
    "$CONTAINER" bash -c '
        set -e
        cd /opt/marta

        echo "→ A iniciar servidor Ollama em $OLLAMA_HOST ..."
        ollama serve > /data/results/ollama_server.log 2>&1 &
        OLLAMA_PID=$!
        sleep 30

        echo "→ Garantir que modelo $MODEL existe (pull-on-miss) ..."
        ollama show "$MODEL" >/dev/null 2>&1 || ollama pull "$MODEL"

        # NOTA: prepare_envs.py NÃO é chamado em Deucalion — os 27 projetos
        # do CM já foram pip-installed nos 3 conda envs em build-time do .sif
        # (ver Singularity.def secção 3a). Se algum projeto tiver falhado no
        # build, é detectado em runtime quando MARTA falhar a importar — aí
        # cai-se no fallback de adicionar /opt/marta/baselines/codamosa/replication/
        # test-apps/$PROJECT ao PYTHONPATH (via patch futuro se preciso).

        echo "→ Arrancar harness ..."
        # state.json e logs vão para /data/results/harness/ (bind mount)
        ln -sfn /data/results/harness baselines/harness

        # Outputs Results_<TOOL>/ → /data/results/Results_<TOOL>/ via symlink
        for t in Pynguin Test4PyBaseline MARTA; do
            mkdir -p "/data/results/Results_$t"
            ln -sfn "/data/results/Results_$t" "baselines/Results_$t"
        done

        # Argumentos opcionais
        EXTRA=""
        [ -n "'"$PROJECTS"'" ] && EXTRA="$EXTRA --projects '"$PROJECTS"'"
        # Nota: resume é automático no harness (lê state.json e salta o que está "ok")
        EXTRA="$EXTRA --tools '"$TOOLS"' --timeout-pynguin '"$TIMEOUT_PYNGUIN"'"

        /opt/conda/envs/test4py_env/bin/python scripts/run_benchmark.py $EXTRA

        EXIT_CODE=$?

        echo "→ Encerrar Ollama ..."
        kill $OLLAMA_PID 2>/dev/null || true

        exit $EXIT_CODE
    '

EXIT_CODE=$?
echo "================================================================="
echo " Job $SLURM_JOB_ID terminou (exit $EXIT_CODE)"
echo "================================================================="

# ============================================================================
# AUTO-CHAIN: se o harness saiu por SIGTERM (143) ainda há trabalho para fazer.
# Submeter automaticamente um job dependente que retoma.
# ============================================================================
if [ $EXIT_CODE -eq 143 ]; then
    echo "→ Walltime atingido. A submeter job de continuação ..."
    NEXT_JOB=$(sbatch --parsable --dependency=afterany:$SLURM_JOB_ID \
        --export=ALL,MODEL=$MODEL,TOOLS=$TOOLS,PROJECTS=$PROJECTS \
        "$0")
    echo "  Próximo job: $NEXT_JOB"
fi

exit $EXIT_CODE

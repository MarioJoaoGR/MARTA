#!/bin/bash
#SBATCH --job-name="marta_bench"
#SBATCH --account=f202407648iacdcf2g
#SBATCH --partition=normal-a100-40
#SBATCH --nodes=1
#SBATCH --gpus=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
# 200G (nó tem ~500G): absorve picos de RAM da análise PyCG e, sobretudo, de
# testes gerados memory-bomb (ex: tqdm(range(1e10)) com input fuzzed) que com
# 64G davam OOM-kill (-9) do job inteiro. Ver falha marta/tqdm.
#SBATCH --mem=200G
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
# Deps pesadas da MARTA/test4dt (torch, transformers, chromadb, langchain...)
# que NÃO estão no .sif base. Instaladas via `pip install --target` em
# /projects/.../pydeps/{marta,baseline} e injetadas via PYTHONPATH (ver README
# secção "Deps pesadas (pydeps)"). Overlay/fakeroot não funcionam no Deucalion.
PYDEPS_DIR="/projects/F202407648IACDCF2/mario/pydeps"
# HF cache (BAAI embedding) copiada para writable — o /opt/hf_cache do .sif é
# read-only e o transformers precisa de escrever locks/migração.
HF_CACHE_DIR="/projects/F202407648IACDCF2/mario/hf_cache"

# Modelo via env var (default: DeepSeek-Coder-V2 16B Lite).
# Para o run de 236B: sbatch --export=MODEL=deepseek-coder-v2:236b,... run_benchmark.sh
# export: para o --export=ALL da continuação (auto-chain) os herdar SEM os meter
# em --export=KEY=VAL (valores com vírgula como TOOLS=pynguin,marta seriam
# partidos pelo sbatch). Passar TOOLS multi-valor: `export TOOLS=...; sbatch --export=ALL`.
export MODEL="${MODEL:-deepseek-coder-v2:16b}"
export TOOLS="${TOOLS:-pynguin,marta,test4py_baseline}"
export PROJECTS="${PROJECTS:-}"          # vazio = todos os 27 projetos do CM
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
# AUTO-CHAIN via trap SIGTERM
# --signal=B:SIGTERM@120 envia SIGTERM à BASH 120s antes do walltime. Sem trap,
# a bash morria sem encadear (bug anterior: o bloco no fim com EXIT_CODE==143
# era inalcançável porque a bash nunca lá chegava). Apanhamos o SIGTERM aqui e
# submetemos a continuação. Resume é seguro: state.json (por-projeto) + caches
# (grafo/análise em Results_<tool>/<proj>/) persistem.
# IMPORTANTE: o srun corre em BACKGROUND + wait — com srun em foreground a bash
# adiaria o trap até o srun terminar (= nunca, até ao SIGKILL do walltime).
# ============================================================================
_chained=0
chain_continuation() {
    if [ "$_chained" -eq 0 ]; then
        _chained=1
        echo "→ SIGTERM (walltime). A submeter continuação ..."
        # --export=ALL só: MODEL/TOOLS/PROJECTS já estão exportados → herdados.
        # NÃO os meter em --export=KEY=VAL: valores com vírgula (TOOLS=pynguin,marta)
        # são partidos pelo sbatch (a vírgula separa vars) → só apanhava o 1º.
        # Foi esse bug que fez o 1692915 correr só pynguin (TOOLS ficou =pynguin).
        #
        # CHAIN_SCRIPT: qual script reenviar. O run_benchmark_236b.sh faz
        # `exec bash run_benchmark.sh` → depois do exec o $0 aqui é
        # run_benchmark.sh, cujo header é a100-40/gpus=1/mem=200G. Se a
        # continuação do 236B reenviasse esse $0, ia p/ a partição errada e
        # morria (modelo 132GB não cabe em a100-40, e 200G dava OOM). O wrapper
        # 236B exporta CHAIN_SCRIPT=<ele próprio> → a continuação herda o header
        # a100-80/gpus=4/mem=400G correto. No run 16B, CHAIN_SCRIPT não existe
        # → cai no $0 = run_benchmark.sh (header a100-40 correto p/ 16B).
        sbatch --parsable --dependency=afterany:"${SLURM_JOB_ID}" \
            --export=ALL "${CHAIN_SCRIPT:-$0}" || echo "⚠️  sbatch da continuação falhou"
    fi
    exit 143
}
trap chain_continuation SIGTERM

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
    --bind "$PYDEPS_DIR:/data/pydeps" \
    --bind "$HF_CACHE_DIR:/data/hf_cache" \
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
    --env "PYDEPS_MARTA=/data/pydeps/marta" \
    --env "PYDEPS_BASELINE=/data/pydeps/baseline" \
    --env "PYDEPS_SUT=/data/pydeps/sut" \
    --env "EMBED_DEVICE=cpu" \
    --env "HF_HOME=/data/hf_cache" \
    --env "HF_HUB_OFFLINE=1" \
    --env "TRANSFORMERS_OFFLINE=1" \
    --env "OLLAMA_FLASH_ATTENTION=0" \
    --env "PYTHONUNBUFFERED=1" \
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
    ' &

# srun em background; wait é interrompível → o trap chain_continuation dispara
# no SIGTERM (120s antes do walltime) e submete a continuação.
SRUN_PID=$!
EXIT_CODE=0
wait "$SRUN_PID" || EXIT_CODE=$?

echo "================================================================="
echo " Job $SLURM_JOB_ID terminou (exit $EXIT_CODE)"
echo "================================================================="
# Auto-chain é via trap SIGTERM (chain_continuation), ~120s antes do walltime.
# Se chegámos aqui sem SIGTERM, ou o harness terminou normalmente (não encadeia)
# ou a TASK foi morta por SIGKILL (exit 137/9) — tipicamente o OOM-killer por um
# teste gerado memory-bomb (ver baseline/sanic, job 1753101). O SIGKILL não é
# apanhável → o trap não dispara → sem isto o run morria silenciosamente a meio.
# Resubmissão é segura (resume via state.json salta o que está ok) e NEUTRA para
# a comparação (infra, não muda nenhum tool). OOM_RETRIES trava loops (projeto
# que OOM sempre): esgota-se ao fim de 5 e fica para intervenção manual.
# Nota: `scancel --batch --signal=KILL` mata a própria bash → este bloco nem
# corre → o kill manual continua a funcionar como sempre.
if [ "$EXIT_CODE" -eq 137 ] || [ "$EXIT_CODE" -eq 9 ]; then
    OOM_RETRIES="${OOM_RETRIES:-0}"
    if [ "$OOM_RETRIES" -lt 5 ] && [ "$_chained" -eq 0 ]; then
        export OOM_RETRIES=$((OOM_RETRIES+1))
        echo "→ Task morta por SIGKILL (OOM provável). Resubmissão automática ($OOM_RETRIES/5) ..."
        sbatch --parsable --export=ALL "${CHAIN_SCRIPT:-$0}" \
            || echo "⚠️  resubmissão automática falhou"
    else
        echo "⚠️  SIGKILL com OOM_RETRIES=$OOM_RETRIES — sem resubmissão (intervir manualmente)"
    fi
fi
exit $EXIT_CODE

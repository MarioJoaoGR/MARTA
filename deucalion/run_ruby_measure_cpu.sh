#!/bin/bash
#SBATCH --job-name="marta_ruby_cov"
#SBATCH --account=f202407648iacdcf2x
#SBATCH --partition=dev-x86
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=64G
#SBATCH --time=04:00:00
#SBATCH --output=logs/ruby_cov_%j.out
#SBATCH --signal=B:SIGTERM@120
# ─────────────────────────────────────────────────────────────────────
# MEDIÇÃO DA COBERTURA SEM GPU. A fase `measure` do harness só corre RSpec e o
# Coverage do Ruby: não chama o modelo. No run_ruby_benchmark.sh (conta GPU) isso
# era tempo de GPU parada. Aqui vai para a conta de CPU (...cf2x, ~3M horas).
#
# Mesmo desenho do job de CPU do Pynguin: walltime curto (4h, seguro em dev-x86)
# e encadeamento no SIGTERM, com retoma por gem.
#
# Pode correr AO MESMO TEMPO que a geração: a medição grava no seu próprio
# state_medicao.json e só LÊ o state.json da geração (escrever os dois no mesmo
# ficheiro já comeu resultados no lado Python). Mede o que já estiver gerado.
#
#   PHASE da geração e da medição com o MESMO modelo e o MESMO braço:
#     MODEL=qwen2.5-coder:32b sbatch --export=ALL deucalion/run_ruby_measure_cpu.sh
#     MARTA_SEM_GRAFO=1 sbatch --export=ALL deucalion/run_ruby_measure_cpu.sh
#
#   ACOMPANHAR=1: ao terminar, se a geração ainda tiver gems por acabar, volta a
#   agendar-se para daqui a 30 min. A medição vai seguindo a geração sozinha.
# ─────────────────────────────────────────────────────────────────────

set -euo pipefail

MARTA_ROOT=/projects/F202407648IACDCF2/mario/MARTA
CONTAINER=/projects/F202407648IACDCF2/mario/containers/marta_benchmark.sif
PYDEPS_DIR=/projects/F202407648IACDCF2/mario/pydeps
RESULTS_DIR=/projects/F202407648IACDCF2/mario/results_ruby
RUBY_PROJECTS=/projects/F202407648IACDCF2/mario/ruby_projects
RUBY_ROOT="${RUBY_ROOT:-/projects/F202407648IACDCF2/mario/ruby-3.4.10}"
# A medição copia cada projeto para uma pasta descartável antes de correr os specs
# (os testes gerados podem apagar ficheiros). Numa pasta de /projects, não no /tmp
# do nó: a cópia de um monorepo tem centenas de MB.
SCRATCH_DIR=/projects/F202407648IACDCF2/mario/scratch_cov

# O MODEL só escolhe a pasta de resultados: tem de ser o da geração a medir.
export MODEL="${MODEL:-qwen2.5-coder:32b}"
export PROJECTS="${PROJECTS:-}"
export MARTA_SEM_GRAFO="${MARTA_SEM_GRAFO:-0}"
export ACOMPANHAR="${ACOMPANHAR:-0}"
SAFE_MODEL=$(echo "$MODEL" | tr ':/' '__')
RUN_RESULTS="$RESULTS_DIR/$SAFE_MODEL"
mkdir -p "$RUN_RESULTS/harness" "$SCRATCH_DIR" logs

echo "=== MARTA-Ruby medição (CPU)  job=$SLURM_JOB_ID  modelo=$MODEL  sem_grafo=$MARTA_SEM_GRAFO ==="
echo "    resultados=$RUN_RESULTS  acompanhar=$ACOMPANHAR"

if [ ! -f "$RUBY_PROJECTS/manifest.json" ]; then
    echo "❌ $RUBY_PROJECTS/manifest.json não existe: correr o prepare e o verificador primeiro"
    exit 2
fi

_chained=0
chain() {
    if [ "$_chained" -eq 0 ]; then
        _chained=1
        echo "→ walltime: a encadear continuação (retoma por gem via state_medicao.json) ..."
        sbatch --parsable --dependency=afterany:"${SLURM_JOB_ID}" \
            --export=ALL "${CHAIN_SCRIPT:-$0}" || echo "⚠️  sbatch da continuação falhou"
    fi
    exit 143
}
trap chain SIGTERM

_harness() {
    srun -n1 singularity exec \
        --bind "$MARTA_ROOT:/opt/marta" \
        --bind "$RUN_RESULTS:/data/results" \
        --bind "$PYDEPS_DIR:/data/pydeps" \
        --bind "$RUBY_PROJECTS:/data/ruby_projects" \
        --bind "$RUBY_ROOT:/opt/ruby" \
        --bind "$SCRATCH_DIR:/data/scratch" \
        --bind "/usr/share/zoneinfo:/usr/share/zoneinfo:ro" \
        --env "MODEL=$MODEL" \
        --env "LANG=C.UTF-8" --env "LC_ALL=C.UTF-8" \
        --env "MARTA_RUBY_BIN=/opt/ruby/bin/ruby" \
        --env "MARTA_RSPEC_BIN=/opt/ruby/bin/rspec" \
        --env "MARTA_SEM_GRAFO=$MARTA_SEM_GRAFO" \
        --env "COV_SCRATCH=/data/scratch" \
        --env "PYTHONUNBUFFERED=1" \
        "$CONTAINER" bash -c '
            set -e
            cd /opt/marta
            export PATH="/opt/ruby/bin:$PATH"
            export HOME=/data/results/.home XDG_CACHE_HOME=/data/results/.home/.cache   # o $HOME da conta está cheio
            mkdir -p "$HOME"
            EXTRA=""
            [ -n "'"$PROJECTS"'" ] && EXTRA="$EXTRA --projects '"$PROJECTS"'"
            PYTHONPATH="/data/pydeps/marta:/opt/marta:${PYTHONPATH:-}" \
            /opt/conda/envs/test4py_env/bin/python -m benchmark.run_ruby_benchmark \
                --projects-dir /data/ruby_projects --out-dir /data/results \
                '"$*"' $EXTRA
        '
}

_harness --phase measure &
SRUN_PID=$!
EXIT_CODE=0
wait "$SRUN_PID" || EXIT_CODE=$?

echo "=== medição CPU $SLURM_JOB_ID terminou (exit $EXIT_CODE) ==="

if [ "$EXIT_CODE" -eq 0 ] && [ "$ACOMPANHAR" = "1" ] && [ "$_chained" -eq 0 ]; then
    PENDENTES=$(_harness --pendentes | tail -1)
    echo "→ gems com a geração por terminar: $PENDENTES"
    if [ "${PENDENTES:-0}" -gt 0 ]; then
        echo "→ a voltar a agendar a medição para daqui a 30 min ..."
        sbatch --parsable --begin=now+30minutes --export=ALL "${CHAIN_SCRIPT:-$0}" \
            || echo "⚠️  reagendamento falhou"
    fi
fi

if [ "$EXIT_CODE" -eq 137 ] || [ "$EXIT_CODE" -eq 9 ]; then
    OOM_RETRIES="${OOM_RETRIES:-0}"
    if [ "$OOM_RETRIES" -lt 5 ] && [ "$_chained" -eq 0 ]; then
        export OOM_RETRIES=$((OOM_RETRIES+1))
        echo "→ SIGKILL. Resubmissão automática ($OOM_RETRIES/5) ..."
        sbatch --parsable --export=ALL "${CHAIN_SCRIPT:-$0}" || echo "⚠️  falhou"
    fi
fi
exit $EXIT_CODE

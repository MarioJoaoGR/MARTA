#!/bin/bash
#SBATCH --job-name="mut_pm"
#SBATCH --account=f202407648iacdcf2x
#SBATCH --partition=dev-x86
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=64G
#SBATCH --time=04:00:00
#SBATCH --output=logs/mutpm_%j.out
#SBATCH --signal=B:SIGTERM@120

# Mutation testing POR MÓDULO, paralelo (run_mutmut_permodule.py). Só CPU.
# Resume por mutmut_permodule.csv → o auto-chain retoma no projeto onde ficou.
#   MUT_TOOL=marta  ONLY_PROJECTS=ansible  MUT_WORKERS=24
set -euo pipefail
MARTA_ROOT=/projects/F202407648IACDCF2/mario/MARTA
CONTAINER=/projects/F202407648IACDCF2/mario/containers/marta_benchmark.sif
PYDEPS=/projects/F202407648IACDCF2/mario/pydeps
export MODEL="${MODEL:-deepseek-coder-v2:16b}"
SAFE_MODEL=$(echo "$MODEL" | tr ':/' '__')
RES=/projects/F202407648IACDCF2/mario/results/$SAFE_MODEL
mkdir -p logs

_chained=0
chain() {
    if [ "$_chained" -eq 0 ]; then
        _chained=1
        echo "→ walltime: a encadear continuação (resume via CSV) ..."
        sbatch --parsable --dependency=afterany:"$SLURM_JOB_ID" --export=ALL "$0" \
            || echo "⚠️  sbatch da continuação falhou"
    fi
    exit 143
}
trap chain SIGTERM

srun -n1 singularity exec \
    --bind "$MARTA_ROOT:/opt/marta" --bind "$RES:/data/results" \
    --bind "$PYDEPS:/data/pydeps" \
    --env "USER_PYTHON_PATH=/opt/conda/envs/test4py_env/bin/python" \
    --env "PYTHONPATH=/data/pydeps/sut:/data/pydeps/marta" \
    --env "MUT_WORKERS=${MUT_WORKERS:-24}" \
    --env "MUT_MODULE_TIMEOUT=${MUT_MODULE_TIMEOUT:-1800}" \
    --env "MUTMUT_SCRATCH=/data/results/_mut_pm" \
    --env "ONLY_PROJECTS=${ONLY_PROJECTS:-}" \
    --env "PYTHONUNBUFFERED=1" \
    "$CONTAINER" /opt/conda/envs/test4py_env/bin/python \
    /opt/marta/scripts/run_mutmut_permodule.py --results /data/results \
    --tool "${MUT_TOOL:-all}" &
SRUN_PID=$!; EXIT_CODE=0
wait "$SRUN_PID" || EXIT_CODE=$?
echo "=== mut_pm job $SLURM_JOB_ID terminou (exit $EXIT_CODE) ==="
exit $EXIT_CODE

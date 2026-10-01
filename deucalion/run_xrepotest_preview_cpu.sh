#!/bin/bash
#SBATCH --job-name=marta_xrepo_preview
#SBATCH --account=f202407648iacdcf2x
#SBATCH --partition=dev-x86
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=04:00:00
#SBATCH --output=logs/xrepo_preview_%j.out
#SBATCH --signal=B:USR1@120
set -euo pipefail
BASE=${MARTA_CLUSTER_BASE:-/projects/F202407648IACDCF2/mario}
export XREPO_RUN
export XREPO_PREVIEW=${XREPO_PREVIEW:-capybara_dotenv_20261001}
export XREPO_PREVIEW_PROJECTS=${XREPO_PREVIEW_PROJECTS:-capybara,dotenv}
[[ "$XREPO_PREVIEW" =~ ^[a-zA-Z0-9][a-zA-Z0-9_-]*$ ]] || exit 2
source "$BASE/MARTA/deucalion/xrepotest_job_common.sh"
CONTINUATION="$CODE/deucalion/run_xrepotest_preview_cpu.sh"
"${CONTAINER[@]}" --pwd /home/marta "$IMAGE" python3 -B \
    /opt/marta/deucalion/xrepotest_preview.py \
    --dataset /app/xrepotest/ruby_functions.jsonl \
    --generation "/data/xrepo/runs/$XREPO_RUN/generation" \
    --projects "$XREPO_PREVIEW_PROJECTS" \
    --output "/data/xrepo/runs/$XREPO_RUN/previews/$XREPO_PREVIEW" \
    --work "/data/xrepo/runs/$XREPO_RUN/work/preview_$XREPO_PREVIEW" &
STEP_PID=$!
wait "$STEP_PID"
STEP_PID=""
echo "Preview complete: $RUN/previews/$XREPO_PREVIEW/presentation.md"

#!/bin/bash
#SBATCH --job-name=xrepo_split_start
#SBATCH --account=f202407648iacdcf2x
#SBATCH --partition=dev-x86
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=00:30:00
#SBATCH --output=logs/xrepo_split_prepare_%j.out
set -euo pipefail
BASE=${MARTA_CLUSTER_BASE:-/projects/F202407648IACDCF2/mario}
CODE=${MARTA_CLUSTER_CODE:-$BASE/MARTA-ablation}
XROOT="$BASE/xrepotest"
PARENT="$XROOT/runs/qwen36_35b_ablation97_no_graph_v1"
: "${XREPO_SPLIT_VALIDATION:?Set the successful validation.json container path}"
[[ "$XREPO_SPLIT_VALIDATION" == /data/xrepo/reports/project_split_*/validation.json ]] || exit 2
HOME_DIR="$XROOT/reports/project_split_prepare_$SLURM_JOB_ID/home"
mkdir -p "$HOME_DIR"
GOMAXPROCS=4 singularity exec --cleanenv --home "$HOME_DIR:/home/marta" \
    --bind "$CODE:/opt/marta:ro" --bind "$XROOT:/data/xrepo" \
    --env PYTHONPATH=/opt/marta --env GOMAXPROCS=4 \
    "$XROOT/repaired-v2.sif" python3 -B \
    /opt/marta/deucalion/xrepotest_project_split.py prepare \
    --validation "$XREPO_SPLIT_VALIDATION"
echo "Project checkpoints prepared; frozen source preserved. Submitting CPU workers ..."
python3 -B "$CODE/deucalion/submit_xrepotest_project_workers.py" --parent "$PARENT" --code "$CODE"

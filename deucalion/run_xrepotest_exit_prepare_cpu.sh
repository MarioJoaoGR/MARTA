#!/bin/bash
#SBATCH --job-name=xrepo_exit_prep
#SBATCH --account=f202407648iacdcf2x
#SBATCH --partition=dev-x86
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --time=00:30:00
#SBATCH --output=logs/xrepo_exit_prepare_%j.out
set -euo pipefail
BASE=${MARTA_CLUSTER_BASE:-/projects/F202407648IACDCF2/mario}
CODE=${MARTA_CLUSTER_CODE:-$BASE/MARTA-ablation}
XROOT="$BASE/xrepotest"
RUN="$XROOT/runs/qwen36_35b_ablation97_no_graph_v1"
mkdir -p "$RUN/home"
GOMAXPROCS=2 singularity exec --cleanenv \
    --home "$RUN/home:/home/marta" \
    --bind "$CODE:/opt/marta:ro" --bind "$XROOT:/data/xrepo" \
    --env PYTHONPATH=/opt/marta --env GOMAXPROCS=2 \
    "$XROOT/repaired-v2.sif" python3 -B \
    /opt/marta/deucalion/upgrade_xrepotest_coverage_system_exit.py \
    /data/xrepo/runs/qwen36_35b_ablation97_no_graph_v1/generation
echo "Coverage SystemExit repair audited. No generation, GPU or LLM calls."

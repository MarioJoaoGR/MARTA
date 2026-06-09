#!/bin/bash
#SBATCH --job-name="marta_236b"
#SBATCH --account=f202407648iacdcf2g
#SBATCH --partition=normal-a100-80
#SBATCH --nodes=1
#SBATCH --gpus=2
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=64
#SBATCH --mem=200G
#SBATCH --time=47:30:00
#SBATCH --output=logs/bench_236b_%j.out
#SBATCH --signal=B:SIGTERM@120

# ─────────────────────────────────────────────────────────────────────
# Mesmo job, configurado para correr DeepSeek-Coder-V2 236B em 2× A100 80GB.
# Wrapper que chama o run_benchmark.sh com MODEL exportado.
# ─────────────────────────────────────────────────────────────────────

export MODEL="deepseek-coder-v2:236b"
exec bash "$(dirname "$0")/run_benchmark.sh"

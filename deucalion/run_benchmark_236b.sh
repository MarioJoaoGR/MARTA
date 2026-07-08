#!/bin/bash
#SBATCH --job-name="marta_236b"
#SBATCH --account=f202407648iacdcf2g
#SBATCH --partition=normal-a100-80
#SBATCH --nodes=1
#SBATCH --gpus=4
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=64
# 400G: o 236B (~132GB em Q4) é carregado para RAM antes de ir p/ VRAM; com
# 200G o smoke-test deu OUT_OF_MEMORY (OOM de sistema). Nó a100-80 tem ~484GB.
#SBATCH --mem=400G
#SBATCH --time=47:30:00
#SBATCH --output=logs/bench_236b_%j.out
#SBATCH --signal=B:SIGTERM@120

# ─────────────────────────────────────────────────────────────────────
# Mesmo job, configurado para DeepSeek-Coder-V2 236B em 4× A100-80GB.
# gpus=4 = nó a100-80 inteiro (320GB VRAM): o modelo de 132GB cabe com folga
# (+ KV cache, que é pequeno por o DeepSeek-V2 usar MLA), e sem partilha de nó
# não há contenção de RAM com outros jobs. Wrapper que chama run_benchmark.sh
# com MODEL exportado.
#
# CHAIN_SCRIPT: o auto-chain (trap SIGTERM no run_benchmark.sh) reenvia ESTE
# wrapper — não o run_benchmark.sh — para a continuação herdar este header
# (a100-80/gpus=4/mem=400G). Sem isto, depois do `exec` o $0 lá dentro seria
# run_benchmark.sh (header a100-40/gpus=1/mem=200G) → continuação morria.
# ─────────────────────────────────────────────────────────────────────

export CHAIN_SCRIPT="$(cd "$(dirname "$0")" && pwd)/$(basename "$0")"
export MODEL="deepseek-coder-v2:236b"
exec bash "$(dirname "$0")/run_benchmark.sh"

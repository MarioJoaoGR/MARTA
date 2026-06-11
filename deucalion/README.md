# Deucalion — guia de execução

Conteúdo desta pasta:
- `Singularity.def` — definição do container (build com `singularity build`)
- `run_benchmark.sh` — job SLURM principal (DeepSeek 16B em 1× A100 40GB)
- `run_benchmark_236b.sh` — wrapper para DeepSeek 236B em 2× A100 80GB

## Setup inicial (uma vez)

```bash
# 1. Estrutura de pastas no Deucalion
mkdir -p /projects/F202407648IACDCF2/mario/{containers,ollama_models,results}
cd /projects/F202407648IACDCF2/mario

# 2. Clonar o repo MARTA
git clone https://github.com/MarioJoaoGR/MARTA.git
cd MARTA

# 3. Pull dos clones externos (Pynguin, Test4Py-baseline, codamosa) +
#    aplicar patches (faz-se localmente como já está descrito em
#    baselines/BASELINES_README.md; depois sync para Deucalion via rsync ou
#    re-clonar lá e re-aplicar os patches manualmente)

# 4. Build do container (~30-60 min)
# NOTA: O Deucalion tem `singularity` (não `apptainer`). São interchangeable
# — sintaxe e .def file iguais.
cd /projects/F202407648IACDCF2/mario/containers

# Se a build falhar por "permission denied" no login node, tenta uma destas:
#   a) com --fakeroot (rootless build):
#      singularity build --fakeroot marta_benchmark.sif ../MARTA/deucalion/Singularity.def
#   b) num compute node interactivo (se login não tiver recursos):
#      salloc -A f202407648iacdcf2g --time=2:00:00 --partition=dev-x86 \
#          --nodes=1 --cpus-per-task=8 --mem=32G
#      # depois, no nó alocado, voltar a esta pasta e correr:
#      singularity build marta_benchmark.sif ../MARTA/deucalion/Singularity.def
singularity build marta_benchmark.sif ../MARTA/deucalion/Singularity.def

# 5. Verificar:
singularity exec --nv marta_benchmark.sif python --version
singularity exec --nv marta_benchmark.sif ollama --version
```

## Overlay de dependências (OBRIGATÓRIO para MARTA + Test4Py-baseline)

O `.sif` base tem os 3 conda envs, Ollama, os 27 projetos CM e a cache do
BAAI, mas **NÃO** tem as deps pesadas da MARTA/test4dt (torch, transformers,
chromadb, sentence-transformers, langchain...). Sem elas, Pynguin corre mas
MARTA e Test4Py-baseline falham com `ModuleNotFoundError`.

Em vez de reconstruir o `.sif`, adicionamos essas deps num **overlay** (camada
writable por cima do `.sif`). Faz-se UMA vez, num nó dev-x86 (tem internet):

```bash
# Alocar nó dev-x86 (internet + sem limites de threads do login node)
salloc -A f202407648iacdcf2x --time=2:00:00 --partition=dev-x86 \
    --nodes=1 --cpus-per-task=8 --mem=32G

SIF=/projects/F202407648IACDCF2/mario/containers/marta_benchmark.sif
MARTA_ROOT=/projects/F202407648IACDCF2/mario/MARTA
OVERLAY=/projects/F202407648IACDCF2/mario/containers/deps_overlay.img

# Criar overlay de 15 GB (torch×2 + transformers + chromadb + ...)
singularity overlay create --size 15360 "$OVERLAY"

# Instalar os 2 requirements nos envs respetivos (escreve no overlay)
singularity exec --overlay "$OVERLAY" --bind "$MARTA_ROOT:/opt/marta" "$SIF" bash -c '
    /opt/conda/envs/test4py_env/bin/pip install --no-cache-dir \
        -r /opt/marta/requirements.txt
    /opt/conda/envs/test4py_baseline_env/bin/pip install --no-cache-dir \
        -r /opt/marta/baselines/test4py-baseline/requirements.txt
'

# Verificar
singularity exec --overlay "$OVERLAY" "$SIF" \
    /opt/conda/envs/test4py_env/bin/python -c \
    "import torch, chromadb, langchain_core, transformers; print('marta deps OK')"
singularity exec --overlay "$OVERLAY" "$SIF" \
    /opt/conda/envs/test4py_baseline_env/bin/python -c \
    "import torch, langchain_chroma, langchain_openai; print('baseline deps OK')"

exit  # liberta o nó dev-x86
```

O `run_benchmark.sh` deteta `deps_overlay.img` automaticamente e monta-o `:ro`.
Os pacotes `marta/` e `test4dt/` (código, não deps) vêm via bind-mount do
`$MARTA_ROOT`; garantir que existem em `MARTA/marta/` e
`MARTA/baselines/test4py-baseline/test4dt/` (rsync do Mac se faltarem —
`test4dt/` é gitignored).

## Submeter jobs

```bash
cd /projects/F202407648IACDCF2/mario/MARTA

# Job principal — DeepSeek 16B (cabe em 1× A100 40GB)
sbatch deucalion/run_benchmark.sh

# Job 236B — para a comparação cross-scale
sbatch deucalion/run_benchmark_236b.sh

# Override do modelo via env var:
sbatch --export=ALL,MODEL=deepseek-coder-v2:236b deucalion/run_benchmark.sh

# Override de tools/projetos (subset):
sbatch --export=ALL,TOOLS=pynguin,PROJECTS=codetiming,apimd deucalion/run_benchmark.sh
```

## Auto-chain (resume automático aos 48h)

O `run_benchmark.sh` está configurado com `#SBATCH --signal=B:SIGTERM@120` — SLURM envia SIGTERM **120s antes do walltime**. O harness apanha o sinal, grava `state.json`, e sai com exit 143.

Quando o job termina com exit 143, o próprio script SLURM **submete automaticamente um job dependente** (`--dependency=afterany`) que arranca depois do anterior terminar. Esse novo job lê o `state.json`, salta tudo o que já está `ok`, e continua de onde parou.

Repete-se até todos os 27 projetos estarem feitos.

## Onde os outputs aparecem

```
/projects/F202407648IACDCF2/mario/results/
└── deepseek-coder-v2_16b/             ← um por modelo ($SAFE_MODEL)
    ├── harness/
    │   ├── state.json                  ← progresso por (tool, projeto[, módulo])
    │   └── logs/<tool>/<projeto>/<mod>.log
    ├── Results_Pynguin/<projeto>/<mod>/test_*.py
    ├── Results_Test4PyBaseline/<projeto>/Test4DT_tests/
    ├── Results_MARTA/<projeto>/Test4DT_tests/
    ├── ollama_server.log
    └── prepare_envs.log
```

## Sincronizar resultados de volta para o Mac

```bash
# Do Mac:
rsync -avz --progress \
    user@deucalion-ln:/projects/F202407648IACDCF2/mario/results/ \
    ~/Desktop/GECAD/Test4Py/baselines/Results_Deucalion/
```

## Verificar progresso a meio

```bash
# No Deucalion, ver state.json em runtime:
watch -n 30 'cat /projects/F202407648IACDCF2/mario/results/deepseek-coder-v2_16b/harness/state.json | jq "to_entries | map(.value.status) | group_by(.) | map({status: .[0], n: length})"'
```

## Estimativas de tempo (DeepSeek 16B)

| Tool | Tempo por módulo | Total p/ 486 módulos |
|---|---|---|
| Pynguin | ~60s | ~8h |
| Test4Py-baseline | ~13min | ~106h ≈ 4.4 dias |
| MARTA | ~9min | ~73h ≈ 3 dias |

Total estimado: **~7-9 dias wall-clock** para o run completo (via chain de jobs de 48h). Ansible (237 mods) domina porque é metade do dataset.

## DeepSeek 236B

Estimativa: throughput ~3× menor (MoE com 21B active vs 2.4B). Total estimado: **~21-27 dias** para um run completo. Considera correr só num subset dos projetos representativos (5-7 projetos médios + ansible parcial).

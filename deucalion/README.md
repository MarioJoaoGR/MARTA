# Deucalion — guia de execução do MARTA-Ruby

Esta pasta tem o necessário para correr o benchmark no cluster:

| Ficheiro | O que é |
|---|---|
| `Singularity.def` | definição do container |
| `run_ruby_benchmark.sh` | o job SLURM |
| `logs/` | saída dos jobs (`ruby_<jobid>.out`) |

> Os `run_benchmark.sh` e `run_benchmark_236b.sh` que este ficheiro descrevia
> eram do lado **Python**, e saíram no commit `9d02d37ac` quando o Python foi
> para o repositório do artefacto. Só existe o da Ruby.

---

## Porque é preciso um passo prévio com rede

**Os nós de computação do Deucalion não têm rede.** Tudo o que precise de
descarregar, clonar ou instalar tem de acontecer antes, no nó de login, e ficar
em `/projects`.

São três coisas: os modelos do Ollama, a cache do HuggingFace (para os
*embeddings*), e os projetos Ruby com as dependências já instaladas.

## Setup, uma vez

```bash
# 1. Estrutura em /projects
mkdir -p /projects/F202407648IACDCF2/mario/{containers,ollama_models,results_ruby,pydeps,hf_cache,ruby_projects}

# 2. Container
singularity build containers/marta_benchmark.sif deucalion/Singularity.def

# 3. Modelo e embeddings (no nó de LOGIN, tem rede)
OLLAMA_MODELS=/projects/.../ollama_models ollama pull deepseek-coder-v2:16b
HF_HOME=/projects/.../hf_cache python -c \
  "from transformers import AutoModel; AutoModel.from_pretrained('BAAI/bge-large-en-v1.5')"
```

## Preparar os projetos, a cada mudança de corpus

```bash
# no nó de LOGIN
python -m benchmark.prepare_ruby_projects \
    --out /projects/F202407648IACDCF2/mario/ruby_projects
```

Clona cada projeto no *commit* fixado e instala as dependências de runtime num
`.gem_home` próprio, para o nó de computação poder correr offline.

## Correr

```bash
sbatch deucalion/run_ruby_benchmark.sh                        # 16B, 1× A100 40GB

MODEL=deepseek-coder-v2:236b sbatch \
    --partition=normal-a100-80 --gpus=4 --mem=400G \
    --export=ALL deucalion/run_ruby_benchmark.sh              # 236B
```

Variáveis de ambiente que o script aceita:

| Variável | Omissão | Para quê |
|---|---|---|
| `MODEL` | `deepseek-coder-v2:16b` | qual o modelo |
| `NUM_ROUNDS` | `3` | rondas do ciclo de cobertura |
| `PROJECTS` | todos | subconjunto, separado por vírgulas |
| `LIMIT` | sem limite | limitar métodos-alvo, para um teste rápido |

**O modelo ainda não está decidido**, 16B ou 236B. O script está parametrizado
para os dois.

## O corpus, e a ligação ao dataset

O harness limita os ficheiros-alvo com `--targets`, que espera:

```json
{ "<gem>": { "files": ["lib/a.rb", "lib/b.rb"] } }
```

Esse ficheiro é escrito pela última camada da construção do dataset:

```
apresentacao/demo_dataset/7_selecao/targets.json      500 módulos, 107 gems
```

Ver `benchmark/dataset/README.md` para como o corpus é construído. Se o corpus
mudar, correr a camada 7 outra vez e voltar a preparar os projetos.

## Walltime e retoma

O job pede 47h30 e tem `#SBATCH --signal=B:SIGTERM@120`: o SLURM avisa **120
segundos antes** de o tempo acabar. O script apanha o sinal, submete a
continuação com `--dependency=afterany`, e sai com 143.

A continuação retoma sozinha: o harness grava `state.json` e salta os projetos
já marcados como `ok`. Não é preciso fazer nada.

## Resultados

```
/projects/F202407648IACDCF2/mario/results_ruby/<modelo>/
    harness/       state.json, targets_<gem>.json
    run_results/   um JSON por projeto, com métricas e cobertura
```

## Armadilhas conhecidas

**`OLLAMA_FLASH_ATTENTION=0`** é obrigatório. O DeepSeek-V2 usa *Multi-head
Latent Attention*, que é incompatível com o *flash attention* nesta versão.

**A porta do Ollama vem do ID do job** (`1` + os últimos 4 dígitos), para dois
jobs em simultâneo não colidirem.

**`HF_HUB_OFFLINE=1` e `TRANSFORMERS_OFFLINE=1`**: sem isto o carregamento dos
*embeddings* tenta ir à rede e o job morre no nó de computação.

**A cache do HuggingFace tem de ser gravável.** Aponta-se `HF_HOME` para
`/projects`, não para a *home*.

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

# 3. Modelo do Ollama (no nó de LOGIN, tem rede)
OLLAMA_MODELS=/projects/.../ollama_models ollama pull deepseek-coder-v2:16b
```

### 4. As deps pesadas (`pydeps`) — obrigatório

O `.sif` traz os *conda envs*, o Ollama e a cache do BAAI, mas **não** traz as
deps pesadas da MARTA: `torch`, `transformers`, `chromadb`, `langchain`. Sem
elas o job morre logo no arranque com `ModuleNotFoundError: No module named
'torch'`.

Não se instalam dentro do `.sif`: **o *overlay* e o `--fakeroot` não funcionam
no Deucalion** (o `allow_other` do FUSE está bloqueado e os *namespaces* de
utilizador esgotam-se), e o `pip --user` cai no `$HOME`, que tem 2 GB de quota.
A saída é `pip install --target` para uma pasta em `/projects`, que é gravável e
sem quota, injetada no `PYTHONPATH` em tempo de execução.

Faz-se **uma vez**, num nó `dev-x86`, que é dos poucos com internet:

```bash
salloc -A f202407648iacdcf2x --time=2:00:00 --partition=dev-x86 \
    --nodes=1 --cpus-per-task=8 --mem=32G

SIF=/projects/F202407648IACDCF2/mario/containers/marta_benchmark.sif
MARTA_ROOT=/projects/F202407648IACDCF2/mario/MARTA
PYDEPS=/projects/F202407648IACDCF2/mario/pydeps

# deps da MARTA -> /data/pydeps/marta  (a corrida Ruby só precisa desta)
singularity exec --bind $PYDEPS:/data/pydeps --bind $MARTA_ROOT:/opt/marta $SIF \
    /opt/conda/envs/test4py_env/bin/pip install --no-cache-dir \
    --target /data/pydeps/marta -r /opt/marta/requirements.txt

# cache do HuggingFace gravável: a do .sif é read-only e o transformers
# precisa de escrever locks
HFCACHE=/projects/F202407648IACDCF2/mario/hf_cache
singularity exec --bind $HFCACHE:/data/hf_cache $SIF cp -r /opt/hf_cache/. /data/hf_cache/

exit   # liberta o nó dev-x86
```

O `run_ruby_benchmark.sh` faz o *bind* de `pydeps` para `/data/pydeps` e põe
`/data/pydeps/marta` à cabeça do `PYTHONPATH`. O pacote `marta/` em si não vem
daqui: vem do *bind* de `$MARTA_ROOT` para `/opt/marta`, que tem de ter o
código atualizado (rsync do portátil).

> Só é preciso repetir isto quando o `requirements.txt` mudar. O
> `pydeps/baseline` do README antigo era das baselines Python, que saíram no
> `9d02d37ac`.

## Preparar e VERIFICAR os projetos, a cada mudança de corpus

São dois comandos, e o segundo não é opcional.

```bash
# no nó de LOGIN (tem rede)
python -m benchmark.prepare_ruby_projects \
    --out /projects/F202407648IACDCF2/mario/ruby_projects

python -m benchmark.verifica_ambiente \
    --projects-dir /projects/F202407648IACDCF2/mario/ruby_projects
```

O `prepare` clona cada gem na etiqueta da versão publicada, confirma o *commit*
fixado e instala as dependências pelo **mesmo degrau** que a camada 6 do dataset
precisou de usar (deps do gemspec, mais a própria gem, ou o Gemfile). Escreve um
`manifest.json` com o que ficou pronto e com as versões instaladas.

O `verifica_ambiente` escreve, para cada um dos 500 módulos, um spec trivial que
só faz `require` do módulo, e corre-o **pela mesma função que a ferramenta usa**.
Não chama modelo nenhum. É o que garante que um módulo certificado pelo dataset
carrega mesmo aqui: se falhar, o erro apareceria no cluster contado como falha da
MARTA, sem ser culpa dela. Sai com código 1 e lista os módulos que falham.

## Correr

```bash
sbatch deucalion/run_ruby_benchmark.sh                        # 16B, 1× A100 40GB

MODEL=qwen2.5-coder:32b sbatch --export=ALL \
    deucalion/run_ruby_benchmark.sh                           # 32B
```

Variáveis de ambiente que o script aceita:

| Variável | Omissão | Para quê |
|---|---|---|
| `MODEL` | `deepseek-coder-v2:16b` | qual o modelo |
| `PHASE` | `all` | `generate` (precisa de GPU) ou `measure` (só CPU) |
| `NUM_ROUNDS` | `3` | rondas do ciclo de cobertura |
| `PROJECTS` | todas | subconjunto, separado por vírgulas |
| `LIMIT` | sem limite | limitar métodos-alvo, para um teste rápido |
| `OLLAMA_CTX` | `16384` | janela de contexto do Ollama |
| `MARTA_SEM_GRAFO` | `0` | `1` corre o braço da ablação do grafo |

**O modelo ainda não está decidido**, 16B ou 32B. Medido nos mesmos 10 projetos
do lado Python: o 32B é 3,4× mais lento a gerar, e o corpus inteiro a 32B rondaria
340 GPU-h, que não cabe nas horas disponíveis. O 236B está fora (4 GPUs).

**A fase `measure` não precisa de GPU.** Corre-se a geração com `PHASE=generate`
neste job, e a medição no job de CPU (conta `...cf2x`, partição `dev-x86`):

```bash
PHASE=generate sbatch --export=ALL deucalion/run_ruby_benchmark.sh
ACOMPANHAR=1 sbatch --export=ALL deucalion/run_ruby_measure_cpu.sh
```

Os dois podem correr ao mesmo tempo. A medição grava num `state_medicao.json`
próprio e só lê o `state.json` da geração; escrever os dois no mesmo ficheiro já
comeu resultados no lado Python. Com `ACOMPANHAR=1`, quando a medição acaba e a
geração ainda tem gems por terminar, o job volta a agendar-se para daqui a 30
minutos, e a medição vai seguindo a geração sozinha. O `MODEL` e o
`MARTA_SEM_GRAFO` têm de ser os mesmos da geração que se quer medir.

## A ablação do grafo

O grafo de chamadas entra na Fase 1 em dois sítios: a 2ª passagem do `done_what`
e a propagação do `what_todo`. O braço da ablação desliga os dois e repete
**só os métodos cujo prompt muda** — os que têm um chamado ou um chamador que
também é alvo. Nos outros o contexto sai igual, e repetir seria pagar GPU para
medir ruído do modelo.

Esse conjunto calcula-se localmente, sem modelo:

```bash
python -m benchmark.alvos_ablacao      # escreve 7_selecao/ablacao.json
```

Medido: **4601 dos 6898 métodos-alvo (66,7%)**. Corre-se depois da execução
normal, com o mesmo modelo:

```bash
MARTA_SEM_GRAFO=1 sbatch --export=ALL deucalion/run_ruby_benchmark.sh
```

Tem cache de análise, estado e outputs próprios (`<gem>_sem_grafo/`), por isso
não toca na execução normal. A primeira passagem dos sumários não usa o grafo e
sai igual nos dois braços: o braço sem grafo vai buscá-la à cache da execução
normal em vez de a pagar outra vez (uma chamada por método afetado), por isso
**tem de correr depois** da execução normal da mesma gem. A comparação faz-se método a método, com os dois
`cobertura_por_metodo.json`, restrita aos métodos afetados.

## O corpus, e a ligação ao dataset

Tudo o que o cluster precisa de saber sobre o corpus está num ficheiro só,
escrito pela última camada da construção do dataset:

```
apresentacao/demo_dataset/7_selecao/projetos.json     500 módulos, 107 gems
```

Por gem traz de onde vem o código (repositório, etiqueta, *commit*, raiz), o
ambiente em que os módulos foram certificados (pastas de carregamento, porta de
entrada, receita de instalação), os ficheiros que a camada 2 analisou, e a lista
de alvos com as etiquetas `modo`, `origem` e `vizinhos_no_corpus`.

O `prepare`, o verificador e o harness leem **os três daqui**. Antes havia três
versões do ambiente e nenhuma era a que tinha certificado os módulos.

Não há modo "sem alvos": o harness só corre gems que estejam no `projetos.json`
**e** preparadas. Sem essa trava, a ferramenta tomava a gem inteira como alvo,
83 766 métodos em vez de 6 976.

Ver `benchmark/dataset/README.md` para como o corpus é construído. Se o corpus
mudar, correr a camada 7 outra vez, e depois o `prepare` e o verificador.

## Walltime e retoma

O job pede 47h30 e tem `#SBATCH --signal=B:SIGTERM@120`: o SLURM avisa **120
segundos antes** de o tempo acabar. O script apanha o sinal, submete a
continuação com `--dependency=afterany`, e sai com 143.

A continuação retoma sozinha: o harness grava `state.json` e salta os projetos
já marcados como `ok`. Não é preciso fazer nada.

## Resultados

```
/projects/F202407648IACDCF2/mario/results_ruby/<modelo>/
    harness/       state.json, ambiente_<gem>.json, alvos_<gem>.json, logs/
    <gem>/         marta_specs/, cobertura_por_metodo.json
                   run_results/<gem>.json          métricas e agregados
                   run_results/<gem>.eventos.jsonl uma linha por chamada
    results.json   resumo por gem
```

O `cobertura_por_metodo.json` tem uma linha por método-alvo, com `origem`,
`modo` e `vizinhos_no_corpus` ao lado da cobertura. É o que permite responder,
dentro da mesma execução, se o contexto entre módulos ajudou.

O `<gem>.json` traz `por_fase` (chamadas, tokens de entrada e saída, segundos de
modelo e de parede) e `subprocessos` (quantas vezes e quanto tempo em `ruby -c`,
RSpec e cobertura). As fases são as sete da Fase 1 — `sumarios_passagem1`,
`sumarios_passagem2`, `what_todo_raiz`, `what_todo_propagado`,
`what_todo_fallback`, `sumario_final`, `sumarios_de_classe` — mais `plano`,
`dev_primeira` e `dev_reparacao` na geração. Também conta `llm_cortadas`
(respostas truncadas pelo limite de tokens) e `llm_erros` (chamadas falhadas, que
o cliente devolve como resposta vazia).

O `<gem>.eventos.jsonl` é a mesma coisa sem agregação: uma linha por chamada ao
modelo e por subprocesso Ruby, com método, ronda e tentativa. Escrito à medida,
por isso um job morto pelo walltime deixa na mesma o que já mediu — ao contrário
do JSON final, que só é escrito no fim.

## Armadilhas conhecidas

**`OLLAMA_FLASH_ATTENTION=0`** é obrigatório. O DeepSeek-V2 usa *Multi-head
Latent Attention*, que é incompatível com o *flash attention* nesta versão.

**A porta do Ollama vem do ID do job** (`1` + os últimos 4 dígitos), para dois
jobs em simultâneo não colidirem.

**A janela de contexto tem de ser fixada** (`OLLAMA_CONTEXT_LENGTH`). Com a
omissão do modelo, um prompt maior é cortado **em silêncio**: o modelo responde
a um prompt truncado e nada no log o diz.

**`OLLAMA_KEEP_ALIVE=-1`**: entre chamadas o harness corre RSpec e mede
cobertura, e com o valor por omissão (5 min) o modelo era descarregado da GPU e
recarregado a seguir.

**`HF_HUB_OFFLINE=1` e `TRANSFORMERS_OFFLINE=1`**: sem isto o carregamento dos
*embeddings* tenta ir à rede e o job morre no nó de computação.

**A cache do HuggingFace tem de ser gravável.** Aponta-se `HF_HOME` para
`/projects`, não para a *home*.

**A pasta dos projetos Ruby também tem de ser gravável.** Cada projeto guarda em
`.marta_ruby_cache/` a análise, o grafo de chamadas e, desde 2026-09-10, os
vetores do RAG (uma coleção ChromaDB). É isso que faz uma segunda execução saltar
o *embedding* de todos os sumários, que aqui corre em CPU (`EMBED_DEVICE=cpu`,
para o Ollama ficar com a GPU sozinho). O *bind* de `ruby_projects` é de
escrita; se algum dia passar a `:ro`, o custo volta a aparecer sem dar erro.

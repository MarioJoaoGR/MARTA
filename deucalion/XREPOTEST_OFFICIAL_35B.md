# XRepoTest oficial no mesmo Qwen3.6:35b

Preparação de 11 de outubro de 2026, na branch
`codex/xrepo-comparable-evaluation`. Não modifica os checkouts de geração da
MARTA ou de ablação. Não instala pacotes, não descarrega modelos e não depende
de Internet nos nós de cálculo.

## O que comparamos

XRepoTest `standard`, 675 tarefas Ruby, uma resposta por tarefa, contra a MARTA
normal nas mesmas 675 tarefas. Os 97 IDs de ablação também podem ser extraídos
posteriormente dos resultados completos, sem uma nova geração.

| Configuração por pedido | Valor comum à MARTA e a esta execução |
| --- | --- |
| Modelo | `qwen3.6:35b`, digest `096fdbd02fe620fc10cbeb6537e080f8041aece851e5d696aed024d4f70f2e47` |
| Ollama | `0.30.7` |
| Thinking | ligado, `reasoning_effort=high` |
| Contexto | 32 768 tokens |
| Saída máxima, incluindo thinking | 16 384 tokens |
| Temperature / top_p / presence_penalty | 0,6 / 0,95 / 0 |
| Timeout por pedido SDK | 1 800 segundos |

É uma comparação controlada com o nosso modelo e ambiente, não uma reprodução
numérica das tabelas do paper. Os defaults publicados do cliente são
`temperature=0`, `top_p=1` e `max_tokens=4096`. Substituímos estes parâmetros no
limite da API pelos usados na MARTA. Não há igualdade de orçamento total:
a MARTA faz análise, pesquisa e geração/reparação iterativa; o XRepoTest standard
faz um pedido lógico por tarefa, com os retries de transporte oficiais.

## Código deles e código nosso

O pacote `vendor/xrepotest-standard-39fb6ab.tar.gz` inclui a licença MIT, fontes
Python inalteradas do commit oficial `39fb6ab3173136d3dac2d38ed7c98baf6c470270`
e os 675 prompts produzidos pelo `PromptCreator`, em modo standard.
Os prompts coincidem byte por byte com a experiência local Qwen3-8B.
SHA-256 dos prompts: `4d3fc5a62d0ebb2a5a1309bf36d2c99a69a9446a89971d12d8ade5d41a3792c2`.
O gerador de prompts não é importado no cluster, evitando instalar datasets e
parsers de outras linguagens. A geração importa `UnifiedProcessor` e o cliente
OpenAI oficiais; o pré-processamento importa `preprocess_response_records`.

`xrepotest_official_generate.py` faz a orquestração: verifica hashes, aplica os
parâmetros comuns na API, guarda checkpoints e exporta resultados. Não altera
mensagens, não acrescenta contexto da MARTA e não gera testes por conta própria.
Thinking fica no registo bruto, separado do conteúdo que o cliente oficial
entrega ao pré-processamento. Código entre fences, respostas sem fences e
mensagens de erro seguem as regras publicadas, sem filtros adicionais.

Uma resposta vazia, cortada, inválida ou um erro terminal continua no
resultado, sem uma nova tentativa para melhorar a qualidade. O cliente mantém
até três tentativas de transporte; o SDK também tem os seus retries automáticos.
Guardamos pedidos e respostas HTTP para observar ambos. Isto não equivale a
três gerações quando o modelo simplesmente devolve conteúdo vazio.

A retoma conserva tarefas terminadas, incluindo erros. É uma política de
checkpoint explícita: não usamos a filtragem de cache upstream que seleciona
apenas sucessos e poderia repetir os erros ao retomar `process_file`.
Só uma tarefa interrompida sem resultado terminal é reiniciada; o checkpoint
anterior é arquivado e os pedidos já feitos permanecem no log. Um trabalho
cancelado pelo utilizador não se reagenda; o aviso de walltime encadeia a retoma.

## Ficheiros e isolamento

- `build_xrepotest_official_assets.py`: regenera o pacote no venv já existente,
  confrontando as fontes com o arquivo GitHub original e os prompts com o 8B.
- `run_xrepotest_official_prepare_cpu.sh`: valida fontes, dataset, imports,
  parâmetros e ambiente contra a execução MARTA normal, sem inferência.
- `run_xrepotest_official_generate_gpu.sh`: arranca Ollama local, verifica versão
  e digest e executa o gerador oficial. Usa a mesma configuração do servidor.
- `tests/test_xrepotest_official_generate.py`: API simulada, exportação das 675
  tarefas, retoma, thinking separado, erro vazio e retries de transporte.

Tudo fica em `xrepotest/runs/qwen36_35b_xrepotest_standard_thinking_v1/`.
Em `generation/`: `experiment.json`, `prompts.jsonl`, `tasks/<id>.json`,
`api_requests.jsonl`, `api_calls.jsonl`, `http_requests.jsonl`,
`http_responses.jsonl`, `responses.jsonl`, `processed.jsonl`, `complete.json`.
O conjunto de fontes validado fica em `xrepotest/assets/official-standard-39fb6ab/`.
Nenhuma análise, cache RAG ou suite da MARTA é reutilizada pelo XRepoTest.

## Comandos no Deucalion

Preparar já em CPU, mesmo durante a ablação GPU:

```bash
(
set -e
cd /projects/F202407648IACDCF2/mario/MARTA-evaluation
test "$(git branch --show-current)" = codex/xrepo-comparable-evaluation
git pull --ff-only
export MARTA_CLUSTER_BASE=/projects/F202407648IACDCF2/mario
export MARTA_CLUSTER_CODE="$PWD"
export XREPO_RUN=qwen36_35b_xrepotest_standard_thinking_v1
unset XREPO_TASK_IDS XREPO_REUSE_ANALYSIS_FROM XREPO_REUSE_FIRST_ROUND_FROM
mkdir -p logs
sbatch --parsable --export=ALL deucalion/run_xrepotest_official_prepare_cpu.sh
)
```

Depois de a preparação terminar com exit 0 e da geração da ablação sem grafo
terminar (incluindo as suas eventuais retomas), arrancar a geração oficial:

```bash
(
set -e
cd /projects/F202407648IACDCF2/mario/MARTA-evaluation
export MARTA_CLUSTER_BASE=/projects/F202407648IACDCF2/mario
export MARTA_CLUSTER_CODE="$PWD"
export XREPO_RUN=qwen36_35b_xrepotest_standard_thinking_v1
unset XREPO_TASK_IDS XREPO_REUSE_ANALYSIS_FROM XREPO_REUSE_FIRST_ROUND_FROM
sbatch --parsable --export=ALL deucalion/run_xrepotest_official_generate_gpu.sh
)
```

Só depois de obter `Generation complete` e `generation/complete.json`, avaliar:

```bash
(
set -e
cd /projects/F202407648IACDCF2/mario/MARTA-evaluation
export MARTA_CLUSTER_BASE=/projects/F202407648IACDCF2/mario
export MARTA_CLUSTER_CODE="$PWD"
export XREPO_RUN=qwen36_35b_xrepotest_standard_thinking_v1
unset XREPO_TASK_IDS
sbatch --parsable --export=ALL deucalion/run_xrepotest_core_evaluate_cpu.sh
)
```

O avaliador é o mesmo usado na MARTA e nas ablações, na imagem `repaired-v2.sif`,
com as duas correções de cobertura documentadas. Medimos CSR, TPR, cobertura e
IR nas 675 tarefas, incluindo falhas. Não alteramos IR para satisfazer a sua
heurística. Mutação permanece fora desta avaliação até estar validada para
todas as abordagens; os scores antigos não são tratados como comparação final.

Validação local: oito testes passaram com os SDKs já instalados 1.42.0 (o usado
pela MARTA) e 3.24.0. A exportação de 675 tarefas e a retoma foram testadas com
API simulada, sem chamar o modelo. Na imagem Docker repaired-v2, offline,
confirmámos os hashes do dataset e das fontes e os 675 prompts. Bash passou `bash -n`. A validação real dos
imports e do ambiente no Deucalion é o primeiro job CPU acima.

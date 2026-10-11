# XRepoTest oficial no mesmo Qwen3.6:35b

Preparação de 11 de outubro de 2026, na branch
`codex/xrepo-comparable-evaluation`. Não modifica os checkouts de geração da
MARTA ou de ablação. Não instala pacotes, não descarrega modelos e não depende
de Internet nos nós de cálculo.

## O que comparamos

Cinco configurações oficiais, cada uma nas mesmas **675 tarefas Ruby**:

| Modo | Contexto do prompt publicado |
| --- | --- |
| `standard` | método focal e instruções de geração |
| `lsp_context` | contexto obtido pelo enriquecimento LSP publicado |
| `file_context` | conteúdo do ficheiro focal |
| `rag_bm25` | os 10 primeiros excertos recuperados por BM25 |
| `rag_dense` | os 10 primeiros excertos recuperados por UniXcoder |

São **3 375 respostas lógicas**, uma por tarefa e por modo, antes dos retries de
transporte. Os modos são experiências separadas; não misturamos os contextos num
prompt. A experiência local Qwen3-8B foi apenas standard e não serve como uma
reprodução dos resultados dos outros quatro modos.

Comparamos cada modo com a MARTA normal nas mesmas 675 tarefas. Os 97 IDs de
ablação também podem ser extraídos posteriormente dos resultados completos, sem uma nova geração.

| Configuração por pedido | Valor desta execução |
| --- | --- |
| Modelo | `qwen3.6:35b`, digest `096fdbd02fe620fc10cbeb6537e080f8041aece851e5d696aed024d4f70f2e47` |
| Ollama | `0.30.7` |
| Thinking | ligado, `reasoning_effort=high` |
| Contexto | escolha explícita em `XREPO_OFFICIAL_CTX`, sem default no job |
| Saída máxima, incluindo thinking | 16 384 tokens |
| Temperature / top_p / presence_penalty | 0,6 / 0,95 / 0 |
| Timeout por pedido SDK | 1 800 segundos |

É uma comparação controlada com o nosso modelo e ambiente, não uma reprodução
numérica das tabelas do paper. Os defaults publicados do cliente são
`temperature=0`, `top_p=1` e `max_tokens=4096`. Substituímos estes parâmetros no
limite da API pelos usados na MARTA. Não há igualdade de orçamento total:
a MARTA faz análise, pesquisa e geração/reparação iterativa; cada modo XRepoTest
faz um pedido lógico por tarefa, com os retries de transporte oficiais.

### Janela necessária para preservar os contextos

A auditoria `vendor/xrepotest-context-token-budget.json` usa o tokenizer oficial
Qwen3.6, revision `995ad96eacd98c81ed38be0c5b274b04031597b0`, sobre o texto das
mensagens, sem o template de chat. É uma estimativa offline; o usage real do
Ollama fica nos logs da execução. Reservámos 1 024 tokens conservadores para o
enquadramento das mensagens e 16 384 para a resposta, incluindo thinking.

O maior prompt RAG denso (tarefa 80) tem cerca de 36 107 tokens de texto, acima da
janela MARTA de 32 768 mesmo antes de gerar. Vinte prompts de ficheiro completo
não deixam os 16 384 tokens de saída inteiramente disponíveis nessa janela.
Todos os prompts cabem com esta reserva numa janela de 65 536. A proposta é usar
65 536 uniformemente nos cinco modos, mantendo prompts, limite de saída e os
restantes parâmetros. Esta escolha exige confirmação antes da submissão.
Se adotada, **a janela difere da MARTA normal**: não se deve afirmar igualdade de
todos os limites de contexto. Cortar ou reescrever os prompts publicados não é
uma operação implementada por estes scripts.

## Código deles e código nosso

O pacote `vendor/xrepotest-contexts-39fb6ab.tar.gz` inclui a licença MIT, fontes
Python inalteradas do commit oficial `39fb6ab3173136d3dac2d38ed7c98baf6c470270`
e os cinco conjuntos de prompts produzidos pelo `PromptCreator` original.
Os prompts standard continuam byte por byte iguais aos da experiência local 8B.
O pacote standard anterior fica como registo da primeira preparação; estes jobs
usam exclusivamente o novo pacote de contextos e um novo diretório de resultados.

Os dados enriquecidos vêm da revisão publicada
`cd694c00d20951aef189a406abac980a6b1c49d4`. Ficheiros, métodos, linhas e código focal
coincidem com as 675 tarefas de base. Os hashes dos dados e de cada conjunto de
prompts ficam no descriptor e no manifesto do pacote. Preservamos as assinaturas
simplificadas de 172 tarefas dos ficheiros RAG; esse campo não é usado pelo
construtor do prompt nem modifica o alvo de avaliação.

Em LSP, **170/675 prompts diferem do standard**. A ausência de contexto adicional
nas restantes tarefas é o comportamento do construtor sobre o enriquecimento
publicado; não inventamos dados que faltam. Em RAG, os ficheiros disponíveis têm
20 excertos por tarefa, mas selecionamos os primeiros **10**, com janela de
**50 linhas** e stride **10**, seguindo a configuração descrita nos apêndices B e
G do paper. A recuperação já foi feita pelos autores: não voltamos a executar
LSP, BM25 ou UniXcoder e não utilizamos a pesquisa RAG da MARTA.

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
  confrontando as fontes com o arquivo GitHub original, os dados enriquecidos com
  os hashes publicados e os prompts standard com o 8B.
- `run_xrepotest_official_prepare_cpu.sh`: valida fontes, dataset, imports,
  parâmetros e ambiente contra a execução MARTA normal, sem inferência.
- `run_xrepotest_official_generate_gpu.sh`: arranca Ollama local, verifica versão
  e digest e executa sequencialmente os cinco modos com um servidor. A janela é explícita.
- `run_xrepotest_official_evaluate_cpu.sh`: avalia os cinco modos separadamente,
  sempre nas 675 tarefas, ignorando seleções antigas exportadas no shell.
- `tests/test_xrepotest_official_jobs.py`: verifica a orquestração dos três jobs
  com comandos simulados, sem Slurm, GPU ou inferência.
- `tests/test_xrepotest_official_generate.py`: API simulada, exportação das 675
  tarefas, retoma, thinking separado, erro vazio e retries de transporte.

Tudo fica em `xrepotest/runs/qwen36_35b_xrepotest_contexts_thinking_v1/`.
Cada modo tem `modes/<modo>/generation/` e `modes/<modo>/evaluation_core_v1/`.
Em cada `generation/`: `experiment.json`, `prompts.jsonl`, `tasks/<id>.json`,
`api_requests.jsonl`, `api_calls.jsonl`, `http_requests.jsonl`,
`http_responses.jsonl`, `responses.jsonl`, `processed.jsonl`, `complete.json`.
O conjunto de fontes validado fica em `xrepotest/assets/official-contexts-39fb6ab/`.
Nenhuma análise, cache RAG ou suite da MARTA é reutilizada pelo XRepoTest.

## Comandos no Deucalion

Após confirmar a janela, preparar em CPU, mesmo durante a ablação GPU:

```bash
(
set -e
cd /projects/F202407648IACDCF2/mario/MARTA-evaluation
test "$(git branch --show-current)" = codex/xrepo-comparable-evaluation
git pull --ff-only
export MARTA_CLUSTER_BASE=/projects/F202407648IACDCF2/mario
export MARTA_CLUSTER_CODE="$PWD"
export XREPO_RUN=qwen36_35b_xrepotest_contexts_thinking_v1
export XREPO_OFFICIAL_CTX=65536 # proposta, confirmar antes de submeter
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
export XREPO_RUN=qwen36_35b_xrepotest_contexts_thinking_v1
export XREPO_OFFICIAL_CTX=65536 # proposta, confirmar antes de submeter
unset XREPO_TASK_IDS XREPO_REUSE_ANALYSIS_FROM XREPO_REUSE_FIRST_ROUND_FROM
sbatch --parsable --export=ALL deucalion/run_xrepotest_official_generate_gpu.sh
)
```

Só depois de os cinco modos terem `generation/complete.json`, avaliar:

```bash
(
set -e
cd /projects/F202407648IACDCF2/mario/MARTA-evaluation
export MARTA_CLUSTER_BASE=/projects/F202407648IACDCF2/mario
export MARTA_CLUSTER_CODE="$PWD"
export XREPO_RUN=qwen36_35b_xrepotest_contexts_thinking_v1
export XREPO_OFFICIAL_CTX=65536 # proposta, confirmar antes de submeter
unset XREPO_TASK_IDS
sbatch --parsable --export=ALL deucalion/run_xrepotest_official_evaluate_cpu.sh
)
```

O avaliador é o mesmo usado na MARTA e nas ablações, na imagem `repaired-v2.sif`,
com as duas correções de cobertura documentadas. Medimos CSR, TPR, cobertura e
IR nas 675 tarefas, incluindo falhas. Não alteramos IR para satisfazer a sua
heurística. Mutação permanece fora desta avaliação até estar validada para
todas as abordagens; os scores antigos não são tratados como comparação final.

Validação local: nove testes de geração passaram com os SDKs já instalados
1.42.0 (o usado pela MARTA) e 3.24.0; um teste adicional verifica os três scripts
Slurm. Incluem os cinco conjuntos de prompts, exportação de 675 tarefas e retoma
com API simulada. Na imagem Docker repaired-v2, offline, confirmámos os hashes
do dataset e das fontes e os 675 prompts de cada modo. Não houve inferência nem
instalação de pacotes. A validação real no Deucalion é o primeiro job CPU acima.

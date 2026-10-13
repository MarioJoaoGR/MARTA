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
| Contexto | 32 768 tokens, fixo e igual à MARTA |
| Saída máxima, incluindo thinking | 16 384 tokens |
| Temperature / top_p / presence_penalty | 0,6 / 0,95 / 0 |
| Timeout por pedido SDK | 1 800 segundos |

É uma comparação controlada com o nosso modelo e ambiente, não uma reprodução
numérica das tabelas do paper. Os defaults publicados do cliente são
`temperature=0`, `top_p=1` e `max_tokens=4096`. Substituímos estes parâmetros no
limite da API pelos usados na MARTA. Não há igualdade de orçamento total:
a MARTA faz análise, pesquisa e geração/reparação iterativa; cada modo XRepoTest
faz um pedido lógico por tarefa, com os retries de transporte oficiais.

### Mesma janela e comportamento quando a entrada excede o limite

Decisão do utilizador em 11 de outubro: **manter todos os parâmetros usados na
MARTA**, incluindo a janela de 32 768. A proposta anterior de 65 536 não foi
adotada. Os jobs e o adaptador rejeitam outra janela, antes da inferência.

A auditoria `vendor/xrepotest-context-token-budget.json` usa o tokenizer oficial
Qwen3.6, revision `995ad96eacd98c81ed38be0c5b274b04031597b0`, sobre o texto das
mensagens, sem o template de chat. É uma estimativa offline, não o usage exato do
Ollama. O maior prompt RAG denso (tarefa 80) tem cerca de 36 107 tokens de texto,
ultrapassando a janela antes da geração. Vinte prompts de ficheiro têm uma soma
de entrada e saída máxima superior à janela. O limite de saída é um teto;
**não representa uma reserva garantida de espaço na janela**.

Enviamos os prompts publicados sem corte próprio, sem reduzir o número de
excertos e sem excluir tarefas. Mantemos a política nativa do Ollama 0.30.7,
como na MARTA: a entrada excessiva pode ser truncada pelo servidor e a gestão da
janela durante a geração permanece a do backend. Isto significa que fornecer o
prompt completo à API **não garante que todo o contexto seja visto pelo modelo**.
Não ligamos `truncate=false` nem implementamos outra política de overflow.

O código fixado de [chatPrompt](https://github.com/ollama/ollama/blob/v0.30.7/server/prompt.go)
preserva mensagens de sistema e a última mensagem ao reduzir o histórico. O
[runner](https://github.com/ollama/ollama/blob/v0.30.7/llm/llama_server.go)
trunca tokens acima de `num_ctx - 1`, preservando o prefixo `num_keep` e o fim da
entrada, e emite `truncating input prompt`. Guardamos pedidos originais, usage,
finish_reason e logs Ollama por job para auditar estas ocorrências. O diagnóstico
offline não é contado como confirmação de truncagem real de uma tarefa.

As 675 tarefas de cada modo permanecem no denominador, incluindo cortes,
respostas vazias e erros terminais. A comparação usa os mesmos limites; a
limitação de contexto deve acompanhar os resultados, sem atribuir automaticamente
um resultado fraco a essa limitação.

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

Preparar em CPU, mesmo durante a ablação GPU:

```bash
(
set -e
cd /projects/F202407648IACDCF2/mario/MARTA-evaluation
test "$(git branch --show-current)" = codex/xrepo-comparable-evaluation
git pull --ff-only
export MARTA_CLUSTER_BASE=/projects/F202407648IACDCF2/mario
export MARTA_CLUSTER_CODE="$PWD"
export XREPO_RUN=qwen36_35b_xrepotest_contexts_thinking_v1
export XREPO_OFFICIAL_CTX=32768
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
export XREPO_OFFICIAL_CTX=32768
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
export XREPO_OFFICIAL_CTX=32768
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
1.42.0 (o usado pela MARTA) e 3.24.0; testes adicionais verificam os scripts
Slurm e a prova de CPU (13 testes no SDK 1.42.0 após a alternativa CPU). Incluem os cinco conjuntos de prompts, exportação de 675 tarefas e retoma
com API simulada. Na imagem Docker repaired-v2, offline, confirmámos os hashes
do dataset e das fontes e os 675 prompts de cada modo. Não houve inferência nem
instalação de pacotes. A validação real no Deucalion é o primeiro job CPU acima.

## Geração exclusivamente CPU (proposta de 12 de outubro, atualizada em 13 de outubro)

A quota GPU reportada em 12 de outubro era de 11 horas; confirmar a quota atual.
Foi preparada uma alternativa para gerar os cinco modos em CPU, mantendo as 675 tarefas por modo, mesmos prompts, mesmo digest Q4_K_M,
Ollama 0.30.7, thinking, amostragem, contexto 32768 e saída máxima 16384.
**Não aumentamos o timeout de 1800 segundos**. Se CPU atingir esse timeout, as
regras oficiais de retries/erro mantêm-se. Esses casos terão de ser reportados,
não tratados como medida pura da qualidade do modelo. A velocidade real no
Deucalion e a adequação do timeout ainda não foram medidas.

A CPU muda o backend de cálculo. Não prometemos respostas iguais às da GPU:
implementações numéricas e amostragem podem diferir. As métricas core continuam
a avaliar testes pelo mesmo protocolo; o hardware deve ser declarado e tempos
CPU/GPU não são uma comparação controlada de eficiência da ferramenta.

A configuração corrigida usa `qwen36_35b_xrepotest_contexts_thinking_cpu_threads8_v2`,
separada do run GPU e da tentativa CPU v1 falhada (preservada para auditoria).
O adaptador regista execution_backend e recusa uma prova de CPU que pertença a
outro modelo, janela, versão, job ou servidor. Não misturamos respostas de
hardware diferente num run existente. A mesma política de retoma conserva
sucessos e erros terminais; uma resposta interrompida é arquivada e reiniciada.

`run_xrepotest_official_generate_cpu.sh` usa conta x86, normal-x86, um nó,
32 CPUs e 64 GiB de RAM solicitada. Não pede GPUs, não usa --nv nem módulos
CUDA. CUDA/ROCm/Vulkan ficam ocultos/desligados. `verify_ollama_cpu.py` carrega
os pesos já existentes com prompt vazio (load-only, sem uma resposta gerada)
e verifica em /api/ps que o modelo está carregado, usa VRAM zero e contexto
32768. A prova, lscpu, dados Slurm, memória e logs ficam guardados por job.
O runtime e os pacotes usados já existem; não há instalação nem downloads.
LLAMA_ARG_THREADS=8 limita o executor; a prova deve confirmar 8 threads de
geração e de batch no log real, além dos campos de /api/ps.

[Ollama documenta o modo CPU](https://github.com/ollama/ollama/blob/v0.30.7/docs/gpu.mdx).
Segundo o [guia Deucalion](https://docs.macc.fccn.pt/start/), a quota CPU é separada
e nós CPU x86 exclusivos são faturados por 128 cores, mesmo que o pedido use
menos. **Uma hora num nó pode consumir 128 core-h, não uma hora da quota GPU**.
Confirmar `billing` antes de ampliar a duração ou ligar retomas automáticas.

### Começar uma hora na nova coorte, após validar um pedido inteiro

Executar esta etapa só depois de verificar a resposta do diagnóstico de
pedido inteiro abaixo. Os resultados desta coorte seguem o protocolo oficial
e conservam-se, incluindo erros terminais. O job começa a geração oficial em standard, nos 675 IDs, seguida dos outros quatro
modos. Cada tarefa terminada fica guardada para a continuação da mesma execução.
Uma hora não implica conclusão de standard, e muito menos dos cinco modos.

```bash
billing
(
set -e
cd /projects/F202407648IACDCF2/mario/MARTA-evaluation
test "$(git branch --show-current)" = codex/xrepo-comparable-evaluation
git pull --ff-only
export MARTA_CLUSTER_BASE=/projects/F202407648IACDCF2/mario
export MARTA_CLUSTER_CODE="$PWD"
export XREPO_RUN=qwen36_35b_xrepotest_contexts_thinking_cpu_threads8_v2
export XREPO_OFFICIAL_CTX=32768 XREPO_CPU_CHAIN=0
unset XREPO_TASK_IDS XREPO_REUSE_ANALYSIS_FROM XREPO_REUSE_FIRST_ROUND_FROM
mkdir -p logs
PRE=$(sbatch --parsable --export=ALL deucalion/run_xrepotest_official_prepare_cpu.sh)
GEN=$(sbatch --parsable --export=ALL --dependency="afterok:$PRE" \
    --partition=dev-x86 --time=01:00:00 deucalion/run_xrepotest_official_generate_cpu.sh)
echo "Preparação CPU: $PRE; geração CPU: $GEN"
squeue -j "$PRE,$GEN"
)
```

O script tem 24 horas em normal-x86 como duração para trabalhos longos, mas
este comando limita a primeira execução a uma hora em dev-x86. O aviso de
walltime termina o job antes do limite conservando checkpoints. A opção
XREPO_CPU_CHAIN=0 é a omissão e impede nova submissão automática. Para ampliar,
verificar tempo por tarefa e quota CPU; uma retoma manual em normal-x86 mantém
o run e todos os resultados anteriores. Só XREPO_CPU_CHAIN=1 permite encadear
jobs de 24h automaticamente. Não ativar sem orçamento suficiente.

A avaliação CPU final usa `run_xrepotest_official_evaluate_cpu.sh` com este mesmo
XREPO_RUN após os cinco exports completos. Pode extrair depois os 97 IDs das
ablações, sem gerar testes adicionais. A ablação MARTA sem grafo continua
incompleta e não é retomada por estes comandos.

## Diagnóstico da primeira execução CPU (job 2008484)

A execução foi cancelada após 4h40: três tarefas terminaram por timeout, sem
respostas válidas, e a quarta foi interrompida. Os logs confirmam três pedidos
HTTP por chamada do SDK, 30 minutos cada, e cerca de 0,1 token/s no runner.
O runner detetou 128 threads; OMP_NUM_THREADS=32 não limitou as threads llama.
O papel das threads na lentidão ainda precisa de medição, não está demonstrado.
Os erros/checkpoints desta tentativa ficam preservados; não são resultados
concluídos dos cinco modos nem evidência de qualidade do modelo.

`run_xrepotest_cpu_threads_probe.sh` é um diagnóstico CPU separado, sem
encadeamento nem GPU. Recupera as mensagens originais da tarefa 0 e testa
8, 16 e 32 threads explicitamente através de `options.num_thread`. Mantém
pesos, thinking=high, contexto 32768, limite de saída 16384 e amostragem.
Usa o endpoint nativo com streaming apenas para medir o runtime; cada medição
é interrompida aos 180s se ainda não terminou. Isso não constitui uma execução
do benchmark com o timeout de 1800s. Não gera métricas de testes, exports ou
checkpoints de tarefas, nem altera os prompts/resultados anteriores.

Os relatórios ficam em `diagnostics/cpu_threads_<JOBID>/report.json`. Taxas de
tokens vêm exclusivamente das métricas finais do runner ou dos seus logs;
chunks e caracteres de streaming não são contabilizados como tokens.
Mesmo havendo melhoria, validar viabilidade antes de submeter novamente os
3375 pedidos. Este diagnóstico não retoma a execução completa.

## Resultado do diagnóstico CPU e validação do endpoint OpenAI

Job 2026463: 8 threads ~9,5 tokens/s, 16 threads ~9,5 tokens/s e
32 threads ~3,6 tokens/s. A primeira execução com 128 threads tinha ~0,1
token/s. Nenhum dos três pedidos de 180s terminou uma resposta: eram medições
de velocidade, não validação da viabilidade ou qualidade do benchmark.

A configuração inicial passa a 8 threads (16 não teve vantagem clara nesta
medição única). O runner é limitado com LLAMA_ARG_THREADS=8, que atua no
llama-server mesmo quando o endpoint OpenAI não fornece num_thread. O log
de arranque deve confirmar 8 threads de geração e de batch; o verificador
recusa outros valores, antes de fazer qualquer pedido do benchmark.

`run_xrepotest_cpu_request_probe.sh` executa UMA vez o corpo HTTP original
da tarefa 0 no endpoint /v1/chat/completions, sem streaming, com thinking
high, contexto 32768, saída 16384 e timeout 1800s. Recupera e compara o
corpo HTTP efetivamente registado com a chamada SDK, não reescreve o prompt.
É um diagnóstico sem métricas nem retries do SDK. Guarda a resposta e o
relatório em diagnostics/cpu_request_threads8_<JOBID>; preserva todos os
checkpoints anteriores. Só depois de verificar uma resposta inteira se deve
ampliar a execução. Uma resposta não demonstra a viabilidade de todos os
contextos (os prompts de ficheiro completo podem ser muito maiores).

A execução oficial corrigida é uma coorte nova:
`qwen36_35b_xrepotest_contexts_thinking_cpu_threads8_v2`. Recomeça as mesmas
675 tarefas em cada um dos cinco modos, com o protocolo fixado, sem importar
os três erros da v1 nem a resposta do diagnóstico. A v1 inteira é mantida
como tentativa de runtime falhada, não como benchmark concluído. O manifesto
CPU regista threads=8 e o controlo LLAMA_ARG_THREADS; cada job tem prova do
runner CPU, do modelo, contexto e threads. Não alterar timeout ou parâmetros
para acelerar; não ativar encadeamento antes de medir duração útil.

## Validação real e execução por modo (13 de outubro)

Job 2028320: pedido original task 0 concluído em 1056,135s (17m36s), HTTP
200, finish_reason=stop, 601 tokens de entrada e 10245 de saída (incluindo
thinking). Resposta útil com 4833 caracteres; thinking com 35211 caracteres.
Não inferimos uma divisão de tokens de reasoning que a API não reportou.
As 8 threads foram confirmadas antes e depois. É evidência de que este pedido
funciona em CPU, não validação de todos os prompts/contextos nem da qualidade
dos testes. A resposta permanece um diagnóstico excluído dos resultados.

A geração CPU aceita XREPO_OFFICIAL_MODE=standard, lsp_context, file_context,
rag_bm25 ou rag_dense (all por omissão mantém a execução sequencial). Cada
modo continua a ter os mesmos 675 IDs, sem subset nem mudança dos pedidos.
Pode submeter-se um job por modo, cada um num nó CPU, sob a mesma coorte v2.
As pastas de saída já são separadas por modo, e cada servidor tem uma porta,
log, prova e home próprios. Um lock partilhado da coorte permite modos
diferentes; um lock exclusivo por modo impede duplicados. O job all usa o
lock exclusivo da coorte e não pode sobrepor-se a nenhum job por modo.

A primeira janela oficial sugerida é de 2h por modo em normal-x86, com
XREPO_CPU_CHAIN=0. Os resultados válidos e erros terminais são conservados
para retoma; pedidos interrompidos são arquivados pelo protocolo existente.
A dependência afterok da preparação impede geração se a preparação falhar.
Só ativar prolongamento/encadeamento depois de medir mais tarefas, incluindo
os prompts maiores. Há 3375 pedidos no total: não extrapolar uma data de fim
a partir de uma única resposta. Paralelismo entre modos reduz tempo de parede
se o scheduler disponibilizar os nós; não reduz o trabalho total ou core-h.

Com cinco nós exclusivos e 2h cada, a janela inicial tem teto de 1280 core-h
(5 × 2 × 128), sem quota GPU. Usar billing para confirmar o orçamento atual.
A avaliação final continua a exigir os cinco exports completos antes de
medir os 675 IDs de cada modo pelo mesmo avaliador.

Comando inicial (sem encadeamento):

```bash
(
set -e
cd /projects/F202407648IACDCF2/mario/MARTA-evaluation
test "$(git branch --show-current)" = codex/xrepo-comparable-evaluation
git pull --ff-only
export MARTA_CLUSTER_BASE=/projects/F202407648IACDCF2/mario
export MARTA_CLUSTER_CODE="$PWD"
export XREPO_RUN=qwen36_35b_xrepotest_contexts_thinking_cpu_threads8_v2
export XREPO_OFFICIAL_CTX=32768 XREPO_CPU_CHAIN=0
unset XREPO_OFFICIAL_MODE XREPO_TASK_IDS XREPO_REUSE_ANALYSIS_FROM XREPO_REUSE_FIRST_ROUND_FROM
mkdir -p logs
PRE=$(sbatch --parsable --export=ALL deucalion/run_xrepotest_official_prepare_cpu.sh)
echo "Preparação: $PRE"
JOB_IDS=""
for MODE in standard lsp_context file_context rag_bm25 rag_dense; do
    GEN=$(XREPO_OFFICIAL_MODE="$MODE" sbatch --parsable --export=ALL \
        --dependency="afterok:$PRE" --partition=normal-x86 --time=02:00:00 \
        --job-name="xrepo_$MODE" deucalion/run_xrepotest_official_generate_cpu.sh)
    echo "$MODE: $GEN"
    JOB_IDS="${JOB_IDS:+$JOB_IDS,}$GEN"
done
squeue -j "$PRE,$JOB_IDS"
)
```

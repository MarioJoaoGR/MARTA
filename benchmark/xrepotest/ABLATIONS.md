# Ablações opcionais da MARTA-Ruby

Estas opções preparam as experiências de remoção de componentes. Todas estão
**desligadas por omissão**. Não existe uma opção `no summaries`: o estudo dos
sumários enriquecidos faz parte da ablação do grafo já definida.
O subset ainda não foi escolhido. Nenhuma execução experimental é iniciada
pela implementação destas opções.

## O que cada braço retira

| CLI XRepoTest | Variável do job GPU, valor `1` | O que é retirado | O que continua |
|---|---|---|---|
| `--no-graph` (existente) | `XREPO_NO_GRAPH` | Enriquecimento `done_what` pelos callees e propagação `what_todo` pelos callers | Primeiro `done_what`, `what_todo` local a partir do README, fusão final, RAG e geração |
| `--no-type-hints` | `XREPO_NO_TYPE_HINTS` | As sugestões de tipos de parâmetros enviadas ao Planner, incluindo o complemento semântico por classes | Índice de tipos usado para construir o grafo, sumários e recuperação de métodos |
| `--no-method-retrieval` | `XREPO_NO_METHOD_RETRIEVAL` | Métodos relacionados recuperados para o plano e ajuda recuperada a partir dos erros | Sumários enriquecidos pelo grafo e sugestões de tipos, incluindo o índice de classes |
| `--no-coverage-feedback` | `XREPO_NO_COVERAGE_FEEDBACK` | Linhas em falta enviadas ao Planner e decisão de saltar um método por estar totalmente coberto | Mesmo número configurado de rondas, validação e medição de cobertura |
| `--no-repair` | `XREPO_NO_REPAIR` | Novas tentativas Dev guiadas pelos erros dentro de cada ronda | Planner, uma resposta Dev por ronda, validação de sintaxe/RSpec, salvamento de exemplos aprovados e rondas de cobertura |

As opções são independentes e podem ser combinadas. Para estudar cada componente,
a comparação principal deverá retirar um de cada vez e conservar o restante.
A política fica registada como `component-removal-v1` em `experiment.json` e na
telemetria das tarefas.

`no-type-hints` abla apenas as sugestões explícitas de tipos do `judge`. Não
apaga informação de tipos que o modelo possa inferir do código ou dos sumários.
O índice de tipos estático continua necessário para o grafo: removê-lo também
misturaria dois mecanismos na mesma experiência.

`no-method-retrieval` é mais específico do que a antiga opção geral `--no_rag`
do executável normal. O índice vetorial dos métodos e o índice das classes têm
utilidades diferentes. Retirar os métodos relacionados não deve retirar as
sugestões de tipos por classes.

`no-coverage-feedback` continua a medir cobertura, mas não utiliza esse resultado
para orientar a próxima geração. Todas as rondas configuradas são elegíveis,
incluindo as dos métodos que já chegaram a cobertura completa. A instrução
genérica de tentar maximizar cobertura continua igual à da primeira ronda normal.
Não se acrescentam informações sobre linhas em falta. Como o normal pode saltar
rondas já cobertas, os custos dos braços podem diferir.

`no-repair` impõe **uma tentativa Dev por ronda**. As rondas seguintes podem ainda
gerar novos testes se forem elegíveis; isso não é uma reparação dentro da mesma
ronda. A validação e o salvamento ficam iguais para não confundir melhoria por
reparação com remoção do controlo de qualidade. Deve reportar-se a diferença
no número de chamadas e no custo, além das métricas oficiais.

## Subset, contexto e avaliação

`--task-ids /caminho/ids.json` aceita uma lista JSON não vazia de IDs oficiais
únicos, todos inteiros. Sem este argumento, mantém-se a execução completa das
675 tarefas. Antes da seleção, verifica-se a integridade da release oficial.
A seleção e o seu hash ficam no manifesto; uma retoma com outros IDs é recusada.

Selecionar tarefas restringe a **geração**, não o contexto de produção dos
projetos presentes no subset. Todos os métodos de produção desses projetos
continuam em `analysis_targets`, incluindo os não selecionados para geração.

O avaliador aceita a mesma opção `--task-ids`. No cluster, geração e avaliação
recebem `XREPO_TASK_IDS=/data/xrepo/.../ids.json`. O ficheiro deve existir na pasta
montada do XRepoTest. O avaliador exige exatamente uma linha de resposta por ID
selecionado; tarefas `no_tests` continuam no denominador com resposta `[]`.
As fórmulas, fontes Ruby e tarefas oficiais não são alteradas.

A comparação normal deverá usar **os mesmos IDs** do subset, retirando esses
resultados da execução completa. As métricas já medidas por tarefa são lidas
dos resultados normais; não é preciso gerar ou avaliar novamente essas tarefas.
Uma avaliação preliminar sem mutação não substitui uma medição de mutação que
ainda não tenha sido feita. A seleção deverá ser definida antes de observar
os ganhos das ablações, e os critérios documentados quando for escolhida.

## Reutilização da análise e separação dos resultados

Usar sempre um `XREPO_RUN` distinto por braço. O manifesto recusa retomar com
outro modelo, parâmetros, fontes, subset ou opções. A execução principal em curso
não recebe estas flags e não é modificada por esta preparação.

`--reuse-analysis-from /caminho/normal/generation`, ou a variável
`XREPO_REUSE_ANALYSIS_FROM=/data/xrepo/runs/.../generation`, permite ler checkpoints
de sumários de uma execução normal compatível. Verificam-se modelo e digest dos
pesos, thinking, parâmetros, políticas, ambiente, fontes e ficheiros de runtime.
As opções de geração e a quantidade de tarefas podem diferir porque não entram
nos prompts da análise de produção.

Só se reutiliza uma resposta quando o prompt de sistema e o prompt de
utilizador coincidem exatamente. A fase deve também coincidir, com uma exceção
explícita: `what_todo_raiz` e `what_todo_fallback` executam a mesma função local
de README. Podem partilhar respostas a pedidos idênticos, registando a fase
de origem. Isto vale também para o braço `no-graph`: a
primeira passagem é comum, e pedidos locais de README ou sumários de classes
podem igualmente ser comuns. A segunda passagem com callees e a propagação com
callers não são executadas nesse braço. Reutilizar uma resposta local idêntica
não reintroduz o grafo.

O grafo estático já registado é copiado quando coincidem as fontes e a versão
do resolvedor. No braço sem grafo, as duas utilizações desse grafo para os
sumários continuam desligadas. A descoberta volta a ler o código para resolver
os alvos: não existe uma cache de resultados Prism na execução de referência.

Nos braços que conservam o grafo, copia-se o bundle completo de análise quando
fontes, modelo e fingerprint da análise coincidem. Assim não é necessário voltar
a percorrer as passagens LLM para encontrar todos os checkpoints. O bundle
enriquecido nunca é aplicado ao braço sem grafo.

Os índices vetoriais compatíveis são copiados para o diretório do novo braço e
validados pelas mesmas chaves e IDs. Preserva-se também o índice HNSW dos métodos.
Quando o texto muda, podem ainda ser reutilizados vetores individuais de textos
que continuam exatamente iguais, por exemplo sumários de classes no braço sem
grafo. Apenas textos novos recebem novos embeddings. A extração do ChromaDB
ocorre numa cópia temporária, nunca sobre o original. As consultas novas de
embeddings ficam em cache no braço para as retomas seguintes.

Não se copiam testes nem estados de tarefas entre braços. Os diretórios da
referência são apenas lidos. `reference_artifacts.json`, por projeto, regista os
hashes dos ficheiros partilhados e a disponibilidade de vetores. O custo herdado
continua separado das novas chamadas.

Existe uma exceção explícita de compatibilidade para o código normal congelado
com fingerprint
`5f731f30e02f62264900a96b2c7efc5f33d4dfff08cbc33c41dab25eb0720d85`.
Outras versões desconhecidas são recusadas. Isto permite poupar a análise já
realizada sem afirmar que configurações diferentes são a mesma experiência.

`analysis_reuse.json` regista a referência, o hash do manifesto, a quantidade de
checkpoints disponíveis e o consumo registado na análise de origem, incluindo
proveniência anterior quando existe. Esse consumo é separado das novas chamadas
físicas. O total da análise de origem não equivale ao custo exclusivo do subset
nem ao número efetivamente reutilizado. Os eventos `llm_cache_hit` com
`source=analysis_reference` identificam as leituras efetivas. Comparar custo marginal e custo completo exige
explicitar esta partilha, sem apresentar contexto previamente calculado como grátis.

## Onde está implementado

- `marta/ruby_backend/ablation.py`: opções com valores por omissão e limite de tentativas.
- `marta/ruby_backend/project.py`: pontos de remoção, sem alterar os prompts normais.
- `marta/ruby_backend/start_react.py`: flags da ferramenta normal; novas ablações exigem `--output_dir` separado e têm sufixos próprios.
- `benchmark/xrepotest/ablation.py`: seleção de IDs e compatibilidade da referência.
- `benchmark/xrepotest/run.py`: aplicação das opções, checkpoints e registo de consumo herdado.
- `benchmark/xrepotest/reuse.py`: bundles e vetores compatíveis, sem copiar respostas de geração.
- `benchmark/xrepotest/evaluate.py`: avaliação do mesmo conjunto de IDs.
- `deucalion/run_xrepotest_generate_gpu.sh` e `run_xrepotest_evaluate_cpu.sh`: passagem das opções aos executores.

Os jobs conservam três rondas e três tentativas por omissão. As variáveis opcionais
`XREPO_ROUNDS` e `XREPO_ATTEMPTS` permitem configurar esses limites; `no-repair`
reduz a uma as tentativas efetivas independentemente do limite normal.

## Versão ativa e verificação

A preparação vive num worktree separado. Não fazer merge/push para a versão
ativa nem `git pull` no cluster enquanto a execução normal congelada ainda
precisar de retomas. Alterar qualquer fonte coberta pelo fingerprint produz uma
versão diferente, mesmo quando todas as flags estão desligadas. As proteções da
execução existente continuam intactas.

Verificação: **383 testes passaram e 2 foram ignorados** nas suites Ruby,
XRepoTest e Deucalion, em container temporário. Após acrescentar a partilha do
grafo estático, passaram também **109 testes focados** de reutilização e
integração. Nenhum pacote foi instalado no computador.

A verificação offline usa respostas LLM fixas, Ruby/RSpec reais onde relevante,
Slurm simulado e índices vetoriais de teste. Inclui comparação literal dos
prompts, chamadas, specs e resultados da geração normal com o `project.py`
anterior. Não constitui medição de qualidade dos braços nem escolha do subset.

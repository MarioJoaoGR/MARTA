# Reutilização do retrieval estático entre rondas

Entrega de 2026-11-04, posterior ao orçamento completo de prompts (`d0c8d27ca`).
Implementa A9 do backlog para novas execuções do backend Ruby.

## Comportamento

O Planner consulta o RAG com `target.summary or target.done_what`, top-3 e
exclusão da definição-alvo. Numa análise/índice estável, essa pergunta não muda
entre rondas. A primeira consulta continua a executar embedding da query e busca
Chroma; o resultado formatado é guardado em memória. As rondas seguintes podem
reutilizar a mesma lista, sem nova consulta estática.

A chave inclui a identidade da definição, o texto exato da consulta e top-k.
O âmbito é a instância e a revisão do índice, dentro do objeto RubyProject.
Métodos com o mesmo nome em ficheiros diferentes não partilham entradas.
Seletores de tarefas para a mesma definição e consulta podem partilhá-las, pois
esse contexto só contém informação de produção, não respostas de outras tarefas.

Cada retorno é uma cópia da lista guardada. A redução de contexto pelo orçamento
do prompt ou alterações feitas pelo consumidor não alteram o valor original.
A cache guarda no máximo uma consulta bem-sucedida por definição consultada,
conservando a ordem e os snippets devolvidos pelo retriever. Não muda o ranking,
o top-k, a exclusão do próprio método ou a seleção por similaridade.

## Validade e duração

`RubyFunctionDatabase.init()` publica uma nova `retrieval_revision` apenas depois
de inicializar com sucesso o índice. Isto acontece também quando reutiliza vetores
do disco ou inicializa um conjunto vazio. Uma reconstrução falhada remove a
revisão e a coleção ativa anteriores. A revisão é uma identidade efémera do
snapshot, não um digest dos pesos, nem parte aleatória da receita da experiência.

A cache é descartada ao descobrir fontes, iniciar uma nova análise ou construir
o RAG. Trocar a instância/revisão do índice também a invalida. Alterar o texto da
consulta de uma definição substitui a entrada anterior. Não se grava esta cache
em disco, nem se partilha entre objetos/projetos ou processos; uma retoma noutro
processo volta a consultar quando necessário. As caches persistentes de análise,
vetores e queries do adapter mantêm os seus contratos separados.

Os textos e a configuração do índice pertencem ao seu snapshot inicializado.
Depois de alterar fontes, sumários indexados, corpus ou embedder, é necessário
reanalisar/reconstruir o índice conforme o fluxo normal. Alterar manualmente o
conteúdo de um índice ativo sem reconstrução não constitui um novo snapshot.

Índices customizados continuam compatíveis. Para permitir memoização devem expor
uma `retrieval_revision` string não vazia, nova sempre que mudem os dados,
formatos ou configuração capazes de alterar os resultados. Sem essa declaração,
a MARTA consulta-os em cada chamada. Não infere validade de um callback opaco.

Resultados vazios e exceções não são guardados. A API Chroma existente também
pode devolver uma lista vazia em falhas transitórias; guardá-la impediria a
recuperação numa ronda posterior. Isto significa que consultas legitimamente
vazias podem continuar a repetir-se.

## A reparação mantém informação dinâmica

`_error_help_fn` continua a executar `rag_db.query(error[:400], k=3, ...)` em cada
pedido de ajuda, conservando as regras anteriores de seleção dos dois primeiros
hits. Mesmo um erro repetido volta a consultar. A procura de um spec disponível
faz-se nesse momento; novos testes podem surgir entre tentativas/rondas.

Não se guarda essa ajuda na cache do Planner. O override de XRepoProject que
impede exemplos gerados noutras tarefas de entrarem no prompt mantém-se ativo.
As ablações de retrieval continuam a impedir os dois consumidores de consultar
o índice; a desativação também limpa o contexto estático memorizado.

## Telemetria e proveniência

`tipo=planner_retrieval` identifica hits/misses, se o índice permite cache,
definição, hash da consulta, top-k e número de resultados. O tempo fica em
`retrieval_estatico`. Não se credita um cache hit como chamada LLM ou como tokens
observados, nem se atribui a essa operação o custo de construção do índice.

A implementação entra nos hashes de proveniência/receitas já existentes.
Não se migram manifests, tarefas ou métricas dos papers nem se relabelam resultados
antigos como execuções desta melhoria. As experiências congeladas conservam o
seu código e configuração originais.

## Validação

`test_retrieval_cache.py` cobre consultas reutilizadas, cópias independentes,
identidades distintas, substituição/revisão/rebuild do índice, ciclo de vida do
projeto, erros transitórios, ablações, providers sem revisão, reparação dinâmica
e proteção do adapter XRepoTest.

Uma fixture com Ruby/RSpec e Chroma reais, embeddings determinísticos e respostas
LLM simuladas executa três rondas com e sem memoização. Mantém os mesmos prompts
do Planner, o mesmo código final e nove pedidos scriptados por braço; reduz de
três para uma as consultas estáticas e conserva três consultas de reparação.
Não há chamadas a modelos, downloads ou instalações. Esta evidência verifica a
poupança de operações repetidas; não estima ganhos de qualidade ou velocidade
para um corpus real.

Validação final: **816 testes locais aprovados**, 3 ignorados e **12 testes
aprovados no container existente**. Total: **828 aprovados**.

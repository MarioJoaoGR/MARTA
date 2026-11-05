# A5, primeira etapa — respostas e contexto de métricas por pedido

Entrega de **2026-11-05**, posterior à evidência do grafo/judge (`dd29a203c`).
Retira dependências de estado global do caminho Ruby nativo. **Não ativa
paralelismo na análise/geração**: ambiente, workspaces e coordenação continuam
pendentes antes de lançar workers.

## Problema corrigido

O wrapper Ruby obtinha usage pela diferença dos contadores do recorder Python
antes/depois de um await. Também lia `gptapi.model.last_call`, mesmo quando o
callback fornecido pertencia a outro cliente. Uma chamada sobreposta podia
creditar tokens de outra; um callback sem metadata podia herdar um erro/corte
antigo do singleton. O recorder tinha ainda listas/dicionários de fase/contexto
partilhados entre tarefas assíncronas.

## Resposta imutável e compatibilidade

`marta.llm_response.ChatReply` transporta conteúdo final, tokens, finish reason e
erro de **um pedido lógico ao SDK**. `MyGPT.chat_result`/`aask_result` devolvem esse
objeto, sem atualizar os contadores Python nem uma última resposta global. A
versão async usa o mesmo limiter e `asyncio.to_thread` já existentes.

A API `chat`/`aask` antiga continua a devolver conteúdo e a atualizar os contadores
legados. Ambas usam a mesma implementação do pedido HTTP. Os testes verificam
corpos HTTP iguais, incluindo modelo, temperatura, thinking, top-p, penalidade,
limite de saída e mensagens. O objeto `ChatReply` é interno; não pede ao modelo
um novo formato JSON. Não muda prompts, rondas, caps ou políticas de reparação.

O caminho Ruby por omissão usa `RubyAsk` e o protocolo declarado
`response_api=True`. O wrapper de métricas consome a resposta diretamente, sem
publicar/ler `last_call`. A fachada também suporta o callback string tradicional,
com um slot de metadata local à tarefa para consumidores que precisem dele;
o caminho nativo instrumentado não escreve nesse slot.

Os adaptadores `GenerationRequests`/`SummaryCheckpoints` preferem igualmente a
resposta direta. Mantêm a política existente de checkpoints, cortes, falhas e
três tentativas de sumários truncados, sem dupla contagem pelo wrapper externo.
Cache hits não se tornam chamadas ao modelo. A API do avaliador XRepoTest,
operadores e resultados congelados não são modificados.

### Providers antigos e callbacks opacos

- Um cliente antigo só com `aask`/`last_call` continua suportado em modo sequencial,
  com `metrics_source=legacy_client_last_call`. Esse caminho não prova isolamento
  em concorrência; um provider precisa do contrato por resposta para isso.
- Um callback sem metadata conta a chamada concluída, mas conserva usage como
  desconhecido, sem ler automaticamente o singleton Python.
- A compatibilidade por deltas globais exige opt-in explícito do callback:
  `legacy_singleton_metrics=True`. Fica marcada `legacy_singleton_opt_in` e não
  serve para workers concorrentes. Não é usada pela configuração Ruby nativa.
- Um provider que declara a API nova e devolve outro tipo falha explicitamente;
  não se repete o pedido nem se muda silenciosamente para o transporte antigo.

`usage_reported` indica se há ambos os contadores inteiros/não negativos.
`llm_usage_unknown_calls` conta os pedidos concluídos cujo usage não está completo.
Nos contadores numéricos antigos, campos ausentes têm contribuição zero apenas
por compatibilidade de formato; isso **não demonstra custo zero**. Eventos
conservam origem e disponibilidade dos dados. Os relatórios pós-geração e por
ronda incluem os novos contadores quando disponíveis.

## Contexto de tarefa e interrupções

Fase e contexto do recorder usam `ContextVar` com estados substituídos, em vez de
mutar estruturas comuns. Uma tarefa filha herda o contexto inicial, mas mudanças
de método/ronda/fase e a restauração por `finally` não alteram a tarefa irmã ou o
pai. Uma falha/cancelamento restaura corretamente os blocos de contexto.

Um pedido interrompido sem resposta incrementa `llm_interrupted_requests` e emite
`llm_interrupted` com duração observável e usage desconhecido. A exceção mantém-se;
não se credita uma resposta anterior como se fosse a atual. Esses pedidos não
entram como respostas concluídas com tokens zero.

Cancelar o await não garante cancelar uma chamada síncrona já iniciada na thread
ou no servidor. A resposta/usage final pode ficar indisponível; a nova API não a
publica tardiamente em contadores/metadata globais. Não se altera aqui o mecanismo
de cancelamento do transporte nem os retries preexistentes do SDK. As métricas
contam pedidos lógicos/usage devolvido, não tentativas HTTP internas ocultas.

## Benefício e custo

| Alteração | Trabalho/erro evitado | Custo ou limite |
|---|---|---|
| Usage acompanha a resposta | Evita leituras/diferenças globais e atribuição a outro pedido | Um objeto pequeno por resposta, sem reter histórico em memória |
| Transporte e limiter existentes | Evita criar outro cliente/modelo/pool por pedido | Configuração do cliente deve permanecer estável durante requests |
| Contexto local de tarefa | Evita cruzar fase/método entre awaits | Dois contextos pequenos por recorder; não isola ambiente nem ficheiros |
| Usage/interrupções explícitos | Evita chamar custo desconhecido de zero | Alguns campos adicionais nos eventos/relatórios |

Não há workers extra, novas chamadas LLM, instalações ou downloads. A execução
normal mantém-se sequencial. Esta é uma correção de atribuição de dados e uma
pré-condição de concorrência, **não uma aceleração global já medida**.

## O que continua em A5

Isolar workspaces/processos Ruby, carregamento/ambiente, outputs, retrieval de
exemplos, timers/contadores por worker e a coordenação de commits/validação da
suite. Os contadores do recorder continuam agregados por objeto e não constituem
uma estrutura thread-safe para partilhar entre event loops/threads. A primeira
ronda e os timers globais desse objeto também precisam de âmbito por worker.

Ainda não existe um novo `--workers` nem gather no fluxo de geração. Os testes
usam gather **apenas em fixtures** para reproduzir interleavings e cancelamentos.
Só depois das restantes fronteiras isoladas faz sentido medir concorrência
limitada 1/2/4 na capacidade real do servidor.

## Proveniência e validação

A proveniência/receita passa a identificar implementação do payload, fachada e
recorder. Mudanças de implementação invalidam reutilizações incompatíveis; não
há migração automática de experiências antigas para esta política. Não se
recalculam resultados dos papers para os atribuir às correções atuais.

`test_request_isolation.py` usa respostas scriptadas e HTTPX MockTransport: testa
respostas intercaladas no mesmo cliente, erros/cortes diferentes, cancelamentos,
usage ausente, contexto do pai/filhos, contrato inválido sem retry, seleção do
cliente por omissão e compatibilidade do corpo HTTP/API legada. Não há rede nem
inferência. Mantêm-se também os testes de budgets, checkpoints, retries, avaliação
e controlos Mutant no container existente.

As durações agregadas de pedidos podem sobrepor-se em concorrência: não são
faturação de GPU nem uma medição de aceleração global.

Validação final: 881 testes na suite local completa, mais um caso adicional
verificado no módulo de isolamento (16/16): **882 testes locais distintos**.
Com os **16 testes do container**, são **898 aprovados**. Dos sete saltados
no host, quatro correram no container; restam três ignorados.

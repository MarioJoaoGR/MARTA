# MARTA-Ruby — backlog revisto

Última revisão: **2026-11-04**, após integração das correções na `main`.

Esta lista distingue as correções já implementadas das melhorias ainda abertas.
As entregas e os respetivos limites estão documentados em
[validação](../../docs/RUBY_VALIDATION.md),
[reparação contextual](../../docs/RUBY_REPAIR_CONTEXT.md),
[planos e código-alvo](../../docs/RUBY_PLAN_SOURCE_CONTEXT.md),
[análise e retoma](../../docs/RUBY_ANALYSIS_RESUME.md),
[identidade dos testes](../../docs/RUBY_SPEC_IDENTITIES.md) e
[README do projeto](../../docs/RUBY_README_CONTEXT.md).

As [notas originais](../../docs/archive/ruby-improvements-before-2026-10-04.md)
foram preservadas integralmente, incluindo comentários e discordâncias do
utilizador. Os IDs abaixo conservam a ligação à lista antiga.

**Mudança importante:** já não é correto afirmar que “nada aqui é bug”.
A revisão encontrou problemas de validade e progresso, reproduzidos offline,
que têm prioridade sobre novas otimizações. A organização documental de outubro
não as implementou; as entregas de novembro, identificadas abaixo, já corrigiram
várias delas. Os resultados congelados dos papers conservam a sua implementação
original e não são reclassificados como resultados destas melhorias.

## A. Estado dos dez itens originais

| ID | Tema | Estado confirmado | Decisão recomendada |
|---|---|---|---|
| A1 | Contexto de métodos chamados sem limite | **Aberto.** A lista `called` continua sem orçamento total/per-callee | Limitar por tokens, relevância e evidência; reservar espaço para o alvo |
| A2 | Trocar segunda passagem por concatenação | **Não aceite pelo utilizador.** A síntese continua implementada | Manter; medir a contribuição do grafo sem impor a substituição rejeitada |
| A3 | Cache ignora versão de contexto | **Parcialmente resolvido.** `ANALYSIS_SCHEMA=5` e fingerprint incluem README, identidades, resolver e limite de contexto | Usar a versão existente; acrescentar fingerprint de prompts, receita/digest de modelos e configuração relevante |
| A4 | `--no_cache` recalcula mas não grava | **Continua aberto.** O bundle é escrito dentro de `if use_cache` | Separar reutilização de cache de arquivo da run; guardar evidência mesmo sem cache |
| A5 | Paralelismo na geração | **Aberto; esforço subestimado.** Fluxo sequencial e estado global/mutável | Isolar cliente, recorder, ambiente e workspaces antes de concorrência limitada |
| A6 | Confiança nas arestas | **Aberto.** `kind` existe, mas não é usado para seleção/confiança | Registar resolução exata vs fallback/ambiguidade; não tratar toda constante como certa |
| A7 | Inferir tipos de retorno | **Aberto; investigação de maior esforço** | Começar por `Foo.new`, atribuições no construtor e anotações; medir valor antes de inferência global |
| A8 | Segunda passagem depende da ordem | **Resolvido para `done_what`.** Lê `passagem1[analysis_id]` | Não duplicar a correção; estudar separadamente a escolha de chamador em `what_todo` |
| A9 | RAG estático repetido por ronda | **Aberto.** `_related_for(t)` continua dentro do ciclo | Memorizar por alvo/contexto; manter retrieval de reparação dependente do erro |
| A10 | Classes pouco informativas e judge sem limiar | **Aberto.** Stub + até 40 assinaturas; top-1 sem abstenção | Testar stub + construtor + sumários existentes; devolver scores e calibrar aceitação |

### A3 — o que mudou desde a nota antiga

A cache já não depende apenas de código e nome de modelo. A fingerprint de
[`project.py`](project.py) inclui schema, âmbito, identidades, README, resolver
e `MAX_CONTEXT_CHARS`. A cache de vetores inclui também os textos efetivamente
indexados. Não precisamos de outra constante redundante chamada
`CONTEXT_VERSION`: precisamos de aplicar/incrementar o schema existente e
fechar as lacunas de proveniência. O README agora é procurado até à raiz do
projeto, com preferência pelo mais próximo. O mesmo snapshot é usado para
calcular a fingerprint e construir os pedidos; o bundle regista o caminho
relativo e SHA-256 por ficheiro de código. Prompts e receita do modelo ainda
precisam da extensão de proveniência prevista em A3.

### A4 — duas coisas diferentes

Os eventos de telemetria não são um arquivo dos sumários completos.
A CLI normal ainda os perde com `--no_cache`. O adapter XRepoTest já conserva
respostas por hash do prompt: é uma solução a aproveitar no caminho comum.
`--no_cache` continua a controlar só a reutilização da análise. A retoma da geração
já exige um checkpoint compatível de rondas validadas e reexecuta a suite; a mera
existência de um ficheiro deixou de justificar um skip.

### A5 — porque não basta gather + semáforo

`model.last_call`, deltas de tokens, contexto/fases do recorder, diretórios de
execução, exemplos consultados pelo RAG e ambiente do adapter podem interferir.
A execução concorrente precisa de estado e métricas por tarefa. Depois faz
sentido medir concorrência 1/2/4, dentro da capacidade real do servidor, sem
prometer aceleração proporcional.

### A6/A7 — confiança e retorno, em concreto

`Money.default_bank.exchange_with(...)` tem duas operações: encontrar
`default_bank` e descobrir o tipo do objeto que este devolve. Só o segundo passo
permite resolver `exchange_with`. Não implica que todas as chamadas tenham de
ter um tipo único: conservar candidatos e “desconhecido”.

A forma do receiver é apenas uma evidência. Uma constante resolvida por nome
curto ambíguo não é uma chamada garantida. Preferir primeiro as arestas cuja
resolução é demonstrável.

### A9 — Planner e reparação não fazem a mesma pergunta

O Planner consulta o mesmo sumário entre rondas; esse resultado pode ser
reutilizado. A reparação usa a mensagem de erro e pode encontrar exemplos
diferentes; não deve usar indiscriminadamente a cache do Planner.
A consulta de métodos usa embedding + Chroma, e não só NumPy.

## B. Estudos por fechar

### B1 — precisão e alcance do grafo

A sondagem `money` mede recall contra arestas observadas por um driver; não
mede precisão global. O helper continua a usar apenas `:call/:return`.

- Validar extensão a eventos C com correspondência correta entre entrada/saída,
  identificação dos accessors e controlo de falsos positivos.
- Auditar amostra estratificada de `static_only`; distinguir não observado,
  invisível ao instrumento e resolução errada.
- Repetir em várias gems. Cobertura alta de linhas não implica observar todas
  as combinações de dispatch.

Evidência histórica: [sondagem 1](https://github.com/MarioJoaoGR/MARTA/blob/1939c60f3/sondagens/s1_callgraph_money/RESULTADOS.md).

### B3 — separar os três consumidores do RAG

| Braço | Related no Planner | Judge semântico | Retrieval no erro |
|---|---|---|---|
| Completo | Sim | Sim | Sim |
| Sem related | Não | Sim | Sim |
| Sem judge | Sim | Não | Sim |
| Sem ajuda no erro | Sim | Sim | Não |
| Sem RAG | Não | Não | Não |
| Estrutural/lexical | Contexto por símbolos/grafo, sem embeddings | Apenas estrutural | Símbolos/diagnóstico |
| Híbrido proposto | Evidências estruturais + retrieval | Candidatos compatíveis e abstenção | Consulta estruturada |

Os primeiros cinco braços ajudam a localizar contribuição; interações entre
componentes podem exigir experiências adicionais. A lista antiga não isolava
a ajuda no erro.

A CLI normal tem `--no_rag`. As flags `no_type_hints` e
`no_method_retrieval` já existem na CLI e no adapter XRepoTest: a primeira desliga
as sugestões de tipos; a segunda desliga conjuntamente related no Planner e
retrieval na reparação. Ainda falta separar estes dois consumidores para executar
exatamente todos os braços desta tabela. As ablações de reparação e feedback de
cobertura também já estão implementadas; não são trabalho pendente de flags.

Medir suites válidas, cobertura, invocação, mutação quando aplicável, tokens,
tempo e custo de análise/embedding. Um empate numa amostra não prova que RAG
é inútil em geral: reportar incerteza, custo e os casos em que altera o resultado.

## C. Novas prioridades da avaliação completa

| Prioridade | Problema / entrega | Estado e trabalho restante |
|---|---|---|
| P0 | Sucesso exige exemplos reais e relatório sem falhas, além do exit code | **Resolvido** (`4061bcd30`): relatório coerente, exemplos passados e estado de saída compatível |
| P0 | Validar suite acumulada/final e separar cobertura de testes falhados | **Resolvido** (`4061bcd30`): gate conjunto e rollback arquivado; cobertura falhada fica como diagnóstico |
| P0 | Limitar propagação de intenção quando o LLM responde vazio | **Resolvido** (`1939c60f3`): resposta vazia/inválida interrompe a análise sem bundle incompleto nem retries adicionais |
| P0 | Preservar o método-alvo ao limitar contexto | **Resolvido para o código focal** (`ded14df34`); orçamento global em tokens continua aberto em A1 |
| P0/P1 | Identidade única de specs e retoma após validação atómica | **Resolvido em `f384cb252` e `1939c60f3`**: identidade completa no nome normal, lookup exato e checkpoints de rondas validadas; recuperação por método dentro de ronda interrompida continua futura |
| P1 | Procurar README até à raiz do projeto | **Resolvido nesta entrega**: raiz de projeto explícita, preferência pelo documento mais próximo e snapshot com caminho/hash usado na cache e no prompt |
| P1 | Reparar com código anterior, plano e diagnóstico estruturado | **Resolvido** (`3476c2e36`): contexto de reparação explícito e preservação do último código não vazio |
| P1 | Validar schema dos cenários | **Resolvido** (`ded14df34`): validação completa e fallback auditável sem novo pedido ao Planner |
| P1 | Proveniência da análise e arquivo com `--no_cache` | **Parcial / aberto**: A3 e A4; não confundir o manifesto da geração com o da cache de análise |
| P1 | Mutação pós-geração antes de mutation-guided generation | **Infraestrutura externa existente**: [protocolo comparável](../../deucalion/COMPARABLE_EVALUATION.md); integração no caminho normal e experiências guiadas por mutantes continuam separadas |
| P2 | Feedback humano, priorização aprendida e backend Python comum | **Aberto**: dados, contratos e experiências próprios; preparar depois da base de engenharia |

### Sequência de implementação a partir desta revisão

1. Completar a proveniência da análise (prompts/modelo/configuração) e o arquivo completo sem reutilizar cache. A procura do README da raiz já está corrigida.
2. Orçamento da mensagem inteira, incluindo sumários dos chamados, plano e erros.
3. Reutilização do retrieval estático entre rondas, mantendo o retrieval de erro dinâmico.
4. Consolidar a avaliação pós-geração por mutação e os dados de custo/utilidade.
5. Isolar estado antes de concorrência; preparar o controlador aprendido da tese.

As identidades normais agora usam ficheiro relativo, nome Ruby qualificado e
linhas da definição. Os nomes de tarefas XRepoTest já protegidos por task ID
mantêm a sua convenção anterior. Isto não renomeia artefactos históricos no disco.

A prova local de outubro (`scripts/audit_pipeline.py`, no checkout de revisão)
reproduzia os problemas antigos com fixtures e respostas simuladas. Não constitui
uma especificação atual: casos corrigidos podem agora parar mais cedo ou exigir
asserts diferentes. A evidência de regressão atual está nas suites
`test_suite_validation.py`, `test_repair_context.py`, `test_plan_source_validation.py`,
`test_analysis_resume.py`, `test_spec_identities.py` e `test_readme_context.py`, em
`marta/ruby_backend/tests/`.

Estas verificações não chamam modelos e não estimam ganhos de qualidade no corpus.
Cada documento de entrega acima descreve o contrato, os limites e a validação.

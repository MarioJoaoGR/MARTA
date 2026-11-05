# MARTA-Ruby — backlog revisto

Última revisão: **2026-11-05**, após integração das correções na `main`.

Esta lista distingue as correções já implementadas das melhorias ainda abertas.
As entregas e os respetivos limites estão documentados em
[validação](../../docs/RUBY_VALIDATION.md),
[reparação contextual](../../docs/RUBY_REPAIR_CONTEXT.md),
[planos e código-alvo](../../docs/RUBY_PLAN_SOURCE_CONTEXT.md),
[análise e retoma](../../docs/RUBY_ANALYSIS_RESUME.md),
[identidade dos testes](../../docs/RUBY_SPEC_IDENTITIES.md),
[README do projeto](../../docs/RUBY_README_CONTEXT.md),
[cache e arquivo de análise](../../docs/RUBY_ANALYSIS_CACHE.md),
[orçamento do pedido](../../docs/RUBY_PROMPT_BUDGET.md),
[retrieval estático](../../docs/RUBY_STATIC_RETRIEVAL.md) e
[avaliação pós-geração](../../docs/RUBY_POST_EVALUATION.md).

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
| A1 | Contexto de métodos chamados sem limite | **Orçamento total implementado.** Cada pedido inclui sistema, entrada, reserva de saída e margem; contador local ou estimativa identificada | Seleção por relevância/evidência continua aberta; não se presume contagem exata sem tokenizer correspondente |
| A2 | Trocar segunda passagem por concatenação | **Não aceite pelo utilizador.** A síntese continua implementada | Manter; medir a contribuição do grafo sem impor a substituição rejeitada |
| A3 | Cache ignora versão de contexto | **Resolvido para a proveniência disponível/declarada.** Schema 7 inclui orçamento, prompts, implementação e parâmetros do cliente; vetores incluem receita/código/metadados do embedding | Pesos e callbacks opacos continuam a exigir identificação externa; digest ausente fica explícito |
| A4 | `--no_cache` recalcula mas não grava | **Resolvido.** Cada análise tem bundle/evidência independente em `run_results/analysis_runs`, incluindo cache hits e recálculo sem cache | `--no_cache` não lê/substitui cache anterior; o arquivo não serve como cache automática |
| A5 | Paralelismo na geração | **Aberto; esforço subestimado.** Fluxo sequencial e estado global/mutável | Isolar cliente, recorder, ambiente e workspaces antes de concorrência limitada |
| A6 | Confiança nas arestas | **Aberto.** `kind` existe, mas não é usado para seleção/confiança | Registar resolução exata vs fallback/ambiguidade; não tratar toda constante como certa |
| A7 | Inferir tipos de retorno | **Aberto; investigação de maior esforço** | Começar por `Foo.new`, atribuições no construtor e anotações; medir valor antes de inferência global |
| A8 | Segunda passagem depende da ordem | **Resolvido para `done_what`.** Lê `passagem1[analysis_id]` | Não duplicar a correção; estudar separadamente a escolha de chamador em `what_todo` |
| A9 | RAG estático repetido por ronda | **Resolvido em memória por projeto.** Related reutilizado por definição/consulta/versão do índice | Rebuild, descoberta e reanálise invalidam; pesquisa de erro e exemplos continuam dinâmicos |
| A10 | Classes pouco informativas e judge sem limiar | **Aberto.** Stub + até 40 assinaturas; top-1 sem abstenção | Testar stub + construtor + sumários existentes; devolver scores e calibrar aceitação |

### A1 — orçamento total com limites explícitos

A política conta sistema + utilizador e reserva saída/margem. Reduz contexto
opcional, conserva código focal/plano/teste anterior e interrompe antes do pedido
se o obrigatório não couber. Mantém a síntese da segunda passagem. Sem tokenizer
local correspondente, usa estimativa UTF-8 identificada; o modo estrito recusa-a.
Isto não atesta a janela/template do servidor nem mede relevância de cada callee.
O [documento de entrega](../../docs/RUBY_PROMPT_BUDGET.md) define a configuração,
as prioridades, a proveniência e o que permanece por estudar.

### A3 — proveniência explícita, sem inferir pesos desconhecidos

A fingerprint já não depende só de fontes e nome do modelo. O schema 7 inclui
contexto, orçamento global, README capturado, prompts, implementação e os parâmetros disponíveis
do cliente LLM. Digest de pesos fornecido pelo chamador é registado como tal;
quando não existe, fica `unavailable`, sem fingir uma verificação automática.
As chaves dos vetores e das queries também identificam código, configuração
local e receita declarada do embedding. Provedores customizados e pesos mutáveis
continuam a precisar de identificação externa, descrita no documento de entrega.

### A4 — arquivo independente da reutilização

Cada invocação cria um arquivo próprio de análise, com manifesto, bundle completo
quando concluída e respostas disponíveis. Com `--no_cache`, os sumários são
recalculados e arquivados sem ler/substituir a cache reutilizável anterior, nem
reaproveitar a primeira passagem de uma referência explícita. Cache hits também
ficam arquivados, sem novos pedidos ao modelo. Falhas conservam respostas parciais
e diagnóstico, mas não publicam uma cache incompleta. Recuperação automática por
pedido continua a ser outro trabalho; o arquivo não seleciona respostas melhores.
A retoma da geração mantém o seu contrato separado de rondas validadas.

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

O Planner reutiliza agora o resultado estático em memória por definição,
consulta e versão do índice. A reconstrução do índice (mesmo com vetores do
disco), nova descoberta ou reanálise descartam essa reutilização. Entradas vazias
e falhas não são memorizadas; índices customizados sem revisão continuam a ser
consultados. O resultado original não é alterado por reduções posteriores do
orçamento de prompt.

A reparação continua a consultar a mensagem de erro em cada pedido e a procurar
os exemplos disponíveis nesse momento, incluindo quando o texto do erro se
repete. A proteção XRepoTest contra exemplos de outras tarefas mantém-se.
A consulta de métodos usa embedding + Chroma, e não só NumPy. Esta melhoria
poupa consultas/embeddings repetidos, não chamadas ao LLM; não demonstra por si
só ganhos de qualidade ou uma aceleração global da ferramenta.

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
| P0 | Preservar o método-alvo ao limitar contexto | **Resolvido para o código focal** (`ded14df34`); orçamento global implementado em A1, dentro dos limites do contador declarado |
| P0/P1 | Identidade única de specs e retoma após validação atómica | **Resolvido em `f384cb252` e `1939c60f3`**: identidade completa no nome normal, lookup exato e checkpoints de rondas validadas; recuperação por método dentro de ronda interrompida continua futura |
| P1 | Procurar README até à raiz do projeto | **Resolvido em `2b073ad4a`**: raiz de projeto explícita, preferência pelo documento mais próximo e snapshot com caminho/hash usado na cache e no prompt |
| P1 | Reparar com código anterior, plano e diagnóstico estruturado | **Resolvido** (`3476c2e36`): contexto de reparação explícito e preservação do último código não vazio |
| P1 | Validar schema dos cenários | **Resolvido** (`ded14df34`): validação completa e fallback auditável sem novo pedido ao Planner |
| P1 | Proveniência da análise e arquivo com `--no_cache` | **Resolvido nesta entrega**: A3/A4, dentro dos limites declarados acima; não confundir o arquivo com retoma automática nem com atestação dos pesos |
| P1 | Mutação pós-geração antes de mutation-guided generation | **Integrado opcionalmente no backend normal**: relatório independente, suite final em cópias e identidade/isolamento auditados; [benchmark mantém executor próprio](../../deucalion/COMPARABLE_EVALUATION.md). Mutation-guided generation continua separada |
| P2 | Feedback humano, priorização aprendida e backend Python comum | **Aberto**: dados, contratos e experiências próprios; preparar depois da base de engenharia |

### Sequência de implementação a partir desta revisão

1. **Concluído nesta entrega:** orçamento da mensagem inteira, incluindo sumários dos chamados, plano e erros. Contagem exata exige tokenizer correspondente; por omissão usa estimativa UTF-8 identificada.
2. **Concluído nesta entrega:** reutilização do retrieval estático entre rondas, mantendo o retrieval de erro dinâmico.
3. **Concluído nesta entrega:** avaliação opcional pós-geração, mutação e observações de custo/progresso por ronda. Não constitui recompensa RL nem migra métricas históricas.
4. Medir propostas de confiança no grafo e abstenção no judge antes de as impor.
5. Isolar estado antes de concorrência; preparar o controlador aprendido da tese.

As identidades normais agora usam ficheiro relativo, nome Ruby qualificado e
linhas da definição. Os nomes de tarefas XRepoTest já protegidos por task ID
mantêm a sua convenção anterior. Isto não renomeia artefactos históricos no disco.

A prova local de outubro (`scripts/audit_pipeline.py`, no checkout de revisão)
reproduzia os problemas antigos com fixtures e respostas simuladas. Não constitui
uma especificação atual: casos corrigidos podem agora parar mais cedo ou exigir
asserts diferentes. A evidência de regressão atual está nas suites
`test_suite_validation.py`, `test_repair_context.py`, `test_plan_source_validation.py`,
`test_analysis_resume.py`, `test_spec_identities.py`, `test_readme_context.py` e
`test_analysis_provenance.py`, `test_prompt_budget.py` e `test_retrieval_cache.py`, em
`marta/ruby_backend/tests/`. A avaliação pós-geração acrescenta
`test_post_evaluation.py` e `test_mutation_runtime.py`.

Estas verificações não chamam modelos e não estimam ganhos de qualidade no corpus.
Cada documento de entrega acima descreve o contrato, os limites e a validação.

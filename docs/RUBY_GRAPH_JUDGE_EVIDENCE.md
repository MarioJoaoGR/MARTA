# Evidência no grafo e abstenção do judge

Entrega de **2026-11-05**, posterior à avaliação pós-geração (`b18378fd5`).
Introduz categorias observáveis e políticas explícitas; não atribui probabilidades
de correção às arestas nem calibra automaticamente tipos. Experiências históricas
conservam código, manifests e resultados originais.

## O que estava errado ou escondido

O `kind` de uma aresta descrevia a sintaxe do receiver (`self`, constante,
variável, etc.), mas não identificava a evidência da resolução. O índice de
nomes curtos conservava a primeira classe encontrada. Um nome como `Service`
podia assim significar arbitrariamente `A::Service`, ignorando `B::Service`.
Também era possível tratar uma chamada implícita num método singleton como uma
chamada a um método de instância com o mesmo nome.

O judge estrutural produzia candidatos por interface, mas o enriquecimento
semântico acrescentava sempre a classe top-1 global. Podia ser estruturalmente
incompatível, provir de vetores nulos ou de um empate. Não havia score/margem
registados nem opção de abstenção.

## Grafo: preservar evidência, não inventar certeza

As arestas conservam receiver, linha, origem da resolução e candidatos de tipo.
Call sites diferentes da mesma relação deixam de perder evidência pela deduplicação
por par; os índices `uses`/`used` continuam a devolver relações únicas. Chamadas
indistinguíveis na mesma linha ainda podem colapsar, pois o parser não fornece
identidade por coluna neste contrato.

| Categoria | Significado |
|---|---|
| `static_lookup` | Resolução suportada pelo modelo estático do projeto |
| `runtime_observed` | Relação observada pelo driver TracePoint naquela execução |
| `constant_short_fallback` | Nome curto com um candidato conhecido, sem resolução lexical Ruby completa |
| `constant_ambiguous` | Várias constantes do projeto têm esse nome curto |
| `duck_unique`, `duck_ambiguous` | Um ou vários tipos do projeto são compatíveis com a interface observada |
| `constructor_mapping` | Mapeamento inferido de `new` para `initialize` |
| `selfclass_inferred` | Uso de `self.class` modelado pela classe da definição, não pelo tipo dinâmico real |
| `implicit_global_fallback` | Fallback para método de topo a partir de um owner |
| `ambiguous_definition` | O nome Ruby não identifica uma definição única |
| `legacy_unknown` | Registo antigo/customizado sem esta evidência |

`static_lookup` e `runtime_observed` formam o conjunto denominado **supported**.
Não significam chamada garantida para qualquer input/runtime. Ruby permite
redefinições, subclasses, autoload e metaprogramação; um driver dinâmico só
observa os caminhos executados. Um único tipo compatível por duck typing continua
inférido, não se torna automaticamente certo.

Nomes curtos mantêm todos os matches conhecidos, com o limite de fan-out histórico
(cinco candidatos). Um nome qualificado inexistente não cai para outra constante
com o mesmo sufixo. Ancestrais ambíguos não são escolhidos por ordem de leitura.
Não se implementa lookup lexical completo a partir de um owner qualificado.

Métodos singleton usam a tabela singleton, não a de instância. `self.class` num
singleton não é tratado como a classe owner. Um `new` singleton próprio tem
precedência sobre o mapeamento inferido para o construtor. Estas correções podem
mudar o grafo, não apenas a sua apresentação.

### Política de contexto

- `MARTA_GRAPH_CONTEXT=all` (omissão): conserva relações candidatas, com etiquetas
  de evidência no contexto e instruções para preservar a incerteza.
- `MARTA_GRAPH_CONTEXT=supported_only`: só relações supported podem fornecer
  sumários de callees **e** propagar intenção de callers. Relações excluídas não
  impedem o fallback para o README.

A segunda passagem continua a sintetizar os sumários originais da primeira.
Não se substitui a síntese por concatenação. Na propagação, callers supported
prontos têm prioridade; a ordem residual é determinística. Não se infere que
esta escolha seja ótima entre vários callers.

O JSON das arestas passa a ter registos com campos. O loader aceita também as
quatro colunas antigas, classificadas como desconhecidas. A versão do resolver
passa a **3**, impedindo reutilização silenciosa do grafo estático antigo. O DOT
mostra relações inferidas/desconhecidas tracejadas. Contagens de `edges` agora
podem incluir vários call sites; `edge_set` conserva pares únicos.

## Judge: compatibilidade, scores e decisão

`RubyClassIndex.query_scored` devolve candidatos com cosseno finito. Vetores nulos
ou não finitos não produzem um top-1 arbitrário. As classes são filtradas por
compatibilidade estrutural **antes** da operação matricial e do ranking; uma
classe incompatível não ganha por ter uma descrição semanticamente parecida.
Empates têm ordenação determinística, sem que isso os torne uma seleção válida.

A interface estrutural continua visível como `project candidates`; não é
apresentada como um tipo de runtime conhecido. O enriquecimento faz o seguinte:

1. Zero candidatos: conserva a interface e abstém-se; não consulta embeddings.
2. Um candidato: conserva-o como hipótese estrutural, sem consulta semântica.
3. Vários candidatos: regista scores dos compatíveis. Sem comparação completa
   (por exemplo, falta um sumário/vetor válido), abstém-se.
4. **Por omissão não há gates numéricos definidos:** o judge regista a evidência
   e abstém-se de selecionar um tipo semântico.

Uma política experimental pode declarar conjuntamente:

```
MARTA_JUDGE_MIN_SIMILARITY=<cosseno mínimo>
MARTA_JUDGE_MIN_MARGIN=<diferença mínima para o segundo>
```

Os valores têm de ser finitos: similaridade em [-1,1], margem em [0,2]. Valores
parciais/inválidos são recusados. Mesmo com margem zero, um empate não é aceite.
Só um vencedor estrito com comparação completa e ambos os gates satisfeitos é
apresentado como `semantic candidate`, explicitamente heurístico.

**Não foram escolhidos limiares de produção nesta entrega.** Os números usados
nos testes são fixtures, não calibração. Uma declaração de limiares não prova a
sua validade estatística. A avaliação de precisão/cobertura, o corpus de calibração
e a separação desse corpus das tarefas finais continuam trabalho necessário.
Scores de cosseno não são probabilidades de tipo. Um provider customizado sem
scores completos provoca abstenção, não fallback para o top-1 antigo.

## Evidência e proveniência

O recorder recebe `graph_context_policy` e `judge_decision`, com candidatos,
scores, decisão, razão e política. O judge conserva também as decisões no objeto
e, quando existem parâmetros avaliados, num arquivo independente:

```
run_results/judge_runs/judge_<único>/report.json
```

O relatório identifica a fingerprint de análise e a chave dos vetores disponíveis.
Sem persistência, a chave pode ser nula; não se finge atestar pesos de callbacks.
Rebuilds não sobrescrevem estes relatórios e os hints são substituídos, não
acumulados. Remover o índice também retira uma escolha semântica anterior,
conservando só o contexto estrutural. Alvos selecionados recebem o mesmo judge da sua definição de análise.

`ANALYSIS_SCHEMA=8`. A proveniência inclui implementação do resolver, índice de
tipos e política do grafo. Alterar `all`/`supported_only` invalida a análise.
Os gates do judge atuam **depois** dos sumários: mudar apenas os seus valores não
obriga a repetir chamadas LLM de análise. A receita de geração inclui a política
completa, impedindo retoma com critérios de geração incompatíveis. A calibração
pode usar os scores guardados e `semantic_decision` sem chamar o modelo.

## Benefício e custo: sem promessa de aceleração global

| Alteração | Trabalho evitado | Custo/limite acrescentado |
|---|---|---|
| Índices de evidência do grafo | Evita varrer todas as arestas em cada consulta/ordenação de callers | Metadados e índices lineares no número de call sites |
| Filtro de classes compatíveis | Compara a query apenas com os vetores elegíveis | Continua a exigir compatibilidade estrutural, que é incompleta |
| Zero/um candidato estrutural | Evita a antiga consulta semântica nesses parâmetros | Perde a escolha global top-1 deliberadamente não sustentada |
| Perguntas idênticas numa passagem do judge | Partilha um resultado/embedding bem-sucedido | Cache em memória só para a passagem/índice atual; vazios não ficam guardados |
| Etiquetas e auditoria | Torna decisões inspecionáveis e permite medir abstenção | Alguns tokens nos prompts, eventos e um relatório por passagem com decisões |

Não há novos modelos nem uma nova fase de chamadas LLM. A construção de embeddings
de classes mantém-se. Correções que mudam as relações encontradas podem mudar
quais métodos recebem os pedidos de enriquecimento já existentes e o tamanho do
contexto; não se promete número/tempo LLM global idêntico. O orçamento de prompt
continua a contar as etiquetas e a proteger o método focal. Não foi medido ganho
de qualidade nem aceleração global num corpus real nesta entrega.

## Validação e pendências

Fixtures offline exercitam constantes ambíguas, qualificadas ausentes, singleton
vs instância, `new` próprio, duck typing único, call sites com evidência diferente,
JSON antigo/novo, filtro nas duas direções e uso dos sumários originais. Os testes
de lookup indexado recusam deliberadamente uma nova varredura da lista de arestas.

NumPy real e vetores determinísticos verificam compatibilidade, zeros/NaN/Inf,
empates, margens, decisão declarada e abstenção por omissão. Consultas idênticas
usam um embedding por passagem; decisões/arquivos continuam independentes. Não há
instalações, downloads nem inferência real nestes testes.

Ainda faltam o estudo empírico da precisão do grafo, calibração dos gates,
melhoria do conteúdo dos sumários de classe (A10), inferência de retornos (A7)
e isolamento de estado para paralelismo (A5). Esta entrega não os dá como feitos.

Validação final: **866 testes locais aprovados** e **16 no container existente**
(12 de compatibilidade e quatro controlos reais de Mutant): **882 aprovados**.
Dos sete saltados no host, quatro foram executados no container; restam três
ignorados. Sem instalações, downloads ou inferência LLM real.

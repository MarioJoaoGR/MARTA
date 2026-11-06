# Propagação de intenção por camadas — A8

Entrega de 6 de novembro de 2026. Corrige a seleção dependente da ordem em
`what_todo` e evita varreduras repetidas de todos os alvos.

## Problema reproduzido

Considere as relações de chamada:

```text
       root
      /    \
   alpha   beta
      \    /
        join
```

O código anterior percorria os alvos e propagava imediatamente de um caller que
já tivesse intenção. Na ordem `root, beta, join, alpha`, `join` recebia a intenção
de `beta`; na ordem `root, alpha, join, beta`, recebia a de `alpha`. Ordenar os
nomes dos callers disponíveis não resolvia a diferença de disponibilidade.

Um teste com respostas simuladas reproduziu essa troca antes da correção. A
escolha agora é igual nas duas ordens e na permutação das adjacências.

## Política explícita

A política `intent-root-layers-v1` prepara o plano antes dos pedidos de intenção:

1. Filtra as relações pelos métodos com definição não ambígua no pool de análise
   e pela política `all`/`supported_only` já existente.
2. Identifica raízes: métodos sem callers elegíveis. Estes recebem intenção a
   partir do README, como antes.
3. Percorre camadas de distância mínima a uma raiz. Todos os candidatos a caller
   da camada anterior já terão uma intenção quando se executar a próxima.
4. Havendo vários candidatos nessa camada, prefere uma relação com suporte no
   modelo do grafo; num empate, escolhe pelo nome qualificado.
5. Ordena os alvos de cada camada pelo nome e executa uma síntese por alvo.

No diamante acima, `alpha` e `beta` ficam na camada 1; `join`, na camada 2.
Com evidência equivalente, escolhe `alpha`. Se só a relação `beta -> join` tiver
suporte, escolhe `beta`, desde que ambos sejam da mesma camada anterior.

**A distância à raiz tem prioridade sobre o suporte da aresta.** Uma ligação
direta inferida de uma raiz pode ganhar a uma ligação suportada que só estaria
disponível numa camada posterior. É uma política determinística e limitada,
não uma alegação de escolha semanticamente ótima ou de certeza em runtime.
Ajustar essa prioridade exige uma política/experiência própria, não uma mudança
silenciosa conforme um teste falha.

Cada método alcançável recebe uma única atribuição de caller. Ciclos alcançáveis
são visitados sem repetir métodos. Ciclos sem caminho desde uma raiz, e os seus
descendentes ainda inacessíveis, continuam a receber o fallback README individual.
Não se usa uma intenção de fallback para iniciar uma segunda propagação.

Métodos com definições ambíguas continuam separados pela identidade de análise:
não se fundem os seus sumários nem se usam como callers elegíveis. Conservam o
comportamento de raiz individual existente. Sem grafo/enriquecimento, todos os
alvos continuam a receber a perspetiva README e não há propagação.

## O que mantém e o que muda

Mantém-se a síntese pelo LLM, o snapshot da primeira passagem de `done_what`, os
orçamentos do pedido, as etiquetas de evidência e o contrato de resposta não vazia.
Não se substituem sumários por concatenação, não se acrescentam retries e não se
usam testes/ground truth para escolher o caller.

Para o mesmo grafo/pool e uma análise concluída, permanece uma chamada de intenção
por alvo: raiz, propagação ou fallback. A contagem dos pedidos de síntese não
aumenta. Os textos enviados podem mudar porque o caller escolhido muda; também
podem mudar tokens de saída/contexto e resultados posteriores.

Este contrato estabiliza o plano de propagação. Não torna o LLM determinístico,
nem ordena todas as outras fases da análise ou garante sumários idênticos se os
inputs/respostas de origem mudarem.

## Custo e registos

`intent_flow.py` percorre as adjacências elegíveis uma vez para construir o plano,
com seleção local de caller por camada. O custo é `O(V log V + E)`, incluindo as
ordenações; a preparação usa memória temporária `O(V + E)`. O plano conservado
tem tamanho `O(V)`. A propagação deixa de pesquisar todos os alvos a cada avanço
numa cadeia longa. Não se afirma uma aceleração global medida: o custo LLM pode
dominar e a preparação agora guarda explicitamente os passos.

O recorder escreve `intent_flow_policy`, com contagens de raízes, camadas,
propagações e fallback. `intent_parent_selection` identifica método/caller por
identidade de análise e nome, profundidade e política. Essa seleção é o passo
planeado; uma resposta inválida ainda interrompe a análise e não publica bundle
incompleto. O arquivo de pedidos conserva o contexto e as respostas disponíveis.

A proveniência inclui a política e o hash da implementação de `intent_flow.py`.
Análises incompatíveis não entram como cache válida. Experiências e resultados
congelados não são migrados nem apresentados como produzidos por esta política.

## Verificação

Fixtures cobrem o diamante reproduzido, permutações de métodos/arestas, prioridades
de suporte e distância, callers excluídos, ciclos alcançáveis/inalcançáveis,
`supported_only`, ausência de grafo e uma cadeia de 2500 métodos. Nesta cadeia há
uma consulta de callers por método, sem recursão nem varreduras globais repetidas.
Os testes de integração verificam a escolha/telemetria e conservam três pedidos
reais de síntese simulada para o enriquecimento do diamante.

A precisão e o efeito na qualidade em repositórios reais continuam por medir.

Validação final: **1117 testes locais aprovados**, seis ignorados no host;
**16 aprovados no contentor existente**, incluindo quatro daqueles ignorados.
Total: **1133 aprovados; dois permanecem ignorados**. Sem inferência real,
instalações ou alteração dos resultados dos papers.

# Consumidores RAG separados — B3

Entrega de 6 de novembro de 2026. Permite medir componentes individualmente;
não é uma nova política aprendida de seleção de contexto.

## Três opções independentes

| Opção nativa | Retira | Conserva |
|---|---|---|
| `--no_planner_retrieval` | Métodos related recuperados para o Planner | Sumário focal, código, tipos, cobertura e retrieval na reparação |
| `--no_error_retrieval` | Sumários/exemplos recuperados a partir do erro | Teste anterior, plano, diagnóstico, resultados observados e tentativas de reparação |
| `--no_semantic_judge` | Refinamento de tipos por similaridade com classes | Candidatos estruturais, índice de tipos do grafo, sumários de classes e retrieval de métodos |

Todas ficam desligadas por omissão: a geração normal continua a usar os três
consumidores. As versões com hífen também são aceites na CLI nativa. O adapter
XRepoTest aceita as versões com hífen através do mesmo parser de opções.

As opções antigas mantêm o significado:

- `--no_method_retrieval` desliga os dois consumidores de métodos, Planner e erro.
- `--no_type_hints` omite todas as sugestões de tipos no Planner e dispensa o
  índice semântico de classes. O índice estrutural do grafo continua disponível.
- `--no_rag`, da CLI nativa, continua a saltar a preparação RAG inteira.
- `--no_repair` continua a limitar o Dev a uma tentativa por ronda. Não é o mesmo
  que retirar apenas a ajuda recuperada na reparação.

As remoções compõem-se: uma opção antiga que desliga um conjunto não é anulada
por deixar as opções novas desligadas. Não se pode reativar um consumidor com
uma destas flags de remoção.

## Experiências que passam a ser possíveis

| Braço | Opções adicionais, relativamente à execução normal |
|---|---|
| Sem related no Planner | `--no_planner_retrieval` |
| Sem ajuda recuperada no erro | `--no_error_retrieval` |
| Sem judge semântico | `--no_semantic_judge` |
| Sem retrieval de métodos | `--no_method_retrieval` |
| Sem os três consumidores por embeddings | As três opções novas em conjunto |

Usar um `--output_dir` separado na CLI nativa, como nas ablações existentes.
Não se fez nenhuma destas experiências nesta entrega. É preciso manter tarefas,
modelo, orçamento, amostragem, avaliador e política de exemplos controlados para
comparar resultados; os testes offline não demonstram ganhos no corpus.

## Trabalho evitado e limites

O índice de métodos só é construído se pelo menos um dos seus consumidores
estiver ativo. Desligar apenas um mantém o índice partilhado necessário ao outro.
O índice semântico de classes não é construído quando o seu consumidor está
desligado. Reconstruir RAG sem esse índice repõe o judge estrutural e apaga as
decisões semânticas anteriores; vetores já existentes não reativam um consumidor.

O cache em memória de related não devolve contexto antigo ao Planner desativado.
A reparação ativa continua a consultar o erro atual e os exemplos permitidos;
as proteções XRepoTest contra testes de outras tarefas mantêm-se.

Na reutilização explícita XRepoTest, a cópia inicial dos stores conserva apenas
os índices pedidos. Classes desativadas não exigem ler a sua matriz para o banco
de embeddings; métodos desativados não exigem abrir Chroma nesse banco. Os hashes
dos ficheiros de referência continuam a ser auditados, mesmo para índices que
não serão usados. Stores já existentes no destino não são apagados.

Esta alteração não acrescenta chamadas LLM, modelos ou embeddings. Desligar um
consumidor pode evitar consultas, embeddings de queries ou de documentos quando
o índice deixa de ser necessário. A análise/síntese de sumários mantém-se; não se
promete acelerar toda a execução nem melhorar a qualidade. O custo real depende
do cache e dos consumidores que restam ativos.

As opções são configuração fixa de uma execução, não ações RL alteradas durante
um pedido. O controlador aprendido e a política estrutural/lexical ou híbrida
continuam trabalhos separados.

## Contrato de execução e proveniência

A política de ablação passa a `component-removal-v2`. As opções entram nos
manifestos/eventos e na identidade de geração pelos mecanismos existentes.
Configurações diferentes não podem reutilizar silenciosamente rondas antigas.
A primeira ronda normal só pode ser partilhada na remoção pura de feedback de
cobertura; qualquer remoção nova impede essa exceção, tanto nativa como XRepoTest.

O launcher GPU XRepoTest encaminha `XREPO_NO_PLANNER_RETRIEVAL`,
`XREPO_NO_ERROR_RETRIEVAL` e `XREPO_NO_SEMANTIC_JUDGE` (0/1), com validação e
propagação às continuações. O launcher CPU existente continua reservado à retoma
do braço sem grafo já certificado; restaura estas flags a zero e recusa um
manifesto que tenha uma remoção adicional. Não se tornou um launcher genérico de
novas experiências CPU.

Não se migram manifestos históricos, não se alteram tarefas/métricas do benchmark
e não se submetem jobs. Resultados congelados permanecem associados ao código e
às opções com que foram obtidos.

## Verificação

Fixtures offline cobrem as oito combinações dos três consumidores, índices
necessários, cache previamente carregado, judge estrutural, prompts reais de
Planner/reparação com respostas simuladas, encaminhamento de flags, rejeição de
valores inválidos e proteção da primeira ronda. A suite inclui equivalência de
prompts/chamadas/specs/resultados por omissão com o `project.py` anterior a esta
entrega. Sem chamadas a modelos, downloads ou instalações.

Validação: **1095 testes locais aprovados**, seis ignorados no host; **16
aprovados no contentor existente**, incluindo quatro daqueles ignorados. Total:
**1111 aprovados; dois permanecem ignorados**. O teste de equivalência foi
executado com um snapshot da implementação anterior e respostas simuladas.

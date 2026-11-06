# A5 — coordenação de geração e métricas por worker

Entrega de 6 de novembro de 2026, posterior a `44333eea0`. Implementa concorrência
**opcional no backend Ruby nativo**, sem a impor às execuções existentes. O ganho
real de tempo/memória no servidor continua por medir.

## Configuração e compatibilidade

Por omissão: `generation_workers=1`, `round_barrier=False`, sem novos workspaces.
O comportamento sequencial de exemplos disponíveis durante a ronda mantém-se.
`isolate_execution=True`, introduzido na entrega anterior, continua opcional.

Para usar o coordenador:

- API: `RubyProject(..., isolate_execution=True, generation_workers=2)`; aceita
  1, 2 ou 4 workers. Com 2/4, a barreira de ronda é obrigatória e automática.
- CLI: `--isolate_execution --workers 2` ou `--workers 4`.
- Referência com a mesma política mas sem concorrência: acrescentar
  `round_barrier=True` à API ou `--round_barrier --workers 1` ao CLI, juntamente
  com o isolamento. Assim se pode comparar 1/2/4 sem trocar simultaneamente a
  política de exemplos/publicação. Usar outputs independentes por configuração.

O cliente tem de fornecer `response_api=True` e `aask_result` com `ChatReply`
por pedido. A fachada Ruby nativa já o faz. Providers legados que dependam de
`last_call`, deltas globais ou contadores partilhados de tentativas são recusados
antes da geração. Os parâmetros e a configuração do cliente/índices devem
permanecer estáveis enquanto a execução decorre.

Backends customizados, incluindo o adaptador XRepoTest, continuam fora desta
opção. Não se ativa concorrência no avaliador ou no ambiente global desse
adaptador. Não se submetem jobs nem se modificam experiências congeladas.

## O que executa em paralelo

Existem no máximo 1/2/4 corrotinas de worker num único event loop. Podem sobrepor
as esperas pelo LLM; reutilizam o mesmo cliente, limiter, modelo e índices.
**Subprocessos Ruby, retrieval e preparação continuam síncronos nesse loop.**
Não se criou outro pool de processos, outro modelo de embeddings ou outro modelo
LLM por worker. O servidor pode continuar a serializar os pedidos; o limite
configurado não demonstra uma aceleração nem deve exceder a capacidade medida.

Cada worker usa um workspace privado, criado apenas quando necessário e
reutilizado entre os seus métodos/rondas. A cobertura usa o workspace do slot 1,
sem acrescentar outra cópia para o coordenador. Se há menos alvos elegíveis que
workers, só são usados os slots necessários. Uma ronda vazia não cria cópias nem
faz pedidos ao modelo.

Mantêm-se os limites de tentativas, reparação e rondas, bem como o skip por
cobertura completa e `--limit`. O scheduler não acrescenta tentativas, não volta
a pedir uma resposta por outra ser pior, e não escolhe o melhor candidato entre
réplicas. Métodos que falham normalmente terminam com o mesmo estado sem testes.

## Barreira, exemplos e publicação

1. O coordenador determina os alvos elegíveis na ordem habitual.
2. Captura uma visão dos exemplos disponíveis no início da ronda. Guarda apenas
   os primeiros 400 caracteres por ficheiro, o limite já usado no prompt de
   reparação. A pesquisa por erro continua a acontecer em cada reparação; não é
   substituída por uma resposta memorizada. O lookup continua exato por definição
   e, quando aplicável, identidade de tarefa.
3. Distribui os alvos em faixas fixas: com dois workers, o primeiro recebe as
   posições 0, 2, 4; o segundo 1, 3, 5. A atribuição não depende de quem responde
   mais depressa. Não se pretende aqui uma política adaptativa de escalonamento.
4. Cada worker executa Planner/Dev/validação individual com recorder e diretório
   próprios. Os candidatos aprovados ficam privados até todos os jobs da ronda
   terminarem. Um worker não usa como exemplo o candidato recém-gerado de outro.
5. O coordenador verifica as fontes e publica os candidatos pela ordem dos alvos,
   comparando o código validado antes da substituição atómica dos ficheiros.
6. Valida a suite acumulada num só processo e mantém o rollback arquivado de
   novos specs incompatíveis, também pela ordem estável dos alvos. Só depois
   grava o checkpoint da ronda.

A referência sequencial antiga permite exemplos concluídos anteriormente na
mesma ronda. A referência `--round_barrier --workers 1` permite apenas os que
estavam disponíveis no início da ronda, tal como 2/4. Essa distinção consta da
receita; **não se devem atribuir diferenças de qualidade entre essas duas
políticas apenas à concorrência**. Mesmo com a política igual, um modelo
estocástico e a execução no servidor podem produzir respostas diferentes.

## Métricas, falhas e retoma

Cada job tem um recorder pequeno: contadores, timers, fase e contexto próprios.
Herdam a origem temporal do run, mas não partilham os dicionários de contadores.
O coordenador recolhe cada job iniciado uma única vez no seu `finally`, incluindo
os interrompidos. Não mistura `first_run` nem cobertura dos workers: a primeira
ronda é identificada no job e o histórico de cobertura pertence ao coordenador.

O relatório agregado conserva os contadores existentes e acrescenta `workers`
com os totais por slot. Os eventos incluem worker, ronda, identidade da definição
e duração do job; falhas/cancelamentos ficam explícitos. Uso desconhecido não é
apresentado como tokens medidos a zero. Os timers dos jobs não substituem o timer
de parede da ronda.

As durações de chamadas/fases somadas podem sobrepor-se entre workers. Para medir
aceleração, comparar o tempo de parede de execuções equivalentes; não usar a soma
dos tempos LLM como duração da execução ou faturação GPU.

Uma exceção interrompe a ronda: o coordenador cancela e aguarda as corrotinas
restantes antes de limpar workspaces. Candidatos privados já concluídos são
arquivados como evidência. Não há retry automático do scheduler nem checkpoint
parcial. A falha de publicação pode deixar specs publicados mas não certificados;
a retoma conserva o mecanismo anterior que os arquiva antes de repetir a ronda.
Essa recuperação não significa que o custo anterior desapareceu.

Cancelar o await não garante cancelar um pedido síncrono já entregue à thread ou
ao servidor. O seu uso final pode ficar desconhecido; a API por resposta evita
que um retorno tardio seja atribuído a outro pedido. SIGKILL/falha de máquina
mantém os limites de limpeza descritos no [documento de isolamento](RUBY_EXECUTION_ISOLATION.md).

## Custo e proveniência

Por omissão não há workers adicionais, snapshots de exemplos ou cópias novas.
Na opção coordenada há no máximo uma cópia por slot usado e uma visão curta dos
exemplos por ronda. Os índices/sumários permanecem partilhados para leitura;
não se repete a descoberta nem os embeddings por worker. A atribuição fixa pode
ficar desequilibrada em métodos com custos muito diferentes: é uma escolha de
previsibilidade, não uma promessa de distribuição ótima.

A receita inclui número de workers, política de barreira/exemplos e hashes da
implementação. Configurações distintas não reutilizam silenciosamente o mesmo
checkpoint. Não se migram métricas nem se reclassificam resultados dos papers.
Este é um mecanismo de engenharia disponível para medição, não uma validação
empírica de ganho, qualidade ou capacidade do servidor.

## Verificação offline

`test_generation_workers.py` usa respostas `ChatReply` scriptadas e Ruby/RSpec
reais: limites 2/4, conclusão fora de ordem, publicação ordenada, contadores exatos,
primeira ronda, cancelamento, falha com candidato privado já concluído, retoma de
publicação parcial, rollback de interação, exemplos fixos, output externo,
referência com um worker, população vazia e skip/limite sem workers ociosos.
Não faz pedidos LLM, instalações ou downloads. Os controlos Mutant e a
compatibilidade XRepoTest usam o container já existente, com rede desligada.

Validação: 926 testes na suite local completa, seguidos de 44 aprovações nos
módulos de workers/pedidos, incluindo três novos casos de providers através de
fachada: **929 testes locais distintos**. Mais **16 aprovações no container**
(Mutant e compatibilidade XRepoTest): **945 no total**. Sete saltados no host,
quatro deles executados no container; três permanecem saltados. O CLI `--help`
foi também verificado. Os avisos Pydantic/Chroma preexistentes não exigiram
atualizar pacotes.

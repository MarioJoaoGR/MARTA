# Avaliação pós-geração, mutação e observações de custo/utilidade

Entrega de **2026-11-05**, depois da reutilização do retrieval estático
(`3d0e73b39`). Aplica-se ao backend Ruby normal. Os executores, manifests, tarefas
e resultados congelados do XRepoTest/papers não foram alterados.

## Utilização

O fluxo normal conserva o comportamento anterior por omissão. Para gerar e
acrescentar um relatório independente:

```bash
python -m marta.ruby_backend.start_react \
  --project_path /caminho/projeto --source_path lib --num 3 --evaluate
```

Para avaliar apenas a suite guardada, sem sumários, RAG ou chamadas ao modelo:

```bash
python -m marta.ruby_backend.start_react \
  --project_path /caminho/projeto --source_path lib --evaluate_only
```

Este modo ainda descobre/parseia o projeto para obter as definições e aplica os
mesmos seletores/ambiente de carregamento da geração. Não inventa os custos da
execução original nem substitui o JSON/eventos antigos da geração. `discover`
conserva os seus mecanismos normais de cache/carregamento; não é uma leitura
forense de um repositório arbitrário. Usar o mesmo `--output_dir`, nome, seletores
e ambiente quando os testes estiverem numa pasta de saída separada.

Para pedir também mutação, acrescentar:

```bash
--mutation --mutation_usage opensource --mutation_timeout 300 --mutation_jobs 1
```

`mutation_usage` é passado explicitamente ao Mutant (aceita também `commercial`).
A ferramenta não escolhe esse modo pelo utilizador. `--mutation_bundle` executa o
Mutant e a sua baseline com o ambiente Bundler fornecido. Não faz bundle install.
Timeout/jobs positivos são validados antes de iniciar a geração.

Não se instala nem descarrega nada. Esta versão do adapter suporta **Mutant e
mutant-rspec 0.15.1** no ambiente escolhido. Ausência, outra versão, incompatibilidade
com o Ruby/projeto ou falha de licença/carregamento produzem `unavailable` com
diagnóstico. A validação real usou exclusivamente a imagem local já existente
`marta-xrepotest:repaired-v2`, offline; não tornou o Mutant disponível no ambiente
Ruby do Mac. Não há chamadas ao Deucalion nesta entrega.

## População e isolamento

A população de testes é a **suite acumulada final de specs gerados** em
`marta_specs`, não tentativas rejeitadas nem os testes humanos. As rondas são
juntas numa suite de avaliação, mantendo o código. Os alvos são as definições
selecionadas para o projeto, com identidade, caminho e linhas; `--limit` limita
os alvos medidos, não extrai uma nova suite mais favorável. Um alvo sem spec
próprio pode ser exercitado por outro teste da suite do projeto.

Cobertura e mutação executam em cópias descartáveis. Guardam-se hashes dos inputs
conhecidos (fontes fornecidas, specs, locks/gemspecs e preloads de ficheiro
explicitamente disponíveis) e verifica-se que os originais não mudaram durante
a avaliação. Alterações impedem a emissão de um relatório completo certificado.
As configs Mutant do projeto são substituídas **só na cópia**, pelos argumentos
controlados; o original conserva-se. A configuração RSpec evita `.rspec` local e
a seleção Mutant só admite exemplos da suite fornecida.

A cópia não é um sandbox de segurança do sistema operativo: dependências,
serviços externos, caminhos absolutos embutidos e recursos ligados por symlinks
podem precisar de um ambiente relocável/pinado. A suite concatenada muda o
ficheiro de origem dos testes; testes que dependam de `__FILE__`/`__dir__` podem
falhar. A baseline da suite efetivamente preparada é validada e a falha fica
explícita. Targets fora da raiz ou que o runtime não consiga identificar não
são adivinhados. O adapter normal recusa backends customizados como XRepoBackend;
o benchmark deve continuar a usar o seu executor próprio.

## Contrato de mutação válida

1. Baseline RSpec completa, com exemplos reais aprovados e sem falhas.
2. Versões efetivas de Ruby, Mutant, mutant-rspec e rspec-core registadas.
3. Exatamente um subject Mutant com expressão, caminho físico e linhas da
   definição focal. A expressão Prism é candidata até esta verificação.
4. Todos os exemplos descobertos, elegíveis e selecionados pertencem à suite
   fornecida; specs humanas são recusadas, não apenas ignoradas no score.
5. Resumo completo: `Results == Mutations`, total igual ao auditado no ambiente,
   `Kills + Alive == Mutations`, total positivo, zero timeouts e sem neutral
   failure. Exit 1 por sobreviventes é uma medição normal, não um erro.
6. Fontes e suite preparadas conservam os seus hashes durante a medição.

Uma medição inválida conserva `mutation_score=null`. Zero mutantes, erro de
arranque, timeout e ausência de testes não se fazem passar por scores zero
medidos. Em timeout termina-se o grupo de processos, incluindo workers. O timeout
configurado refere-se ao processo Mutant; o probe (30 s) e a baseline RSpec
(60 s) têm limites próprios. A pasta de evidência conserva stdout, stderr,
comando, configuração, identidade e contagens. Não há retries automáticos nem
regeneração de testes para melhorar resultados.

O bootstrap adapta o contrato de identidade/isolamento anteriormente validado
para XRepoTest; não modifica os operadores nem a contagem de mortes do Mutant.
Uma suite trivial pode matar mutantes por efeitos de carregamento: não se promete
que todo o mutante morto demonstre uma asserção útil.

## Relatório e denominadores

Cada avaliação cria uma pasta nova:

```
run_results/evaluations/evaluation_<único>/
  manifest.json
  baseline.json          # quando houve execução de cobertura
  targets/<índice>.json
  mutation/<índice>/...  # quando a avaliação desse alvo arrancou
  report.json            # apenas quando a avaliação terminou sem inputs alterados
```

`complete` certifica a conclusão do relatório, não que todas as medições estejam
válidas. A validade da suite e de cada mutação tem campos próprios. Erros de
execução ficam indisponíveis; interrupções preservam o manifesto e resultados
parciais, sem publicação final. Não há retoma automática deste novo relatório:
um pedido explícito seguinte cria outra pasta e não escolhe o melhor resultado.

A cobertura por alvo guarda linhas/ramos/invocação fornecidos pelo helper. Campos
ausentes permanecem desconhecidos; não se inventa invocação a partir de uma linha
`def` coberta. Não se chamam a estes campos CSR/TPR/IR do paper: esta é avaliação
normal de uma suite de projeto, não reprodução das tarefas XRepoTest.

A mutação expõe separadamente:

- `ms_all_targets_zero_imputed`: média sobre todos os alvos, **imputando
  explicitamente zero às indisponibilidades apenas neste agregado**.
- `ms_valid_only`: média condicionada às medições válidas.
- `pooled_diagnostic`: mortos/total agrupados nas medições válidas.
- N de alvos, medições válidas, indisponibilidades e contagens dos mutantes.

Por exemplo, scores 1/1 e 0/9 e um alvo indisponível dão macro global 1/3,
condicional 1/2 e agrupado 1/10. O alvo indisponível continua `null` no registo.
Sem pedido de mutação ou sem denominador, os agregados respetivos são `null`.

## Custo e utilidade observada

O relatório posterior à geração recebe uma cópia dos contadores do recorder:
chamadas, tokens, segundos por fase e subprocessos. O âmbito é **somente o processo
atual**. Uma retoma pode ter herdado trabalho anterior; não se apresenta este
subtotal como o custo integral da experiência. No modo `--evaluate_only`, o custo
de geração fica `null`. O tempo da avaliação está separado. Não se atribuem preços
ou custos monetários sem dados. Callbacks opacos podem contar chamadas com zero
tokens sem que isso prove usage zero; a limitação fica identificada.

Depois de cada ronda validada e comprometida em checkpoint, um evento
`round_utility` regista alvos/IDs, cobertura antes/depois, delta de linhas, gerações
aceites/rejeitadas, chamadas/tokens/tempo LLM novos e tempo total da ronda. A
primeira ronda não tem baseline medida: delta `null`, não ganho contra zero.
Denominadores diferentes/observações ausentes também não produzem deltas. Perdas
observadas conservam o sinal negativo. A validação conjunta e o rollback precedem
a observação; não se credita como progresso código rejeitado.

São observações ao nível da ronda, não uma recompensa de RL pronta nem atribuição
causal a um sumário, retrieval ou tentativa de reparação. A mutação é exclusivamente
pós-geração e nunca entra nos prompts ou nas decisões destas rondas. Crédito por
ação, episódios, objetivos aprendidos e experiências guiadas por mutantes continuam
trabalho próprio da tese/estudos posteriores.

## Validação

Testes offline cobrem relatórios imutáveis, modo sem geração, ausência de engine,
suites vazias/falhadas, fontes alteradas, cópia descartável, denominadores, scope
de custo, deltas desconhecidos/negativos e integração CLI opcional. As respostas
LLM são scriptadas; não há inferência real.

Os controlos reais em Docker usam Mutant instalado, sem rede: suite útil vs
trivial, sentinela de specs humanas, operador Ruby, identidade/linhas incorretas
e baseline falhada. A suite útil deve matar mais que a trivial, sem impor zero ao
controlo fraco. As suites existentes de retoma, ablação, RAG, orçamento e avaliação
XRepoTest continuam a ser verificadas. Os controlos não são resultados de paper.

Validação final: **832 testes locais aprovados**, mais **16 no container**
(12 de compatibilidade e quatro controlos de Mutant reais): **848 aprovados**.
Dos sete saltados no host, quatro foram executados no container; restam três
ignorados. Nenhum pacote/modelo foi instalado ou descarregado.

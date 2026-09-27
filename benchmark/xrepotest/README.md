# MARTA no XRepoTest Ruby

Estado em 27-09-2026: integração implementada e testada localmente; ambiente
derivado construído; os dez bundles e os dez diagnósticos RSpec passam offline.
As duas falhas confirmadas no avaliador de cobertura foram corrigidas na imagem
`marta-xrepotest:repaired-v2`, com autorização do utilizador (detalhes abaixo).
Nenhuma nova geração LLM foi iniciada. No Deucalion, o job CPU 1956251
converteu a imagem e confirmou os imports Python, mas o preflight encontrou
recusas de proprietário do Git em Hanami e RSpec-core. A adaptação em
`runtime.py` autoriza apenas os caminhos exatos do repositório e das suas
dependências Git, por variáveis de ambiente do processo (`safe.directory`).
Não escreve na configuração global da conta nem altera fontes, dependências
ou o avaliador. O erro foi reproduzido em Docker com UID 12345; com esta
adaptação, os bundles afetados, os dez diagnósticos RSpec, os sete casos de
cobertura e a mutação Hashie passam offline com esse UID sem privilégios.
A verificação no cluster tem de voltar a passar.

## Protocolo e âmbito

Usamos as 675 tarefas Ruby oficiais, mantendo os identificadores 0–674, os
repositórios e o código publicado. São 302 ficheiros em dez repositórios. As
coordenadas são linhas começadas em 1, com ambos os extremos incluídos. O
`private def` da tarefa 647 também é identificado corretamente pelo Prism.

| Repositório | Tarefas de geração | Métodos para contexto |
|---|---:|---:|
| capybara | 155 | 1 196 |
| dotenv | 11 | 57 |
| grape | 97 | 606 |
| hanami | 81 | 583 |
| hashie | 28 | 269 |
| httparty | 26 | 235 |
| pundit | 7 | 56 |
| rom | 97 | 796 |
| rspec-core | 123 | 1 064 |
| shoryuken | 50 | 270 |
| Total | 675 | 5 132 |

`RubyProject(full_context=True)` separa `analysis_targets` de `targets`. O
primeiro conjunto inclui métodos de produção nas árvores `lib/`, incluindo
construtores; o segundo corresponde exatamente às tarefas por ficheiro, nome e
intervalo de linhas. Os 48 alvos `initialize` não são excluídos. Construtores
devem ser testados por construção normal de objetos, sem manipular os testes
para satisfazer a heurística de invocação do avaliador.

Os testes humanos, fixtures, exemplos, dependências instaladas e templates não
entram no conjunto de sumários. Podem continuar a fazer parte do ambiente de
execução oficial. `full_context` significa este âmbito de análise estática:
metaprogramação, resoluções ambíguas e truncagens de prompts continuam a limitar
o contexto efetivamente disponível. Não significa enviar o projeto inteiro em
cada pedido ao modelo. Em particular, mantém-se o limite de código por método
e a recuperação top-k da MARTA.

Cada tarefa tem uma cópia de trabalho, os seus testes e a sua cobertura. As
rondas acumulam exemplos numa única suite final. Não usamos testes gerados
para outras tarefas como exemplos no RAG. O contexto de produção é partilhado
entre tarefas do mesmo projeto; não usamos contextos LSP/BM25/dense preparados
pelo XRepoTest.

A segunda passagem de `done_what` lê os sumários originais da primeira passagem,
evitando que a ordem de processamento determine se um callee já foi enriquecido.
Definições com nomes qualificados repetidos mantêm identidades próprias no
armazenamento e no RAG; a propagação pelo grafo omite esses nomes ambíguos.
O limite antigo de 50 sumários de classes deixa de se aplicar no modo full context.

## Versões verificadas

- Código de origem do avaliador: `39fb6ab3173136d3dac2d38ed7c98baf6c470270`;
  correção local `coverage-order-and-exact-path-v1`.
- Dataset Hugging Face: revisão `cd694c00d20951aef189a406abac980a6b1c49d4`.
- SHA-256 de `ruby_functions.jsonl`:
  `811639c4291d3bd14ff58d8b2976bfffbf4df08cbf7d7aab22080c88165747dd`.
- Imagem Linux/amd64:
  `dungxg502/xrepotest-ruby@sha256:e7e857ff5c73345a9492a5352a52262da9796a3cb29c5f18053e0be1e8b6924d`.
- A imagem contém os dez repositórios completos, Ruby 3.2.11 e Prism 1.9.0.
  Os 302 ficheiros focais coincidem com `file_content` do dataset; os ficheiros
  Python `base/` e `ruby/` da imagem original coincidem com a revisão acima.
  Na imagem derivada, só `ruby/command_utils.py` difere, pelas duas correções
  descritas abaixo; os hashes de todos os módulos são registados e validados.

Fontes: [XRepoTest](https://github.com/solis-team/XRepoTest),
[dataset](https://huggingface.co/datasets/solis-soict/xrepotest).

## Ficheiros e utilização

- `protocol.py`: valida tarefas, fontes e identidades das experiências; exporta
  uma resposta por tarefa, ou `[]` se não foram obtidos testes.
- `prepare.py`: verifica a correspondência Prism, conta o âmbito de análise e
  testa os bundles. Uma falha impede a geração completa. O estado da mutação é
  reportado separadamente.
- `backend.py`: feedback de RSpec com `bundle exec`, respeitando `.rspec`, com o
  teste colocado no mesmo local usado pelo avaliador (`spec/temp_spec.rb`).
- `run.py`: análise, geração por tarefa, retoma e exportação. Exige preflight
  válido e diretório de experiência próprio. O modelo e o seu digest são
  explícitos; não há omissão que lance uma escolha diferente por acidente.
- `evaluate.py`: executa o avaliador publicado com as duas correções registadas,
  sobre cópias de trabalho por tarefa,
  grava resultados individuais e usa o agregador oficial. Pode retomar tarefas
  concluídas. A avaliação não é substituída pela cobertura interna da MARTA.
- `report.py`: contabiliza chamadas e tokens por fase, subprocessos Ruby,
  reutilizações de cache e tarefas concluídas, incluindo eventos de retomas.

Exemplo de inspeção dentro da imagem, com o código MARTA montado em `/opt/marta`
e uma pasta de relatórios em `/data/xrepo`:

```bash
PYTHONPATH=/opt/marta python3 -B -m benchmark.xrepotest.prepare \
  --dataset /app/xrepotest/ruby_functions.jsonl \
  --output /data/xrepo/preflight.json
```

`--sources-only` faz apenas a inspeção estática. **Não certifica o ambiente.**

No Deucalion, `deucalion/setup_xrepotest.sh` converte o arquivo Docker validado
em `mario/xrepotest/repaired-v2.sif`, reutiliza o Python existente e verifica
o ambiente em CPU. O arquivo tem de ser transferido previamente; não há fallback
silencioso para a imagem original incompleta.
`deucalion/run_xrepotest_prepare_cpu.sh` é o job correspondente. Estes
scripts são executados pelo utilizador via SSH. A conversão da imagem e a
cópia do Python já passaram; a validação integral do ambiente no cluster
continua pendente.

## Métricas e comparabilidade

Mantemos compilação, execução, invocação, cobertura focal e mutação do avaliador.
Todos os 675 IDs têm de constar dos resultados, incluindo falhas. Uma tarefa
interrompida não é uma tarefa concluída sem testes. O export recusa conjuntos
incompletos. Para ausência de testes usamos `[]`: uma string vazia poderia
receber crédito indevido por compilar ou executar zero exemplos.

Há limites a declarar no paper:

- A implementação de cobertura foi corrigida: ordem de carregamento e seleção
  exata do ficheiro. Não modificámos a fórmula nem os intervalos focais, mas
  resultados anteriormente ausentes ou relativos a outro ficheiro podem mudar.
  A comparação direta com as tabelas publicadas tem esta limitação. Para uma
  comparação controlada, os testes das abordagens comparadas devem ser medidos
  pelo mesmo executor corrigido; isso não obriga a gerar novamente esses testes
  se as respostas originais estiverem disponíveis.

- A invocação oficial procura nomes com Tree-sitter; não confirma despacho nem
  execução e pode não reconhecer `Classe.new` como invocação de `initialize`.
- A cobertura oficial também pode ser obtida de testes que falham; não se deve
  confundir cobertura com correção da suite.
- A implementação agrega a mutação por soma de mortos/total. Guardamos o
  resultado oficial e os dados por tarefa, sem trocar silenciosamente a fórmula.
- MARTA usa várias chamadas e rondas. Comparar com uma resposta de outra LLM
  não é uma comparação com orçamento igual. Custos e configuração têm de constar
  dos resultados. Uma comparação com o pipeline oficial usando o mesmo modelo
  ajudará a separar capacidade do modelo e contribuição da ferramenta.

`--no-graph` desliga enriquecimento e propagação de intenção, mantendo o âmbito
de 5 132 métodos. `--reuse-analysis-from` só aceita a experiência normal com a
mesma configuração e só reaproveita os pedidos da primeira passagem. A cache
dos pedidos serve também para retomar a análise após o limite de tempo do job.

## Isolamento da experiência cancelada

Os resultados existentes em `results_ruby/qwen2.5-coder_32b` ficam intactos.
O adaptador não os lê, não reutiliza o seu `state.json` e não usa as suas gems.
Uma experiência XRepoTest exige `experiment.json` compatível, bloqueia diretórios
antigos sem manifesto, fixa fontes, configuração e código, e impede duas
gerações simultâneas no mesmo diretório. O armazenamento de sumários e vetores
também distingue âmbito e conteúdo. Não basta coincidir o nome de um método
para reutilizar testes da experiência anterior.

## Correções do ambiente e do executor, preservando tarefas e fontes Ruby

1. **Hanami (81 tarefas):** a fonte focal é Hanami 2.3.2, mas as oito componentes
   Hanami em cache são 3.0.0.rc1 e exigem Ruby >=3.3. `dry-operation` 1.1.0
   (`83f0a3af47614429e853caee587d659743f0f3f0`) também exige Ruby >=3.3. A imagem
   usa Ruby 3.2.11, não tem Gemfile.lock do projeto e não tem as restantes gems
   instaladas no bundle Hanami. As referências Git em cache são válidas;
   reparar HEAD ou copiar `.git` não resolve a incompatibilidade.
   Correção autorizada: Ruby 3.3.10 num prefixo separado, preservando os dez
   snapshots Git das dependências da imagem. As restantes gems, anteriormente
   ausentes, foram resolvidas e fixadas em `environment/locks/hanami.lock`.
   O código focal continua a ser Hanami 2.3.2. Não afirmamos que este seja o
   ambiente exato das experiências dos autores; documentamos a reconstrução.
2. **Mutação:** só Capybara, HTTParty e RSpec-core tinham o Mutant acessível pelo
   bundle. Nos outros sete projetos acrescentámos um `Gemfile.xrepotest` auxiliar
   que avalia o Gemfile original e inclui `mutant`/`mutant-rspec` 0.15.1, a versão
   já distribuída na imagem. Os locks originais são preservados e todas as
   versões anteriormente fixadas têm de permanecer iguais. O Shoryuken também
   precisava dos checksums de cinco gems preenchidos no lock auxiliar.
3. **Reporte de CI dos projetos:** `COVERAGE=false` no ROM desliga o envio Codacy
   incompatível com Ruby 3.2; `SIMPLECOV_DISABLED=1` no Shoryuken desliga o limiar
   global de 89% da suite humana. São opções já previstas pelos seus helpers.
   O avaliador continua a iniciar e medir a sua própria cobertura focal.
4. **Monorepos:** o feedback MARTA escolhe o diretório do Gemfile mais próximo do
   ficheiro focal, tal como o avaliador oficial. No ROM isto inclui os subprojetos
   `core/`, `repository/` e `changeset/`. O Gemfile auxiliar resolve o original
   por caminho absoluto, para funcionar também a partir desses subdiretórios.

O utilizador autorizou corrigir a instalação/configuração e, em 27-09, as duas
falhas do executor descritas abaixo, mantendo fontes Ruby, tarefas e definições
das métricas. **Não foi autorizada nem iniciada uma execução adicional
do pipeline XRepoTest como baseline.** A pergunta anterior que associava a
correção do ambiente a essa experiência foi retirada: são decisões separadas.

`environment/Dockerfile` constrói a imagem derivada. `runtime.py` aplica a mesma
configuração à geração, feedback e avaliação; valida o hash do lock e restaura
o ambiente ao mudar de projeto. O manifesto `/opt/xrepo/environment.json` entra
na identidade da experiência e impede retomar com outra configuração.

### Duas correções autorizadas do avaliador

O teste diagnóstico da tarefa 468 (`ROM::Relation::Loaded#one`) passa no RSpec
oficial. Contudo, `ruby/command_utils.py:generate_coverage_report` carrega
diretamente `lib/rom/relation/loaded.rb` antes do teste/spec helper. Esse ficheiro
pressupõe `dry/core`, carregado pela entrada normal `rom/core`, e falha com
`NameError: uninitialized constant Dry`. O avaliador devolve cobertura `null`.
Não é uma gem em falta: a execução RSpec do mesmo teste funciona.

O rastreio dos 60 ficheiros focais ROM encontrou 43 que falham ao carregar
diretamente, correspondentes a 75 das 97 tarefas. Pré-carregar apenas `dry/core`
reduz as falhas para 25 ficheiros (49 tarefas), pelo que não resolve o problema
geral. Estes números são de um diagnóstico de carregamento, não de uma execução
de geração ou avaliação das 97 tarefas.

Foi confirmada uma segunda falha: o avaliador aceita uma coincidência parcial
do nome do ficheiro antes de encontrar o caminho exato. Em três diagnósticos,
selecionou ficheiros de dependências em vez dos alvos ROM presentes no relatório:

| Tarefa | Ficheiro focal | Ficheiro escolhido indevidamente |
|---|---|---|
| 413 | `core/lib/rom/attribute.rb` | `dry/initializer/builders/attribute.rb` |
| 461 | `core/lib/rom/relation/name.rb` | `zeitwerk/real_mod_name.rb` |
| 492 | `repository/lib/rom/repository/class_interface.rb` | `dry/struct/class_interface.rb` |

O resultado oficial nesses diagnósticos foi 0/0 linhas; os ficheiros corretos
tinham respetivamente 7, 6 e 8 linhas executáveis no intervalo focal. Não são
resultados MARTA: usámos testes triviais apenas para inspecionar a medição.

A correção inicia a cobertura como antes, deixa o RSpec carregar e
executar o teste antes do `require` focal de recurso, e seleciona a cobertura
pelo caminho completo. Num teste fixo que invoca `Loaded#one`, o original passa
no RSpec mas não mede cobertura; só a mudança de ordem produz 3/4 linhas (75%).
Com essa mudança, os 60 ficheiros produzem relatórios, mas isso, por si só, não
certifica a escolha correta do ficheiro nem a qualidade dos testes.

**A correção altera o executor, não apenas a instalação.** Foi autorizada e
aplicada apenas na imagem derivada `repaired-v2`. Não devemos apresentar
resultados obtidos com este executor como reprodução literal das tabelas publicadas.
Não excluímos tarefas e não introduzimos preloads no ambiente ROM.

`environment/repair_evaluator.py` recusa qualquer versão de origem diferente
do SHA-256 `0b03a6073e13dfc7bade9fb86327aea22a1c756b720eb5540b8c372076da929d`.
Preserva o original em `/opt/xrepo/original/ruby/command_utils.py` e o diff em
`/opt/xrepo/evaluator-coverage.patch`. O manifesto do ambiente contém os hashes
antes/depois de todos os módulos `base/` e `ruby/`; a avaliação recusa alterações
posteriores não registadas. Nenhum ficheiro Ruby ou tarefa é escrito por esta
correção. Os resultados antigos não são reclassificados nem reutilizados.

As provas estão na cache de trabalho: `rom-original-image.json`,
`rom-focal-loads.json`, `rom-coverage-order.json`,
`rom-coverage-order-all-files.json`, `rom-coverage-file-matching.json` e
`coverage-evaluator.proposal.diff`. Os ensaios iniciais executaram uma cópia
da função em memória num container descartável. `repaired-diagnostics.json`
documenta a falha anterior. A validação da imagem nova usa relatórios separados:
`repaired-v2-diagnostics.json` e `preflight-repaired-v2.json`.

Na imagem original, sem passar pela MARTA, o ROM falha ainda antes por uma
dependência Git (`rom-sql`) não preparada no bundle selecionado. O Dockerfile
publicado permite terminar a construção mesmo quando a instalação de um projeto
falha. Isto comprova limitações da imagem fixada, não que os autores tenham usado
esta mesma configuração incompleta nas experiências do paper.

Antes de GPU: transferir/converter a imagem no cluster, validar o Python
reutilizado, consultar a quota atual e concluir/validar os scripts GPU/CPU da
execução. Não reutilizar os jobs do corpus antigo.

Verificações realizadas: 227 testes passaram e 1 foi ignorado na suite local.
A descoberta real da MARTA dentro da imagem selecionou exatamente 675 alvos e
5 132 métodos de contexto. Um spec diagnóstico fixo do Hashie passou no executor
MARTA e no avaliador oficial; a cobertura focal oficial foi 80%. Depois da
correção, um segundo diagnóstico Hashie produziu 146 mutações (60 mortas) no
avaliador oficial; este número é apenas uma prova de execução, não um resultado
da MARTA. O primeiro método Hashie continua sem sujeitos reconhecidos pelo
Mutant: não alterámos a implementação do avaliador para contornar isso.
Não foram feitas
chamadas a LLMs. Isto valida a integração exercitada, não a qualidade de geração
nem a viabilidade financeira da execução completa.

Na imagem final `repaired-v2`, em 27-09, passaram os dez diagnósticos RSpec e
os sete diagnósticos de cobertura, incluindo os casos de ficheiros homónimos
413/461/492 (denominadores corretos 7/6/8). Hashie (172), Hanami (596) e
Shoryuken (379) mantiveram as coberturas dos diagnósticos anteriores:
64,29%, 80% e 66,67%; ROM (468) passou a medir 75%. A mutação Hashie produziu
60/146, como antes. São diagnósticos fixos, não resultados gerados pela MARTA.
A conferência completa confirmou as 675 tarefas, os 302 ficheiros focais,
os 5 132 métodos de contexto e os dez bundles, todos sem erros. Esta validação
não significa que todos os métodos tenham sido testados nem que todos os
operadores de mutação do corpus tenham sido exercitados.
A heurística oficial de invocação não reconhece `==` na tarefa 379, embora haja
execução e cobertura. Mantemos esse resultado, sem ajustar testes para melhorar
a pontuação da heurística.

Cache de trabalho local, fora do repositório:
`/Users/mario/.cache/marta-xrepotest/`. Contém a imagem extraída, revisão do
avaliador, relatórios `preflight-*.json` e `evaluator-smoke.json`. A imagem
original continua no Docker. Apenas NumPy foi adicionado numa pasta isolada
de dependências para os diagnósticos Docker; o Python do computador não foi alterado.

A imagem validada foi exportada para
`/Users/mario/.cache/marta-xrepotest/marta-xrepotest-repaired-v2.tar`, com um
ficheiro `.tar.sha256` ao lado para validar a transferência. O arquivo contém
uma única imagem `linux/amd64`. O `setup_xrepotest.sh` espera estes ficheiros em
`mario/xrepotest/downloads/` no cluster. A imagem original e a derivada anterior
continuam disponíveis no Docker para comparação; nenhuma foi substituída.

## Modelos: candidatos, não uma nova decisão

Consulta a fontes oficiais em 26-09-2026:

| Modelo | Variante Ollama consultada | Consideração para A100 40 GB |
|---|---|---|
| Qwen3-Coder-30B-A3B | `qwen3-coder:30b`, Q4_K_M, 19 GB | Especializado em código, 3,3B parâmetros ativos, sem modo thinking; candidato simples para o protocolo atual |
| Qwen3.6-35B-A3B | `qwen3.6:35b`, cerca de 23 GB | Candidato mais recente; exige verificar suporte no Ollama do cluster e configurar/contabilizar thinking |
| Qwen2.5-Coder-32B | já presente no cluster | Ambiente e velocidade já observados; nenhuma das alternativas foi medida em geração de testes Ruby por nós |

Os tamanhos são pesos publicados, não memória total com KV cache. Caber na GPU
e ser rápido depende da janela, quantização e runtime. Os resultados publicados
dos candidatos noutros benchmarks não provam superioridade nesta tarefa. A
recomendação prática inicial é testar compatibilidade do Qwen3-Coder-30B; o
Qwen3.6-35B merece consideração se o objetivo for privilegiar capacidade recente.
Nenhum novo modelo foi descarregado ou escolhido automaticamente.

Fontes: [Ollama Qwen3-Coder](https://ollama.com/library/qwen3-coder:30b),
[model card Qwen3-Coder](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct),
[Ollama Qwen3.6](https://ollama.com/library/qwen3.6),
[model card Qwen3.6](https://huggingface.co/Qwen/Qwen3.6-35B-A3B).

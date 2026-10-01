# MARTA no XRepoTest Ruby

Estado em 29-09-2026: integração implementada e testada localmente; ambiente
derivado construído; os dez bundles e os dez diagnósticos RSpec passam offline.
As duas falhas confirmadas no avaliador de cobertura foram corrigidas na imagem
`marta-xrepotest:repaired-v2`, com autorização do utilizador (detalhes abaixo).
No Deucalion, o job CPU 1956251
converteu a imagem e confirmou os imports Python, mas o preflight encontrou
recusas de proprietário do Git em Hanami e RSpec-core. A adaptação em
`runtime.py` autoriza apenas os caminhos exatos do repositório e das suas
dependências Git, por variáveis de ambiente do processo (`safe.directory`).
Não escreve na configuração global da conta nem altera fontes, dependências
ou o avaliador. O erro foi reproduzido em Docker com UID 12345; com esta
adaptação, os bundles afetados, os dez diagnósticos RSpec, os sete casos de
cobertura e a mutação Hashie passam offline com esse UID sem privilégios.
A verificação foi repetida no job CPU **1956272**, que terminou `COMPLETED`,
`0:0`, em 2 min 40 s. Os dez projetos e todos estes diagnósticos passaram
também no Deucalion.

Atualização em 30-09-2026: foram retirados os três mapeamentos manuais de
dependências e os conselhos de configuração introduzidos nos prompts após
observar falhas. A política atual só infere entradas e ficheiros de namespace
existentes no próprio projeto. O resultado anterior de **302/302** pertence à
política retirada, com os mapeamentos, e não certifica a versão atual. A nova
validação e as suas limitações são descritas abaixo. Não submeter nova geração
GPU enquanto a certificação atual não passar.

O job GPU **1956495** iniciou a análise com Qwen3.6:35b e thinking ligado.
Parou após 7 h 56 min na fase `what_todo_raiz` de Capybara, antes de gerar
testes: a chamada para `Capybara::Driver::Base#go_back` atingiu 16 384 tokens
de saída sem texto final (`finish_reason=length`, HTTP 200). Não foi um timeout.
Ficaram guardadas **1 908 respostas válidas**: 1 196 chamadas da primeira
passagem, 686 da segunda e 26 na fase `what_todo_raiz`.

### Retoma após esgotamento de tokens nos sumários

Um sumário com `finish_reason=length` é rejeitado, mesmo que contenha texto
parcial. O executor repete o mesmo pedido até **três tentativas no total**,
mantendo modelo, thinking, temperatura, contexto e limite de saída. Se as três
forem cortadas, para e preserva os checkpoints. Erros de transporte e respostas
vazias sem `length` continuam a parar a execução; não são aceites como sumários.
A política aplica-se aos sumários, não acrescenta tentativas de geração de
testes e fica registada como `summary_truncation_attempts=3` no manifesto.

Cada pedido real, incluindo tentativas cortadas, é contado uma vez nos tokens,
tempos e eventos. `summary_truncated` é um diagnóstico associado ao evento
`llm`, não uma segunda chamada. O relatório também recupera os tokens das
falhas antigas que só tinham `detail`, sem inventar o tempo ou a fase ausentes.
No evento antigo deste job, isso recupera 356 tokens de entrada e 16 384 de saída.

A mudança de código é deliberadamente incompatível com uma retoma silenciosa.
O comando abaixo aceita apenas o fingerprint exato da versão `a7bfb697a`,
com análise iniciada mas nenhuma tarefa de geração registada. Guarda o manifesto
original e hashes dos checkpoints em `summary_retry_upgrade.json`; depois
atualiza apenas o fingerprint do código e a política de repetição. A configuração
de modelo, dados, ambiente e restantes parâmetros é preservada e volta a ser
verificada pela execução normal. Os sumários só são reutilizados para a mesma
fase e os mesmos prompts completos.

Executar no Deucalion, com o job parado, depois de atualizar o código:

```bash
python3 -B -m benchmark.xrepotest.upgrade_summary_retry \
  ../xrepotest/runs/qwen36_35b_thinking_v1/generation
```

O comando é idempotente e não apaga nem reescreve checkpoints ou logs. Esta
correção e o custo das tentativas adicionais devem ser declarados no protocolo
experimental. Não há fallback automático para thinking desligado.

### Retoma após resposta vazia na geração (job 1959036)

O job seguinte terminou com erro após 12 h 50 min 17 s, durante a tarefa 14
(`Capybara::Session#visit`). Ficaram dez tarefas `complete` e quatro `no_tests`
(8, 11, 12 e 13). `complete` significa que existe uma suite exportada, não que
tenha passado a avaliação final do XRepoTest. Os quatro resultados sem testes
permanecem no denominador e não são repetidos para tentar melhorar o resultado.

A última chamada registada pelo Ollama recebeu HTTP 200 e consumiu exatamente
16 384 tokens de saída. O cliente devolveu conteúdo vazio, que o adaptador
classificou genericamente como erro de transporte. Os logs são compatíveis com
thinking a esgotar o limite antes da resposta final, mas não preservaram o
conteúdo nem o `finish_reason` dessa resposta. `truncated=0` no log do servidor
não demonstra que o limite de saída não foi atingido.

`GenerationRequests` regista cada chamada antes de tratar o resultado, incluindo
o `finish_reason`, os tokens e os erros. Uma resposta vazia com `length` passa
ao fluxo normal: o Planner usa o seu plano de recurso já existente; no Dev,
consome uma das **três tentativas existentes** e fornece uma mensagem de erro
para a reparação seguinte. Na última tentativa, termina sem um novo teste
nessa ronda. Não acrescenta repetições escondidas, não aumenta os limites e
não desliga thinking. Texto parcial não vazio continua sujeito às verificações
de sintaxe e RSpec habituais. Erros de transporte e respostas vazias sem
`length` continuam a interromper a tarefa, agora com telemetria.

A geração interrompida reinicia por tarefa, não por pedido. Antes de reiniciar,
move os ficheiros da tarefa `running` para `interrupted_tasks/<id>/<tentativa>/`.
Assim, um spec escrito durante uma reparação não é tratado como uma ronda já
validada. As tarefas `complete` e `no_tests` são preservadas. `report.py` inclui
os eventos arquivados no consumo total, embora apenas `tasks/*/state.json`
conte para o estado atual. `generation.json` resume cada tentativa local;
os eventos e os ficheiros arquivados sustentam a contabilidade das retomas.

A migração `upgrade_generation_empty.py` aceita apenas o fingerprint da versão
`74c02124a`. Guarda o manifesto anterior, os estados e os SHA-256 dos ficheiros
de análise e geração em `generation_empty_upgrade.json`. Só altera o fingerprint
de código e acrescenta `generation_empty_length_policy=counts-as-attempt-v1`.
Inclui a simplificação de contexto completo já pedida: no XRepoTest, o âmbito,
as identidades e as caches continuam iguais ao anterior `full_context=True`.
As tarefas e parâmetros do benchmark não são alterados. A correção do executor
e o reinício da tarefa interrompida devem ser declarados na experiência.

Com o job parado e o código atualizado, executar **esta migração**, não voltar
a executar a migração antiga de sumários:

```bash
cd /projects/F202407648IACDCF2/mario/MARTA
export XREPO_RUN=qwen36_35b_thinking_v1
XROOT=/projects/F202407648IACDCF2/mario/xrepotest
GOMAXPROCS=2 singularity exec --cleanenv \
  --home "$XROOT/runs/$XREPO_RUN/home:/home/marta" \
  --bind "$PWD:/opt/marta:ro" --bind "$XROOT:/data/xrepo" \
  --env PYTHONPATH=/opt/marta --env GOMAXPROCS=2 \
  "$XROOT/repaired-v2.sif" \
  python3 -B -m benchmark.xrepotest.upgrade_generation_empty \
  "/data/xrepo/runs/$XREPO_RUN/generation"
```

Depois, submeter o job GPU com os mesmos parâmetros. O comando de migração é
idempotente, recusa outra versão e não altera os ficheiros cujos hashes guarda.
A chamada que causou esta interrupção não entrou nos eventos do cliente antigo:
os totais históricos de LLM têm essa lacuna. O relatório assinala-a; os logs
Ollama e os registos Slurm devem ser conservados, sem inventar telemetria.

### Nova geração após correção do contexto de carregamento

O job 1959846 foi parado após 45 tarefas finalizadas: 14 com suite exportada e
31 sem testes. As seis respostas vazias cortadas observadas desde a retoma não
explicam esse total. As falhas incluíam inicialização incompleta de Capybara,
constantes inexistentes, configuração inventada e chamadas a métodos privados.
Não atribuímos tudo ao modelo nem ao limite de tokens.

A instrução antiga dizia para começar apenas com o `require` do ficheiro focal.
Foi reproduzido offline que `require "capybara/session"` permite carregar o
ficheiro, mas construir uma sessão falha porque a entrada `capybara.rb` ainda
não inicializou a configuração. `require "capybara"` antes desse ficheiro
resolve essa inicialização. Não resolve, por exemplo, uma classe inventada pelo
modelo ou uma asserção errada. Os dois specs recolhidos foram diagnosticados,
não corrigidos para serem contabilizados como respostas da MARTA.

`marta/ruby_backend/loading.py` acrescenta contexto de produção ao Planner e
a todas as tentativas Dev. Procura a gemspec mais próxima do alvo, verifica os
ficheiros de entrada convencionais existentes e escolhe uma entrada compatível
com o namespace, ou a única candidata. Não executa a gemspec e não adivinha entre
entradas ambíguas. Inclui os ficheiros de namespace existentes, do exterior para
o interior, antes do ficheiro focal, evitando ciclos de autoload como o do
provider SQL do Hanami.

Na versão `98f6f254d`, esta informação vinha acompanhada de três mapeamentos
manuais para Rails, Selenium e Dry::System e de recomendações sobre configurações
e classes inventadas pelo modelo. Foram introduzidos após observar falhas neste
benchmark. Embora não fornecessem respostas ou asserções, eram conhecimento
manual sobre bibliotecas específicas e ajustes de prompt motivados pelos
resultados. Foram **retirados** a pedido do utilizador. Não foram transferidos
para preloads ocultos, para o executor nem para a imagem.

O contexto atual também identifica dependências através de uma regra geral,
implementada em `marta/ruby_backend/dependencies.py` e
`rb/marta_dependencies.rb`:

1. Consulta o bundle já instalado do projeto com Bundler. Usa as versões e os
   require paths selecionados pelo ambiente; não instala nem descarrega gems.
2. Lê com Prism as referências a constantes no ficheiro focal e nos ficheiros
   de namespace existentes. Segue referências qualificadas a ficheiros locais
   de produção, incluindo uma classe base definida noutro ficheiro.
3. Nas gems desse bundle, procura ficheiros de namespace existentes segundo
   as convenções `snake_case` e minúsculas compactas. Só aceita uma correspondência
   se Prism confirmar a declaração do namespace exato nesse ficheiro. Comentários,
   strings e reaberturas de classes em ficheiros não correspondentes não bastam.
4. Seleciona o namespace correspondente mais específico. Se houver vários
   fornecedores ou entradas possíveis, regista a ambiguidade e não escolhe um.
5. Sugere os requires das dependências identificadas antes da entrada da gem,
   dos namespaces locais e do ficheiro focal. Junta uma evidência concreta por
   dependência ao contexto do Planner e Dev: gem, versão, referência e ficheiros.

Não há tabela Rails/Selenium/Dry::System nem instruções sobre configurações ou
asserções. Os mesmos critérios aplicam-se a qualquer gem com essa estrutura.
Não lê testes humanos, fixtures ou respostas do benchmark. Os requires constam
do próprio spec gerado; o executor não modifica a resposta. O plano completo,
incluindo ambiguidades, fica nos eventos `production_loading`; o tempo da
inspeção fica em `production_dependencies`.
Esta informação de carregamento é a mesma nos braços com e sem grafo: não usa
arestas do grafo nem sumários LLM para escolher dependências.

É uma heurística de dependências baseada em metadados e declarações reais,
não uma resolução completa da semântica Ruby. Constantes construídas dinamicamente,
organizações de ficheiros não convencionais ou ambiguidades podem ficar sem
sugestão. Um require correto não garante objetos, configuração ou asserções corretos.
Sem Gemfile do próprio projeto, não procura gems no ambiente global do utilizador.

A comparação com `/Users/mario/Desktop/GECAD/MARTA-artifact` confirmou que a
versão Python prepara a raiz de importação (`marta/message_react.py:31–45`),
escreve o `conftest.py` com esse caminho (`:242–256`) e devolve ao Dev o erro e
o nome do módulo a importar (`:1153–1174`). `marta/testcase_react.py:563–590`
prepara `PYTHONPATH` e executa pytest. Não foi encontrado nesse fluxo um catálogo
manual de dependências ou um mecanismo equivalente a esta inferência Ruby.
Importar um módulo Python inicializa os pacotes que o contêm; carregar diretamente
um ficheiro Ruby interno pode deixar a entrada da biblioteca por inicializar.
A inferência agora introduzida é uma melhoria da MARTA Ruby, não uma funcionalidade
que a versão Python já tivesse e que simplesmente tivesse sido recuperada.

Tarefas, fontes, avaliador, rondas, tentativas, modelo, thinking e limites
permanecem iguais. Os sumários não recebem estas instruções de geração. A
política atual fica no manifesto como
`generation_loading_policy=gemspec-bundle-namespaces-v3`, de modo a recusar
a retoma silenciosa de uma geração feita com os mapeamentos manuais.

`environment/verify_loading.py` exercita as receitas nos 302 ficheiros usando
cópias descartáveis, Bundler, a configuração RSpec original e `spec/temp_spec.rb`.
Confirma o caminho exato em `$LOADED_FEATURES` e inclui a regressão de construção
de uma sessão Capybara. É um diagnóstico fixo, sem LLM, sem métricas de benchmark.
Não garante que os testes gerados sejam corretos. Foi ainda corrigida a deteção
de load paths para árvores `lib` só com ficheiros aninhados, como RSpec-core.

A política estrutural anterior, sem mapeamentos nem inferência de dependências,
carregou **294/302 ficheiros**. As oito falhas eram namespaces de dependências
não inicializados. Esse diagnóstico foi preservado em
`~/.cache/marta-xrepotest/generic-loading-diagnostics.json` (`ready=false`).

A política atual, com a inferência geral, passou **302/302 ficheiros**, nos dez
projetos, e a regressão de construção de sessão Capybara. O diagnóstico foi feito
na imagem `marta-xrepotest:repaired-v2`, sem rede, instalações ou chamadas ao modelo.
O relatório é `~/.cache/marta-xrepotest/bundle-loading-diagnostics.json`. Não foram
excluídas tarefas nem alterados fontes ou avaliador. A suite de regressão passou
**303 testes, com 1 ignorado**, incluindo namespaces ambíguos, declarações reais,
strings/comentários, ciclos locais e exclusão de testes humanos da inspeção.

O bloqueio de inferência continua ativo até repetir esta certificação no
Deucalion com o código atual. Passar o diagnóstico confirma o carregamento
nesse ambiente; não é um resultado de qualidade de testes da MARTA.

O job GPU exige agora `reports/loading-diagnostics.json` aprovado, com os hashes
de código de carregamento, fontes e ambiente correspondentes ao preflight,
antes de iniciar o modelo. Executar primeiro no Deucalion:

```bash
cd /projects/F202407648IACDCF2/mario/MARTA
git pull --ff-only
mkdir -p logs
sbatch --parsable deucalion/run_xrepotest_loading_cpu.sh
```

Depois de confirmar `COMPLETED`, `0:0` e `Loading ready: True; 302 focal files`,
preparar **uma nova experiência**. Não atualizar o manifesto da experiência
antiga nem juntar as suas respostas aos novos resultados:

```bash
cd /projects/F202407648IACDCF2/mario/MARTA
export XREPO_RUN=qwen36_35b_thinking_bundle_loading_v4
XROOT=/projects/F202407648IACDCF2/mario/xrepotest
mkdir -p "$XROOT/runs/$XREPO_RUN/home"
GOMAXPROCS=2 singularity exec --cleanenv \
  --home "$XROOT/runs/$XREPO_RUN/home:/home/marta" \
  --bind "$PWD:/opt/marta:ro" --bind "$XROOT:/data/xrepo" \
  --env PYTHONPATH=/opt/marta --env GOMAXPROCS=2 \
  "$XROOT/repaired-v2.sif" \
  python3 -B -m benchmark.xrepotest.fork_loading_run \
  /data/xrepo/runs/qwen36_35b_thinking_v1/generation \
  "/data/xrepo/runs/$XREPO_RUN/generation"

export MODEL=qwen3.6:35b XREPO_THINKING=on
export OLLAMA_CTX=32768 XREPO_MAX_TOKENS=16384
export XREPO_TEMPERATURE=0.6 XREPO_TOP_P=0.95 XREPO_PRESENCE_PENALTY=0
export XREPO_REQUEST_TIMEOUT=1800 XREPO_NO_GRAPH=0
sbatch --parsable --export=ALL deucalion/run_xrepotest_generate_gpu.sh
```

`fork_loading_run.py` aceita apenas a implementação predecessora `9c3696d12`,
com contexto de produção completo e grafo ligado, e exige ambas as execuções
paradas. Copia apenas checkpoints válidos, caches e vetores de análise. Guarda
hashes, manifestos e consumo herdado em `analysis_reuse.json`; preserva a origem
e recusa ficheiros estranhos no destino. Não copia testes, estados de tarefas,
totais de análise ou eventos antigos. Todas as tarefas de geração recomeçam.
A comparação local com o código predecessor confirmou prompts, identidades,
fingerprints e caches de sumários iguais nos dois braços do grafo, com zero
chamadas LLM ao reutilizar uma análise completa.

`report.py` apresenta o custo herdado em `inherited_analysis`, separado das
novas chamadas. Para custo total da abordagem, considerar ambos e declarar a
reutilização; para novo consumo GPU, consultar Slurm. As chamadas já gastas na
geração antiga continuam no seu diretório e pertencem ao custo de diagnóstico.
Cada tentativa de geração passa agora a guardar código e erro em eventos
`generation_validation`, incluindo sintaxe, RSpec e salvage, mesmo que o spec
seja depois descartado. São evidência de diagnóstico, não novas chamadas LLM.

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

`RubyProject` separa sempre `analysis_targets` de `targets`, também fora do
adaptador XRepoTest. Os filtros de ficheiros,
métodos e o limite de geração não reduzem o conjunto de sumários. O
primeiro conjunto inclui métodos de produção nas árvores `lib/`, incluindo
construtores; o segundo corresponde exatamente às tarefas por ficheiro, nome e
intervalo de linhas. Os 48 alvos `initialize` não são excluídos. Construtores
devem ser testados por construção normal de objetos, sem manipular os testes
para satisfazer a heurística de invocação do avaliador.

Os testes humanos, fixtures, exemplos, dependências instaladas e templates não
entram no conjunto de sumários. Podem continuar a fazer parte do ambiente de
execução oficial. Contexto completo significa este âmbito de análise estática:
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
Não há um limite de 50 classes para a produção de sumários.

Já não existe a opção `full_context`: a análise do código de produção fornecido
é o único comportamento. Os objetos `MethodTarget` são criados diretamente em
`analysis_targets`; a lista intermédia `candidates` foi removida. A geração usa
`targets`, selecionada por tarefas exatas ou por filtros de ficheiros e métodos.
As caches mantêm o nome `.full_context.json` para identificar o âmbito completo
e não aceitar as caches antigas restritas aos alvos.
A CLI normal também analisa todo o código de produção fornecido; `--limit` limita
os testes, não o custo inicial dos sumários. O log apresenta ambos os totais.

Esta simplificação não altera o âmbito da execução XRepoTest já
iniciada com `full_context=True`. Contudo, os ficheiros Python fazem parte da
assinatura de retoma: não atualizar o checkout dessa execução enquanto estiver
em curso, nem reutilizar o diretório com uma assinatura diferente sem uma
migração verificada.

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
cópia do Python e os diagnósticos do ambiente passaram no cluster.

## Execução no Deucalion

Decisão atual: **Qwen3.6:35b com thinking ligado**, instalado pelo utilizador
via Ollama 0.30.7. Geração e avaliação usam jobs distintos:

- `deucalion/run_xrepotest_generate_gpu.sh`: uma GPU, Ollama no container antigo
  e MARTA no ambiente Ruby XRepoTest validado. As duas aplicações comunicam por
  HTTP local. Embeddings em CPU. Não descarrega modelos automaticamente.
- `deucalion/run_xrepotest_evaluate_cpu.sh`: avaliador XRepoTest corrigido,
  incluindo mutação, após existir o export completo das 675 tarefas.
- `deucalion/xrepotest_job_common.sh`: montagens, isolamento e retoma dos jobs.
- `cluster.py`: exige os dois relatórios aprovados e regista o digest do modelo,
  metadados `/api/show` e versão do servidor, sem fazer inferência.
- `deucalion/run_xrepotest_loading_cpu.sh`: certifica os 302 ficheiros focais
  para a política de carregamento da nova geração, sem consumir GPU.

O template GPU pede **32 CPUs por GPU**, conforme o
[guia oficial do Deucalion](https://docs.macc.fccn.pt/jobs/gpu/). O pedido anterior
de oito CPUs foi corrigido em 1 de outubro de 2026. Não é especificado um valor
manual de `--mem`; a alocação efetiva do Slurm fica guardada em
`runs/<experiência>/metadata/slurm_<job>.txt`, antes de arrancar o Ollama.

O job `1960971` terminou como `OUT_OF_MEMORY`, após 32 h 06 min, com 191 tarefas
finalizadas (148 suites exportadas, 43 sem testes) e a tarefa 522 interrompida.
O log também regista uma resposta LLM vazia sem `finish_reason=length`. O Slurm
confirma falta de RAM no job, mas estes dados não identificam o processo morto
nem provam que a alocação de CPUs tenha causado a falha. Antes de retomar,
comparar `ReqMem`, `AllocTRES`, `MaxRSS` e o fim do log do Ollama. Não se aumentam
tokens, tentativas ou rondas em resposta ao OOM.

A correção de recursos e o registo Slurm não alteram o fingerprint de geração.
A retoma usa a mesma experiência: conserva tarefas `complete`/`no_tests` e
checkpoints compatíveis; arquiva a tentativa interrompida antes de a recomeçar.
O custo das tentativas arquivadas continua incluído nos relatórios.

Os scripts foram testados localmente com substitutos de Slurm/Singularity.
O job 1956495 confirmou a inferência no cluster e o carregamento das 42 camadas
do modelo na A100 de 40 GB; a geração completa e a avaliação continuam pendentes.
A validação anterior passou 234 testes, com 1 ignorado. Inclui o envio de thinking
através do cliente OpenAI 1.42.0 real com HTTP simulado, falha sem resubmissão,
cancelamento sem resubmissão e continuação por sinal de walltime. Os argumentos
da geração foram também validados offline na imagem, sobre as 675 tarefas,
com `--validate-only`. Não foram instalados pacotes nem chamadas LLM para isto.

Configuração inicial: três rondas, três tentativas, contexto de 32 768 tokens,
limite de saída de 16 384 tokens (raciocínio e resposta), timeout de 1 800 s por
pedido, temperatura 0,6, top-p 0,95 e presence penalty 0. Estes três parâmetros
de amostragem seguem a recomendação Qwen para código em modo thinking.
O limite de saída é uma escolha operacional nossa, inferior aos 32 768 tokens
recomendados genericamente pelo fabricante. A primeira execução encontrou uma
chamada cortada após 1 908 respostas válidas. Se um sumário atingir o limite,
repete-se até três tentativas no total, sem propagar respostas incompletas;
a execução para se o corte persistir, conforme a política documentada acima.
As escolhas são guardadas no manifesto e não podem mudar durante uma retoma.
O modo thinking é enviado via `reasoning_effort=high`; `none` desliga-o.
Só o conteúdo final entra nos sumários e testes; os tokens de saída reportados
pelo servidor são contabilizados, incluindo raciocínio, sem inferir uma divisão
que o servidor não forneça.

Referências: [parâmetros Qwen](https://huggingface.co/Qwen/Qwen3.6-35B-A3B#best-practices),
[controlo de thinking no Ollama](https://docs.ollama.com/api/openai-compatibility).

Após a certificação de carregamento e a cópia auditada da análise descritas
acima, submeter a geração a partir do repositório no cluster:

```bash
git pull --ff-only
mkdir -p logs
export MODEL=qwen3.6:35b XREPO_THINKING=on
export XREPO_RUN=qwen36_35b_thinking_bundle_loading_v4
export OLLAMA_CTX=32768 XREPO_MAX_TOKENS=16384
export XREPO_TEMPERATURE=0.6 XREPO_TOP_P=0.95 XREPO_PRESENCE_PENALTY=0
export XREPO_REQUEST_TIMEOUT=1800 XREPO_NO_GRAPH=0
sbatch --parsable --export=ALL deucalion/run_xrepotest_generate_gpu.sh
```

Tudo fica em `mario/xrepotest/runs/$XREPO_RUN/`, com `generation/`,
`evaluation/`, `work/`, `metadata/` e `logs/`. Nada é lido dos resultados
cancelados em `results_ruby/`. O nome de experiência e o modelo são obrigatórios.
O sinal antecipado de walltime (`USR1`) agenda uma continuação dependente da
saída do job atual. Cancelamento (`TERM`) ou erro não agenda automaticamente
outro job. A retoma preserva tarefas concluídas e chamadas de análise em cache;
uma tarefa interrompida pode repetir parte da geração. Não editar o código
durante a experiência: a retoma recusa outro hash de implementação.

Só quando existir `generation/processed.jsonl` completo, submeter a avaliação:

```bash
export XREPO_RUN=qwen36_35b_thinking_bundle_loading_v4
sbatch --parsable --export=ALL deucalion/run_xrepotest_evaluate_cpu.sh
```

A avaliação retoma os resultados já gravados por tarefa. Não ligar o job CPU
ao ID inicial da geração com `afterok`: se houver continuação por walltime,
esse ID não corresponde ao final da geração. O script CPU recusa export ausente.

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

Imagem, Python e ambiente já validados no cluster. Os scripts GPU/CPU são os
descritos acima; a execução do novo modelo ainda não foi medida. Não reutilizar
os jobs do corpus antigo.

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

## Pesquisa de modelos e decisão posterior

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
Posteriormente, o utilizador escolheu e descarregou `qwen3.6:35b` no
Deucalion, Q4_K_M, através de Ollama 0.30.7, e escolheu thinking ligado.
A tabela acima documenta a pesquisa anterior; a configuração de execução
atual está na secção Deucalion.

Fontes: [Ollama Qwen3-Coder](https://ollama.com/library/qwen3-coder:30b),
[model card Qwen3-Coder](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct),
[Ollama Qwen3.6](https://ollama.com/library/qwen3.6),
[model card Qwen3.6](https://huggingface.co/Qwen/Qwen3.6-35B-A3B).

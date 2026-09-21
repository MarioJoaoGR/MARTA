# Construção do dataset MARTA-Ruby

Sete camadas, uma por ficheiro, na ordem em que correm. Cada uma lê o artefacto
da anterior e escreve o seu em `apresentacao/demo_dataset/<n>_<nome>/`.

A unidade é o **módulo** (ficheiro Ruby), como no CodaMosa e no CoverUp.

## Duas contribuições no mesmo processo

As três primeiras camadas produzem um **dataset Ruby geral**: projetos públicos
relevantes, apenas o código entregue pela gem, representação estrutural extraída
com o Prism e oito características por módulo. Este artefacto pode ser reutilizado
sem a MARTA e não pressupõe que o módulo seja adequado para geração de testes.

As camadas 4 a 7 refinam esse dataset para construir o **corpus experimental da
MARTA-Ruby**. A elegibilidade, a desduplicação, a certificação do ambiente e a
seleção de grupos respondem às necessidades desta avaliação. A camada 6 mantém-se
depois da 5 porque certifica apenas os candidatos que ainda podem entrar no
benchmark, no ambiente concreto da ferramenta. Certificar também toda a população
da camada 3 seria um artefacto adicional de compatibilidade, não uma condição para
o dataset descritivo existir.

```bash
source scripts/ruby_env.sh          # obrigatório: as camadas 2 e 6 usam Ruby

python -m benchmark.dataset.camada1_universo
python -m benchmark.dataset.camada2_parser              # ~5 min, clona 133 gems
python -m benchmark.dataset.camada3_caracteristicas     # segundos
python -m benchmark.dataset.camada4_elegibilidade       # segundos
python -m benchmark.dataset.camada5_desduplicacao       # ~1 min
python -m benchmark.dataset.camada6_carregamento        # ~1 h 20, instala e certifica
python -m benchmark.dataset.camada7_selecao             # ~6 min
```

As camadas 2 e 6 aceitam `--continuar` e retomam de onde ficaram: nenhuma cabe
no limite de tempo de uma sessão, e a clonagem falha por bloqueio temporário do
GitHub com frequência.

## O funil

| camada | o que decide | resultado |
|---|---|---|
| 1 universo | awesome-ruby ∩ RubyGems, ≥100M descargas | 133 gems, 59 categorias |
| 2 parser | clona a etiqueta da versão; lê com o Prism só o código do projeto | 9 786 módulos, 95 075 métodos |
| 3 características | mede as oito, não exclui nada | 8 776 com métodos |
| 4 elegibilidade | ≥3 formas distintas **e** formas/métodos ≥0,4 | 6 202 |
| 5 desduplicação | semelhança >0,50 descarta | 5 543 |
| 6 carregamento | instala o declarado; carrega num processo limpo **e** pelo RSpec da ferramenta | 5 093 |
| 7 seleção | ranking de diversidade + grupos com chamadas garantidas | 250 (80 gems, 3 800 métodos-alvo) |

A decisão experimental é **250 módulos, fatia alvo de 50% em grupos e
Qwen2.5-Coder 32B**. Os custos medidos no piloto e a comparação das alternativas
ficam em `apresentacao/construcao_dataset.docx`, secção *Decisão*.

## As constantes, e porquê

Cada número foi escolhido a ver a curva do que tira e do que deixa. Os
varrimentos ficam gravados ao lado dos artefactos.

| constante | valor | onde | justificação |
|---|---|---|---|
| descargas mínimas | 100M | camada 1 | filtro objetivo de relevância |
| chão de formas | 3 | camada 4 | tira 28% dos ficheiros mas só 5% dos métodos |
| proporção mínima | 0,4 | camada 4 | acima disso caem os módulos mais ricos |
| limiar de semelhança | 0,50 | camada 5 | planalto entre 0,3 e 0,9; empate entra |
| tamanho de grupo | 3 a 20 | camada 7 | com 2 há uma aresta só; acima de 20 é um subsistema inteiro |
| orçamento | 250 | camada 7 | compromisso entre diversidade, ablação completa e orçamento do modelo 32B |
| fatia de grupos | 50% | camada 7 | conserva mais diversidade do que 75% e ainda cria contexto intermodular suficiente |

## Reprodução verificada (2026-09-16)

Feita na versão anterior da construção (com os dois filtros no início da camada 7). A 17–18 de setembro as camadas 2 a 7 voltaram a correr de raiz com a estrutura
atual; a comparação camada a camada desta versão ainda não foi repetida.

Cada camada foi corrida outra vez numa pasta à parte (`MARTA_DATASET_DIR`), com as
entradas originais, e comparada com o artefacto guardado. **Nunca se verifica
dentro do repositório**: uma verificação assim já escreveu ficheiros por cima e
eles entraram num commit.

| camada | resultado |
|---|---|
| 2 parser | `analise_completa` igual no conteúdo (96 440 métodos); `onde_vive` e `erros` iguais. `parse.csv`, `modulos.jsonl` e `funil.json` diferem só em campos de diagnóstico da versão antiga do script (a coluna `clonou`, o campo `formas`), que nenhum programa lê |
| 3, 4, 5 | iguais |
| 6 carregamento | igual: os mesmos 5 217 módulos, `gems.csv` igual nas colunas de ambiente, porta, pastas e contagens — com as dependências instaladas na versão de hoje |
| 7 seleção | igual (`corpus.csv`, `grupos.csv`) |

A verificação da camada 2 apanhou um defeito da camada 1 reescrita: nos monorepos
guardava a subpasta com o ramo (`tree/master/master/activesupport`), e a camada 2
lia o repositório inteiro. Corrigido. O corpus não foi afetado, porque foi
construído a partir da camada 2 original, anterior ao erro.

**O universo está congelado a 23 de agosto.** A camada 1 consulta o RubyGems ao
vivo, por isso correr noutro dia dá outra fotografia: a 16 de setembro, com o
código corrigido, deu as mesmas 133 gems, os mesmos repositórios e as mesmas
categorias, mas **22 das 133 versões já eram outras** (rubocop 1.91.0,
sentry-ruby 7.0.0, ...). A reprodução começa no `1_universo/` guardado, não numa
nova corrida da camada 1.

O `1_universo/` guardado era uma regeneração de 25 de agosto, com o ramo repetido
e versões posteriores às que a camada 2 usou. Foi reposto o de 23 de agosto, a
partir dos valores que a camada 2 registou ao clonar (`parse.csv`: repositório,
categoria, descargas, versão). A licença vem de 25 de agosto (nenhuma camada a
lê). Nas `candidatas.csv`, as 133 que qualificam têm os valores de 23; as outras
726 ficam com os de 25, que são os únicos guardados, e só mostram que ficam abaixo
do limiar — o que é verdade nos dois dias (as mesmas 133 qualificam a 23 e a 25).

Verificado: zero incoerências entre `universo`, `candidatas` e `parse.csv`; a
camada 2 corrida sobre este universo reproduz o `analise_completa` linha a linha
(a ordem das linhas no ficheiro varia entre corridas; o conteúdo não).

## O que sai para o cluster

A camada 7 escreve, além do corpus, o **manifesto de execução**:

```
apresentacao/demo_dataset/7_selecao/projetos.json
```

Não decide nada de novo: junta, por gem, o que as camadas anteriores já
decidiram.

| campo | de onde vem | para quê |
|---|---|---|
| `repo`, `etiqueta`, `commit`, `raiz` | camada 2 | clonar exatamente o código analisado |
| `ambiente`, `deps` | camada 6 | repetir o degrau de instalação que abriu a porta |
| `load_paths`, `entrada` | camada 6 | correr os specs no ambiente em que o módulo foi certificado |
| `ficheiros_codigo` | camada 2 | o grafo da ferramenta vê o que a camada 7 viu |
| `alvos` (`modo`, `origem`, `vizinhos_no_corpus`) | camadas 6 e 7 | os alvos, e as etiquetas para repartir os resultados |

Três programas leem daqui, e só daqui: `benchmark/prepare_ruby_projects.py`
(clona e instala), `benchmark/verifica_ambiente.py` (confirma que cada módulo
carrega **pela ferramenta**, sem chamar o modelo) e
`benchmark/run_ruby_benchmark.py` (o harness).

**Porque é que isto é uma peça do dataset e não do harness:** a camada 6 não
certificou os módulos em abstrato, certificou-os num ambiente concreto, com todas
as pastas de carregamento da gem e com a porta de entrada já carregada. Uma
ferramenta que corra os specs de outra maneira vê módulos certificados a falhar,
e o erro conta contra a ferramenta sem ser culpa dela. Por isso o ambiente viaja
com os alvos.

## O que NÃO é critério

Não há exclusões por nome, por categoria, nem por o projeto ser uma aplicação,
uma ferramenta ou um framework. O benchmark do CodaMosa, que seguimos, tem
quase metade de aplicações (`ansible`, `black`, `httpie`, `youtube-dl`, e o
`thonny`, que é um IDE). A restrição a bibliotecas não é defensável.

Também não se exclui por não haver `lib/`: das 133, as duas que não a têm são
monorepos (`rspec`, `fastlane`), e o código está lá.

O que se exclui é o que não é código do projeto (exemplos, benchmarks, tarefas de
build), e isso decide-se pela pasta onde o ficheiro vive, não pelo nome nem pelo
tipo de projeto: ver *Só código do projeto*, abaixo.

## Cinco bugs de assunção encontrados ao construir

Nenhum dava erro. Todos produziam um número plausível, e é por isso que
sobreviveram à primeira construção.

1. **O nome da gem adivinhado do nome do repo** deixava fora a `activesupport`
   (1,4 mil milhões de descargas), a `activerecord`, a `cocoapods`, a `mongo` e
   a `selenium-webdriver`.
2. **Deduplicar por repositório** fazia desaparecer entradas de monorepo: a
   ActiveSupport e a ActiveRecord vivem ambas em `rails/rails`. E a `rails`
   nunca esteve na lista — entrou por lermos o nome do repo.
3. **O filtro da suite só via a pasta de topo**, e nos monorepos ela está em
   `fastlane/spec/`: 1182 ficheiros de teste entraram como código.
4. **Clonar o ramo por omissão** deixava fora o `active_model_serializers`, cujo
   `master` não tem `lib/`. Passou a clonar-se a etiqueta da versão publicada.
5. **Confiar na lista da comunidade** para saber onde vive o código: a `tilt` e a
   `kaminari` foram analisadas na casa antiga. Nem a lista nem o RubyGems servem
   sozinhos (no `warden` é o RubyGems que está desatualizado); o juiz é quem tem
   a etiqueta da versão publicada.

Regra que saiu disto: **preferir a declaração à suposição, e quando há duas
declarações que discordam, arranjar um teste objetivo em vez de escolher em quem
confiar.**

## Só código do projeto (camada 2)

A camada 2 tira a suíte humana (`spec/`, `test/`) e tudo o que está fora das
**pastas de código da gem**, as mesmas que a ferramenta põe no *load path*
(`lib/`, `src/`, `app/` e, nos monorepos, `<componente>/lib`), o equivalente Ruby
ao `src`. Saem assim os scripts auxiliares que vivem no repositório: benchmarks
(`mongo/profile/`), exemplos (`puma/examples/`), tarefas de rake (`pg/rakelib/`,
`byebug/tasks/`), o gerador do site (`thin/site/`) e a configuração de extensões
em C (`eventmachine/ext/extconf.rb`). **980 ficheiros.**

Estava no início da camada 7; passou para a camada 2 porque o que não é código do
projeto não deve contar em nenhuma camada (antes já tinha passado pela
elegibilidade e pela desduplicação). Não é uma exclusão por tipo de projeto:
aplicações e *frameworks* continuam.

## Duas fases na camada 6

Um módulo só fica certificado se carregar num processo Ruby limpo **e** pelo
executor de testes da ferramenta: um spec que só faz `require`, corrido pela
mesma função que a MARTA usa, no mesmo clone e com as mesmas gems, e com o
ficheiro a aparecer na cobertura. O RSpec traz os seus argumentos, já está
carregado e corre dentro da pasta do projeto; na população, **51 módulos**
passam na primeira fase e falham na segunda:

| causa | módulos |
|---|---|
| redefinem classes do próprio RSpec | 46 (rspec) |
| a extensão em C não é encontrada pelo caminho do RSpec | 2 (mysql2) |
| `bundler/setup` lê o Gemfile e termina o processo | 2 (spring) |
| arranca o Minitest e recusa o `-O` do RSpec | 1 (minitest) |

Não falham sozinhos: carregados junto com os outros alvos da gem, **apagam a
cobertura deles**. Saem para `6_carregamento/falham_rspec.csv`. A camada
confirma antes de clonar que o RSpec responde; sem isso barraria a população
inteira por um erro de ambiente.

O `ambiente` gravado no `gems.csv` é o degrau **em vigor** quando os módulos
foram carregados, mesmo que a porta nunca abra (a doorkeeper carrega com o
Gemfile do projeto); é esse que o `prepare_ruby_projects` reproduz no cluster.

## Uma limitação medida, e o que a camada 7 faz com ela

A MARTA constrói contexto **entre** módulos (a 2ª passagem dos sumários anexa o
`done_what` dos métodos chamados; o `what_todo` propaga-se do chamador para o
chamado), mas isso só funciona quando o chamado também é alvo.

Uma seleção puramente por diversidade escolhe os módulos mais afastados, ou seja
os que menos se chamam. Medido num corpus assim, de 500 módulos:

```
49,9%  das arestas ficavam dentro do mesmo módulo
 5,1%  chegavam a outro módulo do corpus     <- o único caso que enriquece
45,0%  apontavam para fora do corpus         <- perdidas
```

E não é simétrico: uma ferramenta de busca gera por módulo e não perde nada com
módulos dispersos. A escolha da unidade, herdada por comparabilidade, prejudica
especificamente a nossa.

A camada 7 corrige isso sem partir o corpus em dois, o que tornaria a
comparação confundida. Constrói **um** corpus em dois passos:

1. **Os X melhores**: o ranking de diversidade da população inteira. A ordem do
   *farthest-first* é o ranking, e "melhor" quer dizer "que mais acrescenta à
   cobertura das oito características" (a adequação já vem das camadas 4 a 6).
2. **Grupos ligados no lugar dos piores**: componentes de 3 a 20 módulos com
   **chamadas garantidas** entre si, pela sua ordem de diversidade. Cada grupo
   entra inteiro e acrescenta só os membros que ainda não estão no corpus; sai o
   mesmo número de módulos do fim do ranking. Pára quando os módulos de grupos
   chegam à fatia pedida.

**Chamada garantida** quer dizer: recetor certo (sem recetor, `self`, constante,
`self.class`), nome resolvido sem adivinhar, e o chamado é um método-alvo. O
resolver da ferramenta adivinha quando o nome é ambíguo (fica com a primeira
classe com o mesmo nome curto) e aceita *duck typing* com até 5 candidatos; essas
arestas dizem que **pode** chamar, e não contam.

Com 250 módulos e fatia alvo de 50%, sobre os 5 093 módulos da população: entram
19 grupos inteiros com 139 módulos, dos quais 11 já estavam entre os 250 melhores;
saem 128 módulos do fim do ranking. A fatia real é 55,6%, porque um grupo nunca é
partido para acertar exatamente nos 125. No total, 146 módulos têm uma chamada
estática de alta confiança com outro módulo do corpus, incluindo 7 que já vinham
do ranking. O corpus tem 80 gems, 55 categorias, 4 039 métodos analisados e
3 800 métodos-alvo da ferramenta.

O ranking é sensível à população: cada escolha do *farthest-first* depende das
anteriores, por isso mudar a população muda uma parte grande de cada variante.
O corpus só se fixa depois de a população estar fechada.

As alternativas continuam reproduzíveis sem mexer no código:

```bash
MARTA_DATASET_DIR=/outra/pasta MARTA_ORCAMENTO=250 MARTA_FATIA_GRUPOS=0.75 \
    python -m benchmark.dataset.camada7_selecao
```

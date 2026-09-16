# Construção do dataset MARTA-Ruby

Sete camadas, uma por ficheiro, na ordem em que correm. Cada uma lê o artefacto
da anterior e escreve o seu em `apresentacao/demo_dataset/<n>_<nome>/`.

A unidade é o **módulo** (ficheiro Ruby), como no CodaMosa e no CoverUp.

```bash
source scripts/ruby_env.sh          # obrigatório: as camadas 2 e 6 usam Ruby

python -m benchmark.dataset.camada1_universo
python -m benchmark.dataset.camada2_parser              # ~35 min, clona 133 gems
python -m benchmark.dataset.camada3_caracteristicas     # segundos
python -m benchmark.dataset.camada4_elegibilidade       # segundos
python -m benchmark.dataset.camada5_desduplicacao       # ~1 min
python -m benchmark.dataset.camada6_carregamento        # ~1 h, instala
python -m benchmark.dataset.camada7_selecao             # ~2 min
```

As camadas 2 e 6 aceitam `--continuar` e retomam de onde ficaram: nenhuma cabe
no limite de tempo de uma sessão, e a clonagem falha por bloqueio temporário do
GitHub com frequência.

## O funil

| camada | o que decide | resultado |
|---|---|---|
| 1 universo | awesome-ruby ∩ RubyGems, ≥100M descargas | 133 gems, 59 categorias |
| 2 parser | clona a etiqueta da versão, lê com o Prism | 10 765 módulos, 96 440 métodos |
| 3 características | mede as oito, não exclui nada | 9 074 com métodos |
| 4 elegibilidade | ≥3 formas distintas **e** formas/métodos ≥0,4 | 6 343 |
| 5 desduplicação | semelhança >0,50 descarta | 5 672 |
| 6 carregamento | instala o declarado e tenta carregar | 5 217 |
| 7 seleção | grupos ligados + diversidade | 500 |

## As constantes, e porquê

Cada número foi escolhido a ver a curva do que tira e do que deixa. Os
varrimentos ficam gravados ao lado dos artefactos.

| constante | valor | onde | justificação |
|---|---|---|---|
| descargas mínimas | 100M | camada 1 | filtro objetivo de relevância |
| chão de formas | 3 | camada 4 | tira 30% dos ficheiros mas só 5% dos métodos |
| proporção mínima | 0,4 | camada 4 | acima disso caem os módulos mais ricos |
| limiar de semelhança | 0,50 | camada 5 | planalto entre 0,3 e 0,9; empate entra |
| tamanho de grupo | 3 a 20 | camada 7 | com 2 há uma aresta só |
| orçamento | 500 | camada 7 | decisão do utilizador, perto dos 486 do CodaMosa |
| fatia de grupos | 50% | camada 7 | decisão do utilizador |

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

Consequência assumida: cinco dos 500 alvos não são código de biblioteca
(`kramdown/setup.rb`, `pg/rakelib/task_extension.rb`, `pg/sample/…`,
`httparty/examples/…`, `concurrent-ruby/docs-source/…`). Passaram as camadas 3 a
6 como qualquer outro módulo e carregam; ficam, porque excluí-los seria um
critério por nome, que é precisamente o que esta secção recusa.

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

A camada 7 corrige isso sem partir o corpus em dois — o que tornaria a
comparação confundida. Faz **um** corpus com duas origens e etiqueta cada
módulo (`origem`, `componente`, `vizinhos_no_corpus`), para a diferença poder ser
medida no fim dentro do mesmo conjunto. Resultado, com os mesmos 500 módulos:

```
52,9%  mesmo módulo
12,2%  outro módulo do corpus      (era 5,1%)
34,9%  fora                        (era 45,0%)
```

Dos 500, **410 têm pelo menos um vizinho no corpus e 90 não têm**. É essa divisão
que o `cobertura_por_metodo.json` do harness permite comparar no fim.

# Mapa de verificação

Para cada afirmação sobre a ferramenta, o ficheiro e a linha onde está o código
que a sustenta. Não é para decorar: é para abrires e confirmares, e para poderes
abrir ao vivo se te perguntarem.

Números de linha verificados em 2026-08-24. Se o código mudar, confirma com
`grep -n` antes de apresentar.

---

## 0. As perguntas que já te fizeram

**"Onde se constrói esse índice?"**

Não há índice nem ficheiro. O que eu tenho chamado índice é uma **lista de
objetos em memória**, `self.targets`, de uma classe chamada `MethodTarget`.

- a classe: `marta/ruby_backend/project.py:66`
- onde a lista é construída: `marta/ruby_backend/project.py:211`, método `discover()`
- onde os campos dos sumários são preenchidos: `project.py:304`, `analyze_summaries()`

A resposta honesta é: *"não é um ficheiro, é uma estrutura em memória; o código
está no `discover()` do `project.py`, e posso mostrar."*

**"O `indice.json` é o índice?"**

Não. É uma **apresentação escrita à mão** para a demo. Os dados vieram da
ferramenta, mas o ficheiro não existe quando a ferramenta corre, e as chaves
(`indice_de_classes`, `ordem_de_procura`, `alvos`) são nomes escolhidos por nós,
não do código. Por isso não tem os `siblings`: foram mostrados 6 dos 9 campos.

**"Isto é gerado ou fizeste para a demo?"**, artefacto a artefacto:

| Pasta da demo | Gerado pela ferramenta? |
|---|---|
| `1_codigo/` | escrito à mão (é o exemplo de entrada) |
| `2_prism/` | sim, saída do `marta_parse.rb` |
| `3_grafo/` | sim, saída do `build_call_graph` |
| `4_tipos_e_alvos/indice.json` | **não**, apresentação escrita à mão |
| `5_sumarios/sumarios.json` | sim, é o ficheiro de cache (tem `source_hash` e `model`) |
| `6_contexto_planner/` | sim, o prompt real |
| `7_specs/` | sim, segue a convenção de nomes da ferramenta |
| `8_resultados/metricas.json` | sim, saída do recorder |

---

## 1. Fase de análise: de onde vêm os alvos

| Afirmação | Onde |
|---|---|
| Varre `**/*.rb` e salta a suite de testes | `backend.py:98` (`discover_files`) |
| A pasta da suite é `spec/` | `backend.py:89` |
| Salta pastas de moldes ERB | `backend.py:96` (`NON_RUBY_DIRS`) |
| Constrói um alvo por método | `project.py:211` (`discover`) |
| Ficheiros fora da seleção são lidos mas não geram alvos | `project.py:231` |
| O construtor não é alvo | `project.py:26` (`SKIP_METHODS`) |
| Os campos de um alvo | `project.py:66` (`MethodTarget`) |
| Os tipos inferidos calculam-se no fim | `project.py:252` |

**Ponto sensível:** a linha 231 é a que liga o dataset à ferramenta. O
`target_files` é a lista de módulos escolhidos, e vem de fora (`start_react.py:69`).

## 2. Inferência de tipos

| Afirmação | Onde |
|---|---|
| O índice de tipos do projeto | `param_types.py:24` |
| A ordem de procura de um método (mixins antes da superclasse) | `param_types.py:49` (`ancestors`) |
| Que métodos uma classe responde | `param_types.py:72` (`responds_to`) |
| Duck typing: que classes respondem a esta interface | `param_types.py:78` (`candidates`) |
| Os tipos dos parâmetros que vão no prompt | `param_types.py:87` (`judge_for_method`) |

## 3. Grafo de chamadas

| Afirmação | Onde |
|---|---|
| O grafo estático | `call_graph.py:97` (`StaticCallGraph`) |
| As formas de recetor e como cada uma resolve | `call_graph.py:146` (`resolve`) |
| Procura na cadeia de ancestrais | `call_graph.py:120` (`_instance_lookup`) |
| Duck typing só para `lvar`, `ivar` e `getter` | `call_graph.py:133` (`_duck_targets`) |
| O travão dos 5 candidatos | `call_graph.py:131` (`MAX_CANDIDATES`) |
| A cache do grafo invalida quando o resolver muda | `call_graph.py:26` (`RESOLVER_VERSION`) |

**Se te perguntarem se é sempre duck typing:** não. Abre o `resolve` na linha 146
e mostra: `none`, `self`, `const` e `selfclass` resolvem-se por declaração ou por
âmbito. Só `lvar`, `ivar` e `getter` adivinham.

## 4. Sumários

| Afirmação | Onde |
|---|---|
| A fase toda | `project.py:304` (`analyze_summaries`) |
| Passagem 1: só o código | `project.py:335-337` |
| Passagem 2: junta os sumários dos chamados | `project.py:342` |
| O prompt sem chamadas | `summaries.py:24` |
| O prompt com chamadas | `summaries.py:35` |
| A função que faz as duas | `summaries.py:48` (`analyze_done_what`) |
| O requisito propagado do chamador | `summaries.py:99` |
| A fusão final das duas perspetivas | `summaries.py:130` (`generate_summary`) |

**Onde o grafo entra:** só na passagem 2, e não como grafo. Ele decide **quem**
são os chamados; o que vai no prompt é texto. Ver `project.py:345-349`.

## 5. RAG

| Afirmação | Onde |
|---|---|
| A base é criada no arranque | `project.py:453` |
| Só os sumários são vetorizados | `rag.py:53` (`init`), a linha `text = t.summary or t.done_what` |
| A busca é por cosseno | `rag.py:24` (`_cosine_topk`) |
| Top-3, excluindo o próprio | `rag.py:69` (`query`) |
| O resultado vira linhas de texto | `rag.py:88` (`related_lines`) |
| Quem chama a busca antes do prompt | `project.py:485` (`_related_for`) |
| Segunda utilização: procurar pelo texto do erro | `project.py:504` (`_error_help_fn`) |

**Não é tool calling.** A LLM nunca decide procurar. Mostra a `_related_for`: a
busca acontece em Python e o resultado é passado como argumento.

**Não é ChromaDB.** É uma matriz de NumPy em memória; os vetores vêm de um modelo
do HuggingFace (`marta/embedding.py:160`).

## 6. O contexto que vai para o Planner

| Afirmação | Onde |
|---|---|
| Stub da classe + construtor + método | `project.py:108` (`context_source`) |
| O stub é reconstruído do parser, não lido do ficheiro | `project.py:93` (`class_code`) |
| O código é lido por corte de linhas | `project.py:29` (`_slice_lines`) |
| A montagem final do bloco | `prompts.py:88` (`build_context_block`) |

**Porque é que as três partes levam marcadores:** está explicado no comentário em
`project.py:122-128`. Sem eles, o sumarizador da `formatador` resumiu a classe
inteira em vez do método, e o spec gerado não testava o método certo.

## 7. Fase de geração

| Afirmação | Onde |
|---|---|
| O ciclo por método | `project.py:273` (`generate_all`) |
| O fluxo de um método | `generate.py:63` (`generate_spec_for_method`) |
| Onde tudo se junta num só texto | `generate.py:98` |
| Planner: instrução e pedido | `prompts.py:30` e `prompts.py:33` |
| Agente de asserções: instrução e regras | `prompts.py:60` e `prompts.py:63` |
| Portão de sintaxe antes de correr | `generate.py:135`, implementado em `runner.py:50` |
| Execução do RSpec | `runner.py:126` (`run_rspec`) |
| Salvamento dos exemplos que passam | `generate.py:161`, implementado em `salvage.py:40` |
| Ciclo exterior de cobertura | `project.py:549` (`generate_rounds`) |

## 8. Os auxiliares em Ruby

Três ficheiros, e é tudo o que corre em Ruby:

- `rb/marta_parse.rb` — o parser (usa o Prism)
- `rb/marta_coverage.rb` — recolhe linhas e ramos
- `rb/marta_tracegraph.rb` — grafo dinâmico, só para avaliar o estático

---

## 9. O dataset

Os artefactos estão em `apresentacao/demo_dataset/`, uma pasta por camada, com
os ficheiros que sustentam cada número.

| Camada | Ficheiros |
|---|---|
| 1 universo | `1_universo/funil.json`, `universo.csv`, `candidatas.csv` |
| 2 parser | `2_parser/funil.json`, `parse.csv`, `erros.csv`, `analise_completa.jsonl.gz` |
| 3 características | `3_caracteristicas/modulos.csv`, `distribuicoes.json` |
| 4 elegibilidade | `4_elegibilidade/elegiveis.csv`, `excluidos.csv`, `varrimento_*.csv` |
| 5 desduplicação | `5_desduplicacao/representantes.csv`, `duplicados.csv`, `varrimento.csv` |
| 6 carregamento | `6_carregamento/carregam.csv`, `falham.csv`, `gems.csv` |
| 7 seleção | `7_selecao/corpus.csv`, `comparacao.csv`, `varrimento.csv` |

**AVISO.** O código que produziu estes ficheiros **não está no repo**. Os sete
passos foram corridos a partir de uma pasta temporária. O que está em
`benchmark/` é o pipeline anterior, das 12 gems, que estes artefactos substituem.

Enquanto isso não for resolvido, a resposta a *"onde está o código do dataset"*
é que não está, e os artefactos não são reproduzíveis.

---

## 10. A narrativa, do parser à geração

### Quem manda

Ninguém "manda" de dentro. O maestro é o `start_react.py`, linhas 78 a 98, e são
quatro chamadas em sequência:

```python
proj = RubyProject(..., target_files=target_files).discover()   # 1. estático

async def _pipeline():
    await proj.analyze_summaries(...)       # 2. sumários (chama o modelo)
    if not args.no_rag:
        proj.build_rag()                    # 3. as duas matrizes
    return await proj.generate_rounds(...)  # 4. geração
```

O `discover` faz a primeira e termina. Não chama as outras.

### O `discover`, bloco a bloco (`project.py:211-272`)

**Bloco 1, linhas 213-218: limpar e preparar.**
Zera `files`, `targets` e cria um `ProjectTypeIndex` novo. Chamar duas vezes
refaz, não acumula. O `all_methods` acumula os métodos de TODOS os ficheiros,
incluindo os que não vão gerar alvos, porque o grafo precisa do projeto inteiro
e assim aproveita-se este parse em vez de o repetir.

**Bloco 2, linhas 219-228: ler cada ficheiro.**
Por ficheiro: guarda o caminho, corre o parser, alimenta o índice de tipos,
acumula os métodos, regista onde vive cada classe, e calcula o `require_target`
(`lib/carteira.rb` -> `"carteira"`).

**Bloco 3, linhas 230-232: o filtro do corpus.**
```python
if self.target_files is not None and rel not in self.target_files:
    continue
```
É a linha que liga o dataset à ferramenta. Repara no que já aconteceu ANTES
deste `continue`: o parser correu e o índice foi alimentado. O ficheiro fora da
seleção continua a ser lido, só não produz alvos. É obrigatório: se o método
alvo chamar uma classe que vive num ficheiro não escolhido, essa classe tem de
estar no índice.

**Bloco 4, linhas 233-250: criar os alvos.**
Dois ciclos sobre os mesmos métodos. O primeiro agrupa por classe (para saber
quem são os irmãos de cada método); o segundo cria um `MethodTarget` por método,
saltando os construtores (`SKIP_METHODS = {"initialize"}`).

**Bloco 5, linhas 251-253: o judge.**
Fora do ciclo dos ficheiros, e o comentário diz porquê: precisa do índice
completo, porque a classe candidata pode estar noutro ficheiro.

**Bloco 6, linhas 254-271: o grafo.**
Tenta a cache primeiro. A chave é o hash do código MAIS o `RESOLVER_VERSION`,
para invalidar quando o resolver muda e não só quando o código do projeto muda.
Efeito lateral útil: `code_changed = cached_cg is None`, ou seja, um acerto na
cache do grafo significa que o código não mudou.

### O que o `discover` deixa pronto

```
proj.files          caminhos dos .rb
proj.targets         um MethodTarget por método, com código, irmãos e judge
proj.type_index      quem responde a quê
proj.call_graph      quem chama quem
proj.class_files     onde vive cada classe
```

E **nenhuma chamada ao modelo aconteceu**. Tudo isto é análise estática.

### O que vem no `MethodTarget`, e de onde

| Campo | Origem |
|---|---|
| `method` | `MethodInfo`, do parser |
| `owner_class` | `ClassInfo`, do mesmo `FileParse` |
| `file_path` | o ciclo dos ficheiros |
| `require_target` | calculado: `module_ref(rel)` |
| `siblings` | agrupamento feito no ciclo |
| `judge` | linha 252 (estrutural) + linha 458 (semântico) |
| `done_what`, `what_todo`, `summary` | `analyze_summaries`, fase seguinte |

### A ordem completa, com o que precisa do modelo

```
ESTÁTICO
 :219  lê cada ficheiro com o parser
 :223  alimenta o ProjectTypeIndex
 :240  cria um MethodTarget por método
 :252  calcula o judge estrutural
 :254  constrói o grafo (ou lê da cache)

MODELO — analyze_summaries (:304)
 :323  se a cache bater certo, SALTA A FASE TODA
 :335  passagem 1: done_what de todos, só do código
 :342  passagem 2: done_what outra vez, com os done_what dos chamados  [usa callees]
 :365  what_todo das raízes, a partir do README
 :372  propaga o what_todo pelas arestas até estabilizar               [usa callers]
 :389  funde done_what + what_todo -> summary
 :418  sumários das classes
 :431  grava tudo na cache

MATRIZES — build_rag (:448)
 :454  matriz dos métodos (só os summary são vetorizados)
 :457  matriz das classes
 :458  judge semântico: desempata parâmetros ambíguos

GERAÇÃO — generate_rounds (:549)
 :599  por método e por ronda: busca 3 vizinhos e monta o prompt
```

**Duas fronteiras que convém saber de cor:** nada antes da linha 254 chama o
modelo; e o grafo só é usado em dois sítios, ambos na sumarização (anexar os
`done_what` dos chamados, propagar o `what_todo` dos chamadores). Na geração já
não entra.

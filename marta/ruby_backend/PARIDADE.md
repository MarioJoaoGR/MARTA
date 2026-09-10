# MARTA Python → Ruby: o que difere, e porquê

*A replicação está feita: o pipeline, os dois agentes, os dois ciclos, o
salvamento, a cache e o RAG existem nas duas versões. Este ficheiro guarda só o
que **continua diferente**, para não se confundir uma adaptação obrigatória com
uma lacuna, e para que qualquer comparação entre as duas versões saiba o que
está a comparar.*

Última revisão: 2026-09-10.

---

## 1. Diferenças obrigatórias da linguagem

Não são lacunas. São consequências de Ruby não ser Python, e têm de constar em
qualquer comparação entre as duas versões.

| Tema | Python | Ruby |
|---|---|---|
| **Referência ao módulo** | `a/b.py` → `a.b` (pontos) | `require "a/b"` (caminho) + `-I` no load path; o RSpec já junta `lib/` e `spec/` |
| **Docstrings** | existem, e a MARTA injeta-as no código | Ruby não tem. Os sumários ficam **internos**, só para RAG e contexto |
| **Parâmetros** | `args`, `kwonlyargs`, `vararg`, `kwarg` | sete formas: `req`, `opt`, `*`, `k:`, `k: v`, `**`, `&` |
| **Tipos declarados** | anotações opcionais na assinatura | não existem na linguagem. O RBS vive em ficheiros à parte e, das 16 gems que clonámos, só uma os traz |
| **Procura de métodos** | herança + MRO | `prepend` → própria classe → `include` → superclasse |
| **Grafo de chamadas** | PyCG, ferramenta publicada | escrito de raiz: não existe equivalente para Ruby |
| **Salvamento** | testes são `def`, removidos por nome | `it` são blocos, removidos por intervalo de linhas e indexados por `[1:2]` na saída do RSpec |
| **Cobertura** | `coverage.py`, biblioteca externa | módulo `Coverage`, embutido no interpretador; as linhas em falta **por método** têm de ser sintetizadas |

## 2. Divergências deliberadas de implementação

Não são consequência da linguagem: foram escolhas, e ficam aqui para ninguém as
confundir com lacunas nem lhes dar mais importância do que têm.

### O RAG: mesmo ChromaDB da Python, mas persistente e por cosseno

O armazenamento é o mesmo dos dois lados. Difere em duas coisas, ambas
deliberadas, e as duas na direção de corrigir o lado Python.

| | Python (`embedding.FunctionDatabase`) | Ruby (`rag.RubyFunctionDatabase`) |
|---|---|---|
| Modelo de *embeddings* | `bge-large-en-v1.5` | **o mesmo**, reutilizado tal e qual (`marta.embedding.embedder`) |
| Onde ficam os vetores | coleção ChromaDB | **a mesma coisa** |
| Cliente | `chromadb.Client(...)`, **efémero** (`embedding.py:165`) | `PersistentClient` em `.marta_ruby_cache/vectors` |
| Entre execuções | reembebe tudo, sempre | reaproveita se a chave bater |
| Métrica | `hnsw:space` por omissão, ou seja **L2** | **cosseno** (`hnsw:space: "cosine"`) |
| Nome da coleção | fixo, `'functions_database'` | `functions` e `classes`, separados |

**Porquê persistente.** É o custo real: o índice é reconstruído a cada execução,
e mesmo com a cache de análise cheia (os sumários vêm do disco) os *embeddings*
eram recalculados. No Deucalion isso corre com `EMBED_DEVICE=cpu`, para o Ollama
ficar com a GPU sozinho. A coleção é validada por uma chave de três partes,
`hash das fontes | modelo LLM | modelo de embeddings` (`cache.vectors_key`):
mudar qualquer uma invalida o que está em disco, e o conjunto de ids tem de bater
certo, para um `--limit` diferente não reaproveitar meia coleção.

**Porquê cosseno.** O `HuggingFaceEmbedder` faz *mean pooling* e **não
normaliza** (`embedding.py:43`). Em vetores não normalizados, o L2 e o cosseno
**não ordenam da mesma maneira**: a norma do vetor entra na distância, e um
sumário longo fica penalizado por ser longo. A própria MARTA Python usa cosseno
no outro caminho de recuperação, o `find_topK_message` (`embedding.py:95`), que
já tinha saído do ChromaDB por causa do *overhead* de criar e apagar uma coleção
por chamada. Ou seja: os dois caminhos de recuperação da Python discordam entre
si, e este alinha-os pelo cosseno.

**Porquê nomes de coleção separados.** O `build_rag` cria **duas** bases no mesmo
processo, a dos métodos e a das classes. Com o nome fixo da Python, a segunda
colidia com a primeira (`create_collection` rebenta se já existir). Sem
`persist_dir` o nome leva um sufixo aleatório, para duas instâncias em memória
não se pisarem.

**O que não é argumento.** A busca do ChromaDB é aproximada (HNSW) e a de uma
matriz seria exata, mas isto **não é uma diferença que importe aqui**: o índice é
por projeto, o maior do corpus tem 565 métodos-alvo e a média é 69, e o HNSW só
diverge do exato a partir de escalas ordens de grandeza acima. Não usar isso como
vantagem, em nenhum dos sentidos.

O *embedder* continua injetável, por isso a lógica de recuperação continua
testável sem carregar o torch (`tests/test_rag.py`, incluindo o reaproveitamento
do disco e as três maneiras de o invalidar).

## 3. O que a versão Ruby ainda não tem

| Em falta | Impacto |
|---|---|
| Ponderar as arestas do grafo pela certeza da resolução | Uma chamada sobre uma constante é certa, sobre um parâmetro é palpite, e hoje as duas arestas valem o mesmo |
| Emitir os ramos na medição para lá da síntese por método | Já são recolhidos e usados; falta expô-los no relatório final |
| Medir precisão do grafo, e não só *recall* | Exige ligar os eventos `:c_call` no instrumento dinâmico e auditar uma amostra |

## 4. Divergência encontrada a 2026-08-18, e a lição

O `get_source_code` do Python delimita as três partes do contexto (stub da
classe, construtor, método-alvo) com blocos `"""…"""`. O porte inicial colou-as
com um `join`, sem marca nenhuma.

Custou caro, e foi rastreado de ponta a ponta na `formatador`: o stub daquela
classe são 60 linhas de constantes e metaprogramação antes de 7 linhas do
método. O sumarizador, a quem se diz *"eis o código de UM método"*, resumiu a
**classe inteira**. Esse sumário foi para o Planner, que planeou testes para
outros métodos, e o agente de asserções escreveu-os: o spec gerado para
`Formatador#parse` não testa o `parse`.

Corrigido em `e1060ecf`.

**A lição, e a razão de este ficheiro continuar a existir:** uma divergência de
paridade não se manifesta como erro. Manifesta-se como qualidade pior, sem
sintoma, e sem um registo do que devia ser igual não há como a apanhar.

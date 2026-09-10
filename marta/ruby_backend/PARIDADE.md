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

### O RAG: mesmo armazenamento da Python, mas persistido

Há **dois** índices, e na Python cada um usa um armazenamento diferente. A versão
Ruby mantém essa divisão tal e qual:

| | Python | Ruby | O que responde |
|---|---|---|---|
| Sumários de **métodos** | `FunctionDatabase` → ChromaDB | `RubyFunctionDatabase` → ChromaDB | *"que métodos se parecem com este?"* → os `RELATED` do Planner |
| Sumários de **classes** | `find_topK_message` → cosseno em NumPy | `RubyClassIndex` → cosseno em NumPy | *"que classe é este parâmetro?"* → o `_augment_judge_semantic` |

O modelo de *embeddings* é literalmente o mesmo objeto dos dois lados,
`marta.embedding.embedder` (`bge-large-en-v1.5`).

**A divergência é uma só: a persistência.** Na Python nenhum dos dois índices
sobrevive à execução. O cliente é `chromadb.Client(...)` (`embedding.py:165`), o
efémero, não o `PersistentClient`. Resultado: mesmo com a cache de análise cheia,
em que os sumários vêm todos do disco, eram todos embebidos outra vez. Aqui os
dois índices ficam em `.marta_ruby_cache/vectors`, ao lado da cache dos sumários:

```
.marta_ruby_cache/vectors/
    chroma.sqlite3      colecção 'functions'  (métodos)
    classes.npz         matriz + ids + chave  (classes)
```

Validados por uma chave de três partes, `hash das fontes | modelo LLM | modelo de
embeddings` (`cache.vectors_key`), mais o conjunto exato de ids, para um `--limit`
diferente não reaproveitar meio índice. É aí que está o custo real: no Deucalion
o *embedding* corre em CPU (`EMBED_DEVICE=cpu`), para o Ollama ficar com a GPU.

**Duas afinações menores, dentro da coleção dos métodos:**

*Cosseno em vez do L2.* O `HuggingFaceEmbedder` faz *mean pooling* e **não
normaliza** (`embedding.py:43`), e em vetores não normalizados o L2 (a omissão do
ChromaDB) não ordena como o cosseno: a norma entra na distância, e um sumário
longo fica penalizado por ser longo. O cosseno é o que o `find_topK_message` já
usa do outro lado, por isso isto alinha os dois caminhos, que na Python
discordam entre si.

*Nome da coleção.* A Python fixa `'functions_database'`. Sem `persist_dir` o nome
leva aqui um sufixo aleatório, para duas instâncias em memória não colidirem
(`create_collection` rebenta se a coleção já existir).

**O que não é argumento.** A busca do ChromaDB é aproximada (HNSW) e a de uma
matriz é exata, mas isso **não importa a esta escala**: o índice é por projeto, o
maior do corpus tem 565 métodos-alvo e a média é 69, e o HNSW só diverge do exato
ordens de grandeza acima. Não usar como vantagem, em nenhum dos sentidos. A
escolha do armazenamento aqui é paridade com a Python, mais nada.

O *embedder* continua injetável, por isso a recuperação continua testável sem
carregar o torch (`tests/test_rag.py`, incluindo o reaproveitamento do disco e as
maneiras de o invalidar, para os dois índices).

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

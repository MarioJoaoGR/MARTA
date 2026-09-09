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

### O armazenamento dos vetores do RAG: ChromaDB → matriz NumPy

| | Python | Ruby |
|---|---|---|
| Modelo de *embeddings* | `bge-large-en-v1.5` | **o mesmo**, reutilizado tal e qual (`marta.embedding.embedder`) |
| Onde ficam os vetores | `FunctionDatabase` → coleção ChromaDB | matriz NumPy em memória (`rag.RubyFunctionDatabase._matrix`) |
| Como se pesquisa | `collection.query` (HNSW, aproximado) | cosseno sobre todas as linhas (exato) |
| Persistência entre execuções | **nenhuma nos dois casos** | idem |

Decidido quando o `rag.py` foi escrito (`a324e42af`), pela razão que está no seu
cabeçalho: com a matriz em memória, o *embedder* é injetável e a lógica de busca
é testável **sem carregar o torch** (ver `tests/test_rag.py`).

Três factos que impedem a leitura errada disto, nos dois sentidos:

1. **A MARTA Python já tinha feito a mesma troca** no caminho quente. O
   `find_topK_message` (`marta/embedding.py:95`) faz cosseno em NumPy, e o
   *docstring* diz porquê: criar e apagar uma coleção ChromaDB por chamada era
   *"overhead enorme"*. O ChromaDB sobrevive só no `FunctionDatabase`.
2. **O cliente ChromaDB da Python é efémero.** `chromadb.Client(...)`
   (`embedding.py:165`) é o cliente em memória, não o `PersistentClient`. Ou
   seja, o ChromaDB não está ali a dar persistência, nem escala, nem velocidade.
3. **A escala não justifica um índice aproximado.** O índice é por projeto: o
   maior do corpus tem 565 métodos-alvo, a média é 69. O HNSW compensa a partir
   de centenas de milhares de vetores.

**Cuidado com o argumento inverso:** a nossa busca ser exata e a do HNSW
aproximada é verdade, mas não é vantagem a esta escala, onde o aproximado
devolveria o mesmo. O que **falta mesmo** é persistir a matriz, e isso não é o
ChromaDB que resolve (`MELHORIAS_PENDENTES.md` §B2).

Neste repositório o `FunctionDatabase` já não tem chamador nenhum: o código
Python saiu no `9d02d37ac` e o único consumo de `marta/embedding.py` é o
`embedder` importado pelo `rag.py`.

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

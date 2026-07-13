# MARTA Python → Ruby — Mapa de Paridade (documento vivo)

> Objetivo: **replicação total** da MARTA Python na versão Ruby, respeitando só as
> diferenças obrigatórias da linguagem. Este ficheiro rastreia o que já está
> replicado, o que está simplificado e o que ainda falta. Atualizado à medida que
> avançamos na branch `ruby-backend`.
>
> Legenda: ✅ replicado · 🟡 parcial/simplificado · ❌ em falta

_Última atualização: 2026-07-13 — itens 1–3 feitos (salvamento, cobertura+loop, summaries)._

---

## Sequência `ProjectMessage.init()` (Python) vs Ruby

| # | Etapa Python | Ficheiro Python | Ruby | Estado |
|---|---|---|---|---|
| 1 | Descobrir ficheiros | `_get_files` | `RubyProject.discover` (glob `*.rb`) | ✅ |
| 2 | Cache do grafo (`source_hash`) | `utils.save/load_cg_cache` | — | ❌ |
| 3 | **Call graph (PyCG)** → `cg_output` | `pycg/` | — | ❌ **(o "grafo" que perguntaste)** |
| 4 | Parse params + members | `analyze_function_members` (ast.walk Attribute) | Param **kinds** via Prism (req/opt/rest/key…); members ❌ | 🟡 |
| 5 | Completar imports | `complete_file_imports` | `require_target` + `-I` (load path) | 🟡 |
| 6 | **MRO / herança** | `parseExtend` | Parser dá superclass + include/extend/prepend; MRO não computada | 🟡 |
| 7 | Membros completos da classe | `parse_full_members` | — | ❌ |
| 8 | Construir arestas `uses/used` | `parseCG` | — (depende de #3) | ❌ |
| 9 | README por diretório | `DictionaryMessage.init` | — | ❌ |
| 10 | Cache de análise LLM | `load/save_analysis_cache` | — | ❌ |
| 11 | **`done_what`** (segue call graph) | `analyze_done_what` | `summaries.analyze_done_what` (source-only; hook p/ CG) | 🟡 |
| 12 | **`what_todo`** (do README) | `get_total_what_todo` | — (chega com #9 README) | ❌ |
| 13 | **`summary`** (merge das duas) | `generate_summary` | `summaries.generate_summary` (merge; sem what_todo = done_what) | ✅ |
| 14 | Summaries de classes | `analyze_each_class` | — | ❌ |
| 15 | **RAG / embeddings** (funções+classes) | `embedding.py`, `function_database` | Módulo agnóstico existe; não populado p/ Ruby | ❌ |
| 16 | **Tipos de params** (judge via RAG) | `analyze_param_types`, `ArgMessage` | — | ❌ |
| 17 | Setup de cobertura | `MyCoverage` | `coverage_runner` (Coverage embutido) | ✅ |

## Loop de geração (`generate_once` / `generate_react_flow`)

| Etapa Python | Ruby | Estado |
|---|---|---|
| Feedback de cobertura (missing lines) | `generate_rounds` + `measure_coverage` (feedback ao Planner) | ✅ |
| RAG: funções relacionadas → Planner | — | ❌ |
| **Planner** (plano JSON de cenários) | `prompts.plan_*` + `parse_plan` | ✅ |
| **Dev** (1 ficheiro, todos os cenários) | `prompts.dev_*` | ✅ |
| **Self-healing** (erro → reescrita ×3) | `generate.py` (syntax gate → rspec) | ✅ |
| RAG dirigido ao erro (self-heal) | — | ❌ |
| **Salvamento** (Opção D, testes que passam) | `salvage.py` (remove `it` falhados por linha) | ✅ |

## Infra de linguagem (o que já trocámos)

| Papel | Python | Ruby | Estado |
|---|---|---|---|
| Parsing | `ast` | Prism → JSON (`marta_parse.rb`) | ✅ |
| Syntax check | `ast.parse` | `ruby -c` | ✅ |
| Test runner | `pytest --json-report` | `rspec -f json` | ✅ |
| Cobertura | `coverage.py` (missing_lines/função) | `Coverage` embutido (`:lines`) + síntese | ✅ |
| Salvamento (cirurgia) | `ast` (linhas por `def`) | Prism (linhas por bloco `it`) | ✅ |
| Recorder (tokens/tempo/score) | integrado | só tokens (via `gptapi` global) | 🟡 |
| Caching | `cg_cache` + `analysis_cache` | — | ❌ |

---

## Diferenças **obrigatórias** da linguagem (não são lacunas — são adaptações)

- **Nomes de módulo:** Python `a/b.py`→`a.b` (dotted); Ruby `require "a/b"` (caminho) + `-I` no load path. RSpec auto-adiciona `lib/` e `spec/`.
- **Docstrings:** Ruby não tem. Summaries são **internas para RAG**, não injetadas no código (decisão §4.7). Eventual YARD só como comentário.
- **Modelo de params:** Python `args/kwonlyargs/vararg/kwarg`; Ruby `req/opt/rest(*)/keyreq(k:)/key(k: v)/keyrest(**)/block(&)`. Já capturado pelo Prism.
- **MRO/mixins:** Python herança+MRO; Ruby `include/prepend/extend` + `ancestors`. Membros do RAG de tipos mudam.
- **Call graph:** estático é mais difícil em Ruby (metaprogramação, `method_missing`). Sem drop-in do PyCG — opções: walker sobre Prism, ou TracePoint dinâmico. (ver `MARTA_Ruby_Migracao.docx` §3.1)
- **Salvamento:** `it` são blocos (CallNode), não `def` — remoção por intervalo de linhas via Prism, indexados por `[1:2]` no output RSpec (não por nome como os nodeids do pytest).

---

## Roadmap para replicação total (ordem proposta)

1. ~~**Salvamento por bloco `it`** (Opção D)~~ ✅ feito.
2. ~~**Fase 2 — cobertura** `:lines` × line-ranges → `missing_lines`/método → loop multi-ronda~~ ✅ feito.
3. ~~**Pipeline de summaries** `done_what`/`summary`~~ ✅ feito (source-only; `what_todo` fica p/ #7 README).
4. **RAG / embeddings** — popular `function_database` com dados Ruby (reusa `embedding.py`). ← próximo
5. **Tipos de params + members + MRO** (`ArgMessage`/`judge`/`ancestors`).
6. **Call graph** (walker sobre Prism ou TracePoint) → completa `done_what` + mixins.
7. **README / DictionaryMessage**.
8. **Caching + recorder** completos.
9. **Formalizar `LanguageBackend`** — extrair a interface partilhada Python/Ruby.

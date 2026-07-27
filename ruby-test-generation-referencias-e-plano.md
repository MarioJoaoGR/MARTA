# MARTA-Ruby — Project Brief, Referências e Plano
*Atualizado a 18 de julho de 2026 (revisto no Claude Code: estado do código corrigido + referências fact-checked via web — nenhuma alucinação encontrada nas críticas). Este ficheiro é a fonte de verdade do projeto: lê-o integralmente antes de qualquer tarefa.*

---

## 0. Contexto do projeto (ler primeiro)

**O que existe:** MARTA, uma ferramenta de geração automática de testes unitários para **Python**, já construída e avaliada (paper em finalização). Arquitetura em 2 fases:
- **Phase 1 (contexto, cached):** análise estática do projeto inteiro — call graph global (PyCG) + AST (`ast`) → sumários LLM de funções/classes → embeddings em ChromaDB → inferência de tipos de parâmetros por uso (que métodos são invocados em cada parâmetro) + retrieval semântico. Output: "Rich Type Context" por função.
- **Phase 2 (geração multi-agente):** Planner Agent (persona QA Lead, desenha cenários em JSON, sem código) → Assertion Agent (persona Developer, emite UM ficheiro de teste completo por função, Pytest) → validação `ast.parse` + execução Pytest → inner ReAct loop de reparação com o trace de erro (budget N=3) → salvage por cirurgia de AST (mantém só testes que passam, nunca apaga asserts) → outer loop coverage-driven: linhas não executadas (coverage.py) são atribuídas à função dona e enviadas SÓ ao Planner para novos cenários.
- **Métricas de avaliação:** pass rate, statement/branch coverage (coverage.py), mutation score (mutmut).

**⚠️ ESTADO REAL (atualização Claude Code, 18 jul 2026): o port está FEITO.** O MARTA-Ruby existe, está funcional e validado — vive em `marta/ruby_backend/` na branch `main` do repo Test4Py (merge 100% aditivo; o MARTA Python fica intacto e as duas versões correm lado a lado sem interferência). Paridade completa com o Python (ver `MARTA_Ruby_PARIDADE.md`): parser Prism→JSON, call graph estático próprio + variante dinâmica TracePoint (com comparador), summaries com propagação via grafo + README, RAG (funções + classes, bge), inferência de tipos por uso (members × MRO + hint semântico), loop multi-ronda guiado por cobertura (síntese de missing_lines por método via módulo `Coverage`), self-heal com RAG dirigido ao erro, salvage por blocos `it` (+ limpeza de `describe`/`context` vazios), caching (análise + grafo, por source hash), recorder próprio (tempo/erros/tokens), CLI simétrica ao Python: `python -m marta.ruby_backend.start_react --project_path X --source_path src --num 3`. 87 testes unitários verdes; validado live com deepseek-coder-v2:16b (ollama) em fixtures — 100% de cobertura nos alvos. **Finalizado "em teoria": ainda não foi corrido num projeto Ruby real — esperam-se percalços aí.**

**O objetivo agora:** avaliar o MARTA-Ruby contra o que existe (cover-agent + baseline single-prompt; ver §5) num conjunto curado de projetos Ruby. **Decisão de âmbito (utilizador): NÃO replicar a infra de benchmark completa do Test4Py para Ruby** — corpus leve e curado, não um mega-benchmark; o claim de pioneirismo (§6) mantém-se.

**Fase atual:** (1º) testar a ferramenta num projeto Ruby real e corrigir percalços; (2º) sondagens práticas restantes (§1, já parcialmente resolvidas); (3º) mini-corpus + comparação.

**Equivalências Python → Ruby a usar:**
| Python | Ruby (estado no MARTA-Ruby) |
|---|---|
| Pytest | RSpec ✅ (`rspec -f json`, feito) |
| coverage.py | módulo `Coverage` embutido na ferramenta (síntese missing_lines/método, feito) · SimpleCov para medir suites humanas no harness do corpus |
| mutmut | mutant (gem) — licença verificada: grátis p/ open-source (`--usage opensource`, repo público) |
| `ast` builtin | Prism ✅ (helper `marta_parse.rb`, feito) |
| PyCG (call graph) | ✅ RESOLVIDO: walker estático próprio sobre Prism (`call_graph.py`) + dinâmico TracePoint (`dyn_call_graph.py`) + `compare()`. Falta só MEDIR precisão em gems reais (resto da Sondagem 1) |
| pip/venv | bundler/Gemfile · rbenv Ruby 3.4 |

---

## 1. FASE ATUAL — Sondagens de de-risking (por ordem de prioridade)

Cada sondagem tem critérios de conclusão explícitos. Documentar resultados em `sondagens/RESULTADOS.md` (criar), com comandos usados, versões, e veredicto.

### Sondagem 1 — call graph estático para Ruby ✅ RESOLVIDA NA IMPLEMENTAÇÃO (falta só a medição)
~~RISCO EXISTENCIAL~~ → retirado. Os pontos (a) callers/callees, (b) assinaturas/membros de classes (incl. `attr_*`, mixins, MRO linearizada) e (c) métodos invocados em cada parâmetro estão **implementados e testados** em `marta/ruby_backend/` (`call_graph.py`, `param_types.py`, parser Prism). Existe também a variante **dinâmica** (TracePoint, `dyn_call_graph.py`) e um comparador `compare()` que dá `both/static_only/dynamic_only` + agreement.
**O que sobra (agora é um RESULTADO de paper, não de-risking):** medir num gem real (`httparty`, `faraday` ou `money`) a % de call sites resolvidos pelo estático, usando a suite existente do gem como driver do dinâmico para ground truth parcial; repetir num projeto Rails pequeno para ver a degradação (metaprogramação, `send`, `method_missing`).

### Sondagem 2 — cover-agent (Qodo Cover) em Ruby
É o nosso baseline externo principal. **Fact-check feito:** o suporte Ruby/RSpec está confirmado oficialmente (docs + exemplos Rails com `bundle exec rspec`); continua a precisar de validação prática (que LLM/config, automatizável em batch?).
1. Instalar https://github.com/qodo-ai/qodo-cover, apontar a um gem pequeno com suite RSpec e SimpleCov configurado.
2. Correr um ciclo de geração; registar: funcionou? gerou RSpec válido? aumentou coverage? que LLM/config usa? é automatizável em batch?
- **Critério de sucesso:** um ciclo completo num projeto real. **Se falhar:** documentar o modo de falha; o desenho da avaliação perde o baseline externo (impacto no Paper 1).

### Sondagem 3 — Stack de métricas: SimpleCov + mutant
1. Em 2–3 gems com suites existentes: correr a suite com SimpleCov (statement + branch), depois `mutant` sobre 1–2 classes.
2. Registar fricções de integração do mutant (é conhecido por ser exigente). **Licença: VERIFICADA (jul 2026)** — mutant é comercial mas **grátis para open-source** via `--usage opensource` (exige repo público); gems públicas do corpus qualificam. Ativamente mantido.
- **Critério de sucesso:** pipeline uniforme `bundle exec rspec` → SimpleCov JSON → mutant score, scriptável. A % de projetos onde o mutant corre sem dor torna-se critério de inclusão do corpus.

### Sondagem 4 — Fontes do corpus
1. **SWE-bench Multilingual** *(fact-check: real — 300 tasks, 42 repos, 9 linguagens, com Ruby entre as de maior concentração de tasks)*: descarregar o dataset (HuggingFace), contar quantos repositórios Ruby distintos tem, listar quais, e testar que as imagens Docker de 1–2 deles levantam e correm a suite.
2. **Defects4Ruby** *(fact-check: real — ICPC 2025, autores Dehghan, Meghdad, et al.; dataset anunciado como open-source e reprodutível)*: obter o dataset (paper: https://jie-jw-wu.github.io/assets/ICPC_2025_RENE.pdf; procurar o repositório associado), tentar reproduzir 3–5 bugs: checkout buggy + fixed, correr a suite em ambos, confirmar o par fail/pass.
- **Critério de sucesso:** saber exatamente com quantos repos Ruby "grátis" contamos e se o estudo fixed→buggy é viável ou cai para trabalho futuro.

---

## 2. PRÓXIMA FASE — Corpus leve + comparação (âmbito REDUZIDO por decisão do utilizador)

**Não** se replica a infra de benchmark completa do Test4Py. Corpus = mini-conjunto curado de gems (3–6) + eventual subconjunto Ruby do SWE-bench Multilingual. Critérios: ativamente mantido, suite RSpec existente, instala sem dependências nativas pesadas, mutant executável. ⚠️ Os candidatos Rails originais (Mastodon, Discourse, Forem, Spree) **contradizem** o critério de instalação leve — ficam como stretch goal; começar por gems médias (`httparty`, `money`, `faraday`, `addressable`). Entregáveis: versões fixadas, harness uniforme suite→SimpleCov→mutant, estatísticas descritivas.

**Sistemas comparados:** MARTA-Ruby (nosso) vs cover-agent (externo) vs single-prompt (baseline próprio). Três sistemas → resultados de referência mais fortes.

## 3. ~~FASE FINAL — Port da ferramenta (MARTA-Ruby)~~ ✅ FEITO

O port está completo (ver §0). O que fica desta secção: manter o desenho experimental do paper Python na avaliação (T=0.2, budget N=3, múltiplas runs, Wilcoxon). **Passo prévio obrigatório: correr o MARTA-Ruby num projeto real (1 gem) e resolver os percalços antes de fixar o corpus.**

---

## 4. Referências — trabalho relacionado em Ruby (citar e superar)

- **RuTeG — Mairhofer, Feldt & Torkar, GECCO 2011**, "Search-based software testing and test data generation for a dynamic programming language". Único gerador de testes académico para Ruby. SBST, pré-LLM, descontinuado. DOI 10.1145/2001576.2001826 — https://dl.acm.org/doi/10.1145/2001576.2001826
- **Boorlagadda, Atluri, Olmez & Gehringer 2025** *(citação corrigida — são 4 autores)*, "Comparative Evaluation of Large Language Models for Test-Skeleton Generation" — esqueletos RSpec para UMA classe (curso universitário; GPT-4, DeepSeek-Chat, Llama4-Maverick, Gemma2-9B), sem execução/coverage/mutation. ✅ verificado: https://arxiv.org/abs/2509.04644
- **RAMP — "Collaborative Agents for Automated Program Repair in Ruby"** ✅ verificado no arXiv: https://arxiv.org/abs/2511.03925 (associado ao FARD Lab, UBC Okanagan) — APR multi-agente Ruby (xCodeEval, pass@1 67%, converge em ≤5 iterações); gera testes como meio interno, não como output. Tese UBC associada: https://open.library.ubc.ca/soa/cIRcle/collections/ubctheses/24/items/1.0451047
- **Ruby Bibliography** (varrer secção testing): https://rubybib.org/

## 5. Referências — datasets, baselines e metodologia

**Datasets:** SWE-bench Multilingual (fonte de repos Ruby + Docker): https://www.swebench.com/multilingual-leaderboard.html, paper SWE-smith https://arxiv.org/pdf/2504.21798 · Defects4Ruby (fixed→buggy): https://jie-jw-wu.github.io/assets/ICPC_2025_RENE.pdf · xCodeEval (citar apenas; snippet-level).

**Baselines:** Qodo Cover/cover-agent https://github.com/qodo-ai/qodo-cover (blog: https://www.qodo.ai/blog/we-created-the-first-open-source-implementation-of-metas-testgen-llm/) · single-prompt próprio estilo TEST4PY https://arxiv.org/pdf/2503.14000 · SBST: sem ferramenta viva (argumentar vazio).

**Metodologia a imitar:** TestGenEval (métricas, mutation) https://arxiv.org/pdf/2410.00752 · TestForge https://arxiv.org/pdf/2503.14713 · TestExplora https://arxiv.org/html/2602.10471v2 · Pynguin empírico https://arxiv.org/pdf/2111.05003 e https://arxiv.org/pdf/2007.14049 · "Design choices... prevent them from finding bugs" (justifica fixed→buggy e nunca apagar asserts) https://arxiv.org/pdf/2412.14137 · Shamshiri et al. ASE 2015 "Do Automatically Generated Unit Tests Find Real Faults?" (protocolo fixed→buggy canónico; procurar PDF) · LLM+evolutivo untyped (Python, related work) https://link.springer.com/article/10.1007/s10515-025-00496-7 · SWT-Bench (citar como não-setting).

## 6. Claim de pioneirismo (redação e evidência)

> "To the best of our knowledge, we present the first LLM-based, project-level unit test generation approach and evaluation corpus for Ruby; prior work is limited to early search-based testing [RuTeG 2011] and LLM-generated test skeletons for a single class [2025]."

Verificado: Scholar, IEEE Xplore (4 resultados irrelevantes), Scopus/ACM/DBLP (vazio). Re-verificado no Claude Code (jul 2026): as duas obras que delimitam o claim (skeletons 2509.04644, RAMP 2511.03925) são reais e não o ameaçam. Por fechar: snowballing "Cited by" de Pynguin/EvoSuite/CodaMosa filtrando Ruby; arXiv cs.SE; rubybib. Guardar queries+datas como evidência.

## 7. Plano de publicação

**Paper 1 — benchmark** (MSR Data & Tool Showcase ~4 págs; deadline anual ~out–jan, confirmar): corpus + harness + subconjunto fixed→buggy + resultados de referência (cover-agent, single-prompt). Riscos: poucos repos Ruby no SWE-bench Multilingual; reproduzibilidade Defects4Ruby.

**Paper 2 — ferramenta** (ICST/ISSTA/ASE): MARTA-Ruby + avaliação no benchmark + estudo fixed→buggy + discussão cross-language Python↔Ruby. RQs: (1) yield de testes válidos, (2) coverage com/sem outer loop, (3) mutation + bugs reais, (4) custo (tokens/chamadas).

**Plano B:** fundir num único paper com o corpus como contribuição secundária (precedente: SWE-smith → SWE-bench Multilingual).

---

## 8. Convenções de trabalho para o Claude Code

- Estrutura REAL do repo (Test4Py, branch `main`): a ferramenta vive em `marta/ruby_backend/` (não criar `marta-ruby/`); paridade documentada em `MARTA_Ruby_PARIDADE.md`. Para o trabalho de avaliação: `sondagens/` (uma pasta por sondagem, com scripts + `RESULTADOS.md`) e `benchmark/` (corpus leve). REGRA DURA: o MARTA Python não é tocado — trabalho Ruby é sempre aditivo.
- Tudo reproduzível: versões pinadas (Gemfile.lock, Dockerfiles), comandos registados nos RESULTADOS.md.
- Antes de decisões de desenho com impacto nos papers (ex: abandonar call graph estático, excluir o mutant, mudar de baseline), parar e apresentar as opções com trade-offs — a decisão é discutida, não tomada unilateralmente.
- Se um link/dataset estiver morto ou diferente do descrito aqui, registar no RESULTADOS.md e procurar a fonte atual antes de prosseguir.
- Idioma dos artefactos de investigação (RESULTADOS.md, notas): português ou inglês, mas terminologia técnica e futura escrita de paper em inglês.

---

## 9. Verificação do landscape de ferramentas (2026-07-23) — evidência para o claim

Busca sistemática para responder a "existe alguma ferramenta que gere testes
unitários para Ruby?". Método: docs oficiais + **inspeção do código-fonte**
(não confiar em alegações de "language-agnostic") + busca no próprio RubyGems.

| Ferramenta | Alegação | Verificado | Veredicto p/ Ruby |
|---|---|---|---|
| **cover-agent / Qodo Cover** (open-source do TestGen-LLM da Meta) | multi-linguagem | instalado e corrido E2E c/ ollama; tem exemplo `ruby_sinatra` | ✅ **única viável** — mas só **estende** suites existentes, não gera de raiz |
| **ChatTester** (Yuan et al., arXiv 2305.04207) | "prompting" ⇒ pareceria agnóstico | código: exige `JDK>17 + Maven`, `import javalang`, glob `**/src/test/**/*.java`, `javalang.tree.MethodDeclaration` | ❌ **Java hard-coded** |
| **ChatUniTest** (FSE 2024) | framework LLM | plugin Maven + IntelliJ; "generate tests for an entire **Java** project" | ❌ Java |
| **Keploy** | "**language-agnostic** (eBPF)" | README: intercepta **tráfego de rede** de apps a correr (record-replay de APIs) | ❌ não gera testes unitários de bibliotecas |
| Diffblue Cover | comercial | Java/JVM | ❌ |
| CoverUp, Pynguin | — | Python | ❌ |
| TestPilot | — | JavaScript | ❌ |
| **RuTeG** (GECCO 2011) | SBST p/ Ruby | pré-LLM, descontinuado, sem artefacto usável | ❌ morto |
| Busca no **RubyGems** (`test generation`, `llm test`, `ai test generation`, `gpt rspec`) | — | só geradores de *dados* (faker-likes), relatórios e scaffolding Rails | ❌ nenhuma |

**Lição transversal (o ponto que interessa ao paper):** mesmo as abordagens que
são "só prompting" na ideia têm o **andaime preso a uma linguagem** — parsing do
código-fonte, resolução do método focal, sistema de build e execução da suite. É
aí que a agnosticidade se perde, não no prompt.

**Rigor da afirmação:** não é possível *provar* uma negativa universal. A
formulação defensável é a habitual em SE: *"to the best of our knowledge"*,
suportada por (i) esta verificação de código, (ii) as buscas académicas da §6 e
(iii) a busca no gestor de pacotes do ecossistema. Guardar datas e queries.

### 9.1 Varredura sistemática alargada (2026-07-23) — para além do exemplo do utilizador

Método: (a) survey académico de referência da área, (b) enumeração das ferramentas
da sua secção de geração de testes, (c) verificação de linguagem por repo/código,
(d) buscas diretas no GitHub por geradores de RSpec, (e) busca no RubyGems (§9).

**Achado principal — o survey [AwesomeLLM4SE](https://github.com/iSEngLab/AwesomeLLM4SE)
(SCIS 2025, 1711 linhas):** **ZERO menções a Ruby ou RSpec** em todo o documento.
(As 3 correspondências de "rspec" que o grep devolve são falsos positivos dentro
da palavra "Pe-rspec-tives".) Contagem de menções por linguagem: Python 13,
Rust 8, Java 7, Go 4, JavaScript 3, PHP 1, Kotlin 1, **Ruby 0**.

**Ferramentas da secção "Test Generation" verificadas (25 entradas):**

| Ferramenta | Linguagem | Fonte da verificação |
|---|---|---|
| CODAMOSA | Python | assente no Pynguin |
| RUG | Rust | "Turbo LLM for **Rust** Unit Test Generation" |
| TestART | Java | repo `sikygu/TestART` |
| TestSpark (JetBrains) | Java + Kotlin | plugin IntelliJ; changelog anuncia suporte Kotlin |
| CoverUp | Python | repo `plasma-umass/coverup` |
| TestPilot | TypeScript/JS | repo `githubnext/testpilot` |
| ChatUniTest | Java | plugin Maven/IntelliJ |
| ChatTester | Java | código: `javalang`, JDK+Maven, glob `*.java` |
| **CasModaTest** | Java | ⚠️ "**model**-agnostic" ≠ *language*-agnostic — confusão fácil |

**Buscas diretas no GitHub** (`rspec+generation+llm`, `ruby+test+generation+ai`,
`generate+rspec+gpt`, `ruby+unit+test+generation`): **nenhum gerador de testes
para Ruby**. Os poucos resultados são projetos não relacionados (uma app de
receitas, um projeto escolar de TDD).

**Conclusão:** a lacuna não é só de ferramentas *utilizáveis* — é de **literatura**.
A comunidade de LLM4SE não estudou Ruby. Isto reforça o claim e é, em si, um dado
reportável ("Ruby está ausente do survey de referência da área").

# MARTA-Ruby — referências, baselines e claim de pioneirismo

*Material de escrita do paper: o que se cita, contra o que se compara, e a
evidência que sustenta a afirmação de pioneirismo. Verificado a 2026-07-23.*

O que **não** está aqui, e onde está:

| Assunto | Onde |
|---|---|
| Como o dataset foi construído | `benchmark/dataset/README.md` |
| Estado da ferramenta e diferenças face ao Python | `marta/ruby_backend/PARIDADE.md` |
| O que falta melhorar, com medições | `marta/ruby_backend/MELHORIAS_PENDENTES.md` |
| Onde está o código de cada afirmação | `apresentacao/MAPA_VERIFICACAO.md` |
| Medição do grafo estático vs dinâmico | `sondagens/s1_callgraph_money/RESULTADOS.md` |

---

## 1. Trabalho relacionado em Ruby (citar e superar)

- **RuTeG — Mairhofer, Feldt & Torkar, GECCO 2011**, "Search-based software testing and test data generation for a dynamic programming language". Único gerador de testes académico para Ruby. SBST, pré-LLM, descontinuado. DOI 10.1145/2001576.2001826 — https://dl.acm.org/doi/10.1145/2001576.2001826
- **Boorlagadda, Atluri, Olmez & Gehringer 2025** *(são 4 autores)*, "Comparative Evaluation of Large Language Models for Test-Skeleton Generation" — esqueletos RSpec para UMA classe (curso universitário; GPT-4, DeepSeek-Chat, Llama4-Maverick, Gemma2-9B), sem execução, cobertura ou mutação. Verificado: https://arxiv.org/abs/2509.04644
- **RAMP — "Collaborative Agents for Automated Program Repair in Ruby"**. Verificado: https://arxiv.org/abs/2511.03925 (FARD Lab, UBC Okanagan) — APR multi-agente em Ruby (xCodeEval, pass@1 67%, converge em ≤5 iterações); gera testes como meio interno, não como saída. Tese associada: https://open.library.ubc.ca/soa/cIRcle/collections/ubctheses/24/items/1.0451047
- **Ruby Bibliography** (varrer a secção de testing): https://rubybib.org/

## 2. Datasets, baselines e metodologia

**Datasets:** SWE-bench Multilingual (repos Ruby + Docker): https://www.swebench.com/multilingual-leaderboard.html · SWE-smith: https://arxiv.org/pdf/2504.21798 · Defects4Ruby (fixed→buggy): https://jie-jw-wu.github.io/assets/ICPC_2025_RENE.pdf · xCodeEval (citar apenas; é ao nível do excerto).

**Baselines:** Qodo Cover / cover-agent https://github.com/qodo-ai/qodo-cover (blog: https://www.qodo.ai/blog/we-created-the-first-open-source-implementation-of-metas-testgen-llm/) · SBST: sem ferramenta viva para Ruby, argumentar o vazio.

⚠️ **Regra dura do utilizador (2026-07-22):** não se constroem baselines nossas
(nem single-prompt, nem "test4py-ruby"). A comparação é contra ferramentas
**existentes**. Se não existir mais nada, isso é o claim de pioneirismo, não um
buraco a preencher por nós.

**Metodologia a imitar:** TestGenEval (métricas, mutação) https://arxiv.org/pdf/2410.00752 · TestForge https://arxiv.org/pdf/2503.14713 · TestExplora https://arxiv.org/html/2602.10471v2 · Pynguin empírico https://arxiv.org/pdf/2111.05003 e https://arxiv.org/pdf/2007.14049 · "Design choices... prevent them from finding bugs" (justifica fixed→buggy e nunca apagar asserts) https://arxiv.org/pdf/2412.14137 · Shamshiri et al. ASE 2015, "Do Automatically Generated Unit Tests Find Real Faults?" (protocolo fixed→buggy canónico) · LLM+evolutivo em linguagens não tipadas https://link.springer.com/article/10.1007/s10515-025-00496-7 · SWT-Bench (citar como cenário diferente).

**Desenho experimental**, herdado do paper Python: T=0.2, orçamento de reparação
N=3, múltiplas execuções, Wilcoxon.

## 3. Claim de pioneirismo

> "To the best of our knowledge, we present the first LLM-based, project-level
> unit test generation approach and evaluation corpus for Ruby; prior work is
> limited to early search-based testing [RuTeG 2011] and LLM-generated test
> skeletons for a single class [2025]."

Verificado em Scholar, IEEE Xplore (4 resultados irrelevantes), Scopus, ACM e
DBLP (vazio). Re-verificado em julho de 2026: as duas obras que delimitam o claim
(skeletons 2509.04644, RAMP 2511.03925) são reais e não o ameaçam.

**Por fechar:** snowballing do "Cited by" de Pynguin, EvoSuite e CodaMosa
filtrando Ruby; arXiv cs.SE; rubybib. Guardar as consultas e as datas.

## 4. Plano de publicação

**Paper 1 — benchmark** (MSR Data & Tool Showcase, ~4 páginas): corpus, harness,
subconjunto fixed→buggy, resultados de referência.

**Paper 2 — ferramenta** (ICST/ISSTA/ASE): MARTA-Ruby, avaliação no benchmark,
estudo fixed→buggy, discussão cross-language Python↔Ruby. Perguntas de
investigação: (1) proporção de testes válidos, (2) cobertura com e sem o ciclo
exterior, (3) mutação e bugs reais, (4) custo em tokens e chamadas.

**Plano B:** fundir num só paper, com o corpus como contribuição secundária
(precedente: SWE-smith → SWE-bench Multilingual).

---

## 5. Verificação do landscape (2026-07-23) — a evidência do claim

Busca sistemática para responder a *"existe alguma ferramenta que gere testes
unitários para Ruby?"*. Método: documentação oficial, **inspeção do código-fonte**
(não confiar em alegações de "language-agnostic") e busca no próprio RubyGems.

| Ferramenta | Alegação | Verificado | Veredicto para Ruby |
|---|---|---|---|
| **cover-agent / Qodo Cover** | multi-linguagem | instalado e corrido de ponta a ponta com ollama; tem exemplo `ruby_sinatra` | **única viável** — mas só **estende** suites existentes, não gera de raiz |
| **ChatTester** (arXiv 2305.04207) | "prompting", pareceria agnóstico | código: exige `JDK>17 + Maven`, `import javalang`, glob `**/src/test/**/*.java` | Java, fixo no código |
| **ChatUniTest** (FSE 2024) | framework LLM | plugin Maven + IntelliJ; "generate tests for an entire **Java** project" | Java |
| **Keploy** | "**language-agnostic** (eBPF)" | README: intercepta **tráfego de rede** de aplicações a correr | não gera testes unitários de bibliotecas |
| Diffblue Cover | comercial | Java/JVM | não |
| CoverUp, Pynguin | — | Python | não |
| TestPilot | — | JavaScript | não |
| **RuTeG** (GECCO 2011) | SBST para Ruby | pré-LLM, descontinuado, sem artefacto usável | morto |
| RubyGems (`test generation`, `llm test`, `gpt rspec`) | — | só geradores de *dados* (tipo faker), relatórios e scaffolding Rails | nenhuma |

**A lição transversal, e é o ponto que interessa ao paper:** mesmo as abordagens
que na ideia são "só prompting" têm o **andaime preso a uma linguagem** — parsing
do código, resolução do método focal, sistema de build, execução da suite. É aí
que a agnosticidade se perde, não no prompt.

**Rigor:** não se prova uma negativa universal. A formulação defensável é a
habitual em engenharia de software, *"to the best of our knowledge"*, suportada
por (i) esta verificação de código, (ii) as buscas académicas da secção 3 e
(iii) a busca no gestor de pacotes do ecossistema.

### 5.1 Varredura alargada — para além do exemplo do utilizador

Método: survey académico de referência, enumeração das ferramentas da secção de
geração de testes, verificação de linguagem por repositório, buscas diretas no
GitHub por geradores de RSpec, e a busca no RubyGems acima.

**Achado principal — o survey [AwesomeLLM4SE](https://github.com/iSEngLab/AwesomeLLM4SE)
(SCIS 2025, 1711 linhas): ZERO menções a Ruby ou RSpec** em todo o documento. (As
3 correspondências de "rspec" no grep são falsos positivos dentro de
"Pe-rspec-tives".) Menções por linguagem: Python 13, Rust 8, Java 7, Go 4,
JavaScript 3, PHP 1, Kotlin 1, **Ruby 0**.

**As 25 entradas da secção "Test Generation", verificadas:**

| Ferramenta | Linguagem | Fonte |
|---|---|---|
| CODAMOSA | Python | assente no Pynguin |
| RUG | Rust | "Turbo LLM for **Rust** Unit Test Generation" |
| TestART | Java | repo `sikygu/TestART` |
| TestSpark (JetBrains) | Java + Kotlin | plugin IntelliJ |
| CoverUp | Python | repo `plasma-umass/coverup` |
| TestPilot | TypeScript/JS | repo `githubnext/testpilot` |
| ChatUniTest | Java | plugin Maven/IntelliJ |
| ChatTester | Java | código: `javalang`, JDK+Maven, glob `*.java` |
| **CasModaTest** | Java | "**model**-agnostic" não é *language*-agnostic |

**Buscas diretas no GitHub** (`rspec+generation+llm`, `ruby+test+generation+ai`,
`generate+rspec+gpt`, `ruby+unit+test+generation`): **nenhum gerador de testes
para Ruby**. Os poucos resultados são projetos não relacionados.

**Conclusão:** a lacuna não é só de ferramentas *utilizáveis*, é de
**literatura**. A comunidade de LLM4SE não estudou Ruby, e isso é em si um dado
reportável: *"Ruby está ausente do survey de referência da área"*.

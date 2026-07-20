# Sondagem 4 — Fontes do corpus (SWE-bench Multilingual + gems candidatas)

**Data:** 2026-07-19 · **Estado:** parte 1 (SWE-bench) CONCLUÍDA · parte 2 (Defects4Ruby) por fazer

## Parte 1 — SWE-bench Multilingual: quanto Ruby existe?

**Dataset localizado:** `swe-bench/SWE-bench_Multilingual` no HuggingFace (1 parquet, split `test`).
⚠️ Correção ao plano: **não existe** `princeton-nlp/SWE-bench_Multilingual`; o namespace é `swe-bench/` (ou `SWE-bench/`). Não confundir com `Daoguang/Multi-SWE-bench` (outro dataset, Java).

**Composição total:** 300 tasks / 41 repos. Não tem coluna `language` — as linguagens foram identificadas por repo.

### O subconjunto Ruby: 44 tasks / 6 repos (14.7% das tasks)

| Repo | Tasks | Dir de testes | Framework | Adequação p/ nós |
|---|---:|---|---|---|
| `rubocop/rubocop` | 16 | `spec/` | **RSpec** | ✅ mas é um linter enorme (AST-heavy) |
| `fluent/fluentd` | 12 | `test/` | test-unit | ❌ não é RSpec |
| `fastlane/fastlane` | 7 | `*/spec/` | **RSpec** (monorepo, spec por subprojeto) | 🟡 monorepo grande, muitos sub-gems |
| `jekyll/jekyll` | 5 | `test/` | minitest/shoulda | ❌ não é RSpec |
| `faker-ruby/faker` | 2 | `test/` | minitest | ❌ não é RSpec |
| `jordansissel/fpm` | 2 | `spec/` (+`test/`) | **RSpec** | 🟡 poucas tasks |

### 🔴 Conclusão crítica para o desenho do benchmark
**Só 3 dos 6 repos Ruby do SWE-bench usam RSpec** (rubocop, fastlane, fpm = 25 das 44 tasks), e são **aplicações grandes**, não gems de tamanho médio. Ou seja: **o SWE-bench Multilingual NÃO serve como espinha dorsal do nosso corpus.** Serve para uma coisa específica e valiosa — fornecer **bugs reais com pares FAIL_TO_PASS/PASS_TO_PASS** (`base_commit`, `patch`, `test_patch`) para o estudo fixed→buggy, se o quisermos, e apenas nos 3 repos RSpec.

**Implicação:** o corpus principal tem de vir de **gems curadas por nós** (parte 2 abaixo). Isto reforça o claim de pioneirismo: não há corpus Ruby pronto para geração de testes — temos de o construir.

## Parte 2 — Levantamento de gems candidatas

20 candidatas medidas via API do GitHub (estrelas, tamanho, último push, framework por layout de diretórios). **Filtro decisivo: RSpec** (a nossa ferramenta gera RSpec; um alvo minitest exigiria outro backend).

### ✅ Candidatas RSpec (todas ativas em 2026)
| Gem | Stars | Tamanho (KB) | Último push | Nota |
|---|---:|---:|---|---|
| `paper-trail-gem/paper_trail` | 7026 | 3936 | 2026-05-08 | depende de Rails/AR (pesado) |
| `lostisland/faraday` | 5948 | 3433 | 2026-06-24 | ✅ forte candidata (HTTP abstrato, adapters) |
| `jnunemaker/httparty` | 5896 | 1597 | 2026-03-04 | ✅ forte candidata (já prevista no plano) |
| `jeremyevans/sequel` | 5087 | 62427 | 2026-07-19 | ❌ enorme (62 MB) |
| `bblimke/webmock` | 4051 | 2761 | 2026-03-18 | ✅ candidata |
| `jwt/ruby-jwt` | 3687 | 2527 | 2026-07-16 | ✅ **excelente** (cripto pura, sem I/O) |
| `mikel/mail` | 3673 | 7105 | 2026-07-01 | 🟡 grande, parsing complexo |
| `RubyMoney/money` | 2880 | 3296 | 2026-06-22 | ✅ **já validada** (sondagem 1) |
| `sporkmonger/addressable` | 1611 | 1984 | 2026-06-27 | ✅ **excelente** (URI puro, sem deps) |

### ❌ Excluídas por framework (minitest/test-unit)
`sidekiq`, `kaminari`, `friendly_id`, `rack`, `oj`, `httprb/http`, `rubyzip`, `rgeo`, `i18n`, `flori/json` — **10 de 20**. Nota: **metade do ecossistema Ruby popular não usa RSpec**; é um facto a reportar no paper (limita qualquer benchmark RSpec-only).

## Recomendação de corpus (v1)

**Núcleo (4-5 gems, RSpec, Ruby puro, instalação leve):**
`money` (validada) · `addressable` · `ruby-jwt` · `httparty` · `faraday`

Racional: cobrem domínios diferentes (aritmética/moeda, parsing de URI, cripto/tokens, cliente HTTP, abstração HTTP), todas ativas, todas RSpec, nenhuma com dependências nativas pesadas. Tamanhos 1.6–3.4 MB (exceto money 3.3 MB) — tratáveis.

⚠️ **Lição da `money` (cobertura humana 99.8%)**: é preciso **medir a cobertura da suite humana de cada candidata antes de fixar o corpus** — gems com cobertura ~100% deixam pouca margem para demonstrar ganho. Idealmente o corpus tem variedade de cobertura-base.

**Opcional (bugs reais):** `rubocop` e `fpm` do SWE-bench, só para o estudo fixed→buggy.

## Próximos passos
1. Clonar as 4 candidatas restantes, `bundle install`, correr suite, **medir cobertura humana** com o nosso harness (não-LLM) → tabela de cobertura-base.
2. Correr a frente estática do MARTA-Ruby em cada uma (métodos-alvo, arestas, erros de parse) → confirma robustez do parser fora da `money`.
3. Defects4Ruby (parte 2 desta sondagem, ainda por fazer).
4. Sondagem 2 (cover-agent) e 3 (mutant) nas mesmas gems.

## Reprodução
```python
from huggingface_hub import hf_hub_download
import pandas as pd
p = hf_hub_download('swe-bench/SWE-bench_Multilingual','data/test-00000-of-00001.parquet',repo_type='dataset')
df = pd.read_parquet(p)            # 300 tasks, 41 repos
ruby = ['rubocop/rubocop','fluent/fluentd','fastlane/fastlane','jekyll/jekyll','faker-ruby/faker','jordansissel/fpm']
df[df.repo.isin(ruby)]             # 44 tasks
```
(requer `pip install pyarrow`, instalado nesta sondagem)

# Comparação de resultados — httpie

Comparação dos resultados da geração de testes da abordagem **MARTA / Test4Py** com baselines externos (**CodaMOSA** e **CoverUp**) no projeto-alvo **httpie**.

---

## 1. Resultados locais (MARTA — Results_httpie)

Configuração: `3_Gen`, `temp_0.2`. Fontes: `Results_httpie/Results_MARTA/<modelo>/3_Gen/temp_0_2/httpie/`.

### 1.1 Cobertura (`coverage.json`)

Medido com `coverage.py` sobre o package `httpie/` (78 ficheiros, **4 207 statements**, **1 448 branches**).

| Modelo | Statement Cov. | Branch Cov. | Linhas cobertas | Statements em falta | Branches cobertas | Branches em falta |
|---|---:|---:|---:|---:|---:|---:|
| codestral | **57,03 %** | **39,71 %** | 2 650 | 1 557 | 575 | 873 |
| deepseek-coder-v2-16b | 41,10 % | 22,24 % | 2 002 | 2 205 | 322 | 1 126 |
| qwen2.5-coder_32b | 42,35 % | 24,93 % | 2 034 | 2 173 | 361 | 1 087 |

### 1.2 Execução dos testes (`run_results/httpie.json`)

| Modelo | Assertions ✓ | Assertions ✗ | Syntax errors | Syntax pass | Tempo total | Tempo LLM (∑ runs) |
|---|---:|---:|---:|---:|---:|---:|
| codestral | 853 | 3 912 | 5 181 | 4 765 | 30 849 s (~8,6 h) | 25 754 s |
| deepseek-coder-v2-16b | 867 | 3 880 | 5 258 | 4 747 | 30 267 s (~8,4 h) | 25 210 s |
| qwen2.5-coder_32b | 734 | 3 522 | 4 995 | 4 256 | 29 735 s (~8,3 h) | 24 633 s |

### 1.3 Top de tipos de erro em asserções (agregado das 3 runs)

| Modelo | AttributeError | AssertionError | TypeError | Failed | KeyError | Outros notáveis |
|---|---:|---:|---:|---:|---:|---|
| codestral | 1 109 | 970 | 679 | 666 | 160 | ModuleNotFoundError 56; OSError 44; ValueError 44 |
| deepseek-coder-v2-16b | 1 179 | 1 009 | 680 | 633 | 135 | ModuleNotFoundError 52; FileNotFoundError 49; ValueError 43 |
| qwen2.5-coder_32b | 962 | 864 | 600 | 585 | 114 | FileNotFoundError 59; ModuleNotFoundError 37; OSError 33 |

> **Nota — mutation score:** ainda **não** foram corridos `mutmut` para estas execuções, logo a coluna *Mutation Score (%)* (presente no `aggregate_results.py`) sai como `N/A`.

---

## 2. Baselines externos

### 2.1 microsoft/codamosa-dataset

Verificado em [github.com/microsoft/codamosa-dataset](https://github.com/microsoft/codamosa-dataset). A pasta `final-exp/` **não contém httpie** — são quase todos benchmarks Ansible. Logo, os números do CodaMOSA para httpie têm de vir de outro lado.

### 2.2 plasma-umass/coverup-eval (FSE'25)

Tem o **CodaMOSA replicado (baseline)** **e** o **CoverUp** corridos em httpie, dentro da suite **CM**.

- Diretoria-base: `output/<config>/httpie/`
- Ficheiro relevante: `final.json` (relatório do **slipcover**)
- Tamanho da medição: **2 881 linhas / 560 branches** em `httpie/`

#### Tabela CM (httpie)

| Aproximação | Pasta no repo | Line Cov. | Branch Cov. | Linhas cobertas | Branches cobertas |
|---|---|---:|---:|---:|---:|
| **CodaMOSA (baseline)** | `output/cm/httpie` | **61,03 %** | **34,10 %** | 1 909 / 2 881 | 191 / 560 |
| CoverUp (gpt4o) | `output/cm.gpt4o/httpie` | **70,50 %** | ~46 % | 2 167 / 2 881 | 259 / 560 |
| **CoverUp v2 (gpt4o-v2)** | `output/cm.gpt4o-v2/httpie` | **68,64 %** | **48,03 %** | 2 093 / 2 881 | 269 / 560 |
| CoverUp v2 — no-coverage | `output/cm.gpt4o-v2-no-coverage/httpie` | 66,70 % | — | 2 046 / 2 881 | 249 / 560 |
| CoverUp v2 — no-code-context | `output/cm.gpt4o-v2-no-code-context/httpie` | 63,21 % | — | 1 971 / 2 881 | 204 / 560 |
| CoverUp v2 — no-error-fixing | `output/cm.gpt4o-v2-no-error-fixing/httpie` | 60,65 % | — | 1 749 / 2 881 | 141 / 560 |
| CoverUp v2 — ablated (tudo off) | `output/cm.gpt4o-v2-ablated/httpie` | 37,11 % | 13,74 % | 1 200 / 2 881 | 77 / 560 |

> Existe também `output/1_0/httpie` e `output/1_0.gpt4o-v2/httpie` (suite **PY**) — ambos a 7,35 %. **Não é comparável**: nesta suite só geram testes para um subconjunto pequeno de módulos. Ignorar.

---

## 3. Comparação direta — MARTA vs. baselines (suite CM)

| Aproximação | Line/Stmt Cov. | Branch Cov. |
|---|---:|---:|
| CoverUp v1 (gpt4o) | 70,50 % | ~46 % |
| CoverUp v2 (gpt4o-v2) | 68,64 % | 48,03 % |
| CoverUp v2 — no-coverage | 66,70 % | — |
| CoverUp v2 — no-code-context | 63,21 % | — |
| **CodaMOSA (baseline)** | **61,03 %** | **34,10 %** |
| CoverUp v2 — no-error-fixing | 60,65 % | — |
| **MARTA — codestral** | **57,03 %** | **39,71 %** |
| **MARTA — qwen2.5-coder-32b** | 42,35 % | 24,93 % |
| **MARTA — deepseek-coder-v2-16b** | 41,10 % | 22,24 % |
| CoverUp v2 — ablated (tudo off) | 37,11 % | 13,74 % |

### Observações

- **MARTA-codestral** (57 %) fica **abaixo** do CodaMOSA baseline (61 %) em linhas, mas **acima** em branches (39,7 % vs 34,1 %).
- **deepseek-v2-16b** e **qwen2.5-coder-32b** ficam claramente abaixo do baseline em ambas as métricas.
- Todos os modelos MARTA ficam acima da ablação total do CoverUp (37 %).
- A diferença para os melhores CoverUp (~68–70 %) é maior em linhas do que em branches.

---

## 4. Caveats importantes para o paper

1. **Ferramentas de cobertura diferentes**
   - MARTA: `coverage.py` → **4 207 statements** / 1 448 branches.
   - CoverUp / CodaMOSA-replication: `slipcover` → **2 881 lines** / 560 branches.
   - As percentagens medem o mesmo package `httpie/*`, mas a base não é idêntica. Comparar **percentagens** é defensável; comparar **valores absolutos** não.

2. **Versão de httpie**
   - O delta 4 207 vs 2 881 sugere versões diferentes (a tua mais recente) ou contagens distintas de statements vs lines. **Vale a pena fixar a mesma versão de httpie** antes de publicar números absolutos.

3. **Métricas que cada lado tem e o outro não**
   - MARTA reporta: `assertion_pass`, `assertion_error`, tipos de erro, tempos LLM, etc. → o CoverUp não publica isto no `final.json`.
   - O CoverUp publica: cobertura por ficheiro detalhada via slipcover.
   - **Mutation score (mutmut):** ainda não foi corrido para estas execuções; o CoverUp também não o reporta. Eixo onde podes acrescentar valor se correres `mutmut`.

4. **Suite CM vs suite PY**
   - Comparação válida é só com `cm/`. Os ficheiros `1_0/` (suite PY) usam um conjunto de módulos diferente — números a 7 % não significam pior desempenho.

---

## 5. Fontes (ficheiros lidos)

**Locais:**
- `Results_httpie/Results_MARTA/codestral/3_Gen/temp_0_2/httpie/{coverage.json, run_results/httpie.json}`
- `Results_httpie/Results_MARTA/deepseek-coder-v2-16b/3_Gen/temp_0_2/httpie/{coverage.json, run_results/httpie.json}`
- `Results_httpie/Results_MARTA/qwen2.5-coder_32b/3_Gen/temp_0_2/httpie/{coverage.json, run_results/httpie.json}`

**Externos (apenas lidos via HTTP, nada descarregado para disco):**
- `https://github.com/plasma-umass/coverup-eval/tree/main/output/cm/httpie/final.json`
- `https://github.com/plasma-umass/coverup-eval/tree/main/output/cm.gpt4o/httpie/final.json`
- `https://github.com/plasma-umass/coverup-eval/tree/main/output/cm.gpt4o-v2/httpie/final.json`
- `https://github.com/plasma-umass/coverup-eval/tree/main/output/cm.gpt4o-v2-no-coverage/httpie/final.json`
- `https://github.com/plasma-umass/coverup-eval/tree/main/output/cm.gpt4o-v2-no-code-context/httpie/final.json`
- `https://github.com/plasma-umass/coverup-eval/tree/main/output/cm.gpt4o-v2-no-error-fixing/httpie/final.json`
- `https://github.com/plasma-umass/coverup-eval/tree/main/output/cm.gpt4o-v2-ablated/httpie/final.json`
- `https://github.com/plasma-umass/coverup-eval/tree/main/output/1_0/httpie/final.json`
- `https://github.com/plasma-umass/coverup-eval/tree/main/output/1_0.gpt4o-v2/httpie/final.json`
- `https://github.com/microsoft/codamosa-dataset/tree/main/final-exp/` (não contém httpie)

# Baselines — Setup e Estrutura

Esta pasta contém as ferramentas baseline para a comparação com a MARTA na
suite **CM (CodaMosa)** — 486 módulos de 27 projetos Python.

## Estrutura

```
baselines/
├── pynguin/                  # clone se2p/pynguin       (search-based, sem LLM)
├── coverup/                  # clone plasma-umass/coverup (LLM + tools)
├── test4py-baseline/         # clone Test4DT/Test4Py    (LLM, base da MARTA)
├── codamosa/                 # clone microsoft/codamosa (scripts do benchmark)
│   └── replication/test-apps/  ← DATASET CM: 27 projetos × 486 módulos (read-only!)
├── Results_Pynguin/          # outputs da Pynguin       (por projeto/módulo)
├── Results_CoverUp/          # outputs do CoverUp
├── Results_Test4PyBaseline/  # outputs do Test4Py-baseline
└── Results_MARTA/            # outputs da MARTA na suite CM (futuro)
```

⚠️ **`baselines/codamosa/replication/test-apps/` é dataset READ-ONLY.** Todas as
ferramentas devem ser executadas a partir de um working dir separado para não
poluir o dataset. Os outputs vão para `Results_<TOOL>/<project>/`.

## Ambientes Conda (todos Python 3.10)

| Env | Função | Como ativar |
|---|---|---|
| `pynguin_env` | Pynguin | `conda activate pynguin_env` |
| `test4py_baseline_env` | Test4Py baseline | `conda activate test4py_baseline_env` |
| `test4py_env` | MARTA (existente) | `conda activate test4py_env` |

(`coverup_env` foi removido: comparamos contra paper publicado.)

## Setup final: 3 baselines locais + 1 "compare against published"

| Tool | Como avalia | LLM |
|---|---|---|
| **Pynguin** | Corre localmente no benchmark CM | — (sem LLM) |
| **MARTA** | Corre localmente no benchmark CM | `deepseek-coder-v2:16b` |
| **Test4Py-baseline** | Corre localmente no benchmark CM | `deepseek-coder-v2:16b` |
| **CoverUp** | **NÃO corre localmente — comparamos contra os números publicados no paper FSE 2025** | (paper deles usou GPT-4o) |

### Justificação para o paper (Threats to Validity)

> *"We evaluate MARTA against three independent baselines: Pynguin (search-based, no-LLM, run locally), TEST4PY (LLM-based monolithic, run locally with the same DeepSeek-Coder-V2 16B model as MARTA), and CoverUp (LLM-based agentic, **results taken from the published FSE 2025 paper [1] which used GPT-4o on the same CM benchmark**). The choice to compare against CoverUp's published numbers rather than re-run locally reflects the unavailability of an open-weights LLM with both the function-calling capabilities required by CoverUp's architecture and the inference speed required to run at the 486-module scale; we tested 9 local LLMs empirically and none satisfied both constraints (see appendix)."*

Esta formulação dá-nos:
- 2 baselines **independentes** controladas em apples-to-apples (Pynguin, TEST4PY)
- 1 baseline contra estado-da-arte LLM-frontier (CoverUp via paper)
- Justifica e antecipa críticas do tipo "porque não correste CoverUp?"

### Bake-off empírico que justifica saltar CoverUp local

Testámos 9 LLMs locais com CoverUp em codetiming._timers; **nenhum cumpre
simultaneamente** os requisitos: function calling sem loops + qualidade
output + velocidade suficiente para o benchmark de 486 módulos.

| LLM | Tools | CoverUp cov | MARTA-friendly | Veredito |
|---|---|---|---|---|
| DeepSeek-Coder-V2 16B | ❌ | n/a | ✅ 98% | Usado em MARTA/Test4Py |
| Codestral 22B (Ollama) | ❌ | n/a | — | Não tem tools |
| Qwen2.5-Coder 14B/32B | ✅ | 0% (loops) | — | Loops |
| Mistral-Nemo 12B | ✅ | crash | — | Alucina tools |
| Llama 3.1 8B | ✅ | loops lentos | — | Loops |
| Granite 3.1-dense 8B | ✅ | 62% | — | Qualidade insuficiente |
| gpt-oss 20B | ✅ | 96% | ❌ (crashes runs longos) | Instável a escala |
| Mistral-small 24B | ✅ | 76% | ❌ (3x lento MARTA) | Não passa em MARTA |
| command-r:35b | ✅ | content vazio | n/t | Bug Ollama wrapping |

Conclusão: aceitamos comparar CoverUp contra resultados publicados no
paper FSE 2025 (GPT-4o no mesmo benchmark CM).

### Config dos envs

```env
# Test4Py/.env (MARTA)
MODEL='deepseek-coder-v2:16b'
OPENAI_API_KEY='ollama'
OPENAI_API_BASE='http://localhost:11434/v1'
TRANSFORMER_PATH='BAAI/bge-large-en-v1.5'

# Test4Py/baselines/test4py-baseline/.env (idem MARTA)
```

### Modelos no Ollama necessários

```
deepseek-coder-v2:16b   8.9 GB    (MARTA, Test4Py-baseline)
```
Total: ~8.9 GB

### Se quiseres correr CoverUp localmente no futuro

(removido do setup actual; foi explicitamente decidido deixar para
comparação contra paper publicado.)

```bash
git clone https://github.com/plasma-umass/coverup baselines/coverup
conda create -y -n coverup_env python=3.10
/opt/homebrew/Caskroom/miniconda/base/envs/coverup_env/bin/pip install coverup
ollama pull gpt-oss:20b  # ou modelo escolhido
# Adicionar "coverup" ao DEFAULT_TOOLS em scripts/run_benchmark.py
```

## Modificações ao código das ferramentas

### Patches arquiteturais à MARTA e Test4Py-baseline

Dois patches importantes nos dois projetos:

**1. Filtro `projects.json` no loop de geração**

Helper `_targeted_file_messages()` em:
- `Test4Py/marta/message_react.py`
- `Test4Py/baselines/test4py-baseline/test4dt/message.py`

Quando `--run_benchmark=True` (default) E o projeto está em `projects.json`,
a geração de testes fica limitada aos módulos dessa lista. Call-graph e RAG
continuam a analisar o projeto inteiro (necessário para contexto), mas
LLM calls só acontecem para módulos-alvo. Sem este patch, MARTA/Test4Py
gerariam testes para todos os ficheiros do projeto, sem alinhamento com
Pynguin/CoverUp (que aceitam módulo a módulo).

**2. `--output_dir` para isolar outputs do source**

Adicionado o flag `--output_dir <DIR>` em:
- `marta/start_react.py`
- `baselines/test4py-baseline/test4dt/start.py`

Quando definido, TODAS as outputs (Test4DT_tests/, test_quarantine/,
coverage.json, caches do call graph e análise LLM, run_results/,
react_history.txt) vão para `{output_dir}/{project_name}/...` em vez de
poluírem o source do projeto.

Sem este patch, MARTA/Test4Py escreviam para dentro do `{project_path}/`,
o que sujava o dataset CM (read-only) a cada run. Com `--output_dir`, o
dataset fica intocado e podemos correr os 4 tools sobre o mesmo source
em paralelo sem conflitos.

A mudança preserva backward compat: sem `--output_dir`, comportamento legacy.

### Aplicar os patches a um clone fresco do test4py-baseline

A MARTA tem os patches diretamente no source tracked. O test4py-baseline é
um clone externo (gitignored), por isso os patches estão guardados como
`.patch` em `baselines/patches/`:

```bash
cd baselines/test4py-baseline
git apply ../patches/test4py-baseline-output-dir-and-projects-filter.patch
```

### projects.json — entradas adicionadas

`codetiming` adicionada em ambos os `projects.json` (MARTA e Test4Py-baseline)
para o smoke test. Os restantes 26 projetos do CM ainda precisam de ser
adicionados antes da corrida grande, com os módulos extraídos de
`codamosa/replication/scripts/modules_base_and_name.csv` (486 entradas).

## Status (smoke test em `codetiming._timers`)

| Tool | Tempo | Tests | Stmt Cov | Branch Cov | Pytest |
|---|---|---|---|---|---|
| Pynguin | 60s | 15 | 95.0% | 75.0% | ✓ |
| Test4Py-baseline | 13:41 | 50 | 98.1% | 91.7% | ✓ |
| MARTA | 8:45 | 27 | 98.1% | 91.7% | ✓ |
| CoverUp | n/a | 0 | n/a | n/a | (LLM blocker) |

## TODO antes da corrida grande dos 486 módulos

1. Resolver decisão CoverUp (LLM).
2. Popular `projects.json` (MARTA + Test4Py-baseline) com os restantes 26
   projetos × módulos extraídos do `modules_base_and_name.csv`.
3. Escrever harness unificado (`run_benchmark.py`?) que:
   - Para cada (tool, project, module): cria working dir, instala o projeto
     no env certo, corre a tool com output direcionado para `Results_<TOOL>/<project>/<module>/`.
   - Captura outputs E quarantine.
   - Recolhe runtime + tokens (resposta ao Revisor A).
   - Mata após timeout configurável.
4. Pipeline de avaliação consistente (coverage.py + Mutmut em env dedicado).
5. Re-correr MARTA na suite CM completa (o smoke ficou só num módulo).

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
| `coverup_env` | CoverUp | `conda activate coverup_env` |
| `test4py_baseline_env` | Test4Py baseline | `conda activate test4py_baseline_env` |
| `test4py_env` | MARTA (existente) | `conda activate test4py_env` |

## LLMs por tool (decisão final após bake-off de 9 modelos)

### Setup final: MIXED (não foi possível single-LLM apples-to-apples)

| Tool | LLM | Endpoint |
|---|---|---|
| MARTA | `deepseek-coder-v2:16b` | OpenAI-compat `/v1` (env: MODEL) |
| Test4Py-baseline | `deepseek-coder-v2:16b` | OpenAI-compat `/v1` (env: MODEL) |
| CoverUp | `gpt-oss:20b` via `ollama_chat/` | Ollama nativo `/api/chat` (env: COVERUP_MODEL) |
| Pynguin | — | — |

**Justificação científica (Threats to Validity):** após testar 9 LLMs locais
empiricamente, nenhum cumpre simultaneamente os requisitos de rapidez em
MARTA (muitas chamadas curtas), function calling correcto em CoverUp,
qualidade de output, e estabilidade em runs longos. MARTA e Test4Py-baseline
correm em apples-to-apples (deepseek-coder-v2:16b); CoverUp usa gpt-oss
por ser o único modelo local que produziu coverage decente (96% no smoke
de codetiming._timers).

### Bake-off empírico completo (CoverUp em codetiming._timers)

| LLM | Tools | MARTA-friendly | CoverUp cov | Veredito |
|---|---|---|---|---|
| DeepSeek-Coder-V2 16B | ❌ | ✅ 98% | n/a | **ESCOLHIDO para MARTA/Test4Py** |
| Codestral 22B (Ollama) | ❌ | — | n/a | Não testado em MARTA |
| Qwen2.5-Coder 14B/32B | ✅ | — | 0% (loops) | Não serve |
| Mistral-Nemo 12B | ✅ | — | crash (alucina) | Não serve |
| Llama 3.1 8B | ✅ | — | loops lentos | Não serve |
| Granite 3.1-dense 8B | ✅ | — | 62% | Qualidade insuficiente |
| **gpt-oss 20B** | ✅ | ❌ (3x+ lento) | **96%** | **ESCOLHIDO para CoverUp** |
| Mistral-small 24B | ✅ | ❌ (3x lento MARTA) | 76% | Não passa MARTA |
| command-r:35b | ✅ | n/t | content vazio | Bug Ollama wrapping com tools |

### Config dos envs

```env
# Test4Py/.env (MARTA)
MODEL='deepseek-coder-v2:16b'
OPENAI_API_KEY='ollama'
OPENAI_API_BASE='http://localhost:11434/v1'
TRANSFORMER_PATH='BAAI/bge-large-en-v1.5'

# Test4Py/baselines/test4py-baseline/.env (idem MARTA)
```

CoverUp configurado via env var na invocação do harness:
```bash
COVERUP_MODEL='ollama_chat/gpt-oss:20b'  # default do harness
```

### Modelos no Ollama necessários

```
deepseek-coder-v2:16b   8.9 GB    (MARTA, Test4Py-baseline)
gpt-oss:20b             14 GB     (CoverUp)
```
Total: ~23 GB

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

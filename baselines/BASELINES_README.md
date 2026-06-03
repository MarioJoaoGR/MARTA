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

## LLM endpoint (apples-to-apples)

Todos os tools LLM-based apontam para o mesmo Ollama local:

```env
MODEL='deepseek-coder-v2:16b'
OPENAI_API_KEY='ollama'
OPENAI_API_BASE='http://localhost:11434/v1'
TRANSFORMER_PATH='BAAI/bge-large-en-v1.5'    # cache HF para RAG
```

Configurado em `Test4Py/.env` (MARTA) e `baselines/test4py-baseline/.env`.

⚠️ **CoverUp NÃO consegue usar DeepSeek-Coder-V2 16B** porque a sua arquitetura
exige function calling. Tentativas falhadas (documentadas no projeto):
- DeepSeek-Coder-V2 16B → não suporta function calling
- Qwen2.5-Coder 14B → loop infinito em tool calls
- Qwen2.5-Coder 32B → loop infinito (idem)

Decisão sobre CoverUp pendente (GPT-4o vs ablated mode vs skip).

## Modificações ao código das ferramentas

### Patch: filtro `projects.json` na MARTA e Test4Py-baseline

Adicionado helper `_targeted_file_messages()` em:
- `Test4Py/marta/message_react.py`
- `Test4Py/baselines/test4py-baseline/test4dt/message.py`

Quando `--run_benchmark=True` (default) E o projeto está listado em
`projects.json`, a geração de testes fica limitada aos módulos dessa lista.
Call-graph e RAG continuam a analisar o projeto inteiro (necessário para
contexto), mas LLM calls só acontecem para módulos-alvo.

Sem o patch, MARTA/Test4Py-baseline gerariam testes para TODOS os ficheiros
do projeto, incluindo módulos fora dos 486 oficiais do CM. Não seria
apples-to-apples com Pynguin/CoverUp (que aceitam módulo a módulo).

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

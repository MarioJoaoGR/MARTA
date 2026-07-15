# RUNBOOK — Dia 1 pós-manutenção do Deucalion

Plano de execução por ordem. Objetivo: quando o Deucalion voltar, ser **só
disparar** — cada passo já pensado e validado no que era validável sem cluster.

## Estado atual (2026-07-15) — o que já fizemos e o que falta

| Tarefa | Estado | Nota |
|---|---|---|
| 16B marta — geração | ✅ | 27 projetos |
| 16B marta — cobertura | ✅ | **51.9% stmt / 29.6% branch** (per-módulo-alvo, fix `d39e1e1d`) |
| 16B pynguin — geração | ✅ | 417 ok / 10 timeout / 59 limites do Pynguin |
| 16B pynguin — cobertura | ✅/⏳ | **60.2% / 40.9%** (25 proj); re-correr JUSTO (`d4263e6f`, falhados→0%) |
| **16B baseline — re-run** | ⏳ a correr | job 1753101 (fix pylint `f8cf8e1` deployado) |
| Cobertura baseline (16B) | ⛔ | depois do re-run acabar |
| **mutmut (todos)** | ⛔ **PRÓXIMO** | é o eixo onde a MARTA deve ganhar (deteção de faltas) |
| **236B marta+baseline** | ⛔ por correr | pynguin NÃO (independente do modelo) |
| black — cobertura | ⚠️ | `no_target_match` nos 2 tools — investigar (chaves do coverage.json) |

**DESCOBERTA-CHAVE:** na cobertura crua o **Pynguin > MARTA** (é o objetivo-de-vida do SBST).
A tese da MARTA tem de assentar em **mutation score + vencer o baseline**, não em cobertura.
A cobertura estava a ser medida sobre o pacote inteiro (diluída) → corrigido p/ módulos-alvo.

Paths fixos:
```
MARTA_ROOT=/projects/F202407648IACDCF2/mario/MARTA
RES16=/projects/F202407648IACDCF2/mario/results/deepseek-coder-v2_16b
RES236=/projects/F202407648IACDCF2/mario/results/deepseek-coder-v2_236b
SIF=/projects/F202407648IACDCF2/mario/containers/marta_benchmark.sif
PYDEPS=/projects/F202407648IACDCF2/mario/pydeps
```

---

## FASE 0 — Pré-voo (verificar ANTES de lançar seja o que for)

```bash
# 0.1 Deucalion vivo?
squeue -u $USER ; sinfo -p normal-a100-40,normal-a100-80 | head

# 0.2 [Deucalion] Atualizar a MARTA (traz o fix do auto-chain CHAIN_SCRIPT + os
#     scripts novos: run_mutmut.py, measure_pynguin_coverage.py)
cd $MARTA_ROOT && git pull
git log --oneline -6   # confirmar: 15b7dc17 (auto-chain), ea0a2b5d/15d2dee9 (mutmut), 6faa4bf3 (pynguin cov)
```

**0.3 [NO TEU MAC — não no Deucalion] Deploy do test4dt.** O `test4dt/` é repo
aninhado e gitignored → NÃO vem no `git pull`. Tem o fix crítico do pylint
(`f8cf8e1`) e a contagem de tokens. Copia do Mac:
```bash
# no Terminal do Mac (a shell do agente não faz ssh):
cd ~/Desktop/GECAD/Test4Py
scp -r baselines/test4py-baseline/test4dt/*.py \
  deucalion:/projects/F202407648IACDCF2/mario/MARTA/baselines/test4py-baseline/test4dt/
```

```bash
# 0.4 [Deucalion] Confirmar que o fix do pylint está deployado (senão o baseline
#     volta a sair VAZIO). Deve mostrar PYTHONPATH=...:$PYTHONPATH (não override):
grep -n 'PYTHONPATH=' $MARTA_ROOT/baselines/test4py-baseline/test4dt/testcase.py

# 0.5 Modelos puxados? (persistem em /projects/ollama_models mas confirmar)
#     Se faltar o 236b: pré-pull num nó dev-x86 (tem internet; compute node não).
salloc -A f202407648iacdcf2x --partition=dev-x86 --time=1:00:00 --nodes=1 --mem=16G
singularity exec --bind /projects/F202407648IACDCF2/mario/ollama_models:/data/ollama \
  --env OLLAMA_MODELS=/data/ollama $SIF bash -c 'ollama serve & sleep 10; ollama list'
# se faltar: ollama pull deepseek-coder-v2:236b   (~132GB, demora)
exit

# 0.6 Instalar mutmut em pydeps (para a Fase 4). Precisa de internet → dev-x86.
#     (podes juntar ao passo 0.5 no mesmo salloc)
singularity exec --bind $PYDEPS:/data/pydeps $SIF \
  /opt/conda/envs/test4py_env/bin/pip install --target /data/pydeps/marta 'mutmut<3'
```

---

## FASE 1 — Re-run do baseline 16B (o que ficou vazio)

⚠️ **GOTCHA:** o `state.json` antigo marca `test4py_baseline/<proj>` como `ok`
(apesar de vazio) → o harness SALTA-os. Tens de limpar SÓ essas entradas.

```bash
STATE=$RES16/harness/state.json
cp "$STATE" "$STATE.bak_$(date +%s)"                       # backup primeiro
# remove só as entradas do baseline; mantém marta/pynguin intactos:
jq 'with_entries(select(.key | startswith("test4py_baseline/") | not))' \
   "$STATE" > "$STATE.new" && mv "$STATE.new" "$STATE"
# opcional: limpar os outputs vazios do baseline
rm -rf $RES16/Results_Test4PyBaseline/*
# confirmar que já não há test4py_baseline no state:
jq 'keys[]' "$STATE" | grep test4py_baseline | wc -l    # deve dar 0
```

A cache de análise do baseline (grafo + análise LLM) vive em
`Results_Test4PyBaseline/<proj>/` — se a apagaste no passo acima, o re-run
re-analisa de raiz (lento, ~106h). Se quiseres reusar a cache e ir **só à
geração** (muito mais rápido), NÃO apagues a pasta e confia no `[CACHE HIT]`;
limpa apenas o state.

Lançar (só o baseline; MODEL faz default para 16b):
```bash
cd $MARTA_ROOT
export TOOLS=test4py_baseline
export PROJECTS=            # vazio = os 27
sbatch --export=ALL deucalion/run_benchmark.sh
```

---

## FASE 2 — 236B (marta + baseline)

Pode correr **em paralelo com a Fase 1**: escreve noutro results dir
(`deepseek-coder-v2_236b`) → **sem race** no state.json. (Nunca dois jobs no
MESMO results dir.)

**DECISÃO (tua):** 27 projetos ≈ **21-27 dias** (throughput ~3× menor, MoE).
Recomendação: primeira passagem num **subset representativo** (5-7 médios) e
estender depois. Escolhe em `PROJECTS`.

```bash
cd $MARTA_ROOT
export TOOLS=marta,test4py_baseline          # pynguin NÃO (independente do modelo)
export PROJECTS=codetiming,apimd,PySnooper,flutes,mimesis   # exemplo de subset; vazio = 27
sbatch --export=ALL deucalion/run_benchmark_236b.sh
```

O auto-chain já preserva `a100-80/gpus=4/mem=400G` (fix `CHAIN_SCRIPT`) — a
continuação NÃO cai para a partição errada. Confirma na 1ª continuação:
`squeue -u $USER -o '%.10i %.20j %.15P %.6D %m'` (partição = normal-a100-80).

---

## FASE 3 — Cobertura do Pynguin (16B)  [CPU, num nó via salloc — NÃO na login node]

O Pynguin não deixa `coverage.json`. Mede com o script. ⚠️ CORRE NUM NÓ (os
testes fuzzed podem rebentar memória) e usa o env `test4py_env` (é onde estão o
coverage+pytest, via pydeps/marta):
```bash
salloc -A f202407648iacdcf2x --partition=dev-x86 --time=4:00:00 --cpus-per-task=16 --mem=64G

singularity exec \
  --bind $MARTA_ROOT:/opt/marta --bind $RES16:/data/results \
  --bind $PYDEPS:/data/pydeps \
  --env USER_PYTHON_PATH=/opt/conda/envs/test4py_env/bin/python \
  --env PYTHONPATH=/data/pydeps/sut:/data/pydeps/marta \
  --env COV_TIMEOUT=900 \
  $SIF /opt/conda/envs/test4py_env/bin/python \
  /opt/marta/scripts/measure_pynguin_coverage.py /data/results
# PYTHONPATH TEM de incluir /data/pydeps/marta (coverage+pytest vivem lá, não no env).
# ONLY_PROJECTS=a,b,c p/ sanity-check rápido. saída: RES16/pynguin_coverage.csv
# projetos onde o Pynguin falhou em tudo contam 0% (justo); no_target_match = investigar.
```

---

## FASE 4 — mutmut (mutation score)  [CPU, paralelo aos runs GPU]

Só precisa dos testes já gerados → arranca com marta+pynguin 16B logo; baseline
e 236B à medida que saem. **Validar dia-1 antes dos 27×3:**

```bash
BASE="singularity exec --bind $MARTA_ROOT:/opt/marta --bind $RES16:/data/results --bind $PYDEPS:/data/pydeps \
  --env USER_PYTHON_PATH=/opt/conda/envs/test4py_env/bin/python --env PYTHONPATH=/data/pydeps/marta:/data/pydeps/sut \
  $SIF /opt/conda/envs/test4py_env/bin/python /opt/marta/scripts/run_mutmut.py --results /data/results"

# 4.1 mutmut chamável?
$BASE --tool marta --project codetiming --dry-run     # confirma paths_to_mutate + testes
# 4.2 um par real pequeno:
$BASE --tool marta --project codetiming               # status ok, total>0, score preenchido
# 4.3 tudo (marta+pynguin+baseline 16B):
$BASE                                                  # saída: RES16/mutmut.csv
```
Se `total=0` sempre → paths errados; se `score≈0%` sempre → PYTHONPATH do scratch
não ganha (testes veem source original). Ver checklist no fim de `run_mutmut.py`.

---

## FASE 5 — Consolidação

```bash
# cobertura + executability + tokens + tempo (marta/baseline):
python3 $MARTA_ROOT/scripts/consolidate_16b.py $RES16
# + juntar pynguin_coverage.csv e mutmut.csv (à mão ou script de merge)
# repetir consolidate para o 236B quando terminar:
python3 $MARTA_ROOT/scripts/consolidate_16b.py $RES236
```

---

## GOTCHAS (não repetir os erros já pagos)

- **NUNCA** dois jobs a escrever o MESMO `harness/state.json` (race → um
  sobrescreve o outro). 16B e 236B em results dirs diferentes = ok.
- **Vírgula no `--export`**: usar `export VAR=...; sbatch --export=ALL` — NÃO
  `--export=ALL,TOOLS=a,b` (a vírgula parte e só apanha o 1º). O README antigo
  mostra a forma errada; ignora-a.
- **test4dt não vem no git pull** (repo aninhado) → scp do Mac (passo 0.3).
- **Baseline vazio** = fix do pylint não deployado → passo 0.4.
- **236B mem/particao**: o wrapper já tem gpus=4/mem=400G; 200G dava OOM.
- **Compute nodes sem internet**: pull de modelos / pip só em dev-x86.
```

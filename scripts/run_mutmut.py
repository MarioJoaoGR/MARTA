#!/usr/bin/env python3
"""Mutation testing (mutmut) por (tool, projeto) — mede fault-detection.

Cobertura diz que linhas o teste EXECUTA; mutation score diz se o teste
DETETA faltas (mata mutantes). Muta APENAS os módulos-alvo (projects.json),
não o repo inteiro → viável (menos mutantes) e mais significativo (mede
deteção no código realmente sob teste).

Por cada (tool, projeto):
  1. Copia a source do projeto p/ um scratch isolado. O mutmut altera os
     ficheiros in-place → NUNCA mutar a source partilhada (/opt/marta/...).
  2. Pré-voo verde: corre pytest ficheiro-a-ficheiro e fica só com os que
     passam 100%. O mutmut aborta se o baseline não for verde; apesar da
     quarentena remover testes falhados, o ambiente do mutmut pode reintroduzir
     falhas (imports, rootdir), por isso filtramos aqui à cabeça.
  3. setup.cfg: paths_to_mutate = ficheiros dos módulos-alvo (no scratch);
     runner = pytest sobre os testes verdes copiados p/ scratch/_mut_tests,
     com PYTHONPATH=scratch_import_root → os testes importam a source MUTADA
     (do scratch), não a original.
  4. mutmut run (com timeout por projeto).
  5. mutmut result-ids {killed,survived,timeout,suspicious} → mutation score
     = killed / (killed+survived+timeout+suspicious).

CORRE DENTRO DO CONTAINER (precisa de pytest + o SUT + mutmut):
  # envs conda estão no .sif (read-only) → instalar mutmut em pydeps via --target
  # (como as outras deps); invoca-se por `python -m mutmut` (ver MUTMUT_CMD):
  singularity exec --bind $PYDEPS:/data/pydeps $SIF \
    /opt/conda/envs/test4py_env/bin/pip install --target /data/pydeps/marta 'mutmut<3'
  singularity exec ... python scripts/run_mutmut.py --tool marta --project codetiming

Args:
  --tool X            (marta|test4py_baseline|pynguin) — default: os 3
  --project Y         um só projeto — default: os 27
  --results DIR       default /data/results/deepseek-coder-v2_16b
  --dry-run           só imprime paths_to_mutate/testes (não corre mutmut)

⚠️ DRAFT — VALIDAR DIA 1 com `--tool marta --project codetiming --dry-run` e
   depois sem --dry-run, ANTES dos 27×3. Ver CHECKLIST no fim do ficheiro.
"""
import argparse
import csv
import glob
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
PY = os.getenv("USER_PYTHON_PATH", sys.executable)
# Invocação do mutmut. No Deucalion os envs conda estão no .sif (read-only) → o
# mutmut instala-se em pydeps via `pip install --target ... 'mutmut<3'`, onde NÃO
# há console-script. Por isso invoca-se como módulo: `python -m mutmut`. Override:
# MUTMUT_BIN="/caminho/para/mutmut" (split por espaços) se preferires o executável.
MUTMUT_CMD = os.getenv("MUTMUT_BIN", "").split() or [PY, "-m", "mutmut"]
GREEN_TIMEOUT = int(os.getenv("MUTMUT_GREEN_TIMEOUT", "90"))    # s por ficheiro de teste
MUTMUT_TIMEOUT = int(os.getenv("MUTMUT_TIMEOUT", "10800"))      # s por projeto (3h)
SCRATCH = os.getenv("MUTMUT_SCRATCH", "/data/results/_mutmut_scratch")

TOOL_DIRS = {
    "marta": "Results_MARTA",
    "test4py_baseline": "Results_Test4PyBaseline",
    "pynguin": "Results_Pynguin",
}


def import_root(project_path, source_path):
    """Raiz de sys.path (== _import_root do run_benchmark.py)."""
    src_full = os.path.join(project_path, source_path) if source_path else project_path
    if source_path and not os.path.exists(os.path.join(src_full, "__init__.py")):
        return src_full
    return project_path


def module_files(project_path, source_path, modules):
    """Módulos dotted → paths de ficheiro RELATIVOS ao project_path (== ao scratch)."""
    iroot = import_root(project_path, source_path)
    iroot_rel = os.path.relpath(iroot, project_path)
    out = []
    for m in modules:
        base = os.path.join(iroot_rel, m.replace(".", os.sep))
        for cand in (base + ".py", os.path.join(base, "__init__.py")):
            if os.path.exists(os.path.join(project_path, cand)):
                out.append(cand)
                break
    return out, iroot_rel


def locate_tests(tool, proj, results):
    """(test_dir, [test_files absolutos]).

    Glob recursivo p/ todos os tools: a MARTA/baseline gravam em
    Test4DT_tests_<SAFE_MODEL>/ (com sufixo do modelo), não 'Test4DT_tests'. Os
    ficheiros em quarentena chamam-se 'quarantined_*.py' → não batem em test_*.py.
    """
    base = os.path.join(results, TOOL_DIRS[tool], proj)
    files = glob.glob(os.path.join(base, "**", "test_*.py"), recursive=True)
    return base, sorted(files)


def green_filter(test_files, scratch, scratch_iroot, env):
    """Corre cada ficheiro de teste; devolve os que passam 100% (returncode 0)."""
    green = []
    for tf in test_files:
        cmd = [PY, "-m", "pytest", tf, "-q", "-c", "/dev/null",
               "--rootdir", scratch, "-p", "no:cacheprovider"]
        try:
            r = subprocess.run(cmd, cwd=scratch, env=env,
                               capture_output=True, timeout=GREEN_TIMEOUT)
            if r.returncode == 0:
                green.append(tf)
        except subprocess.TimeoutExpired:
            pass
    return green


def count_ids(cat, scratch, env):
    r = subprocess.run([*MUTMUT_CMD, "result-ids", cat], cwd=scratch, env=env,
                       capture_output=True, text=True)
    # IDs vêm um por token; se o mutmut abortou, sai vazio (0). Não confiar em
    # stdout com texto de ajuda → filtrar tokens que não parecem IDs.
    return len([t for t in r.stdout.split() if t.strip().isdigit()])


def runner_cmd(scratch):
    """O comando EXATO que o mutmut vai usar como runner (ver setup.cfg).

    A validação do baseline TEM de usar este mesmo comando: validar com um
    comando diferente (ex.: sem -x) pode dar verde onde o runner dá vermelho →
    o mutmut aborta e devolve 0 mutantes (ex.: tqdm, err='1 failed, 51 passed').
    """
    return [PY, "-m", "pytest", "_mut_tests", "-x", "-q", "-c", "/dev/null",
            f"--rootdir={scratch}", "-p", "no:cacheprovider"]


def suite_green(scratch, env, runs=2):
    """Corre a suite TODA junta, como o mutmut faz. → (ok, [ficheiros que falham]).

    O filtro por-ficheiro NÃO chega: testes que passam isolados falham em conjunto
    (poluição de estado, ordem, fixtures). Se o baseline não for verde o mutmut
    ABORTA e devolve lixo — era a causa dos total=8/total=0 (ex.: tornado, 286
    passed + 1 failed → mutmut não produzia nada).

    runs=2: repete a validação para apanhar testes FLAKY (passam à 1ª, falham à
    2ª — típico em código com timing/barras de progresso, ex.: tqdm). Basta
    falhar numa das passagens para o ficheiro ser removido.
    """
    bad = set()
    for _ in range(runs):
        try:
            r = subprocess.run(runner_cmd(scratch), cwd=scratch, env=env,
                               capture_output=True, text=True,
                               timeout=GREEN_TIMEOUT * 10)
        except subprocess.TimeoutExpired:
            return False, sorted(bad)
        if r.returncode == 0:
            continue
        for line in ((r.stdout or "") + (r.stderr or "")).splitlines():
            if line.startswith(("FAILED ", "ERROR ")):
                parts = line.split()
                if len(parts) > 1:
                    bad.add(os.path.basename(parts[1].split("::")[0]))
    return (not bad), sorted(bad)


def run_one(tool, proj, cm, projects, results, dry):
    if proj not in cm:
        return {"status": "not_in_cm"}
    info = cm[proj]
    ppath, spath = info["project_path"], info.get("source_path", "")
    mods = projects.get(proj, [])
    mut_paths, iroot_rel = module_files(ppath, spath, mods)
    if not mut_paths:
        return {"status": "no_target_files"}
    _, test_files = locate_tests(tool, proj, results)
    if not test_files:
        return {"status": "no_tests"}

    if dry:
        print(f"    paths_to_mutate ({len(mut_paths)}): {mut_paths[:4]}"
              f"{' ...' if len(mut_paths) > 4 else ''}")
        print(f"    testes ({len(test_files)}): {[os.path.basename(t) for t in test_files[:4]]}"
              f"{' ...' if len(test_files) > 4 else ''}")
        return {"status": "dry", "n_mut_files": len(mut_paths), "n_tests": len(test_files)}

    if not os.path.exists(ppath):
        return {"status": "project_path_missing"}
    scratch = os.path.join(SCRATCH, tool, proj)
    shutil.rmtree(scratch, ignore_errors=True)
    shutil.copytree(ppath, scratch, symlinks=True)
    scratch_iroot = os.path.join(scratch, iroot_rel)

    env = os.environ.copy()
    prev = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = f"{scratch_iroot}:{prev}" if prev else scratch_iroot

    # pré-voo verde
    green = green_filter(test_files, scratch, scratch_iroot, env)
    if not green:
        return {"status": "no_green_tests", "n_tests": len(test_files)}

    # copiar testes verdes p/ scratch/_mut_tests (nomes únicos)
    mtests = os.path.join(scratch, "_mut_tests")
    os.makedirs(mtests, exist_ok=True)
    open(os.path.join(mtests, "__init__.py"), "w").close()
    with open(os.path.join(mtests, "conftest.py"), "w") as f:
        f.write(f"import sys\nsys.path.insert(0, {scratch_iroot!r})\n")
    seen = set()
    for tf in green:
        name = os.path.basename(tf)
        i = 0
        while name in seen:
            i += 1
            name = f"{i}_{os.path.basename(tf)}"
        seen.add(name)
        shutil.copy(tf, os.path.join(mtests, name))

    # BASELINE VERDE COM A SUITE JUNTA — o mutmut aborta se os testes não passarem
    # todos juntos. Vai removendo os ficheiros que falham em conjunto até ficar
    # verde (max 6 iterações). Sem isto, 1 teste mau em 287 deitava tudo abaixo.
    # GREEN_ITERS alto: com -x (igual ao runner do mutmut) o pytest para na 1ª
    # falha → cada iteração remove ~1 ficheiro. 6 iterações eram poucas para
    # suites grandes; 25 dá margem sem custo (cada iteração é rápida).
    dropped = []
    for _ in range(int(os.getenv("MUTMUT_GREEN_ITERS", "25"))):
        ok, bad = suite_green(scratch, env)
        if ok:
            break
        if not bad:
            # falhou SEM produzir linhas FAILED/ERROR parseáveis (crash de
            # coleção, erro de import em massa) → não há o que remover.
            return {"status": "suite_not_green", "green_tests": len(green),
                    "dropped": len(dropped), "n_mut_files": len(mut_paths)}
        for b in bad:
            p = os.path.join(mtests, b)
            if os.path.exists(p):
                os.remove(p)
                dropped.append(b)
    else:
        return {"status": "suite_not_green_maxiter", "green_tests": len(green),
                "dropped": len(dropped), "n_mut_files": len(mut_paths)}
    kept = len(glob.glob(os.path.join(mtests, "test_*.py")))
    if kept == 0:
        return {"status": "no_green_tests", "n_tests": len(test_files)}

    # setup.cfg do mutmut — runner_cmd() garante que é EXATAMENTE o comando com
    # que validámos o baseline verde acima (senão o mutmut aborta com o baseline
    # vermelho e devolve 0 mutantes).
    runner = " ".join(runner_cmd(scratch))
    with open(os.path.join(scratch, "setup.cfg"), "w") as f:
        f.write("[mutmut]\n")
        f.write("paths_to_mutate=" + ",".join(mut_paths) + "\n")
        # tests_dir EXPLÍCITO: sem isto, o mutmut adivinha procurando uma pasta
        # 'tests/' no cwd e aborta com FileNotFoundError se não existir. Os
        # projetos que 'funcionavam' tinham uma pasta tests/ própria copiada do
        # source; os que não têm (apimd, docstring_parser) falhavam. Apontar aos
        # NOSSOS testes remove a adivinhação e é correto para todos.
        f.write("tests_dir=_mut_tests\n")
        f.write("runner=" + runner + "\n")

    partial = False
    try:
        run = subprocess.run([*MUTMUT_CMD, "run"], cwd=scratch, env=env,
                             capture_output=True, text=True, timeout=MUTMUT_TIMEOUT)
    except subprocess.TimeoutExpired:
        partial = True
        run = None
    except FileNotFoundError:
        return {"status": "mutmut_not_found", "hint": " ".join(MUTMUT_CMD)}

    counts = {c: count_ids(c, scratch, env)
              for c in ("killed", "survived", "timeout", "suspicious")}
    denom = sum(counts.values())
    score = 100 * counts["killed"] / denom if denom else None
    result = {
        "status": "partial" if partial else "ok",
        "killed": counts["killed"], "survived": counts["survived"],
        "timeout_mut": counts["timeout"], "suspicious": counts["suspicious"],
        "total": denom, "score": score,
        # green_tests = os que ficaram DEPOIS de garantir a suite verde em conjunto
        "green_tests": kept, "dropped": len(dropped), "n_mut_files": len(mut_paths),
    }
    # total=0 apesar de mutar ficheiros reais = o mutmut run falhou (parse/erro)
    # e o capture escondeu-o. Marca status='run_error' e guarda a última linha do
    # stderr → diagnóstico sem re-correr às cegas (ex.: tornado/ansible, 2026-07).
    if denom == 0 and not partial and run is not None:
        tail = (run.stderr or run.stdout or "").strip().splitlines()
        result["status"] = "run_error"
        result["err"] = (tail[-1][:160] if tail else f"rc={run.returncode}")
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", default="/data/results/deepseek-coder-v2_16b")
    ap.add_argument("--tool", choices=list(TOOL_DIRS))
    ap.add_argument("--project")
    ap.add_argument("--cm", default=os.path.join(HERE, "cm_benchmark.json"))
    ap.add_argument("--projects", default=os.path.join(REPO, "projects.json"))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    cm = json.load(open(args.cm))
    projects = json.load(open(args.projects))
    tools = [args.tool] if args.tool else list(TOOL_DIRS)
    projs = [args.project] if args.project else sorted(projects)
    out = os.path.join(args.results, "mutmut.csv")
    cols = ["tool", "project", "status", "score", "killed", "survived",
            "timeout_mut", "suspicious", "total", "green_tests", "dropped",
            "n_mut_files", "err", "hint"]

    # RESUME: salta combos já em mutmut.csv (mutmut é lento; sobrevive ao walltime).
    done = set()
    if not args.dry_run and os.path.exists(out):
        for row in csv.DictReader(open(out)):
            done.add((row["tool"], row["project"]))

    for tool in tools:
        for proj in projs:
            if (tool, proj) in done:
                print(f"→ {tool}/{proj} … já feito (skip)")
                continue
            print(f"→ {tool}/{proj}")
            r = run_one(tool, proj, cm, projects, args.results, args.dry_run)
            print(f"    {r}")
            sys.stdout.flush()
            if not args.dry_run:
                # append imediato → progresso persiste mesmo se o job morrer a meio
                new = not os.path.exists(out)
                with open(out, "a", newline="") as f:
                    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
                    if new:
                        w.writeheader()
                    w.writerow({"tool": tool, "project": proj, **r})

    if not args.dry_run and os.path.exists(out):
        rows = list(csv.DictReader(open(out)))
        print(f"\nCSV: {out}")
        for tool in tools:
            tr = [r for r in rows if r["tool"] == tool and r.get("score") not in (None, "", "None")]
            if tr:
                print(f"  {tool:18}: mutation score médio "
                      f"{sum(float(r['score']) for r in tr)/len(tr):.1f}%  ({len(tr)} proj)")


if __name__ == "__main__":
    main()

# ─────────────────────────────────────────────────────────────────────────────
# CHECKLIST DE VALIDAÇÃO (DIA 1, antes dos 27×3):
#   1. mutmut instalado e chamável (via módulo, com pydeps no PYTHONPATH):
#        pip install --target /data/pydeps/marta 'mutmut<3'
#        PYTHONPATH=/data/pydeps/marta python -m mutmut version   # deve imprimir versão
#      Se `python -m mutmut` falhar, instalar num env writable e
#        export MUTMUT_BIN=/caminho/para/mutmut
#   2. Paths certos (sem correr mutmut):
#        python scripts/run_mutmut.py --tool marta --project codetiming --dry-run
#      → confirmar paths_to_mutate = codetiming/_timers.py e testes existem.
#   3. Um par real pequeno:
#        python scripts/run_mutmut.py --tool marta --project codetiming
#      → status 'ok', total>0, score preenchido. Se total=0 → paths_to_mutate
#        errado ou mutmut não encontrou os módulos.
#   4. Confirmar que os testes veem a source MUTADA (senão survived=100%):
#      sanity — se score sempre ~0%, o PYTHONPATH do scratch não está a ganhar.
#   5. `mutmut result-ids <cat>` existe nesta versão? Se falhar, usar
#      `mutmut results` / `mutmut junitxml` (ajustar count_ids).
# ─────────────────────────────────────────────────────────────────────────────

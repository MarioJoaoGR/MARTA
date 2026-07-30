#!/usr/bin/env python3
"""Mutation testing POR MÓDULO, em paralelo — torna o ansible viável.

PROBLEMA DA ABORDAGEM ANTERIOR (run_mutmut.py):
o mutmut corre a suite INTEIRA por cada mutante. No ansible (237 módulos-alvo,
~50k mutantes, suite de 1653 ficheiros) isso é inviável: os 3 tools ficaram em
`partial` ou `run_error`, com denominadores diferentes (marta 996, pynguin 1937)
→ scores incomparáveis.

ABORDAGEM AQUI: para cada módulo-alvo M, mutar SÓ M e correr SÓ os testes que
visam M (os nomes dos ficheiros contêm o módulo nas 3 ferramentas). Ganhos:
  • suite por mutante cai de ~1600 para ~10 ficheiros  → ~100x mais rápido
  • módulos independentes → paraleliza pelos CPUs do nó → outro ~16-32x
  • MAIS CORRETO: um mutante em A deve ser morto por testes de A, não por um
    teste de B que por acaso importa A.

Módulos SEM testes contam com todos os seus mutantes SOBREVIVIDOS (não são
excluídos — excluí-los inflacionaria o score de quem gera menos testes).

O score do projeto = Σ killed / Σ (killed+survived+timeout+suspicious) sobre
todos os módulos-alvo → denominador comparável entre tools.

Uso (dentro do container, nó CPU):
  python scripts/run_mutmut_permodule.py --results /data/results --tool marta
  MUT_WORKERS=16  MUT_MODULE_TIMEOUT=600  ONLY_PROJECTS=ansible
"""
import argparse
import csv
import glob
import json
import multiprocessing as mp
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
PY = os.getenv("USER_PYTHON_PATH", sys.executable)
MUTMUT_CMD = os.getenv("MUTMUT_BIN", "").split() or [PY, "-m", "mutmut"]
WORKERS = int(os.getenv("MUT_WORKERS", str(min(16, mp.cpu_count()))))
MODULE_TIMEOUT = int(os.getenv("MUT_MODULE_TIMEOUT", "1800"))   # por MÓDULO
GREEN_TIMEOUT = int(os.getenv("MUT_GREEN_TIMEOUT", "120"))
SCRATCH = os.getenv("MUTMUT_SCRATCH", "/data/results/_mut_pm")

TOOL_DIRS = {
    "marta": "Results_MARTA",
    "test4py_baseline": "Results_Test4PyBaseline",
    "pynguin": "Results_Pynguin",
}


def canon(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def import_root_rel(project_path, source_path):
    """Caminho (relativo ao projeto) da raiz de import — 'lib' no ansible,
    'src' no black, '.' nos projetos normais."""
    src = os.path.join(project_path, source_path) if source_path else project_path
    if source_path and not os.path.exists(os.path.join(src, "__init__.py")):
        return source_path
    return "."


def module_file(project_path, iroot_rel, module):
    base = os.path.join(iroot_rel, module.replace(".", os.sep))
    for cand in (base + ".py", os.path.join(base, "__init__.py")):
        if os.path.exists(os.path.join(project_path, cand)):
            return cand
    return None


def tests_by_module(test_files, modules):
    """Atribui cada ficheiro de teste ao módulo-alvo que melhor casa.

    Os 3 tools põem o caminho do módulo no nome do ficheiro:
      marta     test_lib_ansible_cli_adhoc_AdHocCLI_init_0.py
      baseline  test_lib_ansible_cli_adhoc_tAdHocCLI_init0.py
      pynguin   test_ansible_cli_adhoc.py
    Compara-se em forma canónica (minúsculas, sem separadores) e escolhe-se o
    módulo com o match MAIS LONGO, para 'a.b' não roubar testes de 'a.bc'.
    """
    cmods = sorted(((canon(m), m) for m in modules), key=lambda x: -len(x[0]))
    out = {m: [] for m in modules}
    for f in test_files:
        cb = canon(os.path.basename(f))
        for cm, m in cmods:
            if cm and cm in cb:
                out[m].append(f)
                break
    return out


def _count(cat, cwd, env):
    r = subprocess.run([*MUTMUT_CMD, "result-ids", cat], cwd=cwd, env=env,
                       capture_output=True, text=True)
    return len([t for t in r.stdout.split() if t.strip().isdigit()])


def _prune_green(mtests, scratch, env):
    """Deixa no _mut_tests só o que passa em conjunto. Devolve (n_kept, n_dropped).

    O mutmut aborta se o baseline não for verde. Deteta-se sem -x (todas as
    falhas de uma vez) e verifica-se com -x (o comando exato do runner)."""
    dropped = 0
    for _ in range(8):
        for stop_first in (False, True):
            cmd = [PY, "-m", "pytest", "_mut_tests", "-q", "-c", "/dev/null",
                   f"--rootdir={scratch}", "-p", "no:cacheprovider"]
            if stop_first:
                cmd.insert(4, "-x")
            try:
                r = subprocess.run(cmd, cwd=scratch, env=env, capture_output=True,
                                   text=True, timeout=GREEN_TIMEOUT)
            except subprocess.TimeoutExpired:
                return 0, dropped
            if r.returncode == 0:
                if stop_first:
                    return len(glob.glob(os.path.join(mtests, "test_*.py"))), dropped
                continue
            bad = set()
            for line in ((r.stdout or "") + (r.stderr or "")).splitlines():
                if line.startswith(("FAILED ", "ERROR ")):
                    p = line.split()
                    if len(p) > 1:
                        bad.add(os.path.basename(p[1].split("::")[0]))
            if not bad:      # crash sem falhas parseáveis → isolar por coleção
                for f in sorted(glob.glob(os.path.join(mtests, "test_*.py"))):
                    c = [PY, "-m", "pytest", "--collect-only", "-q", "-c", "/dev/null",
                         f"--rootdir={scratch}", "-p", "no:cacheprovider", f]
                    try:
                        if subprocess.run(c, cwd=scratch, env=env, capture_output=True,
                                          timeout=60).returncode != 0:
                            bad.add(os.path.basename(f))
                    except subprocess.TimeoutExpired:
                        bad.add(os.path.basename(f))
                if not bad:
                    return 0, dropped
            for b in bad:
                p = os.path.join(mtests, b)
                if os.path.exists(p):
                    os.remove(p)
                    dropped += 1
            break
    return len(glob.glob(os.path.join(mtests, "test_*.py"))), dropped


def do_module(task):
    """Muta UM módulo no scratch do worker. Devolve as contagens."""
    scratch, iroot_rel, module, mfile, tests = task
    mtests = os.path.join(scratch, "_mut_tests")
    shutil.rmtree(mtests, ignore_errors=True)
    os.makedirs(mtests, exist_ok=True)
    scratch_iroot = os.path.join(scratch, iroot_rel)
    open(os.path.join(mtests, "__init__.py"), "w").close()
    with open(os.path.join(mtests, "conftest.py"), "w") as f:
        f.write(f"import sys\nsys.path.insert(0, {scratch_iroot!r})\n")

    env = os.environ.copy()
    prev = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = f"{scratch_iroot}:{prev}" if prev else scratch_iroot

    # cache limpa → as contagens seguintes são SÓ deste módulo
    for p in glob.glob(os.path.join(scratch, ".mutmut-cache*")):
        os.remove(p)

    seen = set()
    for t in tests:
        name = os.path.basename(t)
        i = 0
        while name in seen:
            i += 1
            name = f"{i}_{os.path.basename(t)}"
        seen.add(name)
        shutil.copy(t, os.path.join(mtests, name))

    kept, dropped = (0, 0)
    if tests:
        kept, dropped = _prune_green(mtests, scratch, env)

    runner = (f"{PY} -m pytest _mut_tests -x -q -c /dev/null "
              f"--rootdir={scratch} -p no:cacheprovider")
    with open(os.path.join(scratch, "setup.cfg"), "w") as f:
        f.write(f"[mutmut]\npaths_to_mutate={mfile}\ntests_dir=_mut_tests\n"
                f"runner={runner}\n")

    status = "ok"
    if kept == 0:
        # Sem testes utilizáveis para este módulo, os mutantes têm de contar como
        # SOBREVIVIDOS — excluir o módulo favoreceria quem gera menos testes.
        # Mas se o baseline não for verde o mutmut ABORTA e não conta nada (visto
        # no baseline/sty: total 54 em vez de 62, o que INFLACIONAVA o score).
        # Solução: um teste dummy que passa sempre → baseline verde, o mutmut
        # corre, e nenhum mutante é detetado (o dummy não importa o módulo) →
        # todos sobrevivem. É exatamente a semântica correta.
        status = "no_tests" if not tests else "no_green"
        for f in glob.glob(os.path.join(mtests, "test_*.py")):
            os.remove(f)
        with open(os.path.join(mtests, "test_dummy.py"), "w") as f:
            f.write("def test_dummy():\n    assert True\n")
    try:
        subprocess.run([*MUTMUT_CMD, "run"], cwd=scratch, env=env,
                       capture_output=True, timeout=MODULE_TIMEOUT)
    except subprocess.TimeoutExpired:
        status = "partial"
    except FileNotFoundError:
        return dict(module=module, status="mutmut_not_found", killed=0, total=0,
                    kept=kept, dropped=dropped)

    c = {k: _count(k, scratch, env) for k in
         ("killed", "survived", "timeout", "suspicious")}
    return dict(module=module, status=status, killed=c["killed"],
                total=sum(c.values()), kept=kept, dropped=dropped)


def run_project(tool, proj, info, modules, results):
    ppath = info["project_path"]
    iroot_rel = import_root_rel(ppath, info.get("source_path", ""))
    base = os.path.join(results, TOOL_DIRS[tool], proj)
    tests = sorted(f for f in glob.glob(os.path.join(base, "**", "test_*.py"),
                                        recursive=True)
                   if "OLD" not in f and "quarantine" not in f
                   and "_cov_" not in f and "_mut_tests" not in f)
    tmap = tests_by_module(tests, modules)
    tasks_src = []
    for m in modules:
        mf = module_file(ppath, iroot_rel, m)
        if mf:
            tasks_src.append((m, mf, tmap[m]))
    if not tasks_src:
        return dict(status="no_target_files", score=None, killed=0, total=0,
                    n_mod=0, n_tests=len(tests), modules_partial=0)

    nw = max(1, min(WORKERS, len(tasks_src)))
    # W cópias do source (uma por worker) — o mutmut escreve .mutmut-cache no cwd,
    # por isso processos paralelos precisam de diretórios distintos.
    wdirs = []
    for i in range(nw):
        d = os.path.join(SCRATCH, tool, proj, f"w{i}")
        if not os.path.exists(os.path.join(d, iroot_rel)):
            shutil.rmtree(d, ignore_errors=True)
            shutil.copytree(ppath, d, symlinks=True)
        wdirs.append(d)

    tasks = [(wdirs[i % nw], iroot_rel, m, mf, ts)
             for i, (m, mf, ts) in enumerate(tasks_src)]
    with mp.Pool(nw) as pool:
        res = pool.map(do_module, tasks)

    killed = sum(r["killed"] for r in res)
    total = sum(r["total"] for r in res)
    return dict(
        status="ok" if total else "no_mutants",
        score=(100 * killed / total) if total else None,
        killed=killed, total=total, n_mod=len(res), n_tests=len(tests),
        modules_partial=sum(1 for r in res if r["status"] == "partial"),
        modules_no_tests=sum(1 for r in res if r["status"] == "no_tests"),
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", default="/data/results")
    ap.add_argument("--tool", default="all")
    ap.add_argument("--project")
    ap.add_argument("--cm", default=os.path.join(HERE, "cm_benchmark.json"))
    ap.add_argument("--projects", default="/opt/marta/projects.json")
    args = ap.parse_args()

    cm = json.load(open(args.cm))
    targets = json.load(open(args.projects))
    tools = list(TOOL_DIRS) if args.tool == "all" else [args.tool]
    projs = [args.project] if args.project else sorted(targets)
    only = set(p.strip() for p in os.getenv("ONLY_PROJECTS", "").split(",") if p.strip())

    out = os.path.join(args.results, "mutmut_permodule.csv")
    cols = ["tool", "project", "status", "score", "killed", "total", "n_mod",
            "n_tests", "modules_partial", "modules_no_tests"]
    done = set()
    if os.path.exists(out):
        for r in csv.DictReader(open(out)):
            done.add((r["tool"], r["project"]))

    print(f"workers={WORKERS}  timeout/módulo={MODULE_TIMEOUT}s")
    print(f"{'tool':18} {'projeto':22} {'status':12} {'score':>7} {'killed':>8} "
          f"{'total':>8} {'#mod':>5} {'partial':>8}")
    print("-" * 96)
    for tool in tools:
        for proj in projs:
            if only and proj not in only:
                continue
            if proj not in cm or (tool, proj) in done:
                continue
            r = run_project(tool, proj, cm[proj], targets[proj], args.results)
            s = f"{r['score']:.1f}" if r.get("score") is not None else "-"
            print(f"{tool:18} {proj:22} {r['status']:12} {s:>7} {r['killed']:>8} "
                  f"{r['total']:>8} {r['n_mod']:>5} {r.get('modules_partial',0):>8}")
            sys.stdout.flush()
            new = not os.path.exists(out)
            with open(out, "a", newline="") as f:
                w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
                if new:
                    w.writeheader()
                w.writerow({"tool": tool, "project": proj, **r})
    print(f"\nCSV: {out}")


if __name__ == "__main__":
    main()

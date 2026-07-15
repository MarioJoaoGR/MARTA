#!/usr/bin/env python3
"""Mede a cobertura dos testes gerados pelo Pynguin, por projeto.

O Pynguin (SBST) não passa pelo MyCoverage do marta/baseline → não deixa
coverage.json. Este script corre `coverage.py` sobre TODOS os testes de um
projeto contra o source, para obter statement%+branch% COMPARÁVEIS aos outros
dois tools (mesma ferramenta, mesma métrica).

Espelha a lógica do MyCoverage: cwd=project_path, --branch, --source=source_path,
PYTHONPATH=import_root (raiz de import correta p/ containers ansible/lib, black/src).

CORRE DENTRO DO CONTAINER (precisa de coverage.py dos pydeps + pytest + o SUT):
  singularity exec --bind ... $SIF \\
    ENV... /opt/conda/envs/pynguin_env/bin/python scripts/measure_pynguin_coverage.py

  Args:  measure_pynguin_coverage.py <RESULTS_DIR> <CM_BENCHMARK_JSON>
  (defaults abaixo, paths do container)

⚠️ DRAFT — validar no dia 1 num projeto pequeno (codetiming) antes de correr os 27.
"""
import json
import os
import glob
import subprocess
import sys
import csv

RES = sys.argv[1] if len(sys.argv) > 1 else "/data/results/deepseek-coder-v2_16b"
CM = sys.argv[2] if len(sys.argv) > 2 else "/opt/marta/scripts/cm_benchmark.json"
PROJECTS_JSON = sys.argv[3] if len(sys.argv) > 3 else "/opt/marta/projects.json"
PY = os.getenv("USER_PYTHON_PATH", "python")
PER_PROJ_TIMEOUT = int(os.getenv("COV_TIMEOUT", "1800"))  # 30 min/projeto
TARGETS = json.load(open(PROJECTS_JSON))


def _dotted(fname):
    d = fname[:-3] if fname.endswith(".py") else fname
    d = d.replace("/", ".").replace("\\", ".").lstrip(".")
    return d[:-len(".__init__")] if d.endswith(".__init__") else d


def _matches(dotted, targets):
    return any(dotted == t or dotted.endswith("." + t) for t in targets)


def import_root(project_path, source_path):
    """Raiz de sys.path p/ importar (== _import_root do run_benchmark.py):
    container (sem __init__.py) → project_path/source_path; senão project_path."""
    src_full = os.path.join(project_path, source_path) if source_path else project_path
    if source_path and not os.path.exists(os.path.join(src_full, "__init__.py")):
        return src_full
    return project_path


def measure(proj, info):
    proj_dir = os.path.join(RES, "Results_Pynguin", proj)
    tests = sorted(glob.glob(os.path.join(proj_dir, "**", "test_*.py"), recursive=True))
    if not tests:
        return None
    project_path = info["project_path"]
    source_path = info["source_path"]
    root = import_root(project_path, source_path)

    env = os.environ.copy()
    existing = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = f"{root}:{existing}" if existing else root

    cov_dir = os.path.join(proj_dir, "_pynguin_cov")
    os.makedirs(cov_dir, exist_ok=True)
    dataf = os.path.join(cov_dir, ".coverage")
    jf = os.path.join(cov_dir, "coverage.json")
    if os.path.exists(dataf):
        os.remove(dataf)

    # coverage run --branch --source=<source> -m pytest <todos os testes do projeto>
    run = [PY, "-m", "coverage", "run", "--branch", f"--source={source_path}",
           f"--data-file={dataf}", "-m", "pytest", "--continue-on-collection-errors",
           "-q", "-p", "no:cacheprovider"] + tests
    try:
        subprocess.run(run, cwd=project_path, env=env,
                       capture_output=True, timeout=PER_PROJ_TIMEOUT)
    except subprocess.TimeoutExpired:
        return ("timeout", None, None, len(tests))

    subprocess.run([PY, "-m", "coverage", "json", f"--data-file={dataf}", "-o", jf],
                   cwd=project_path, env=env, capture_output=True)
    try:
        cj = json.load(open(jf))
    except Exception as e:
        return (f"parse_err:{e}", None, None, len(tests))
    # Cobertura só sobre os módulos-alvo (como os papers), não o source_dir inteiro:
    # o 'totals' contaria centenas de ficheiros não-alvo a 0% e diluía tudo.
    targets = TARGETS.get(proj, [])
    cl = ns = cb = nb = matched = 0
    for fname, fobj in cj.get("files", {}).items():
        if _matches(_dotted(fname), targets):
            s = fobj.get("summary", {})
            cl += s.get("covered_lines", 0)
            ns += s.get("num_statements", 0)
            cb += s.get("covered_branches", 0)
            nb += s.get("num_branches", 0)
            matched += 1
    if matched == 0:
        return ("no_target_match", None, None, len(tests))
    stmt = 100 * cl / ns if ns else 0.0
    br = 100 * cb / nb if nb else 0.0
    return ("ok", stmt, br, len(tests))


cm = json.load(open(CM))
# Filtro opcional p/ sanity-check rápido: ONLY_PROJECTS=codetiming,sty,...
_only = set(p.strip() for p in os.getenv("ONLY_PROJECTS", "").split(",") if p.strip())
rows = []
print(f"{'projeto':24} {'status':10} {'stmt%':>6} {'brnch%':>6} {'#tests':>7}")
print("-" * 60)
for proj, info in sorted(cm.items()):
    if _only and proj not in _only:
        continue
    r = measure(proj, info)
    if r is None:
        print(f"{proj:24} {'sem-testes':10} {'-':>6} {'-':>6} {'0':>7}")
        continue
    status, stmt, br, n = r
    sd = f"{stmt:.1f}" if stmt is not None else "-"
    bd = f"{br:.1f}" if br is not None else "-"
    print(f"{proj:24} {status:10} {sd:>6} {bd:>6} {n:>7}")
    rows.append([proj, status, stmt, br, n])
    sys.stdout.flush()

ok = [r for r in rows if r[2] is not None]
if ok:
    print(f"\npynguin: stmt média {sum(r[2] for r in ok)/len(ok):.1f}%  "
          f"branch média {sum(r[3] for r in ok)/len(ok):.1f}%  ({len(ok)} projetos)")

out = os.path.join(RES, "pynguin_coverage.csv")
with open(out, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["project", "status", "stmt_pct", "branch_pct", "n_tests"])
    w.writerows(rows)
print(f"CSV: {out}")

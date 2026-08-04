#!/usr/bin/env python3
"""Mede a cobertura dos testes gerados — IGUAL para os 3 tools, à prova de crash.

PORQUÊ ESTE SCRIPT (e não o coverage.json que os tools produzem):
o MyCoverage de cada tool corre `pytest <dir_de_testes>` numa única invocação. Se
UM ficheiro rebentar durante a COLEÇÃO, o pytest morre inteiro e a cobertura
medida colapsa. Aconteceu no ansible: um teste instancia `AnsibleModule`, que lê
os parâmetros do stdin (`module_utils/basic.py:_load_params`), falha o
json.loads e chama `sys.exit(1)` → `INTERNALERROR` → 84 erros em 6s e cobertura
de ~11% em vez dos ~31% reais. Afeta MARTA e baseline por igual.

Aqui o pytest corre em LOTES (default 50 ficheiros) com `coverage run --append`:
um lote que rebente perde só os seus testes, os restantes contam. É medição —
não altera nada em nenhum tool, e aplica-se identicamente aos três.

Cobertura reportada sobre os MÓDULOS-ALVO (projects.json), como os papers.

Uso (dentro do container, num nó CPU):
  python scripts/measure_coverage.py --results /data/results --tool marta
  (--tool all p/ os três; ONLY_PROJECTS=a,b p/ subconjunto)
"""
import argparse
import csv
import glob
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
PY = os.getenv("USER_PYTHON_PATH", sys.executable)
BATCH = int(os.getenv("COV_BATCH", "50"))
BATCH_TIMEOUT = int(os.getenv("COV_BATCH_TIMEOUT", "900"))

TOOL_DIRS = {
    "marta": "Results_MARTA",
    "test4py_baseline": "Results_Test4PyBaseline",
    "pynguin": "Results_Pynguin",
    # Suites publicadas pelo CoverUp (FSE'25), do repositorio de replicacao
    # plasma-umass/coverup-eval. NAO sao re-execucao da ferramenta: sao os
    # ficheiros de teste que eles geraram com GPT-4o, medidos pelo NOSSO
    # pipeline sobre os NOSSOS modulos-alvo. Isso elimina a diferenca de
    # granularidade (eles reportam por funcao) e a de pipeline de medicao,
    # deixando o modelo como unica diferenca por declarar.
    "coverup": "Results_CoverUp",
}


def import_root(project_path, source_path):
    """Raiz de sys.path (== _import_root do run_benchmark.py)."""
    src_full = os.path.join(project_path, source_path) if source_path else project_path
    if source_path and not os.path.exists(os.path.join(src_full, "__init__.py")):
        return src_full
    return project_path


def _dotted(fname):
    d = fname[:-3] if fname.endswith(".py") else fname
    d = d.replace("/", ".").replace("\\", ".").lstrip(".")
    return d[:-len(".__init__")] if d.endswith(".__init__") else d


def _matches(dotted, targets):
    return any(dotted == t or dotted.endswith("." + t) for t in targets)


def find_tests(results, tool, proj, max_gen=None):
    """Ficheiros de teste ATUAIS (exclui arquivos de runs anteriores e quarentena).

    `max_gen` serve a ablação do ciclo externo (contribuição 3). AS DUAS
    ferramentas LLM gravam o ÍNDICE DE GERAÇÃO POR FUNÇÃO no nome do ficheiro —
    o 1.º, 2.º ou 3.º ficheiro produzido para aquela função:

      MARTA     f"{react_prefix}_{len(existing)}.py"        message_react.py:1020
      Test4Py   ... + func_name + str(len(self.testcases))  testcase.py:46

    A MARTA separa com underscore, o baseline cola o dígito ao nome da função.
    Ler o ÚLTIMO CARACTERE resolve os dois: o índice nunca passa de 2 (são 3
    rondas), por isso uma função chamada `md5` com índice 0 dá `...md50`, cujo
    último caractere é `0` — correto. Um `rsplit("_")` é que falharia no
    baseline.

    NÃO é o número da ronda: se a ronda 1 não deixou ficheiro para uma função, a
    ronda 2 escreve o índice 0. Reportar como 'primeira geração vs todas'.

    O Pynguin não tem rondas e nunca é filtrado.
    """
    base = os.path.join(results, TOOL_DIRS[tool], proj)
    out = [f for f in glob.glob(os.path.join(base, "**", "test_*.py"), recursive=True)
           if "OLD" not in f and "quarantine" not in f and "_cov_" not in f]
    if max_gen is not None and tool in ("marta", "test4py_baseline"):
        keep = []
        for f in out:
            last = os.path.basename(f)[:-3][-1:]
            # sem dígito final: não classificável, fica (conservador)
            if not last.isdigit() or int(last) <= max_gen:
                keep.append(f)
        out = keep
    return sorted(out)


def measure(results, tool, proj, info, targets, max_gen=None):
    tests = find_tests(results, tool, proj, max_gen)
    if not tests:
        # o tool não produziu testes para este projeto → 0% (não excluir: excluir
        # inflacionaria a média ao contar só onde o tool teve sucesso)
        return dict(status="no_tests", stmt=0.0, branch=0.0, lb=0.0,
                    n_mod=0, n_tests=0, batches_failed=0)

    ppath0 = info["project_path"]
    spath = info.get("source_path", "")
    if not os.path.isdir(ppath0):
        return dict(status="project_missing", stmt=None, branch=None, lb=None,
                    n_mod=0, n_tests=len(tests), batches_failed=0)

    # CÓPIA DESCARTÁVEL: os testes gerados (sobretudo os do Pynguin, que correm
    # com PYNGUIN_DANGER_AWARE) criam e apagam ficheiros no cwd. Medindo com
    # cwd no diretório REAL do projeto, cada medição deixava-o num estado
    # diferente e a seguinte media outra coisa: o ansible deu 27.7% numa
    # execução e 8.4% noutra, com os MESMOS 227 ficheiros e zero lotes
    # falhados. Medir sobre uma cópia torna a medição reprodutível e impede
    # que medir um tool contamine a medição do seguinte.
    scratch = tempfile.mkdtemp(prefix=f"cov_{proj}_", dir=os.getenv("COV_SCRATCH") or None)
    ppath = os.path.join(scratch, os.path.basename(ppath0.rstrip("/")) or "proj")
    try:
        shutil.copytree(ppath0, ppath, symlinks=True)
    except Exception as e:
        shutil.rmtree(scratch, ignore_errors=True)
        return dict(status=f"copy_err:{str(e)[:30]}", stmt=None, branch=None,
                    lb=None, n_mod=0, n_tests=len(tests), batches_failed=0)
    root = import_root(ppath, spath)

    env = os.environ.copy()
    prev = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = f"{root}:{prev}" if prev else root

    # a ablação escreve num dir próprio para não destruir a medição canónica
    sfx = f"_g{max_gen}" if max_gen is not None else ""
    covdir = os.path.join(results, TOOL_DIRS[tool], proj, f"_cov_{tool}{sfx}")
    os.makedirs(covdir, exist_ok=True)
    dataf = os.path.join(covdir, ".coverage")
    jf = os.path.join(covdir, "coverage.json")
    for f in glob.glob(dataf + "*"):
        os.remove(f)

    # RCFILE PRÓPRIO: sem isto o coverage.py lê a configuração DO PROJETO
    # (.coveragerc / setup.cfg / pyproject.toml no cwd) e aplica os `omit` dele.
    # O black omite `src/blib2to3` (código vendored) — que são precisamente os
    # seus 6 módulos-alvo → 0 ficheiros medidos e o projeto ficava sem número.
    # Cada projeto teria regras diferentes = medição enviesada e não comparável.
    rcfile = os.path.join(covdir, "coveragerc")
    with open(rcfile, "w") as f:
        f.write("[run]\nbranch = True\nomit =\n")

    # LOTES: um ficheiro que rebente na coleção (sys.exit/INTERNALERROR) só
    # invalida o seu lote; os restantes continuam a contar.
    failed = 0
    for i in range(0, len(tests), BATCH):
        chunk = tests[i:i + BATCH]
        cmd = [PY, "-m", "coverage", "run", f"--rcfile={rcfile}", "--append", "--branch",
               f"--source={spath or '.'}", f"--data-file={dataf}",
               "-m", "pytest", "-q", "-c", "/dev/null", "--rootdir", ppath,
               "--continue-on-collection-errors", "-p", "no:cacheprovider"] + chunk
        try:
            r = subprocess.run(cmd, cwd=ppath, env=env,
                               capture_output=True, timeout=BATCH_TIMEOUT)
            # returncode 3 (INTERNALERROR) ou 2 (interrupção) = lote perdido
            if r.returncode in (2, 3):
                failed += 1
        except subprocess.TimeoutExpired:
            failed += 1

    subprocess.run([PY, "-m", "coverage", "json", f"--rcfile={rcfile}", "-i",
                    f"--data-file={dataf}", "-o", jf],
                   cwd=ppath, env=env, capture_output=True)
    shutil.rmtree(scratch, ignore_errors=True)
    try:
        cj = json.load(open(jf))
    except Exception as e:
        return dict(status=f"parse_err:{str(e)[:40]}", stmt=None, branch=None,
                    lb=None, n_mod=0, n_tests=len(tests), batches_failed=failed)

    tgt = targets.get(proj, [])
    cl = ns = cb = nb = matched = 0
    for fname, fobj in cj.get("files", {}).items():
        if _matches(_dotted(fname), tgt):
            s = fobj.get("summary", {})
            cl += s.get("covered_lines", 0);  ns += s.get("num_statements", 0)
            cb += s.get("covered_branches", 0); nb += s.get("num_branches", 0)
            matched += 1
    if matched == 0:
        return dict(status="no_target_match", stmt=None, branch=None, lb=None,
                    n_mod=0, n_tests=len(tests), batches_failed=failed)
    stmt = 100 * cl / ns if ns else 0.0
    br = 100 * cb / nb if nb else 0.0
    lb = 100 * (cl + cb) / (ns + nb) if (ns + nb) else 0.0
    return dict(status="ok", stmt=stmt, branch=br, lb=lb, n_mod=matched,
                n_tests=len(tests), batches_failed=failed)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", default="/data/results")
    ap.add_argument("--tool", default="all")
    ap.add_argument("--cm", default=os.path.join(HERE, "cm_benchmark.json"))
    ap.add_argument("--projects", default="/opt/marta/projects.json")
    ap.add_argument("--max-gen", type=int, default=None,
                    help="ablação do ciclo externo: usa só os ficheiros cujo índice "
                         "de geração por função é <= N (0 = só o 1.º ficheiro de cada "
                         "função). Escreve em ficheiros separados; não toca na medição "
                         "canónica.")
    args = ap.parse_args()

    cm = json.load(open(args.cm))
    targets = json.load(open(args.projects))
    tools = list(TOOL_DIRS) if args.tool == "all" else [args.tool]
    only = set(p.strip() for p in os.getenv("ONLY_PROJECTS", "").split(",") if p.strip())

    out = os.path.join(args.results, "coverage_measured.csv" if args.max_gen is None
                       else f"coverage_measured_g{args.max_gen}.csv")
    cols = ["tool", "project", "status", "stmt_pct", "branch_pct", "lb_pct",
            "n_target_mods", "n_tests", "batches_failed"]
    done = set()
    if os.path.exists(out):
        for row in csv.DictReader(open(out)):
            done.add((row["tool"], row["project"]))

    print(f"{'tool':18} {'projeto':22} {'status':14} {'stmt':>6} {'brnch':>6} {'l+b':>6} {'#mod':>5} {'#test':>6} {'lotes✗':>7}")
    print("-" * 100)
    for tool in tools:
        for proj in sorted(targets):
            if only and proj not in only:
                continue
            if (tool, proj) in done:
                continue
            if proj not in cm:
                continue
            r = measure(args.results, tool, proj, cm[proj], targets, args.max_gen)
            f = lambda k: f"{r[k]:.1f}" if r.get(k) is not None else "-"
            print(f"{tool:18} {proj:22} {r['status']:14} {f('stmt'):>6} {f('branch'):>6} "
                  f"{f('lb'):>6} {r['n_mod']:>5} {r['n_tests']:>6} {r['batches_failed']:>7}")
            sys.stdout.flush()
            new = not os.path.exists(out)
            with open(out, "a", newline="") as fh:
                w = csv.DictWriter(fh, fieldnames=cols)
                if new:
                    w.writeheader()
                w.writerow({"tool": tool, "project": proj, "status": r["status"],
                            "stmt_pct": r["stmt"], "branch_pct": r["branch"],
                            "lb_pct": r["lb"], "n_target_mods": r["n_mod"],
                            "n_tests": r["n_tests"], "batches_failed": r["batches_failed"]})
    print(f"\nCSV: {out}")


if __name__ == "__main__":
    main()

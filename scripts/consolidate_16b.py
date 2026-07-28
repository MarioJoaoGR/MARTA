#!/usr/bin/env python3
"""Consolida os resultados do benchmark (cobertura + executability + runtime).

COBERTURA — medida sobre os MÓDULOS-ALVO (projects.json), como os papers, e NÃO
sobre o source_dir inteiro. O coverage.json tem o `summary` de cada ficheiro em
`files`; filtramos aos módulos-alvo (por sufixo, p/ apanhar containers: ansible
source=lib → ficheiros `lib.ansible...`; black source=src → `src.blib2to3...`) e
somamos. O uso antigo de `totals` media o PACOTE INTEIRO — centenas de ficheiros
não-alvo contados a 0% pelo coverage.py `--source` → diluía tudo (ex.: thonny
reportava 0.8%, que é EXATAMENTE a fração de ficheiros que eram alvo). Mantemos o
`totals` numa coluna `pkg%` só para transparência/comparação.

MARTA e Test4Py-baseline: coverage.json + run_results/<proj>.json por projeto.
O Pynguin é medido à parte (measure_pynguin_coverage.py, mesma lógica de alvos).

Uso:  python3 scripts/consolidate_16b.py [RESULTS_DIR] [PROJECTS_JSON]
"""
import json
import os
import glob
import csv
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT = "/projects/F202407648IACDCF2/mario/results/deepseek-coder-v2_16b"
RES = sys.argv[1] if len(sys.argv) > 1 else DEFAULT
PROJECTS_JSON = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "..", "projects.json")
TARGETS = json.load(open(PROJECTS_JSON))

TOOLS = [("marta", "Results_MARTA"), ("baseline", "Results_Test4PyBaseline")]


def _cov_json(proj_dir):
    """coverage.json ATUAL do projeto.

    ⚠️ O glob '**' apanha também os coverage.json de pastas ARQUIVADAS de runs
    anteriores (Test4DT_tests_OLD_prompts/, *_OLD*, quarentena). Com hits[0] a
    ordem do filesystem decidia qual era lido → ~18 projetos apareciam com a
    cobertura EXATA do run antigo. Filtra-se o arquivo e, havendo mais que um,
    escolhe-se o mais RECENTE (mtime).
    """
    hits = [h for h in glob.glob(os.path.join(proj_dir, "**", "coverage.json"),
                                 recursive=True)
            if "OLD" not in h and "quarantine" not in h and "_pynguin_cov" not in h]
    if not hits:
        return None
    hits.sort(key=os.path.getmtime, reverse=True)
    try:
        return json.load(open(hits[0]))
    except Exception:
        return None


def _dotted(fname):
    """Caminho de ficheiro do coverage.json → nome de módulo dotted."""
    d = fname[:-3] if fname.endswith(".py") else fname
    d = d.replace("/", ".").replace("\\", ".").lstrip(".")
    if d.endswith(".__init__"):
        d = d[:-len(".__init__")]
    return d


def _matches(dotted, targets):
    # sufixo tolera prefixos de container (lib., src.) sem falsos positivos práticos
    return any(dotted == t or dotted.endswith("." + t) for t in targets)


def coverage_target(proj, proj_dir):
    """(stmt%, br%, cl, ns, cb, nb, n_mods) sobre os módulos-alvo, ou None."""
    cj = _cov_json(proj_dir)
    if not cj:
        return None
    targets = TARGETS.get(proj, [])
    cl = ns = cb = nb = matched = 0
    for fname, f in cj.get("files", {}).items():
        if _matches(_dotted(fname), targets):
            s = f.get("summary", {})
            cl += s.get("covered_lines", 0)
            ns += s.get("num_statements", 0)
            cb += s.get("covered_branches", 0)
            nb += s.get("num_branches", 0)
            matched += 1
    if matched == 0:
        return None
    stmt = 100 * cl / ns if ns else 0.0
    br = 100 * cb / nb if nb else 0.0
    return (stmt, br, cl, ns, cb, nb, matched)


def pkg_coverage(proj_dir):
    """(stmt%, br%) sobre o source_dir inteiro (totals) — só transparência."""
    cj = _cov_json(proj_dir)
    if not cj:
        return None
    t = cj.get("totals", {})
    stmt = 100 * t["covered_lines"] / t["num_statements"] if t.get("num_statements") else 0.0
    br = 100 * t.get("covered_branches", 0) / t["num_branches"] if t.get("num_branches") else 0.0
    return (stmt, br)


def run_results(proj_dir):
    hits = glob.glob(os.path.join(proj_dir, "run_results", "*.json"))
    if not hits:
        return {}
    try:
        return json.load(open(hits[0]))
    except Exception:
        return {}


rows = []
for tool, base in TOOLS:
    root = os.path.join(RES, base)
    if not os.path.isdir(root):
        continue
    for proj in sorted(os.listdir(root)):
        pd = os.path.join(root, proj)
        if not os.path.isdir(pd):
            continue
        cov = coverage_target(proj, pd)   # PRIMÁRIO: módulos-alvo
        pkg = pkg_coverage(pd)            # secundário: pacote inteiro
        rr = run_results(pd)
        if cov is None and not rr:
            continue
        stmt = cov[0] if cov else None
        br = cov[1] if cov else None
        nmods = cov[6] if cov else None
        # line+branch COMBINADO — é assim que o CoverUp reporta ("line+branch
        # coverage"), = (covered_lines+covered_branches)/(num_statements+num_branches),
        # o mesmo que o percent_covered do coverage.py com --branch. Sem isto não
        # somos comparáveis aos números publicados.
        comb = None
        if cov:
            den = cov[3] + cov[5]
            comb = 100 * (cov[2] + cov[4]) / den if den else 0.0
        pkgstmt = pkg[0] if pkg else None
        ap = rr.get("assertion_pass")     # testes que passam (executáveis + assert válido)
        ae = rr.get("assertion_error")     # testes que falham
        sp = rr.get("syntax_pass")         # sintaticamente válidos
        tm = rr.get("time")                # runtime total (s)
        tt = rr.get("total_tokens")        # tokens totais
        rows.append([tool, proj, stmt, br, comb, pkgstmt, nmods, sp, ap, ae, tm, tt,
                     rr.get("prompt_tokens"), rr.get("completion_tokens")])

# ── Tabela ──
hdr = (f"{'tool':9} {'projeto':22} {'stmt%':>6} {'brnch%':>6} {'l+b%':>6} {'pkg%':>6} {'#mod':>5} "
       f"{'syn':>4} {'pass':>5} {'fail':>5} {'time_s':>8} {'tokens':>10}")
print(hdr)
print("-" * len(hdr))
for r in rows:
    stmt = f"{r[2]:.1f}" if r[2] is not None else "-"
    br = f"{r[3]:.1f}" if r[3] is not None else "-"
    comb = f"{r[4]:.1f}" if r[4] is not None else "-"
    pkg = f"{r[5]:.1f}" if r[5] is not None else "-"
    nm = str(r[6]) if r[6] is not None else "-"
    syn = str(r[7]) if r[7] is not None else "-"
    ap = str(r[8]) if r[8] is not None else "-"
    ae = str(r[9]) if r[9] is not None else "-"
    tm = f"{r[10]:.0f}" if r[10] is not None else "-"
    tk = f"{r[11]:,}" if r[11] is not None else "-"
    print(f"{r[0]:9} {r[1]:22} {stmt:>6} {br:>6} {comb:>6} {pkg:>6} {nm:>5} "
          f"{syn:>4} {ap:>5} {ae:>5} {tm:>8} {tk:>10}")


def _median(xs):
    s = sorted(xs)
    n = len(s)
    if not n:
        return 0.0
    m = n // 2
    return s[m] if n % 2 else (s[m - 1] + s[m]) / 2


# ── Agregados ──
print("\n=== AGREGADOS (sobre módulos-alvo) ===")
print("  l+b% = line+branch COMBINADO — a métrica que o CoverUp reporta (mediana + overall).")
for tool, _ in TOOLS:
    tr = [r for r in rows if r[0] == tool and r[2] is not None]
    if not tr:
        continue
    n = len(tr)
    combs = [r[4] for r in tr if r[4] is not None]
    print(f"  {tool:9}: stmt {sum(r[2] for r in tr)/n:5.1f}%  branch {sum(r[3] for r in tr)/n:5.1f}%  "
          f"| l+b méd {sum(combs)/len(combs):5.1f}%  l+b MEDIANA {_median(combs):5.1f}%  "
          f"| Σpass {sum(r[8] or 0 for r in tr)}  Σfail {sum(r[9] or 0 for r in tr)}  "
          f"| Σtokens {sum(r[11] or 0 for r in tr):,}  "
          f"Σtempo {sum(r[10] or 0 for r in tr)/3600:.1f}h  ({n} proj)")

# ── CSV ──
out = os.path.join(RES, "consolidated_16b.csv")
with open(out, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["tool", "project", "stmt_pct", "branch_pct", "line_branch_pct",
                "pkg_stmt_pct", "n_target_mods", "syntax_pass", "assertion_pass",
                "assertion_error", "time_s", "total_tokens", "prompt_tokens",
                "completion_tokens"])
    w.writerows(rows)
print(f"\nCSV escrito: {out}")

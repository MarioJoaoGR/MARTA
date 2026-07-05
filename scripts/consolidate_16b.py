#!/usr/bin/env python3
"""Consolida os resultados do benchmark (cobertura + executability + runtime).

MARTA e Test4Py-baseline: lê o coverage.json (totals) e o run_results/<proj>.json
de cada projeto → statement%, branch%, testes passados/falhados, tempo. Agrega
por tool e escreve CSV. O Pynguin é medido à parte (não tem coverage.json — ver
consolidate_pynguin_cov.py).

Uso:  python3 scripts/consolidate_16b.py [RESULTS_DIR]
      (default: results/deepseek-coder-v2_16b)
"""
import json
import os
import glob
import csv
import sys

DEFAULT = "/projects/F202407648IACDCF2/mario/results/deepseek-coder-v2_16b"
RES = sys.argv[1] if len(sys.argv) > 1 else DEFAULT

TOOLS = [("marta", "Results_MARTA"), ("baseline", "Results_Test4PyBaseline")]


def coverage(proj_dir):
    """(stmt%, branch%, covered_lines, num_statements, covered_branches, num_branches) ou None."""
    hits = glob.glob(os.path.join(proj_dir, "**", "coverage.json"), recursive=True)
    if not hits:
        return None
    try:
        t = json.load(open(hits[0]))["totals"]
    except Exception:
        return None
    stmt = 100 * t["covered_lines"] / t["num_statements"] if t.get("num_statements") else 0.0
    br = 100 * t.get("covered_branches", 0) / t["num_branches"] if t.get("num_branches") else 0.0
    return (stmt, br, t["covered_lines"], t.get("num_statements", 0),
            t.get("covered_branches", 0), t.get("num_branches", 0))


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
        cov = coverage(pd)
        rr = run_results(pd)
        if cov is None and not rr:
            continue
        stmt = cov[0] if cov else None
        br = cov[1] if cov else None
        ap = rr.get("assertion_pass")       # testes que passam (executáveis + assert válido)
        ae = rr.get("assertion_error")       # testes que falham
        sp = rr.get("syntax_pass")           # sintaticamente válidos
        tm = rr.get("time")                  # runtime total (s)
        rows.append([tool, proj, stmt, br, sp, ap, ae, tm])

# ── Tabela ──
hdr = f"{'tool':9} {'projeto':24} {'stmt%':>6} {'brnch%':>6} {'syn':>4} {'pass':>5} {'fail':>5} {'time_s':>8}"
print(hdr)
print("-" * len(hdr))
for r in rows:
    stmt = f"{r[2]:.1f}" if r[2] is not None else "-"
    br = f"{r[3]:.1f}" if r[3] is not None else "-"
    syn = str(r[4]) if r[4] is not None else "-"
    ap = str(r[5]) if r[5] is not None else "-"
    ae = str(r[6]) if r[6] is not None else "-"
    tm = f"{r[7]:.0f}" if r[7] is not None else "-"
    print(f"{r[0]:9} {r[1]:24} {stmt:>6} {br:>6} {syn:>4} {ap:>5} {ae:>5} {tm:>8}")

# ── Agregados ──
print("\n=== AGREGADOS (média por projeto) ===")
for tool, _ in TOOLS:
    tr = [r for r in rows if r[0] == tool and r[2] is not None]
    if not tr:
        continue
    n = len(tr)
    avg_stmt = sum(r[2] for r in tr) / n
    avg_br = sum(r[3] for r in tr) / n
    tot_pass = sum(r[5] or 0 for r in tr)
    tot_fail = sum(r[6] or 0 for r in tr)
    print(f"  {tool:9}: stmt {avg_stmt:5.1f}%  branch {avg_br:5.1f}%  "
          f"| Σpass {tot_pass}  Σfail {tot_fail}  ({n} projetos)")

# ── CSV ──
out = os.path.join(RES, "consolidated_16b.csv")
with open(out, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["tool", "project", "stmt_pct", "branch_pct", "syntax_pass",
                "assertion_pass", "assertion_error", "time_s"])
    w.writerows(rows)
print(f"\nCSV escrito: {out}")

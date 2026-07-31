#!/usr/bin/env python3
"""Cobertura POR MÓDULO — necessária para comparar com o CoverUp.

O CoverUp reporta a MEDIANA POR-MÓDULO de line+branch (80% com GPT-4o) e a
cobertura OVERALL/pooled (60%). A nossa medição agrega por projeto, o que dá uma
mediana por-PROJETO — grandeza diferente e não comparável. Este script recalcula
a partir dos coverage.json já em disco, tratando cada MÓDULO-ALVO como uma
observação, que é a unidade do benchmark (486 módulos) e a do CoverUp.

Módulos que um tool não cobre de todo contam como 0% (não são excluídos).

Uso:  python scripts/per_module_coverage.py --results <dir>
"""
import argparse
import collections
import json
import os
import statistics as st

TOOLS = ["marta", "test4py_baseline", "pynguin"]
LABEL = {"marta": "MARTA", "test4py_baseline": "Test4Py", "pynguin": "Pynguin"}
DIRS = {"marta": "Results_MARTA", "test4py_baseline": "Results_Test4PyBaseline",
        "pynguin": "Results_Pynguin"}


def dotted(fname):
    d = fname[:-3] if fname.endswith(".py") else fname
    d = d.replace("/", ".").replace("\\", ".").lstrip(".")
    return d[:-len(".__init__")] if d.endswith(".__init__") else d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", required=True)
    ap.add_argument("--projects", default="/opt/marta/projects.json")
    a = ap.parse_args()
    targets = json.load(open(a.projects))

    per_mod = collections.defaultdict(dict)   # tool -> "proj::mod" -> lb%
    pooled = collections.defaultdict(lambda: [0, 0, 0, 0])
    for t in TOOLS:
        for proj, mods in targets.items():
            j = os.path.join(a.results, DIRS[t], proj, f"_cov_{t}", "coverage.json")
            found = {}
            if os.path.exists(j):
                try:
                    cj = json.load(open(j))
                except Exception:
                    cj = {}
                for fn, fo in cj.get("files", {}).items():
                    d = dotted(fn)
                    for m in mods:
                        if d == m or d.endswith("." + m):
                            s = fo.get("summary", {})
                            cl = s.get("covered_lines", 0); ns = s.get("num_statements", 0)
                            cb = s.get("covered_branches", 0); nb = s.get("num_branches", 0)
                            den = ns + nb
                            found[m] = 100 * (cl + cb) / den if den else 0.0
                            x = pooled[t]
                            x[0] += cl; x[1] += ns; x[2] += cb; x[3] += nb
                            break
            # módulos sem medição contam 0% (o tool não os cobriu)
            for m in mods:
                per_mod[t][f"{proj}::{m}"] = found.get(m, 0.0)

    print("═══ COBERTURA POR MÓDULO (line+branch) — unidade do benchmark e do CoverUp ═══\n")
    print(f"{'ferramenta':12} {'módulos':>8} {'mediana':>9} {'média':>8} {'pooled':>8}")
    print("-" * 50)
    for t in TOOLS:
        v = list(per_mod[t].values())
        cl, ns, cb, nb = pooled[t]
        po = 100 * (cl + cb) / (ns + nb) if (ns + nb) else 0.0
        print(f"{LABEL[t]:12} {len(v):>8} {st.median(v):>8.1f}% {sum(v)/len(v):>7.1f}% {po:>7.1f}%")

    print("\n── Referências publicadas (mesmo benchmark de origem) ──")
    print(f"  {'CoverUp (GPT-4o)':22} mediana por-módulo 80.0%   overall 60.0%")
    print(f"  {'CodaMosa (Codex)':22} mediana por-módulo 47.0%   overall 45.0%")
    print("  NOTA: valores dos papers respetivos; modelos e subconjunto diferentes.")


if __name__ == "__main__":
    main()

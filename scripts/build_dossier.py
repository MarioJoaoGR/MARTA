#!/usr/bin/env python3
"""Reúne TODOS os resultados num só markdown, pronto para o paper.

Junta cobertura, mutation score, qualidade dos oráculos, custo e
executabilidade, com as três agregações e as limitações. Usa a mutação
POR-MÓDULO se existir (mutmut_permodule.csv), senão a de suite-completa
(mutmut.csv), indicando sempre qual foi usada.

Uso:  python scripts/build_dossier.py --results <dir> [--out dossier.md]
"""
import argparse
import collections
import csv
import glob
import json
import os
import statistics as st

TOOLS = ["marta", "test4py_baseline", "pynguin"]
LABEL = {"marta": "MARTA", "test4py_baseline": "Test4Py", "pynguin": "Pynguin"}
DIRS = {"marta": "Results_MARTA", "test4py_baseline": "Results_Test4PyBaseline",
        "pynguin": "Results_Pynguin"}


def read(path):
    if not os.path.exists(path):
        return []
    seen = {}
    for r in csv.DictReader(open(path)):
        seen[(r.get("tool"), r.get("project"))] = r      # última linha vence
    return list(seen.values())


def fmt(v, d=1):
    return f"{v:.{d}f}" if isinstance(v, (int, float)) else "—"


def agg_block(vals_by_tool, title, unit="%"):
    out = [f"\n**{title}**\n",
           "| ferramenta | média | mediana | n |", "|---|---|---|---|"]
    for t in TOOLS:
        v = vals_by_tool.get(t, [])
        if v:
            out.append(f"| {LABEL[t]} | {sum(v)/len(v):.1f}{unit} | "
                       f"{st.median(v):.1f}{unit} | {len(v)} |")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", required=True)
    ap.add_argument("--projects", default="/opt/marta/projects.json")
    ap.add_argument("--out")
    a = ap.parse_args()
    R = a.results
    targets = json.load(open(a.projects))
    md = ["# Dossiê de resultados — benchmark CM (486 módulos, 27 projetos)\n"]

    # ───────────────────────── COBERTURA ─────────────────────────
    cov = read(f"{R}/coverage_measured.csv")
    if cov:
        md.append("\n## 1. Cobertura (line+branch, sobre os módulos-alvo)\n")
        by = collections.defaultdict(dict)
        for r in cov:
            if r["status"] == "ok" and r["lb_pct"]:
                by[r["project"]][r["tool"]] = float(r["lb_pct"])
        md += ["| projeto | " + " | ".join(LABEL[t] for t in TOOLS) + " |",
               "|---|" + "---|" * len(TOOLS)]
        for p in sorted(by):
            md.append(f"| {p} | " + " | ".join(fmt(by[p].get(t)) for t in TOOLS) + " |")
        md.append(agg_block({t: [d[t] for d in by.values() if t in d] for t in TOOLS},
                            "Agregado por PROJETO (média das médias)"))
        # ponderado por módulo
        w = collections.defaultdict(lambda: [0.0, 0])
        for p, d in by.items():
            n = len(targets.get(p, [])) or 1
            for t, v in d.items():
                w[t][0] += v * n
                w[t][1] += n
        md += ["\n**Ponderado por MÓDULO** (unidade de avaliação do CodaMosa)\n",
               "| ferramenta | l+b |", "|---|---|"]
        for t in TOOLS:
            if w[t][1]:
                md.append(f"| {LABEL[t]} | {w[t][0]/w[t][1]:.1f}% |")
        # pooled
        pooled = collections.defaultdict(lambda: [0, 0, 0, 0])
        for t in TOOLS:
            for p, mods in targets.items():
                j = f"{R}/{DIRS[t]}/{p}/_cov_{t}/coverage.json"
                if not os.path.exists(j):
                    continue
                try:
                    cj = json.load(open(j))
                except Exception:
                    continue
                for fn, fo in cj.get("files", {}).items():
                    dd = fn[:-3].replace("/", ".").lstrip(".")
                    dd = dd[:-9] if dd.endswith(".__init__") else dd
                    if any(dd == m or dd.endswith("." + m) for m in mods):
                        s = fo.get("summary", {}); x = pooled[t]
                        x[0] += s.get("covered_lines", 0); x[1] += s.get("num_statements", 0)
                        x[2] += s.get("covered_branches", 0); x[3] += s.get("num_branches", 0)
        if pooled:
            md += ["\n**POOLED / overall** (Σcobertos / Σtotal — denominador idêntico; "
                   "é como o CoverUp reporta)\n",
                   "| ferramenta | statement | branch | line+branch |", "|---|---|---|---|"]
            for t in TOOLS:
                cl, ns, cb, nb = pooled[t]
                if ns:
                    md.append(f"| {LABEL[t]} | {100*cl/ns:.1f}% | {100*cb/nb:.1f}% | "
                              f"{100*(cl+cb)/(ns+nb):.1f}% |")

    # ───────────────────────── MUTATION ─────────────────────────
    pm = read(f"{R}/mutmut_permodule.csv")
    ws = read(f"{R}/mutmut.csv")
    mut, how = (pm, "por-módulo (mutantes de M avaliados só com os testes de M)") \
        if len(pm) >= len(ws) and pm else (ws, "suite completa por mutante")
    if mut:
        md.append(f"\n## 2. Mutation score\n\n_Metodologia: {how}._\n")
        by = collections.defaultdict(dict)
        for r in mut:
            if r.get("status") == "ok" and r.get("score") not in (None, "", "None"):
                by[r["project"]][r["tool"]] = float(r["score"])
        md += ["| projeto | " + " | ".join(LABEL[t] for t in TOOLS) + " |",
               "|---|" + "---|" * len(TOOLS)]
        for p in sorted(by):
            md.append(f"| {p} | " + " | ".join(fmt(by[p].get(t)) for t in TOOLS) + " |")
        common = [p for p, d in by.items() if all(t in d for t in TOOLS)]
        md.append(agg_block({t: [by[p][t] for p in common] for t in TOOLS},
                            f"Agregado nos {len(common)} projetos com valor nos 3"))
        miss = [(r["tool"], r["project"], r.get("status"))
                for r in mut if r.get("status") != "ok"]
        if miss:
            md.append("\n_Sem valor: " + ", ".join(f"{p} ({t}, {s})" for t, p, s in miss) + "._")

    # ─────────────────── QUALIDADE DOS ORÁCULOS ───────────────────
    tq = read(f"{R}/test_quality.csv")
    if tq:
        md.append("\n## 3. Qualidade dos oráculos\n")
        agg = collections.defaultdict(lambda: collections.Counter())
        for r in tq:
            n = int(r["n_tests"]); a = agg[r["tool"]]
            a["n"] += n
            for k in ("asserts_per_test", "pct_zero_assert", "pct_trivial", "loc_per_test"):
                a[k] += float(r[k]) * n
        md += ["| ferramenta | #testes | asserts/teste | **sem assertion** | triviais | loc/teste |",
               "|---|---|---|---|---|---|"]
        for t in TOOLS:
            a = agg.get(t)
            if a and a["n"]:
                n = a["n"]
                md.append(f"| {LABEL[t]} | {n} | {a['asserts_per_test']/n:.2f} | "
                          f"**{a['pct_zero_assert']/n:.1f}%** | {a['pct_trivial']/n:.1f}% | "
                          f"{a['loc_per_test']/n:.1f} |")

    # ───────────────────── CUSTO / EXECUTABILIDADE ─────────────────────
    md.append("\n## 4. Custo e executabilidade\n")
    md += ["| ferramenta | tokens | tempo (h) | testes que passam | falhados |",
           "|---|---|---|---|---|"]
    for t in ("marta", "test4py_baseline"):
        tok = tim = ap_ = ae = 0
        for f in glob.glob(f"{R}/{DIRS[t]}/*/run_results/*.json"):
            try:
                d = json.load(open(f))
            except Exception:
                continue
            tok += d.get("total_tokens") or 0
            tim += d.get("time") or 0
            ap_ += d.get("assertion_pass") or 0
            ae += d.get("assertion_error") or 0
        md.append(f"| {LABEL[t]} | {tok:,} | {tim/3600:.1f} | {ap_} | {ae} |")
    md.append("| Pynguin | — (sem LLM) | — | — | — |")

    # ───────────────────────── NOTAS ─────────────────────────
    md.append("""
## 5. Notas de metodologia e limitações

- **Pynguin**: 300s de busca por módulo, algoritmo por omissão (DynaMOSA — o
  melhor segundo Lukasczyk & Fraser 2022). O CodaMosa usou 600s × 16 repetições;
  aqui é 1 repetição, por restrições de computação.
- **MARTA e Test4Py**: 3 rondas de geração (mesmo protocolo do Test4Py), mesmo
  modelo (DeepSeek-Coder-V2 16B, local via Ollama) e mesmo hardware.
- **Temperatura**: MARTA 0.2, Test4Py 0.0 (valores por omissão de cada
  ferramenta).
- **CoverUp**: não foi possível executar a ferramenta; a comparação é feita
  com os números publicados (FSE 2025) e é, por isso, **não controlada**.
- **Test4Py** aplica uma *heuristic reduction* que minimiza o teste até passar
  (§3.4.2), o que remove assertions — daí a métrica «% de testes sem assertion».
- **Uma repetição por ferramenta**: sem intervalos de confiança. Os testes de
  significância (Wilcoxon emparelhado + tamanho de efeito) estão por fazer.
- Cobertura medida em **lotes** para resistir a ficheiros que abortam a coleção
  do pytest, e com configuração de coverage própria (o `.coveragerc` do black
  excluía os seus próprios módulos-alvo).
""")

    text = "\n".join(md)
    out = a.out or os.path.join(R, "dossier.md")
    open(out, "w", encoding="utf-8").write(text)
    print(text)
    print(f"\n\n>>> escrito: {out}")


if __name__ == "__main__":
    main()

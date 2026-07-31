#!/usr/bin/env python3
"""Custo SEPARADO em análise (Fase 1) e geração — comparação justa.

O total bruto engana: um run cuja Fase 1 veio da cache parece muito mais barato
que outro que a fez de raiz. O run_results de cada projeto regista os tempos por
etapa em `times` (`collect_message` = análise; `run_0..n` = rondas de geração),
o que permite comparar geração com geração.

Os tokens não estão separados por etapa, pelo que se reportam apenas os totais,
assinalando se a análise foi executada nesse run (collect_message alto) ou veio
da cache (quase zero).

Uso:  python scripts/cost_breakdown.py --results <dir>
"""
import argparse, glob, json, os

DIRS = {"marta": "Results_MARTA", "test4py_baseline": "Results_Test4PyBaseline"}

ap = argparse.ArgumentParser()
ap.add_argument("--results", required=True)
a = ap.parse_args()

print(f"{'tool':18} {'análise(h)':>11} {'geração(h)':>11} {'total(h)':>9} "
      f"{'tokens':>14} {'projetos':>9}")
print("-" * 78)
for tool, d in DIRS.items():
    an = gen = tok = 0.0
    n = 0
    for f in glob.glob(os.path.join(a.results, d, "*", "run_results", "*.json")):
        try:
            j = json.load(open(f))
        except Exception:
            continue
        t = j.get("times") or {}
        an += t.get("collect_message", 0) or 0
        gen += sum(v for k, v in t.items() if k.startswith("run_"))
        tok += j.get("total_tokens") or 0
        n += 1
    print(f"{tool:18} {an/3600:>11.1f} {gen/3600:>11.1f} {(an+gen)/3600:>9.1f} "
          f"{tok:>14,.0f} {n:>9}")
print("\nNOTA: 'análise' perto de zero indica que a Fase 1 veio da cache nesse run;")
print("nesse caso o total NÃO é comparável ao de um run que a executou de raiz.")
print("A comparação defensável é a coluna 'geração'.")

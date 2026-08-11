"""Seleção estratificada do corpus a partir da população diagnosticada.

Entrada: benchmark/results/population_diagnose.json (112 gems incluídas, com
métricas de diversidade). Método: **farthest-first traversal** no espaço de
características normalizado — escolhe iterativamente a gem mais distante das já
escolhidas, o que garante que o corpus cobre os EXTREMOS e o centro de cada
dimensão. Determinístico (semente = gem mais afastada do centróide) e
reprodutível. Restrição de domínio: no máximo 2 gems por categoria.

A ordem de seleção é significativa: as primeiras k cobrem a maior diversidade,
por isso o corpus final é "as primeiras k desta ordenação" para qualquer k.

    python -m benchmark.select_corpus            # ordena todas, propõe 15
    python -m benchmark.select_corpus --k 12
"""
from __future__ import annotations

import json
import math
import os
import sys
import urllib.request

# Excluir gems que nao sao "library standalone testavel":
#  - acopladas a Rails (dep runtime -> install pesado);
#  - plugins de ferramentas (rubocop, ...): o proposito e' estender a ferramenta,
#    testa-los isoladamente e' artificial;
#  - gigantes/auto-geradas (cap de tamanho): extremo matematico, nao codigo util.
RAILS_DEPS = {"rails", "activerecord", "activesupport", "railties", "actionpack",
              "activemodel", "actionview", "activejob", "actionmailer", "actioncable"}
PLUGIN_DEPS = {"rubocop", "rubocop-ast"}
EXCLUDE_DEPS = RAILS_DEPS | PLUGIN_DEPS
MAX_METHODS = 2000

FEATURES = [
    ("target_methods", "log"),
    ("avg_method_loc", "lin"),
    ("pct_singleton", "lin"),
    ("pct_duck_typed", "lin"),
    ("mixins_per_class", "lin"),
    ("max_ancestor_depth", "log"),
    ("metaprog_per_100methods", "lin"),
]
MAX_PER_CATEGORY = 2


def _feat(g, key):
    m = g.get("metrics", {})
    return m[key] if key in m else (g.get("code") or {}).get(key)


def _rails_coupling(gems) -> dict:
    """{gem: set(deps de Rails)} — via RubyGems API, cacheado em disco."""
    cache_path = "benchmark/results/rails_deps.json"
    cache = {}
    if os.path.exists(cache_path):
        cache = json.load(open(cache_path, encoding="utf-8"))
    changed = False
    for g in gems:
        name = g["gem"]
        if name in cache:
            continue
        try:
            req = urllib.request.Request(
                f"https://rubygems.org/api/v1/gems/{name}.json",
                headers={"User-Agent": "marta"})
            d = json.load(urllib.request.urlopen(req, timeout=15))
            deps = [x["name"] for x in d.get("dependencies", {}).get("runtime", [])]
        except Exception:
            deps = []
        cache[name] = sorted(EXCLUDE_DEPS & set(deps))
        changed = True
    if changed:
        os.makedirs("benchmark/results", exist_ok=True)
        json.dump(cache, open(cache_path, "w", encoding="utf-8"), indent=2)
    return {n: set(v) for n, v in cache.items()}


def _load():
    d = json.load(open("benchmark/results/population_diagnose.json", encoding="utf-8"))
    included = [g for g in d["gems"] if g["status"] == "included"]

    rails = _rails_coupling(included)
    survivors, n_rails, n_big = [], 0, 0
    for g in included:
        if rails.get(g["gem"]):
            n_rails += 1
            continue
        if g["metrics"]["target_methods"] > MAX_METHODS:
            n_big += 1
            continue
        survivors.append(g)
    print(f"Refinamento: {len(included)} incluidas -> excluidas {n_rails} acopladas "
          f"a Rails + {n_big} gigantes/auto-geradas (>{MAX_METHODS} met.) = "
          f"{len(survivors)} elegiveis.\n")
    return survivors


def _matrix(gems):
    cols = {}
    for key, mode in FEATURES:
        vals = []
        for g in gems:
            v = _feat(g, key) or 0.0
            vals.append(math.log1p(v) if mode == "log" else float(v))
        lo, hi = min(vals), max(vals)
        rng = (hi - lo) or 1.0
        cols[key] = [(v - lo) / rng for v in vals]
    return [[cols[k][i] for k, _ in FEATURES] for i in range(len(gems))]


def _dist(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def farthest_first(gems, vecs, k):
    n = len(gems)
    centroid = [sum(v[j] for v in vecs) / n for j in range(len(FEATURES))]
    # semente determinística: a mais afastada do centróide (a mais "extrema")
    seed = max(range(n), key=lambda i: _dist(vecs[i], centroid))
    chosen = [seed]
    cat_count = {gems[seed]["section"]: 1}
    while len(chosen) < min(k, n):
        best, best_d = None, -1.0
        for i in range(n):
            if i in chosen:
                continue
            if cat_count.get(gems[i]["section"], 0) >= MAX_PER_CATEGORY:
                continue
            d = min(_dist(vecs[i], vecs[c]) for c in chosen)  # min-dist às escolhidas
            if d > best_d:
                best, best_d = i, d
        if best is None:  # todas as categorias saturadas -> relaxa a restrição
            for i in range(n):
                if i in chosen:
                    continue
                d = min(_dist(vecs[i], vecs[c]) for c in chosen)
                if d > best_d:
                    best, best_d = i, d
        chosen.append(best)
        cat_count[gems[best]["section"]] = cat_count.get(gems[best]["section"], 0) + 1
    return chosen


def main(k=15):
    gems = _load()
    vecs = _matrix(gems)
    order = farthest_first(gems, vecs, k)

    print(f"População incluída: {len(gems)} gems. Seleção farthest-first (k={k}):\n")
    hdr = (f"{'#':>2} {'gem':22s}{'categoria':26s}{'mét':>6s}{'loc/m':>6s}"
           f"{'sing%':>6s}{'duck%':>6s}{'mix':>5s}{'metap':>7s}")
    print(hdr)
    sel = []
    for rank, i in enumerate(order, 1):
        g = gems[i]
        c = g.get("code") or {}
        print(f"{rank:>2} {g['gem']:22s}{g['section'][:24]:26s}"
              f"{g['metrics']['target_methods']:>6}{c.get('avg_method_loc',0):>6.1f}"
              f"{c.get('pct_singleton',0):>6}{c.get('pct_duck_typed',0):>6}"
              f"{c.get('mixins_per_class',0):>5.1f}{c.get('metaprog_per_100methods',0):>7.1f}")
        sel.append({"rank": rank, "gem": g["gem"], "repo": g["repo"],
                    "section": g["section"], "downloads": g["downloads"],
                    "metrics": g["metrics"], "code": g.get("code")})

    # Quais das 12 ad-hoc originais foram recuperadas (validação)?
    original = {"money", "addressable", "jwt", "httparty", "i18n", "rubyzip",
                "faker", "liquid", "kramdown", "hashie", "public_suffix", "chronic"}
    picked = {s["gem"] for s in sel}
    print(f"\nDas 12 ad-hoc originais, recuperadas pela seleção sistemática: "
          f"{sorted(original & picked)}")

    with open("benchmark/results/corpus_selection.json", "w", encoding="utf-8") as f:
        json.dump({"k": k, "selected": sel}, f, indent=2)


if __name__ == "__main__":
    k = 15
    if "--k" in sys.argv:
        k = int(sys.argv[sys.argv.index("--k") + 1])
    main(k=k)

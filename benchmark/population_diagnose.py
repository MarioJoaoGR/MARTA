"""Diagnostica ESTATICAMENTE toda a população (build_population.py) e agrega.

Para cada gem: clone raso -> diagnóstico estático (parse + métricas de
diversidade; SEM bundle install, SEM correr testes) -> APAGA o clone. Nada fica
instalado no sistema; o disco é libertado à medida.

Critérios de inclusão aplicados aqui (reprodutíveis):
  * tem lib/ (é library gem)          * clona sem erro
  * 0 erros de parse                  * >= MIN_METHODS métodos-alvo

Saída: benchmark/results/population_diagnose.json — a base de dados a partir da
qual se faz a seleção estratificada (a seleção deixa de ser juízo).

    python -m benchmark.population_diagnose            # tudo
    python -m benchmark.population_diagnose --limit 20 # amostra p/ testar
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile

from benchmark.diagnose import diagnose

MIN_METHODS = 15          # gems minúsculas não dão sinal
# Nomes que não são library gems testáveis (frameworks/ferramentas/meta).
EXCLUDE = {"rails", "rake", "rspec", "minitest", "bundler", "rubocop-ast",
           "rubygems-update", "did_you_mean", "power_assert", "test-unit"}


def _git(root: str, *args) -> str:
    try:
        r = subprocess.run(["git", "-C", root, *args], capture_output=True,
                           text=True, errors="replace", timeout=20)
        return r.stdout.strip()
    except Exception:
        return ""


def clone(url: str, dest: str) -> bool:
    try:
        r = subprocess.run(["git", "clone", "--depth", "1", url, dest],
                           capture_output=True, text=True, errors='replace', timeout=120)
        return r.returncode == 0
    except Exception:
        return False


def main(limit=None):
    with open("benchmark/results/population.json", encoding="utf-8") as f:
        pop = json.load(f)["gems"]
    pop = [p for p in pop if p["gem"] not in EXCLUDE]
    if limit:
        pop = pop[:limit]

    work = tempfile.mkdtemp(prefix="marta_pop_")
    results, kept, skipped = [], 0, 0
    try:
        for i, p in enumerate(pop):
            dest = os.path.join(work, p["gem"])
            ok = clone(p["clone"], dest)
            if not ok:
                results.append({**p, "status": "clone_failed"})
                skipped += 1
            else:
                try:
                    d = diagnose(dest)  # estático (sem cobertura)
                    # Motivo explícito da exclusão: sem isto o funil tem um passo
                    # opaco ("9 gems saíram, não sabemos porquê") — e recomputá-lo
                    # depois só funciona enquanto as métricas estiverem frescas.
                    motivos = []
                    if "files" not in d:
                        motivos.append("sem lib/ nem src/")
                    else:
                        if d["target_methods"] < MIN_METHODS:
                            motivos.append(f"menos de {MIN_METHODS} metodos")
                        if d["parse_errors"] > 0:
                            motivos.append(f"{d['parse_errors']} erros de leitura")
                    d_status = "excluded" if motivos else "included"
                    skipped, kept = (skipped + 1, kept) if motivos else (skipped, kept + 1)
                    results.append({**p, "status": d_status,
                                    "excluded_by": motivos or None,
                                    # ramo e commit: clonar o ramo por omissão é uma
                                    # suposição, e o active_model_serializers mostrou
                                    # que ele pode não trazer código nenhum.
                                    "branch": _git(dest, "rev-parse", "--abbrev-ref", "HEAD"),
                                    "commit": _git(dest, "rev-parse", "HEAD")[:12],
                                    "metrics": {k: d.get(k) for k in
                                                ("files", "loc", "target_methods",
                                                 "classes", "call_graph_edges",
                                                 "parse_errors")},
                                    "code": d.get("code")})
                except Exception as e:
                    results.append({**p, "status": f"error:{type(e).__name__}"})
                    skipped += 1
                shutil.rmtree(dest, ignore_errors=True)  # limpa JA
            if i % 10 == 0:
                print(f"  {i}/{len(pop)}  incluidas={kept} excluidas={skipped}", flush=True)
    finally:
        shutil.rmtree(work, ignore_errors=True)  # limpeza total garantida

    os.makedirs("benchmark/results", exist_ok=True)
    with open("benchmark/results/population_diagnose.json", "w", encoding="utf-8") as f:
        json.dump({"total": len(pop), "included": kept, "gems": results}, f, indent=2)
    print(f"\nDIAGNOSTICO: {kept} incluidas de {len(pop)} (population.json). "
          f"Clones apagados. Resultado em benchmark/results/population_diagnose.json")


if __name__ == "__main__":
    lim = None
    if "--limit" in sys.argv:
        lim = int(sys.argv[sys.argv.index("--limit") + 1])
    main(limit=lim)

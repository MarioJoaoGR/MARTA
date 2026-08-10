"""Seleciona os FICHEIROS-alvo dentro de cada projeto do corpus.

Porquê: testar todos os métodos de todos os ficheiros dos 12 projetos são 5876
alvos (~114h de LLM por run) — impraticável, e desnecessário. O estado da arte
faz o mesmo: o benchmark Python (herdado do CodaMosa) tem **486 módulos** em 27
projetos, não os projetos inteiros. Nem todo o ficheiro vale a pena testar.

Critérios de inclusão de um ficheiro (objetivos e reprodutíveis):
  * >= MIN_METHODS métodos      — ficheiros triviais não medem nada
  * <= MAX_METHODS métodos      — mega-ficheiros (tipicamente dados/gerados)
  * tem lógica: pelo menos um método com ramificação (if/case/while/rescue),
    medido pelos calls do parser — ficheiros de puro `attr_reader`/constantes
    não exercitam a ferramenta
  * exclui caminhos óbvios de não-lógica (version.rb, locale/, data/)

Depois ordena os ficheiros elegíveis por densidade de lógica e escolhe os
primeiros até esgotar o orçamento de métodos do projeto.

    python -m benchmark.select_targets --budget 40
    python -m benchmark.select_targets --budget 40 --corpus benchmark/results/corpus_final.json
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import sys

from marta.ruby_backend.ruby_ast import RubyParseError, parse_file

MIN_METHODS = 3
# Teto alto: o sinal de "ficheiro de dados/gerado" NÃO é o tamanho, é a baixa
# densidade de lógica (ver MIN_LOGIC_RATIO). Um teto baixo excluía ficheiros
# legítimos — a `parallel` é uma gem de ficheiro único com 51 métodos, 44 deles
# com lógica, e ficava de fora.
MAX_METHODS = 120
MIN_LOGIC_RATIO = 0.35   # % mínima de métodos com lógica (filtra dados/gerado)
# Caminhos que quase nunca contêm lógica testável.
SKIP_PATH_TOKENS = ("version.rb", "/locale/", "/locales/", "/data/", "/generated/",
                    "/vendor/", "/templates/")
# Chamadas que denunciam ramificação/lógica no corpo de um método.
BRANCHY = {"raise", "fail", "then", "map", "select", "reject", "each", "reduce",
           "detect", "find", "sort", "gsub", "sub", "match", "split", "fetch"}


def file_stats(path: str) -> dict | None:
    """Métricas de um ficheiro: nº métodos, nº com lógica, densidade."""
    try:
        fp = parse_file(path)
    except RubyParseError:
        return None
    if fp.errors:
        return None
    methods = [m for m in fp.methods if m.name != "initialize"]
    if not methods:
        return None
    with_logic = 0
    total_calls = 0
    for m in methods:
        calls = m.calls or []
        total_calls += len(calls)
        # heurística de lógica: chama algo (não é puro getter) e o corpo tem
        # mais que uma linha
        if (m.end_line - m.start_line) >= 2 and (
                len(calls) >= 2 or any(c["name"] in BRANCHY for c in calls)):
            with_logic += 1
    return {"methods": len(methods), "with_logic": with_logic,
            "calls_per_method": round(total_calls / len(methods), 2)}


def eligible(path: str, st: dict) -> bool:
    low = path.replace(os.sep, "/").lower()
    if any(tok in low for tok in SKIP_PATH_TOKENS):
        return False
    if not (MIN_METHODS <= st["methods"] <= MAX_METHODS):
        return False
    if st["with_logic"] < 2:
        return False
    return (st["with_logic"] / st["methods"]) >= MIN_LOGIC_RATIO


def select_for_project(proj_dir: pathlib.Path, source_path: str, budget: int) -> dict:
    src = proj_dir / source_path
    files = sorted(str(p) for p in src.glob("**/*.rb"))
    scored = []
    for f in files:
        st = file_stats(f)
        if st is None or not eligible(f, st):
            continue
        rel = os.path.relpath(f, src)
        # ordenar por densidade de lógica (proporção de métodos com lógica,
        # desempate por chamadas/método): ficheiros mais "interessantes" primeiro
        score = (st["with_logic"] / st["methods"], st["calls_per_method"])
        scored.append((score, rel, st))
    scored.sort(key=lambda x: x[0], reverse=True)

    chosen, used = [], 0
    for _score, rel, st in scored:
        # o primeiro ficheiro entra sempre (gems de ficheiro único ficariam
        # sem alvos se o ficheiro sozinho excedesse o orçamento)
        if used >= budget and chosen:
            break
        chosen.append({"file": rel, **st})
        used += st["methods"]
    return {"eligible_files": len(scored), "selected_files": len(chosen),
            "selected_methods": used, "files": chosen}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--budget", type=int, default=40,
                    help="máximo de métodos-alvo por projeto (default 40)")
    ap.add_argument("--corpus", default="benchmark/results/corpus_final.json")
    ap.add_argument("--projects-dir", default=None,
                    help="onde estão os clones (default: sondagens/targets)")
    ap.add_argument("--out", default="benchmark/results/targets.json")
    args = ap.parse_args()

    corpus = json.load(open(args.corpus, encoding="utf-8"))["corpus"]
    base = pathlib.Path(args.projects_dir or "sondagens/targets")

    out, total = {}, 0
    print(f"{'gem':18s}{'elegíveis':>11s}{'escolhidos':>12s}{'métodos':>9s}")
    for c in corpus:
        proj = base / c["gem"]
        if not proj.is_dir():
            print(f"{c['gem']:18s}  (não clonado — saltado)")
            continue
        src = "lib" if (proj / "lib").is_dir() else "src"
        r = select_for_project(proj, src, args.budget)
        r["source_path"] = src
        out[c["gem"]] = r
        total += r["selected_methods"]
        print(f"{c['gem']:18s}{r['eligible_files']:>11}{r['selected_files']:>12}"
              f"{r['selected_methods']:>9}")

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    json.dump({"budget_per_project": args.budget, "total_methods": total,
               "projects": out}, open(args.out, "w", encoding="utf-8"), indent=2)
    print(f"\nTOTAL: {total} métodos-alvo (era 5876 sem seleção) → {args.out}")


if __name__ == "__main__":
    sys.exit(main())

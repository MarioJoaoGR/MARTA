"""Que métodos é que a ablação do grafo tem mesmo de repetir.

O grafo de chamadas entra em DOIS sítios da Fase 1, e em mais nenhum:

  1. a 2ª passagem do ``done_what``, que junta ao contexto de um método o que os
     métodos CHAMADOS fazem;
  2. a propagação do ``what_todo``, em que um método herda a perspetiva de
     requisito de quem o CHAMA.

Logo, desligar o grafo só muda o prompt de um método se ele tiver um chamado ou
um chamador que também seja alvo. Para os outros, o contexto sai igual e repetir
a geração seria pagar horas de GPU para medir ruído do modelo.

Este programa calcula esse conjunto **localmente, sem chamar o modelo**, com o
mesmo resolver da ferramenta e a mesma análise da camada 2. O resultado diz, antes
de reservar tempo de cluster, quanto custa o braço da ablação.

    python -m benchmark.alvos_ablacao
    python -m benchmark.alvos_ablacao --out /tmp/ablacao.json
"""
from __future__ import annotations

import argparse
import gzip
import json
import os
import pathlib
import sys
from collections import defaultdict

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from benchmark import prepare_ruby_projects as prep            # noqa: E402
from marta.ruby_backend.call_graph import StaticCallGraph      # noqa: E402
from marta.ruby_backend.param_types import ProjectTypeIndex    # noqa: E402
from marta.ruby_backend.project import SKIP_METHODS            # noqa: E402
from marta.ruby_backend.ruby_ast import _from_json             # noqa: E402

ANALISE = REPO / "apresentacao" / "demo_dataset" / "2_parser" / "analise_completa.jsonl.gz"
SAIDA = REPO / "apresentacao" / "demo_dataset" / "7_selecao" / "ablacao.json"


def por_gem(gems: set) -> dict:
    """gem -> lista de ficheiros analisados pela camada 2 (com métodos e classes)."""
    fora = defaultdict(list)
    with gzip.open(ANALISE, "rt", encoding="utf-8") as f:
        for linha in f:
            d = json.loads(linha)
            if d["gem"] in gems:
                fora[d["gem"]].append(d)
    return fora


def afetados(ficheiros: list, alvos: set) -> dict:
    """Para uma gem: quais dos métodos-alvo mudam de prompt sem o grafo.

    `alvos` são os ficheiros-alvo. Um método conta como afetado se chamar, ou for
    chamado por, um método que viva noutro ficheiro-alvo **ou no mesmo** — a 2ª
    passagem não distingue, basta o chamado ser alvo.
    """
    idx, metodos, dono = ProjectTypeIndex(), [], {}
    for d in ficheiros:
        fp = _from_json({"path": d["ficheiro"], "classes": d["classes"],
                         "methods": d["metodos"], "examples": [],
                         "groups": [], "errors": []})
        idx.add_file(fp)
        for m in fp.methods:
            metodos.append(m)
            dono[m.qualified_name] = d["ficheiro"]

    # Os alvos da ferramenta: métodos de ficheiros-alvo, menos os saltados.
    alvo_qns = {m.qualified_name for m in metodos
                if dono.get(m.qualified_name) in alvos and m.name not in SKIP_METHODS}

    g = StaticCallGraph.build(metodos, idx)
    chama, chamado_por = defaultdict(set), defaultdict(set)
    for e in g.edges:
        if e.caller in alvo_qns and e.callee in alvo_qns and e.caller != e.callee:
            chama[e.caller].add(e.callee)
            chamado_por[e.callee].add(e.caller)

    linhas = {}
    for qn in sorted(alvo_qns):
        c1, c2 = len(chama.get(qn, ())), len(chamado_por.get(qn, ()))
        if c1 or c2:
            linhas[qn] = {"ficheiro": dono[qn], "chama": c1, "chamado_por": c2}
    return {"alvos": len(alvo_qns), "afetados": linhas}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--manifest", default=str(prep.PROJETOS))
    ap.add_argument("--out", default=str(SAIDA))
    args = ap.parse_args()

    projetos = prep.carrega_projetos(pathlib.Path(args.manifest))
    ficheiros = por_gem(set(projetos))

    fora, tot_alvos, tot_afetados = {}, 0, 0
    for gem in sorted(projetos):
        alvos = {a["ficheiro"] for a in projetos[gem]["alvos"]}
        r = afetados(ficheiros.get(gem, []), alvos)
        fora[gem] = r
        tot_alvos += r["alvos"]
        tot_afetados += len(r["afetados"])

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump({"_nota": "metodos cujo prompt muda sem o grafo (ver docstring)",
                   "total_alvos": tot_alvos, "total_afetados": tot_afetados,
                   "gems": fora}, f, indent=1, ensure_ascii=False)

    pct = 100 * tot_afetados / tot_alvos if tot_alvos else 0
    print(f"métodos-alvo:        {tot_alvos}")
    print(f"afetados pelo grafo: {tot_afetados}  ({pct:.1f}%)")
    print(f"→ o braço da ablação só precisa de repetir estes {tot_afetados}")
    piores = sorted(fora.items(), key=lambda kv: -len(kv[1]["afetados"]))[:5]
    for gem, r in piores:
        print(f"   {gem}: {len(r['afetados'])}/{r['alvos']}")
    print(f"gravado em {args.out}")


if __name__ == "__main__":
    main()

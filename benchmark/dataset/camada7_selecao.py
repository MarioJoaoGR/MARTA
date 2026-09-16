"""Camada 7: seleccao do corpus, com grupos ligados e diversidade.

O problema que esta camada resolve, e que so se viu depois de medir: a MARTA
constroi contexto ENTRE modulos (a 2a passagem dos sumarios anexa o `done_what`
dos metodos chamados, e o `what_todo` propaga-se do chamador para o chamado),
mas esse enriquecimento so funciona quando o chamado TAMBEM e alvo.

Uma seleccao puramente por diversidade escolhe os modulos mais afastados uns dos
outros, ou seja os que menos se chamam. Medido no corpus anterior, de 500
modulos escolhidos so por diversidade:

    49,9% das arestas ficavam dentro do mesmo modulo
     5,1% chegavam a outro modulo do corpus     <- o unico caso que enriquece
    45,0% apontavam para fora do corpus         <- perdidas

Ou seja, a avaliacao desligava metade daquilo que distingue a ferramenta. E nao
e simetrico: uma ferramenta de busca (Pynguin) gera por modulo e nao perde nada
com modulos dispersos.

A correccao NAO e fazer dois corpora — isso tornaria a comparacao confundida.
E fazer UM corpus com duas origens e etiquetar cada modulo, para a diferenca
poder ser medida no fim, dentro do mesmo conjunto:

    parte 1   GRUPOS INTEIROS (componentes ligadas do grafo, 3 a 20 modulos),
              escolhidos entre si por diversidade das caracteristicas agregadas
    parte 2   MODULOS SOLTOS, por diversidade, do resto da populacao

Cada linha do corpus leva `componente`, `tamanho_componente` e
`vizinhos_no_corpus`, o que permite reportar a cobertura repartida por modulos
com e sem vizinhos, e responder a "o contexto entre modulos ajuda?" com dados.

    python -m benchmark.dataset.camada7_selecao
"""
from __future__ import annotations

import csv
import gzip
import json
import math
import os
import sys
from collections import defaultdict
from datetime import date

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, RAIZ)

from marta.ruby_backend.call_graph import StaticCallGraph        # noqa: E402
from marta.ruby_backend.param_types import ProjectTypeIndex      # noqa: E402
from marta.ruby_backend.ruby_ast import _from_json               # noqa: E402

D = os.path.join(RAIZ, "apresentacao", "demo_dataset")
OUT = os.path.join(D, "7_selecao")

ORCAMENTO = 500          # alvo total (o utilizador fixou 400-600)
FATIA_GRUPOS = 0.5       # metade do orcamento vem de grupos inteiros
MIN_GRUPO, MAX_GRUPO = 3, 20

NUMERICAS = ["loc_medio", "pct_singleton", "pct_duck", "mixins_por_classe",
             "profundidade_heranca", "metaprog_por_100", "formas"]


# --------------------------------------------------------------- diversidade
def normaliza(itens, campos):
    """Cada valor vira a sua posicao relativa em [0,1].

    Por POSICAO e nao por min-max: a metaprogramacao vai de 0 a 800 e um so
    modulo extremo esmagava a escala toda.
    """
    for c in campos:
        vals = sorted({float(i[c]) for i in itens})
        pos = {v: (n / (len(vals) - 1) if len(vals) > 1 else 0.0)
               for n, v in enumerate(vals)}
        for i in itens:
            i["_" + c] = pos[float(i[c])]


def distancia(a, b, campos):
    d = sum((a["_" + c] - b["_" + c]) ** 2 for c in campos)
    if a["categoria"] != b["categoria"]:
        d += 1.0                     # pesa como uma caracteristica no maximo
    return math.sqrt(d)


def farthest_first(itens, campos, para):
    """Guloso: semente = o mais tipico, depois sempre o mais afastado do que ja
    foi escolhido. `para(escolhidos)` diz quando chega."""
    centro = {"_" + c: sum(i["_" + c] for i in itens) / len(itens) for c in campos}
    semente = min(itens, key=lambda i: math.sqrt(
        sum((i["_" + c] - centro["_" + c]) ** 2 for c in campos)))
    escolhidos = [semente]
    dmin = {id(i): distancia(i, semente, campos) for i in itens}
    restantes = [i for i in itens if i is not semente]
    while restantes and not para(escolhidos):
        alvo = max(restantes, key=lambda i: dmin[id(i)])
        escolhidos.append(alvo)
        restantes.remove(alvo)
        for i in restantes:
            d = distancia(i, alvo, campos)
            if d < dmin[id(i)]:
                dmin[id(i)] = d
    return escolhidos


# ------------------------------------------------------------ componentes
def componentes():
    """gem -> lista de conjuntos de ficheiros ligados entre si.

    Grafo ao nivel do MODULO: M1 liga-se a M2 se um metodo de M1 chamar um
    metodo de M2. Usa o mesmo resolver da ferramenta, nao uma aproximacao.
    """
    carregam = defaultdict(set)
    with open(f"{D}/6_carregamento/carregam.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            carregam[r["gem"]].add(r["ficheiro"])

    porgem = defaultdict(list)
    with gzip.open(f"{D}/2_parser/analise_completa.jsonl.gz", "rt",
                   encoding="utf-8") as f:
        for linha in f:
            d = json.loads(linha)
            if d["gem"] in carregam:
                porgem[d["gem"]].append(d)

    fora = {}
    for gem, ficheiros in porgem.items():
        idx, metodos, dono = ProjectTypeIndex(), [], {}
        for d in ficheiros:
            fp = _from_json({"path": d["ficheiro"], "classes": d["classes"],
                             "methods": d["metodos"], "examples": [],
                             "groups": [], "errors": []})
            idx.add_file(fp)
            for m in fp.methods:
                metodos.append(m)
                dono[m.qualified_name] = d["ficheiro"]
        g = StaticCallGraph.build(metodos, idx)
        elig = carregam[gem]
        adj = defaultdict(set)
        for e in g.edges:
            a, b = dono.get(e.caller), dono.get(e.callee)
            if a in elig and b in elig and a != b:
                adj[a].add(b)
                adj[b].add(a)
        visto, comps = set(), []
        for m in sorted(elig):
            if m in visto:
                continue
            pilha, comp = [m], set()
            while pilha:
                x = pilha.pop()
                if x in comp:
                    continue
                comp.add(x)
                visto.add(x)
                pilha.extend(adj[x] - comp)
            comps.append(comp)
        fora[gem] = comps
    return fora


def main() -> None:
    os.makedirs(OUT, exist_ok=True)
    with open(f"{D}/6_carregamento/carregam.csv", encoding="utf-8") as f:
        mods = list(csv.DictReader(f))
    por_chave = {(m["gem"], m["ficheiro"]): m for m in mods}
    print(f"populacao: {len(mods)} modulos que carregam")

    print("a construir os grafos por gem...", flush=True)
    comps = componentes()
    # etiquetar cada modulo com o seu componente
    grupos = []
    for gem, lista in comps.items():
        for n, comp in enumerate(lista):
            cid = f"{gem}#{n}"
            for f in comp:
                if (gem, f) in por_chave:
                    por_chave[(gem, f)]["componente"] = cid
                    por_chave[(gem, f)]["tamanho_componente"] = len(comp)
            if MIN_GRUPO <= len(comp) <= MAX_GRUPO:
                membros = [por_chave[(gem, f)] for f in sorted(comp)
                           if (gem, f) in por_chave]
                if membros:
                    grupos.append({"id": cid, "gem": gem,
                                   "categoria": membros[0]["categoria"],
                                   "membros": membros})
    for m in mods:
        m.setdefault("componente", "")
        m.setdefault("tamanho_componente", 1)
    print(f"componentes de {MIN_GRUPO} a {MAX_GRUPO} modulos: {len(grupos)}, "
          f"{sum(len(g['membros']) for g in grupos)} modulos, "
          f"{len({g['gem'] for g in grupos})} gems")

    # ---- parte 1: grupos inteiros, escolhidos por diversidade entre grupos --
    # As caracteristicas de um grupo sao a mediana das dos seus modulos; junta-se
    # o tamanho, porque um subsistema de 4 e diferente de um de 18.
    for g in grupos:
        for c in NUMERICAS:
            vals = sorted(float(m[c]) for m in g["membros"])
            g[c] = vals[len(vals) // 2]
        g["tamanho"] = len(g["membros"])
    campos_g = NUMERICAS + ["tamanho"]
    normaliza(grupos, campos_g)
    teto = int(ORCAMENTO * FATIA_GRUPOS)
    escolhidos_g = farthest_first(
        grupos, campos_g,
        para=lambda esc: sum(len(x["membros"]) for x in esc) >= teto)
    n_g = sum(len(x["membros"]) for x in escolhidos_g)
    print(f"parte 1: {len(escolhidos_g)} grupos, {n_g} modulos "
          f"(teto {teto})")

    # ---- parte 2: modulos soltos, por diversidade -------------------------
    ja = {(m["gem"], m["ficheiro"]) for g in escolhidos_g for m in g["membros"]}
    resto = [m for m in mods if (m["gem"], m["ficheiro"]) not in ja]
    normaliza(resto, NUMERICAS)
    falta = ORCAMENTO - n_g
    escolhidos_m = farthest_first(resto, NUMERICAS,
                                  para=lambda esc: len(esc) >= falta)
    print(f"parte 2: {len(escolhidos_m)} modulos soltos (faltavam {falta})")

    # ---- juntar e etiquetar ----------------------------------------------
    corpus = [m for g in escolhidos_g for m in g["membros"]] + escolhidos_m
    no_corpus = defaultdict(int)
    for m in corpus:
        if m["componente"]:
            no_corpus[m["componente"]] += 1
    for m in corpus:
        m["origem"] = "grupo" if m in [x for g in escolhidos_g for x in g["membros"]] \
            else "diversidade"
        m["vizinhos_no_corpus"] = max(0, no_corpus.get(m["componente"], 1) - 1)

    campos = [c for c in mods[0] if not c.startswith("_")]
    for extra in ("componente", "tamanho_componente", "origem", "vizinhos_no_corpus"):
        if extra not in campos:
            campos.append(extra)
    with open(f"{OUT}/corpus.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore")
        w.writeheader()
        w.writerows(sorted(corpus, key=lambda m: (m["gem"], m["ficheiro"])))

    with open(f"{OUT}/grupos.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["componente", "gem", "categoria", "modulos", "escolhido"])
        esc = {g["id"] for g in escolhidos_g}
        for g in sorted(grupos, key=lambda x: -len(x["membros"])):
            w.writerow([g["id"], g["gem"], g["categoria"], len(g["membros"]),
                        g["id"] in esc])

    # projetos.json: tudo o que o cluster precisa para correr este corpus, num so
    # ficheiro. Nao decide nada de novo, junta o que as camadas anteriores ja
    # decidiram: de onde vem o codigo (camada 2), em que ambiente cada modulo foi
    # certificado (camada 6) e quais sao os alvos (esta camada). O prepare, o
    # verificador e o harness leem todos daqui. Antes havia tres versoes do
    # ambiente, e nenhuma era a que certificou os modulos.
    with open(f"{D}/2_parser/parse.csv", encoding="utf-8") as f:
        origem_codigo = {r["gem"]: r for r in csv.DictReader(f)}
    with open(f"{D}/6_carregamento/gems.csv", encoding="utf-8") as f:
        receita = {r["gem"]: r for r in csv.DictReader(f)}
    gems_corpus = {m["gem"] for m in corpus}
    codigo = defaultdict(list)
    with gzip.open(f"{D}/2_parser/analise_completa.jsonl.gz", "rt",
                   encoding="utf-8") as f:
        for linha in f:
            d = json.loads(linha)
            if d["gem"] in gems_corpus:
                codigo[d["gem"]].append(d["ficheiro"])
    projetos = {"_gerado": f"camada 7, {date.today()}"}
    for gem in sorted(gems_corpus):
        o, r = origem_codigo[gem], receita[gem]
        raiz = o["raiz_codigo"] or "."
        # A camada 6 grava as pastas relativas a raiz do CLONE (activesupport/lib);
        # a ferramenta corre com cwd na raiz do codigo, por isso passam a relativas
        # a essa raiz (lib).
        pref = "" if raiz == "." else raiz.rstrip("/") + "/"
        load_paths = []
        for p in r["load_paths"].split():
            if pref and not p.startswith(pref):
                raise SystemExit(f"{gem}: pasta de carregamento {p} fora da raiz {raiz}")
            load_paths.append(p[len(pref):])
        projetos[gem] = {
            "repo": o["repo_usado"], "etiqueta": o["etiqueta"],
            "commit": o["commit"], "raiz": raiz,
            "ambiente": r["ambiente"], "deps": r["deps"].split(),
            "load_paths": load_paths,
            "entrada": "" if r["entrada"] in ("", "(sem porta)") else r["entrada"],
            "ficheiros_codigo": sorted(codigo[gem]),
            "alvos": [{"ficheiro": m["ficheiro"], "modo": m["modo"],
                       "origem": m["origem"], "componente": m["componente"],
                       "vizinhos_no_corpus": m["vizinhos_no_corpus"],
                       "metodos": int(m["metodos"])}
                      for m in sorted(corpus, key=lambda x: x["ficheiro"])
                      if m["gem"] == gem],
        }
    with open(f"{OUT}/projetos.json", "w", encoding="utf-8") as f:
        json.dump(projetos, f, indent=1, ensure_ascii=False)

    com = sum(1 for m in corpus if m["vizinhos_no_corpus"] > 0)
    funil = {
        "data": str(date.today()),
        "orcamento": ORCAMENTO, "fatia_grupos": FATIA_GRUPOS,
        "grupo_min": MIN_GRUPO, "grupo_max": MAX_GRUPO,
        "populacao": len(mods),
        "componentes_elegiveis": len(grupos),
        "grupos_escolhidos": len(escolhidos_g),
        "modulos_de_grupos": n_g,
        "modulos_soltos": len(escolhidos_m),
        "corpus": len(corpus),
        "gems": len({m["gem"] for m in corpus}),
        "categorias": len({m["categoria"] for m in corpus}),
        "metodos": sum(int(m["metodos"]) for m in corpus),
        "com_vizinhos_no_corpus": com,
        "sem_vizinhos_no_corpus": len(corpus) - com,
    }
    with open(f"{OUT}/funil.json", "w", encoding="utf-8") as f:
        json.dump(funil, f, indent=2, ensure_ascii=False)
    print("\n" + json.dumps(funil, indent=1))


if __name__ == "__main__":
    main()

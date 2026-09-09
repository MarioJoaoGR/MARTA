"""Camada 3: as oito caracteristicas de cada modulo.

Nao exclui nada e nao decide nada: e a fotografia da populacao antes de qualquer
corte. As mesmas nocoes que o `benchmark/diagnose.py` antigo media POR PROJETO,
agora POR MODULO, que foi a mudanca de unidade decidida.

Cada caracteristica esta aqui porque exercita uma parte DIFERENTE da ferramenta,
e nao porque era facil de medir:

    categoria do dominio    os sumarios e a busca por semelhanca
    linhas por metodo       o contexto enviado ao modelo, e o corte que o trunca
    % de singletons         o resolver do grafo (formas `const` e `self.class`)
    % de duck typing        a inferencia de tipos por uso, e o travao dos 5
    mixins por classe       a cadeia de ancestrais (include/prepend antes da
                            superclasse)
    profundidade de heranca a procura do metodo ao longo dessa cadeia
    metaprogramacao         o limite da analise estatica: metodos sem `def`
    formas distintas        o Planner, que inventa cenarios por estrutura

NOTA sobre a heranca: o Ruby quase nunca escreve o nome completo da superclasse
(dentro de `module Foo` escreve-se `class Bar < Base`). Casar so nomes completos
resolvia 5% das 11 819 superclasses e dava profundidade maxima 4, que era
artefacto da medicao. Resolver tambem pelo ultimo segmento leva isso a ~88%.

    python -m benchmark.dataset.camada3_caracteristicas
"""
from __future__ import annotations

import csv
import gzip
import json
import os
import statistics
from collections import Counter, defaultdict
from datetime import date

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = os.path.join(RAIZ, "apresentacao", "demo_dataset")
ENTRADA = os.path.join(D, "2_parser", "analise_completa.jsonl.gz")
OUT = os.path.join(D, "3_caracteristicas")

# As mesmas do benchmark/diagnose.py antigo, para as medicoes serem comparaveis.
METAPROG = {
    "define_method", "define_singleton_method", "method_missing",
    "respond_to_missing?", "send", "__send__", "public_send", "instance_eval",
    "class_eval", "module_eval", "instance_exec", "const_get", "const_set",
    "instance_variable_get", "instance_variable_set", "define_delegator",
    "def_delegator", "delegate", "method_added", "included", "extended",
    "inherited",
}
DUCK = {"lvar", "ivar", "getter"}      # recetores que so se resolvem por uso
ESCALOES = (1, 3, 6, 12, 25, 50)

NUMERICAS = ["loc_medio", "loc_max", "pct_singleton", "pct_duck",
             "mixins_por_classe", "profundidade_heranca", "metaprog_por_100",
             "metodos", "classes", "formas", "razao_formas"]


def escalao(n: int) -> int:
    for i, teto in enumerate(ESCALOES):
        if n <= teto:
            return i
    return len(ESCALOES)


def forma(m) -> tuple:
    """(nº parametros, nomes chamados, escalao de tamanho).

    O escalao entrou depois de medir: 15,6% dos metodos nao chamam nada e
    colapsavam todos na mesma forma. Um ficheiro da `rouge` tinha 14 metodos de
    3 a 122 linhas contados como um so. Com o escalao, os grupos com dispersao
    de tamanho >2,0 passam de 4,2% para 0%, e o total de formas sobe 1,3%.
    """
    ch = tuple(c.get("name") for c in (m.get("calls") or []))
    linhas = max(1, m["end_line"] - m["start_line"] + 1)
    return (len(m.get("params") or []), ch, escalao(linhas))


def main() -> None:
    os.makedirs(OUT, exist_ok=True)
    with gzip.open(ENTRADA, "rt", encoding="utf-8") as f:
        registos = [json.loads(L) for L in f]

    # Indice de superclasses por gem: a heranca atravessa ficheiros.
    pai, todas = defaultdict(dict), defaultdict(set)
    por_ultimo = defaultdict(lambda: defaultdict(set))
    for d in registos:
        for c in d["classes"]:
            qn = c["qualified_name"]
            todas[d["gem"]].add(qn)
            por_ultimo[d["gem"]][qn.split("::")[-1]].add(qn)
            if c.get("superclass"):
                pai[d["gem"]][qn] = c["superclass"]

    def resolve(gem, nome):
        nome = nome.lstrip(":")
        if nome in todas[gem]:
            return nome
        cands = por_ultimo[gem].get(nome.split("::")[-1], ())
        return next(iter(cands)) if len(cands) == 1 else None

    def profundidade(gem, qn):
        visto, n = set(), 0
        while qn in pai[gem] and qn not in visto:
            visto.add(qn)
            alvo = resolve(gem, pai[gem][qn])
            if not alvo:
                return n + 1                  # sobe para fora do projeto
            qn, n = alvo, n + 1
        return n

    linhas = []
    for d in registos:
        ms, cls = d["metodos"], d["classes"]
        if not ms:
            continue
        n = len(ms)
        comp = [max(1, m["end_line"] - m["start_line"] + 1) for m in ms]
        chamadas = [c for m in ms for c in (m.get("calls") or [])]
        formas = {forma(m) for m in ms}
        duck = sum(1 for m in ms
                   if any((m.get("param_members") or {}).values())
                   or any(c.get("recv") in DUCK for c in (m.get("calls") or [])))
        mixins = sum(len(c.get("includes") or []) + len(c.get("extends") or [])
                     + len(c.get("prepends") or []) for c in cls)
        meta = sum(1 for c in chamadas if c.get("name") in METAPROG)
        prof = max([profundidade(d["gem"], c["qualified_name"]) for c in cls] or [0])
        linhas.append({
            "gem": d["gem"], "ficheiro": d["ficheiro"], "commit": d["commit"],
            "categoria": d["categoria"],
            "loc_medio": round(statistics.mean(comp), 1), "loc_max": max(comp),
            "pct_singleton": round(100 * sum(1 for m in ms if m.get("singleton")) / n),
            "pct_duck": round(100 * duck / n),
            "mixins_por_classe": round(mixins / len(cls), 2) if cls else 0.0,
            "profundidade_heranca": prof,
            "metaprog_por_100": round(100 * meta / n, 1),
            "metodos": n, "classes": len(cls),
            "formas": len(formas),
            "razao_formas": round(len(formas) / n, 3),
        })

    with open(f"{OUT}/modulos.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0].keys()))
        w.writeheader()
        w.writerows(sorted(linhas, key=lambda r: (r["gem"], r["ficheiro"])))

    def dist(chave):
        vs = sorted(float(r[chave]) for r in linhas)
        q = statistics.quantiles(vs, n=4)
        return {"min": vs[0], "q1": round(q[0], 2), "mediana": round(q[1], 2),
                "q3": round(q[2], 2), "max": vs[-1],
                "media": round(statistics.mean(vs), 2)}

    resumo = {
        "data": str(date.today()),
        "modulos_com_metodos": len(linhas),
        "gems": len({r["gem"] for r in linhas}),
        "categorias": len({r["categoria"] for r in linhas}),
        "distribuicoes": {k: dist(k) for k in NUMERICAS},
        "modulos_por_categoria": dict(Counter(r["categoria"] for r in linhas).most_common()),
        "modulos_por_gem": dict(Counter(r["gem"] for r in linhas).most_common()),
    }
    json.dump(resumo, open(f"{OUT}/distribuicoes.json", "w", encoding="utf-8"),
              indent=2, ensure_ascii=False)

    print(f"modulos com metodos: {len(linhas)}   gems: {resumo['gems']}   "
          f"categorias: {resumo['categorias']}\n")
    print(f"{'caracteristica':22s}{'min':>8s}{'q1':>8s}{'mediana':>9s}{'q3':>8s}{'max':>9s}")
    print("-" * 64)
    for k in NUMERICAS:
        d = resumo["distribuicoes"][k]
        print(f"{k:22s}{d['min']:>8}{d['q1']:>8}{d['mediana']:>9}{d['q3']:>8}{d['max']:>9}")


if __name__ == "__main__":
    main()

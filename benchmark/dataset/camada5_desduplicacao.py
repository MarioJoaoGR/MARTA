"""Camada 5: desduplicacao. Dois modulos sao o mesmo se partilharem MAIS de
metade das formas; guarda-se um representante, o maior.

A camada 4 olha para DENTRO de cada modulo. Esta olha ENTRE modulos: o ficheiro
do registo diario da `twilio-ruby` tem variedade interna que chega para passar a
camada 4, e o do registo mensal tambem, e sao o mesmo codigo.

Semelhanca de Jaccard entre os conjuntos de formas: quantas partilham a dividir
por quantas tem ao todo.

EMPATE ENTRA. Descarta-se so se a semelhanca for MAIOR que 0,50. Sem isso caiam
os repetidores de hora, minuto e segundo da `chronic`, que dao exactamente 0,50
e tem aritmetica diferente.

O limiar foi escolhido a ver a curva: entre 0,3 e 0,9 o numero de sobreviventes
mal se mexe, portanto a regra e robusta e nao foi afinada para dar jeito. Nas 16
gems de sondagem o efeito vinha quase todo da duplicacao exacta (678 -> 527); na
populacao completa nao: 0,5 remove 671 e a igualdade exacta so 216.

    python -m benchmark.dataset.camada5_desduplicacao
"""
from __future__ import annotations

import csv
import gzip
import json
import os
from collections import defaultdict
from datetime import date

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# MARTA_DATASET_DIR desvia os artefactos para outra pasta. Serve para verificar
# se uma camada reproduz o seu artefacto sem escrever por cima do que esta no
# repositorio (uma verificacao assim ja apanhou ficheiros por engano num commit).
D = os.environ.get("MARTA_DATASET_DIR") or \
    os.path.join(RAIZ, "apresentacao", "demo_dataset")
ANALISE = os.path.join(D, "2_parser", "analise_completa.jsonl.gz")
ELEG = os.path.join(D, "4_elegibilidade", "elegiveis.csv")
OUT = os.path.join(D, "5_desduplicacao")

LIMIAR = 0.50           # descarta so se a semelhanca for MAIOR que isto
VARRIMENTO = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.999]
ESCALOES = (1, 3, 6, 12, 25, 50)


def escalao(n):
    for i, teto in enumerate(ESCALOES):
        if n <= teto:
            return i
    return len(ESCALOES)


def carrega():
    with open(ELEG, encoding="utf-8") as f:
        quero = {(r["gem"], r["ficheiro"]): r for r in csv.DictReader(f)}
    fps = {}
    with gzip.open(ANALISE, "rt", encoding="utf-8") as f:
        for L in f:
            d = json.loads(L)
            k = (d["gem"], d["ficheiro"])
            if k not in quero:
                continue
            fps[k] = {(len(m.get("params") or []),
                       tuple(c.get("name") for c in (m.get("calls") or [])),
                       escalao(max(1, m["end_line"] - m["start_line"] + 1)))
                      for m in d["metodos"]}
    return quero, fps


def desduplica(chaves, fps, limiar, tamanho):
    """Guloso do maior para o menor, com indice invertido por forma: so se
    compara com quem partilha pelo menos uma forma (o resto tem semelhanca 0)."""
    ordem = sorted(chaves, key=lambda k: -tamanho[k])
    porforma = defaultdict(list)
    aceites, saem = [], {}
    for k in ordem:
        fa = fps[k]
        vistos = set()
        for f in fa:
            vistos.update(porforma.get(f, ()))
        melhor, quem = 0.0, None
        for j in vistos:
            fb = fps[j]
            inter = len(fa & fb)
            s = inter / (len(fa) + len(fb) - inter)
            if s > melhor:
                melhor, quem = s, j
        if melhor > limiar:                 # EMPATE ENTRA
            saem[k] = (quem, round(melhor, 3))
        else:
            aceites.append(k)
            for f in fa:
                porforma[f].append(k)
    return aceites, saem


def main() -> None:
    os.makedirs(OUT, exist_ok=True)
    quero, fps = carrega()
    chaves = list(fps)
    tamanho = {k: int(quero[k]["metodos"]) for k in chaves}
    print(f"elegiveis carregados: {len(chaves)}")

    with open(f"{OUT}/varrimento.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["limiar", "representantes", "duplicados_removidos"])
        for L in VARRIMENTO:
            ac, sa = desduplica(chaves, fps, L, tamanho)
            w.writerow([L, len(ac), len(sa)])
            print(f"  limiar {L}: {len(ac)} representantes, {len(sa)} removidos",
                  flush=True)

    aceites, saem = desduplica(chaves, fps, LIMIAR, tamanho)
    campos = list(next(iter(quero.values())).keys())
    with open(f"{OUT}/representantes.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore")
        w.writeheader()
        w.writerows(quero[k] for k in sorted(aceites))
    with open(f"{OUT}/duplicados.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos + ["copia_de", "semelhanca"],
                           extrasaction="ignore")
        w.writeheader()
        for k, (quem, s) in sorted(saem.items(), key=lambda kv: -kv[1][1]):
            w.writerow({**quero[k], "copia_de": f"{quem[0]}/{quem[1]}",
                        "semelhanca": s})

    porgem = defaultdict(lambda: [0, 0])
    for k in chaves:
        porgem[k[0]][0] += 1
    for k in aceites:
        porgem[k[0]][1] += 1
    funil = {"data": str(date.today()), "limiar": LIMIAR,
             "entram": len(chaves), "representantes": len(aceites),
             "duplicados_removidos": len(saem),
             "metodos": sum(int(quero[k]["metodos"]) for k in aceites),
             "gems": len({k[0] for k in aceites}),
             "categorias": len({quero[k]["categoria"] for k in aceites}),
             "maiores_quedas": sorted(
                 ({"gem": g, "antes": a, "depois": b}
                  for g, (a, b) in porgem.items() if a - b > 0),
                 key=lambda r: -(r["antes"] - r["depois"]))[:15]}
    json.dump(funil, open(f"{OUT}/funil.json", "w", encoding="utf-8"),
              indent=2, ensure_ascii=False)
    print("\n" + json.dumps({k: v for k, v in funil.items()
                             if k != "maiores_quedas"}, indent=1))
    print("\nmaiores quedas:")
    for r in funil["maiores_quedas"]:
        print(f"  {r['gem']:22s} {r['antes']:5d} -> {r['depois']:5d}")


if __name__ == "__main__":
    main()

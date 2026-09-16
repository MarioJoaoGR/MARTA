"""Camada 4: elegibilidade. Chao de 3 formas distintas, proporcao >= 0,4.

DUAS condicoes, e sao medidas de natureza DIFERENTE:

  chao (contagem)     >= 3 formas distintas
                      responde a "ha aqui materia que chegue?"
                      Como as formas nunca sao mais que os metodos, exigir 3
                      formas ja exige 3 metodos: dispensa o MIN_METHODS antigo.

  proporcao (racio)   formas / metodos >= 0,4
                      responde a "essa materia e variada?"
                      Sem ela passava o `geocoder/results/ipregistry.rb`: 71
                      metodos e 4 formas, porque 68 deles sao a mesma linha a ir
                      buscar um campo diferente.

Estas duas substituem TRES filtros da versao anterior — `MIN_METHODS`,
`MAX_METHODS` e `MIN_LOGIC_RATIO`. O `MAX_METHODS` morre porque um modulo grande
com muitas formas e rico e deve entrar (o `addressable/uri.rb` tem 88 metodos e
85 formas); um modulo grande com poucas formas sai por ser repetitivo, nao por
ser grande. O `MIN_LOGIC_RATIO=0.35` morre porque nao fazia o trabalho: deixava
passar 238 dos 390 modulos da `twilio-ruby`.

PORQUE 0,4 E NAO MAIS: acima disso comecam a cair os modulos mais ricos do
corpus, que sao grandes e por isso dificilmente chegam a proporcoes altas — o
`mail/message.rb` tem 180 metodos e 115 formas, o que da 0,64, e o terceiro
quartil da populacao sao 10 formas. Abaixo de 0,4 morre so codigo repetido.

Grava tambem os VARRIMENTOS que levaram aos dois numeros, para o documento poder
mostrar que foram escolhidos com a curva a frente.

    python -m benchmark.dataset.camada4_elegibilidade
"""
from __future__ import annotations

import csv
import json
import os
from datetime import date

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# MARTA_DATASET_DIR desvia os artefactos para outra pasta. Serve para verificar
# se uma camada reproduz o seu artefacto sem escrever por cima do que esta no
# repositorio (uma verificacao assim ja apanhou ficheiros por engano num commit).
D = os.environ.get("MARTA_DATASET_DIR") or \
    os.path.join(RAIZ, "apresentacao", "demo_dataset")
ENT = os.path.join(D, "3_caracteristicas", "modulos.csv")
OUT = os.path.join(D, "4_elegibilidade")

CHAO = 3         # formas distintas minimas (contagem)
X = 0.4          # formas / metodos minimo   (proporcao)

GRELHA_CHAO = [1, 2, 3, 4, 5, 6]
GRELHA_X = [0.0, 0.3, 0.4, 0.5, 0.6, 0.7]


def main() -> None:
    os.makedirs(OUT, exist_ok=True)
    with open(ENT, encoding="utf-8") as f:
        mods = list(csv.DictReader(f))
    for m in mods:
        m["metodos"] = int(m["metodos"])
        m["formas"] = int(m["formas"])
        m["razao_formas"] = float(m["razao_formas"])
    total_met = sum(m["metodos"] for m in mods)

    # ---- varrimentos: o estudo que justifica os dois numeros --------------
    with open(f"{OUT}/varrimento_grelha.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["chao_formas"] + [f"X={x}" for x in GRELHA_X])
        for c in GRELHA_CHAO:
            w.writerow([c] + [sum(1 for m in mods if m["formas"] >= c
                                  and m["razao_formas"] >= x) for x in GRELHA_X])

    with open(f"{OUT}/varrimento_chao.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["chao_formas", "sobram", "saem", "metodos_que_levam",
                    "pct_dos_metodos"])
        for c in GRELHA_CHAO:
            sai = [m for m in mods if m["formas"] < c]
            met = sum(m["metodos"] for m in sai)
            w.writerow([c, len(mods) - len(sai), len(sai), met,
                        round(100 * met / total_met, 1)])

    base = [m for m in mods if m["formas"] >= CHAO]
    with open(f"{OUT}/varrimento_prop.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["proporcao_minima", "sobram", "saem", "maior_que_sai",
                    "formas_do_maior_que_sai"])
        for x in GRELHA_X:
            sai = [m for m in base if m["razao_formas"] < x]
            maior = max(sai, key=lambda m: m["metodos"]) if sai else None
            w.writerow([x, len(base) - len(sai), len(sai),
                        f"{maior['gem']}/{maior['ficheiro']}" if maior else "",
                        maior["formas"] if maior else ""])

    # ---- aplicar ---------------------------------------------------------
    campos = list(mods[0].keys())
    elegiveis, excluidos = [], []
    for m in mods:
        motivos = []
        if m["formas"] < CHAO:
            motivos.append(f"menos de {CHAO} formas distintas")
        if m["razao_formas"] < X:
            motivos.append(f"proporcao {m['razao_formas']} abaixo de {X}")
        (excluidos if motivos else elegiveis).append(
            {**m, "excluido_por": "; ".join(motivos)} if motivos else m)

    for nome, dados, cs in (("elegiveis.csv", elegiveis, campos),
                            ("excluidos.csv",
                             sorted(excluidos, key=lambda m: -m["metodos"]),
                             campos + ["excluido_por"])):
        with open(os.path.join(OUT, nome), "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=cs, extrasaction="ignore")
            w.writeheader()
            w.writerows(dados)

    so_chao = sum(1 for m in excluidos if "formas distintas" in m["excluido_por"]
                  and "proporcao" not in m["excluido_por"])
    so_prop = sum(1 for m in excluidos if "proporcao" in m["excluido_por"]
                  and "formas distintas" not in m["excluido_por"])
    funil = {"data": str(date.today()), "chao_formas": CHAO, "proporcao_minima": X,
             "entram": len(mods), "saem_pelo_chao": so_chao,
             "saem_pela_proporcao": so_prop,
             "saem_por_ambos": len(excluidos) - so_chao - so_prop,
             "elegiveis": len(elegiveis),
             "metodos_elegiveis": sum(m["metodos"] for m in elegiveis),
             "gems": len({m["gem"] for m in elegiveis}),
             "categorias": len({m["categoria"] for m in elegiveis})}
    json.dump(funil, open(f"{OUT}/funil.json", "w", encoding="utf-8"),
              indent=2, ensure_ascii=False)
    print(json.dumps(funil, indent=1))


if __name__ == "__main__":
    main()

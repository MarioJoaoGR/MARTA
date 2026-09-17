"""Porta RSpec: os modulos que carregam na camada 6 mas nao pela ferramenta.

A camada 6 certifica o carregamento com o seu proprio carregador. A MARTA-Ruby
corre o RSpec, e ha modulos que passam no primeiro e falham no segundo: um
exemplo que instala gems ao carregar (bundler/inline), um `require
"bundler/setup"` que le o Gemfile da pasta onde corre, um generator que precisa
do Rails, uma dependencia so de desenvolvimento. Num corpus, um modulo destes
nao so falha: ao ser carregado com os outros alvos da gem, apaga a cobertura
deles tambem (no puma e no spring, 49 modulos que carregavam ficavam sem
cobertura por causa de 6).

A porta corre-se sobre a POPULACAO inteira, e a camada 7 so escolhe entre os
modulos que passam:

    # 1. manifesto da populacao inteira (numa pasta fora do repositorio)
    MARTA_DATASET_DIR=/tmp/pop MARTA_ORCAMENTO=<populacao> MARTA_FATIA_GRUPOS=0 \\
        python -m benchmark.dataset.camada7_selecao
    # 2. preparar e verificar pela ferramenta
    python -m benchmark.prepare_ruby_projects --out /tmp/rp --manifest /tmp/pop/7_selecao/projetos.json
    python -m benchmark.verifica_ambiente --projects-dir /tmp/rp \\
        --manifest /tmp/pop/7_selecao/projetos.json --out /tmp/pop/verificacao.csv
    # 3. gravar os que falham, para a camada 7
    python -m benchmark.dataset.porta_rspec /tmp/pop/verificacao.csv

O passo 1 le o falham_rspec.csv se ja existir; para refazer a porta do zero,
apaga-lo primeiro.
"""
from __future__ import annotations

import csv
import json
import os
import sys
from datetime import date

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = os.environ.get("MARTA_DATASET_DIR") or \
    os.path.join(RAIZ, "apresentacao", "demo_dataset")
SAIDA = os.path.join(D, "6_carregamento", "falham_rspec.csv")


def main() -> None:
    with open(sys.argv[1], encoding="utf-8") as f:
        linhas = list(csv.DictReader(f))
    falham = [r for r in linhas if r["estado"] != "ok"]
    sem_cobertura = [r for r in linhas if r["estado"] == "ok" and r["na_cobertura"] != "True"]
    with open(SAIDA, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["gem", "ficheiro", "modo", "erro"])
        for r in sorted(falham, key=lambda r: (r["gem"], r["ficheiro"])):
            w.writerow([r["gem"], r["ficheiro"], r["modo"],
                        " ".join(r["erro"].split())[:300]])
    print(json.dumps({"data": str(date.today()), "verificados": len(linhas),
                      "falham": len(falham),
                      "carregam_sem_cobertura": len(sem_cobertura)}, indent=1))
    print(f"-> {SAIDA}")


if __name__ == "__main__":
    main()

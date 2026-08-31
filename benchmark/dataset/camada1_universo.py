"""Camada 1: o universo = awesome-ruby cruzado com o RubyGems.

Regra: a entrada tem gem publicada e a gem tem >= 100 milhoes de descargas.
Sem excludes de categoria, de nome ou de tipo de projeto. So se leem metadados
publicos: nada e clonado nem instalado.

Tres armadilhas que esta camada tem de tratar, e que custaram gems reais:

1. A chave de deduplicacao e a ENTRADA, nao o repo. O rails/rails aparece duas
   vezes na lista, como ActiveSupport e como ActiveRecord, e sao gems
   diferentes. Deduplicar por repo fazia desaparecer a segunda.

2. Quando o link aponta para uma SUBPASTA (/tree/), o nome da gem vem do texto
   do link e nao do nome do repo: "ActiveSupport" -> activesupport. Ler o nome
   do repo dava "rails", que e outra gem (e que a lista nem sequer propoe).

3. Quando o nome adivinhado nao existe no RubyGems, tentam-se variantes antes
   de desistir: mongo-ruby-driver -> mongo, CocoaPods -> cocoapods. Sem isto
   perdiam-se gems com mais de 100 milhoes de descargas por um palpite de nome.

    python -m benchmark.dataset.camada1_universo
    python -m benchmark.dataset.camada1_universo --dry   # so conta, nao consulta
"""
from __future__ import annotations

import csv
import json
import os
import re
import sys
import time
import urllib.request
from datetime import date

AWESOME = "https://raw.githubusercontent.com/markets/awesome-ruby/master/README.md"
MIN_DOWNLOADS = 100_000_000
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), "apresentacao", "demo_dataset", "1_universo")

# Exige dono/repo, e aceita opcionalmente /tree/<subpasta>. Sem os dois
# segmentos entram paginas de organizacao (github.com/dry-rb) e pesquisas
# (github.com/trending?l=ruby), que nao sao projetos.
LINHA = re.compile(
    r"^\s*[*-]\s*\[([^\]]+)\]\("
    r"(https://github\.com/[^)/#?]+/[^)/#?]+(?:/tree/[^)#?]+)?)/?[^)]*\)")
CABECALHO = re.compile(r"^#{2,4}\s+(.+?)\s*$")


def get(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "marta-benchmark"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "ignore")


def _limpo(s: str) -> str:
    """Nome de exibicao -> nome plausivel de gem."""
    return (s.strip().lower().replace("::", "-").replace(" ", "-")
            .replace("_", "-"))


def extrai(md: str):
    """[(gem_palpite, repo, subpasta, categoria)] — todas as seccoes."""
    out, seccao = [], "?"
    for line in md.splitlines():
        h = CABECALHO.match(line)
        if h:
            seccao = h.group(1).strip().lower()
            continue
        m = LINHA.match(line)
        if not m:
            continue
        nome, url = m.group(1), m.group(2).rstrip("/")
        partes = url.replace("https://github.com/", "").split("/tree/")
        repo = "/".join(partes[0].split("/")[:2])
        sub = partes[1] if len(partes) > 1 else ""
        if sub:
            # monorepo: a gem e a subpasta, e o nome vem do texto do link
            gem = _limpo(nome)
        else:
            gem = repo.split("/")[-1].removesuffix(".rb").removeprefix("ruby-")
        out.append((gem, repo, sub, seccao))
    return out


def variantes(gem: str, repo: str):
    """Outros nomes plausiveis, para quando o palpite nao existe."""
    base = repo.split("/")[-1]
    cands = [base, base.lower(),
             base.removesuffix("-ruby"), base.removesuffix("_ruby"),
             base.removeprefix("ruby-"), base.removeprefix("ruby_"),
             base.removesuffix("-rails"), base.removesuffix("-ruby-driver"),
             base.replace("-", "_"), base.replace("_", "-"),
             base.lower().replace("-", "_")]
    fora, vistos = [], {gem}
    for c in cands:
        if c and c not in vistos:
            vistos.add(c)
            fora.append(c)
    return fora


def rubygems(gem: str):
    try:
        d = json.loads(get(f"https://rubygems.org/api/v1/gems/{gem}.json", 15))
        return {"existe": True, "downloads": d.get("downloads", 0),
                "versao": d.get("version"),
                "licenca": (d.get("licenses") or [None])[0], "erro": ""}
    except Exception as e:
        cod = getattr(e, "code", None)
        return {"existe": False, "downloads": None, "versao": None,
                "licenca": None, "erro": f"HTTP {cod}" if cod else type(e).__name__}


def main(dry: bool = False) -> None:
    md = get(AWESOME)
    entradas = extrai(md)
    # Deduplicacao pela ENTRADA (repo + subpasta), nao pelo repo.
    vistos, uniq = set(), []
    for gem, repo, sub, sec in entradas:
        chave = (repo, sub)
        if chave not in vistos:
            vistos.add(chave)
            uniq.append((gem, repo, sub, sec))
    print(f"awesome-ruby: {len(entradas)} entradas, {len(uniq)} unicas, "
          f"{len({s for *_, s in uniq})} categorias")
    if dry:
        return

    os.makedirs(OUT, exist_ok=True)
    with open(f"{OUT}/awesome_ruby.md", "w", encoding="utf-8") as f:
        f.write(md)

    linhas = []
    for i, (gem, repo, sub, sec) in enumerate(uniq):
        info = rubygems(gem)
        corrigido = ""
        if not info["existe"]:
            for alt in variantes(gem, repo):
                alt_info = rubygems(alt)
                if alt_info["existe"]:
                    corrigido, gem, info = gem, alt, alt_info
                    break
        linhas.append({"gem": gem,
                       "repo": f"{repo}/tree/master/{sub}" if sub else repo,
                       "categoria": sec, "subpasta_de": repo if sub else "",
                       "nome_corrigido_de": corrigido, **info})
        if i % 50 == 0:
            print(f"  ... {i}/{len(uniq)}", flush=True)
        time.sleep(0.05)

    linhas.sort(key=lambda r: -(r["downloads"] or 0))
    campos = ["gem", "repo", "categoria", "existe", "downloads", "versao",
              "licenca", "erro", "nome_corrigido_de", "subpasta_de"]
    with open(f"{OUT}/candidatas.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore")
        w.writeheader()
        w.writerows(linhas)

    universo = [r for r in linhas if (r["downloads"] or 0) >= MIN_DOWNLOADS]
    with open(f"{OUT}/universo.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["gem", "repo", "categoria", "downloads",
                                          "versao", "licenca"], extrasaction="ignore")
        w.writeheader()
        w.writerows(universo)
    json.dump({"fonte": AWESOME, "data": str(date.today()),
               "min_downloads": MIN_DOWNLOADS, "total": len(universo),
               "gems": [{k: r[k] for k in ("gem", "repo", "categoria",
                                           "downloads", "versao", "licenca")}
                        for r in universo]},
              open(f"{OUT}/universo.json", "w", encoding="utf-8"),
              indent=2, ensure_ascii=False)

    sem = [r for r in linhas if not r["existe"]]
    abaixo = [r for r in linhas if r["existe"] and (r["downloads"] or 0) < MIN_DOWNLOADS]
    cats: dict = {}
    for r in universo:
        cats[r["categoria"]] = cats.get(r["categoria"], 0) + 1
    funil = {"data": str(date.today()), "fonte": AWESOME,
             "min_downloads": MIN_DOWNLOADS,
             "1_entradas_awesome_ruby": len(entradas),
             "2_entradas_unicas": len(uniq),
             "3_com_gem_no_rubygems": len(uniq) - len(sem),
             "4_acima_do_limiar": len(universo),
             "perdidas_sem_gem": len(sem),
             "perdidas_abaixo_do_limiar": len(abaixo),
             "nomes_corrigidos": sum(1 for r in linhas if r["nome_corrigido_de"]),
             "entradas_em_subpasta": sum(1 for r in linhas if r["subpasta_de"]),
             "categorias_no_universo": dict(sorted(cats.items(), key=lambda x: -x[1]))}
    json.dump(funil, open(f"{OUT}/funil.json", "w", encoding="utf-8"),
              indent=2, ensure_ascii=False)
    print(json.dumps({k: v for k, v in funil.items()
                      if k != "categorias_no_universo"}, indent=1))


if __name__ == "__main__":
    main(dry="--dry" in sys.argv)

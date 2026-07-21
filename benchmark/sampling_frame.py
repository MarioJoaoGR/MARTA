"""Verifica que o corpus cai dentro de um universo de amostragem OBJETIVO.

Universo = popularidade no RubyGems (medida reprodutível, não juízo nosso):
  * downloads totais   — RubyGems.org API (contínuo)
  * ranking de downloads — bestgems.org API (posição no ecossistema)

Critérios de inclusão aplicados (reprodutíveis):
  1. popularidade: rank de downloads <= TOP_N  (ou downloads >= MIN_DOWNLOADS)
  2. (verificados noutro sítio) instalável, tem suite, parseia sem erros

Produz a tabela de evidência para o paper: "selecionámos de entre as gems no
top-N de downloads que cumprem [critérios], estratificando por diversidade".

    python -m benchmark.sampling_frame
"""
from __future__ import annotations

import json
import urllib.request

# repo local -> nome no RubyGems (alguns diferem)
CORPUS = {
    "money": "money", "addressable": "addressable", "ruby-jwt": "jwt",
    "httparty": "httparty", "i18n": "i18n", "rubyzip": "rubyzip",
    "faker": "faker", "liquid": "liquid", "kramdown": "kramdown",
    "hashie": "hashie", "public_suffix": "public_suffix", "chronic": "chronic",
}

TOP_N = 200                  # limiar de ranking do universo de amostragem
MIN_DOWNLOADS = 100_000_000  # limiar alternativo (contínuo)


def _get_json(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "marta-benchmark"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


def downloads(gem: str):
    try:
        return _get_json(f"https://rubygems.org/api/v1/gems/{gem}.json").get("downloads")
    except Exception:
        return None


def total_rank(gem: str):
    """Rank de downloads totais mais recente (bestgems.org)."""
    try:
        hist = _get_json(f"https://bestgems.org/api/v1/gems/{gem}/total_ranking.json")
        return hist[0].get("total_ranking") if hist else None
    except Exception:
        return None


def main():
    rows = []
    for repo, gem in CORPUS.items():
        dl, rk = downloads(gem), total_rank(gem)
        in_frame = (rk is not None and rk <= TOP_N) or (dl is not None and dl >= MIN_DOWNLOADS)
        rows.append({"repo": repo, "gem": gem, "downloads": dl, "total_rank": rk,
                     "in_frame": in_frame})

    rows.sort(key=lambda r: (r["total_rank"] is None, r["total_rank"] or 1e9))

    print(f"Universo de amostragem: RubyGems, top-{TOP_N} por downloads totais "
          f"(bestgems.org) OU >= {MIN_DOWNLOADS:,} downloads\n")
    print(f"{'repo':16s}{'gem':16s}{'rank':>7s}{'downloads':>16s}   frame")
    all_in = True
    for r in rows:
        rk = r["total_rank"]
        dl = r["downloads"]
        mark = "OK" if r["in_frame"] else "FORA"
        all_in &= r["in_frame"]
        print(f"{r['repo']:16s}{r['gem']:16s}{(rk if rk else '?'):>7}"
              f"{(f'{dl:,}' if dl else '?'):>16}   {mark}")

    ranks = [r["total_rank"] for r in rows if r["total_rank"]]
    print()
    if ranks:
        print(f"Amplitude de ranking do corpus: #{min(ranks)}–#{max(ranks)} "
              f"(de todas as gems Ruby, por downloads totais).")
    print(f"Corpus inteiro dentro do universo (top-{TOP_N} / >={MIN_DOWNLOADS:,}): "
          f"{'SIM' if all_in else 'NAO — rever'}")

    import os
    os.makedirs("benchmark/results", exist_ok=True)
    with open("benchmark/results/sampling_frame.json", "w", encoding="utf-8") as f:
        json.dump({"top_n": TOP_N, "min_downloads": MIN_DOWNLOADS,
                   "all_in_frame": all_in, "gems": rows}, f, indent=2)


if __name__ == "__main__":
    main()

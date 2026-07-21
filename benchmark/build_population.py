"""Constrói a POPULAÇÃO de amostragem para o corpus, de forma reprodutível.

Universo citável = awesome-ruby (lista curada da comunidade, organizada por
categoria — a categoria dá diversidade de domínio de graça). Filtro objetivo =
downloads no RubyGems.org acima de um limiar. NADA é instalado: só se leem
metadados via HTTP.

Saída: benchmark/results/population.json — a lista de gems (categoria, repo,
downloads) que passam o filtro. É a partir DESTA lista que se clona e diagnostica
(build_population_diagnose), tornando a seleção uma função dos dados, não juízo.

    python -m benchmark.build_population
"""
from __future__ import annotations

import json
import os
import re
import time
import urllib.request

AWESOME = "https://raw.githubusercontent.com/markets/awesome-ruby/master/README.md"
MIN_DOWNLOADS = 100_000_000

# Categorias do awesome-ruby que NÃO são bibliotecas testáveis por nós
# (frameworks pesados, ferramentas, apps, docs). Filtro de domínio explícito.
SKIP_SECTIONS = {
    "resources", "podcasts", "screencasts", "newsletters", "books", "blogs",
    "services", "editors", "web frameworks", "application servers",
    "web servers", "containers", "deployment", "continuous integration",
    "environment management", "process management", "monitoring",
}


def fetch_readme() -> str:
    req = urllib.request.Request(AWESOME, headers={"User-Agent": "marta"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "ignore")


def parse_candidates(md: str):
    """Devolve [(gem_guess, owner/repo, categoria)] do awesome-ruby."""
    out = []
    section = "?"
    line_re = re.compile(r"^\s*[*-]\s*\[([^\]]+)\]\(https://github\.com/([^)/]+/[^)/#]+)")
    for line in md.splitlines():
        h = re.match(r"^#{2,4}\s+(.+?)\s*$", line)
        if h:
            section = h.group(1).strip().lower()
            continue
        m = line_re.match(line)
        if not m:
            continue
        if section in SKIP_SECTIONS:
            continue
        repo = m.group(2).rstrip("/")
        gem_guess = repo.split("/")[-1].removesuffix(".rb").removeprefix("ruby-")
        out.append((gem_guess, repo, section))
    return out


def gem_info(gem: str):
    try:
        req = urllib.request.Request(f"https://rubygems.org/api/v1/gems/{gem}.json",
                                     headers={"User-Agent": "marta"})
        with urllib.request.urlopen(req, timeout=15) as r:
            d = json.load(r)
        return d.get("downloads"), d.get("source_code_uri") or d.get("homepage_uri")
    except Exception:
        return None, None


def main():
    md = fetch_readme()
    cands = parse_candidates(md)
    # dedup por repo
    seen, uniq = set(), []
    for g, repo, sec in cands:
        if repo not in seen:
            seen.add(repo)
            uniq.append((g, repo, sec))
    print(f"awesome-ruby: {len(uniq)} candidatas (após skip de secções não-lib)")

    pop = []
    for i, (gem, repo, sec) in enumerate(uniq):
        dl, src = gem_info(gem)
        if dl and dl >= MIN_DOWNLOADS:
            pop.append({"gem": gem, "repo": repo, "section": sec,
                        "downloads": dl, "clone": f"https://github.com/{repo}"})
        if i % 50 == 0:
            print(f"  ... {i}/{len(uniq)} verificadas, {len(pop)} acima do limiar", flush=True)
        time.sleep(0.05)

    pop.sort(key=lambda r: -r["downloads"])
    os.makedirs("benchmark/results", exist_ok=True)
    with open("benchmark/results/population.json", "w", encoding="utf-8") as f:
        json.dump({"min_downloads": MIN_DOWNLOADS, "source": "awesome-ruby",
                   "count": len(pop), "gems": pop}, f, indent=2)

    print(f"\nPOPULAÇÃO: {len(pop)} gems com >= {MIN_DOWNLOADS:,} downloads")
    cats = {}
    for p in pop:
        cats[p["section"]] = cats.get(p["section"], 0) + 1
    print("por categoria:", dict(sorted(cats.items(), key=lambda x: -x[1])))
    print("\ntop 15:")
    for p in pop[:15]:
        print(f"  {p['downloads']:>15,}  {p['gem']:20s} [{p['section']}]")


if __name__ == "__main__":
    main()

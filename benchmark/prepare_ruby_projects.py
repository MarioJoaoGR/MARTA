"""Prepara os projetos Ruby do benchmark (PASSO COM REDE — correr ANTES do job).

Os nós de computação do Deucalion não têm rede, por isso os projetos têm de vir
clonados e com as dependências instaladas.

Lê o ``projetos.json`` da camada 7 e, por gem, reproduz o ambiente em que a
camada 6 certificou que os módulos carregam. Não inventa uma receita própria:
chama as mesmas funções da camada 6 (``clona``, ``instala``, ``bundle``). Uma
receita diferente foi exatamente o que antes fazia módulos certificados falharem
no cluster (nos monorepos o gemspec nem está na raiz; o fastlane precisa do
Gemfile).

  clone da etiqueta publicada --> confirma o commit --> instala segundo o
  `ambiente` da camada 6 --> regista as versões que ficaram instaladas

Nada vai para o sistema: as gems ficam dentro de cada projeto (``.gem_home/``, ou
``.gem_bundle/`` quando a receita é o Gemfile). O diretório de saída é
auto-contido e o ``manifest.json`` diz o que ficou pronto.

    python -m benchmark.prepare_ruby_projects --out /caminho/ruby_projects
    python -m benchmark.prepare_ruby_projects --out ... --projects aasm,puma
    python -m benchmark.prepare_ruby_projects --out ... --continuar
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import shutil
import subprocess
import sys
import time

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from benchmark.dataset import camada6_carregamento as camada6  # noqa: E402

PROJETOS = REPO / "apresentacao" / "demo_dataset" / "7_selecao" / "projetos.json"


def carrega_projetos(path: pathlib.Path = PROJETOS) -> dict:
    with open(path, encoding="utf-8") as f:
        return {k: v for k, v in json.load(f).items() if not k.startswith("_")}


def raiz_de(clone: pathlib.Path, projeto: dict) -> pathlib.Path:
    return clone if projeto["raiz"] in ("", ".") else clone / projeto["raiz"]


def _default_dir() -> str:
    try:
        return subprocess.run([camada6.ruby(), "-e", "print Gem.default_dir"],
                              capture_output=True, text=True, timeout=30).stdout.strip()
    except Exception:
        return ""


def gem_env(clone: pathlib.Path, gems: dict) -> dict:
    """GEM_HOME/GEM_PATH para correr specs no ambiente preparado.

    Usado pelo verificador e pelo harness, para os dois correrem exatamente no
    ambiente que este script montou. O GEM_PATH vê, por esta ordem:
      1. as gems do projeto (a mesma disposição que a camada 6 usou: com Gemfile,
         as pastas que o bundler cria dentro de .gem_bundle);
      2. o venv de Ruby (``MARTA_RUBY_ENV``), onde vive o rspec;
      3. ``Gem.default_dir``, as bundled gems da distribuição.
    """
    base = _default_dir()
    pasta = str(clone / gems["dir"])
    if gems.get("tipo") == "bundle" and os.path.isdir(pasta):
        e = camada6.env_bundle(pasta, base)
        home, caminhos = e["GEM_HOME"], e["GEM_PATH"].split(":")
    else:
        home, caminhos = pasta, [pasta, base]
    # NÃO herdar o GEM_PATH do ambiente: o harness e o verificador chamam isto
    # gem a gem no MESMO processo e fazem os.environ.update() com o resultado.
    # Herdando, o caminho ia acumulando os .gem_home de todas as gems anteriores,
    # e à décima a ferramenta via as dependências das outras nove — a cocoapods
    # passava sozinha e falhava 5/5 na corrida completa, por apanhar versões de
    # outra gem. O ambiente tem de ser função da gem, e de mais nada.
    extra = [os.environ.get("MARTA_RUBY_ENV", "")]
    vistos, ordem = set(), []
    for p in caminhos[:-1] + extra + caminhos[-1:]:
        for parte in p.split(os.pathsep):
            if parte and parte not in vistos:
                vistos.add(parte)
                ordem.append(parte)
    return {"GEM_HOME": home, "GEM_PATH": os.pathsep.join(ordem)}


def _git(clone: pathlib.Path, *args, timeout=600) -> str:
    try:
        return subprocess.run(["git", "-C", str(clone), *args], capture_output=True,
                              text=True, timeout=timeout).stdout.strip()
    except Exception:
        return ""


def prepara(gem: str, p: dict, out_dir: pathlib.Path) -> dict:
    clone = out_dir / gem
    reg = {"gem": gem, "repo": p["repo"], "etiqueta": p["etiqueta"],
           "commit": p["commit"], "raiz": p["raiz"], "ambiente": p["ambiente"],
           "estado": "", "detalhe": ""}

    # 1. Código: a etiqueta da versão publicada, e o commit tem de bater certo.
    if not (clone / ".git").is_dir():
        shutil.rmtree(clone, ignore_errors=True)
        if not camada6.clona(p["repo"], p["etiqueta"] or None, str(clone)):
            return {**reg, "estado": "nao clonou"}
    head = _git(clone, "rev-parse", "HEAD")[:12]
    if head != p["commit"]:
        # Sem etiqueta a camada 2 usou o ramo por omissão, que entretanto pode ter
        # andado: vai-se buscar o historial e volta-se ao commit certificado.
        _git(clone, "fetch", "--unshallow", timeout=1800)
        _git(clone, "checkout", "--quiet", p["commit"])
        head = _git(clone, "rev-parse", "HEAD")[:12]
        if head != p["commit"]:
            return {**reg, "estado": "commit diferente",
                    "detalhe": f"HEAD {head or '?'} != {p['commit']}"}

    raiz = raiz_de(clone, p)
    em_falta = [a["ficheiro"] for a in p["alvos"] if not (raiz / a["ficheiro"]).is_file()]
    if em_falta:
        return {**reg, "estado": "alvos em falta", "detalhe": ", ".join(em_falta[:5])}

    # 2. Dependências, pelo mesmo degrau que a camada 6 precisou de usar.
    if p["ambiente"] == "Gemfile do projeto":
        gems = {"tipo": "bundle", "dir": ".gem_bundle"}
        ok, err = camada6.bundle(str(raiz), str(clone / gems["dir"]))
    else:
        gems = {"tipo": "gem_home", "dir": ".gem_home"}
        ok, err = camada6.instala(p["deps"], str(clone / gems["dir"]))
        if ok and p["ambiente"] == "deps + a propria gem":
            ok, err = camada6.instala([gem], str(clone / gems["dir"]))
    reg["gems"] = gems
    if not ok:
        return {**reg, "estado": "falhou a instalar", "detalhe": err}

    # 3. O que ficou instalado, com versões. A camada 6 instalou as versões mais
    #    recentes à data; se entretanto saiu uma que parte o carregamento, o
    #    verificador apanha-o, e isto diz qual foi.
    env = {**os.environ, **gem_env(clone, gems)}
    try:
        lista = subprocess.run([camada6.ruby(), "-S", "gem", "list", "--local"],
                               capture_output=True, text=True, env=env, timeout=120).stdout
    except Exception:
        lista = ""
    reg["gems_instaladas"] = [ln.strip() for ln in lista.splitlines() if ln.strip()]
    return {**reg, "estado": "pronto"}


def _grava(path: pathlib.Path, dados: dict) -> None:
    """Temporário + os.replace: um write interrompido nunca deixa o manifesto
    truncado (já se perderam linhas de um CSV assim)."""
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(dados, indent=2, ensure_ascii=False) + "\n")
    os.replace(tmp, path)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True, help="diretório de saída (auto-contido)")
    ap.add_argument("--manifest", default=str(PROJETOS),
                    help="projetos.json da camada 7")
    ap.add_argument("--projects", default=None, help="subconjunto separado por vírgulas")
    ap.add_argument("--continuar", action="store_true",
                    help="salta as gems que o manifest.json já dá como prontas")
    args = ap.parse_args()

    projetos = carrega_projetos(pathlib.Path(args.manifest))
    if args.projects:
        pedidas = {x.strip() for x in args.projects.split(",")}
        desconhecidas = sorted(pedidas - set(projetos))
        if desconhecidas:
            sys.exit(f"não estão no corpus: {', '.join(desconhecidas)}")
        projetos = {g: p for g, p in projetos.items() if g in pedidas}

    out_dir = pathlib.Path(args.out).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = out_dir / "manifest.json"
    feitos = {}
    if manifest.exists():
        feitos = {r["gem"]: r for r in json.loads(manifest.read_text())["projetos"]}

    print(f"A preparar {len(projetos)} gems em {out_dir}\n")
    for i, (gem, p) in enumerate(sorted(projetos.items()), 1):
        antes = feitos.get(gem)
        # O --continuar so salta uma gem preparada com a MESMA receita e o MESMO
        # commit. A receita muda quando a camada 6 muda de degrau (a doorkeeper
        # passou de "deps do gemspec" para o Gemfile do projeto): saltar a gem
        # deixava no disco um ambiente diferente do que o dataset certificou, e o
        # verificador acusava um modulo que no cluster funcionaria.
        if args.continuar and antes and antes["estado"] == "pronto" \
                and antes["commit"] == p["commit"] \
                and antes.get("ambiente") == p["ambiente"]:
            print(f"[{i}/{len(projetos)}] {gem}: já pronto")
            continue
        t0 = time.time()
        print(f"[{i}/{len(projetos)}] {gem} ({p['repo']} @ {p['etiqueta'] or p['commit']}, "
              f"{p['ambiente']}) ...", flush=True)
        r = prepara(gem, p, out_dir)
        r["segundos"] = round(time.time() - t0, 1)
        feitos[gem] = r
        _grava(manifest, {"projetos": [feitos[g] for g in sorted(feitos)]})
        print(f"   {r['estado']}  {r['segundos']}s"
              + (f"  ({str(r['detalhe'])[:150]})" if r.get("detalhe") else ""))

    prontos = sum(1 for r in feitos.values() if r["estado"] == "pronto")
    print(f"\n{prontos}/{len(feitos)} prontos. Manifesto: {manifest}")
    print("A seguir: python -m benchmark.verifica_ambiente --projects-dir", out_dir)


if __name__ == "__main__":
    main()

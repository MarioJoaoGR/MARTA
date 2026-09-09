"""Camada 6: o modulo carrega com um `gem install` e mais nada?

E a unica camada que instala. Substitui por MEDICAO aquilo que antes era
decretado por uma lista de nomes banidos: se um modulo precisa do Rails de pe,
nao carrega, e o ficheiro diz porque. Mesma regua para bibliotecas, aplicacoes e
frameworks.

O AMBIENTE E O MINIMO QUE UM UTILIZADOR TEM, e so se alarga quando sem ele a
biblioteca nem sequer carrega. Tres degraus, cada um so se o anterior deixar a
porta fechada, e o degrau usado fica escrito no `gems.csv`:

  1. dependencias declaradas no gemspec      o que um `gem install` traz
  2. + a propria gem                          traz as partes em C ja compiladas
                                              (o clone traz-nas por compilar)
  3. + o Gemfile do projeto                   resolve conflitos de versoes

Porque nao instalar sempre o Gemfile, que seria o obvio: medido em 15 gems, o
`bundle install` FALHA em 5 delas (activerecord, activesupport, rspec, tilt,
activerecord-import — 499 modulos), e nas 10 onde corre recupera 270 modulos dos
quais 252 sao de uma so gem (fastlane). Fora dessa, 18 em 1010, 1,8%. Instalar
sempre teria saldo negativo.

O que fica de fora sao dependencias OPCIONAIS, que nao estao declaradas em lado
nenhum — nem no gemspec nem no Gemfile. O Gemfile da `brakeman`, por exemplo,
acrescenta so `rake` e `minitest`; o `ruby2ruby` que falta a 99 modulos dela nao
esta la. Nao ha instalacao automatica que os traga.

SEGUNDA OPORTUNIDADE: carregar um ficheiro sozinho e mais estrito do que a
realidade — quando a ferramenta correr um spec, a biblioteca esta carregada.
Medido: 55% dos NameError eram dessa rigidez, nao do modulo. Por isso, o que
falha isolado tem uma segunda tentativa com a biblioteca inteira carregada, e o
modo usado fica na coluna `modo` do `carregam.csv`.

Nada e instalado no sistema: GEM_HOME isolado por gem, apagado a seguir.

    python -m benchmark.dataset.camada6_carregamento
    python -m benchmark.dataset.camada6_carregamento --continuar
"""
from __future__ import annotations

import csv
import json
import os
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from collections import defaultdict
from datetime import date

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = os.path.join(RAIZ, "apresentacao", "demo_dataset")
ENT = os.path.join(D, "5_desduplicacao", "representantes.csv")
PARSE = os.path.join(D, "2_parser", "parse.csv")
OUT = os.path.join(D, "6_carregamento")
_RB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rb")
CARREGA, ORDEM = os.path.join(_RB, "carrega.rb"), os.path.join(_RB, "ordem.rb")


def ruby() -> str:
    b = os.environ.get("MARTA_RUBY_BIN")
    if b and os.access(b, os.X_OK):
        return b
    alt = os.path.expanduser("~/.rbenv/versions/3.4.10/bin/ruby")
    return alt if os.access(alt, os.X_OK) else "ruby"


def deps_runtime(gem: str):
    """A API do RubyGems e a fonte fiavel: o gemspec do repo pode ser dinamico
    (a `kramdown` gera-o com rake)."""
    try:
        req = urllib.request.Request(
            f"https://rubygems.org/api/v1/gems/{gem}.json",
            headers={"User-Agent": "marta-benchmark"})
        d = json.load(urllib.request.urlopen(req, timeout=20))
        return [x["name"] for x in d.get("dependencies", {}).get("runtime", [])]
    except Exception:
        return None


def clona(repo, ref, dest) -> bool:
    cmd = ["git", "clone", "--depth", "1"]
    if ref:
        cmd += ["--branch", ref]
    cmd += [f"https://github.com/{repo}", dest]
    try:
        return subprocess.run(cmd, capture_output=True, text=True,
                              timeout=300).returncode == 0
    except Exception:
        return False


def instala(deps, home, timeout=600):
    """Sempre pelo Ruby do venv: chamar `gem` pelo PATH usava o 2.6 do macOS e
    tudo falhava com 'the last version to support your Ruby was X'."""
    if not deps:
        return True, ""
    env = {**os.environ, "GEM_HOME": home, "GEM_PATH": home}
    try:
        r = subprocess.run([ruby(), "-S", "gem", "install", "--no-document",
                            "--conservative", *deps], capture_output=True,
                           text=True, errors="replace", env=env, timeout=timeout)
        return r.returncode == 0, (r.stderr or r.stdout or "").strip()[-300:]
    except subprocess.TimeoutExpired:
        return False, "timeout a instalar"
    except Exception as e:
        return False, type(e).__name__


def bundle(raiz, caminho_gems, timeout=1200):
    """`bundle install` isolado: gems E configuracao vao para caminho_gems.
    Nada toca no ~/.bundle nem no store global."""
    gemfile = os.path.join(raiz, "Gemfile")
    if not os.path.isfile(gemfile):
        return False, "sem Gemfile"
    env = {**os.environ, "BUNDLE_GEMFILE": gemfile, "BUNDLE_PATH": caminho_gems,
           "BUNDLE_PATH__SYSTEM": "false", "BUNDLE_FROZEN": "false",
           "GEM_HOME": caminho_gems,
           "BUNDLE_APP_CONFIG": os.path.join(caminho_gems, ".bundle")}
    try:
        r = subprocess.run([ruby(), "-S", "bundle", "install", "--jobs", "4"],
                           cwd=raiz, capture_output=True, text=True,
                           errors="replace", env=env, timeout=timeout)
        return r.returncode == 0, (r.stderr or r.stdout or "").strip()[-250:]
    except subprocess.TimeoutExpired:
        return False, "timeout no bundle install"
    except Exception as e:
        return False, type(e).__name__


def env_bundle(bpath, base):
    niveis = [bpath]
    for d in (os.path.join(bpath, x) for x in os.listdir(bpath)):
        if os.path.isdir(d):
            niveis.append(d)
            niveis += [os.path.join(d, x) for x in os.listdir(d)
                       if os.path.isdir(os.path.join(d, x))]
    return {**os.environ, "GEM_HOME": bpath, "GEM_PATH": ":".join(niveis + [base])}


def load_paths(raiz):
    """Alem de lib/ na raiz, os monorepos tem uma lib por sub-gem: a fastlane
    tem fastlane/lib, spaceship/lib, gym/lib. Sem elas, nada dela carrega."""
    out = [os.path.join(raiz, b) for b in ("lib", "src", "app")
           if os.path.isdir(os.path.join(raiz, b))]
    try:
        for nome in sorted(os.listdir(raiz)):
            d = os.path.join(raiz, nome, "lib")
            if not nome.startswith(".") and os.path.isdir(d):
                out.append(d)
    except OSError:
        pass
    return out


def nome_require(gem, caminhos):
    """A porta de entrada. A convencao e lib/<nome>.rb, mas o nome da gem e o do
    ficheiro separam as palavras de forma diferente: `activerecord` abre em
    `lib/active_record.rb`. Compara-se sem separadores.

    NAO ha recurso a "se so houver um .rb, usa esse": era isso que fazia a
    fastlane abrir no `spec_helper` e perder os 506 modulos dela."""
    def limpo(s):
        return s.replace("-", "").replace("_", "").replace("/", "").lower()

    alvo = limpo(gem)
    for d in caminhos:
        for f in sorted(x[:-3] for x in os.listdir(d) if x.endswith(".rb")):
            if limpo(f) == alvo:
                return f
        cand = gem.replace("-", "/")
        if os.path.isfile(os.path.join(d, f"{cand}.rb")):
            return cand
    return ""


def _feito(continuar):
    def le(nome):
        try:
            with open(os.path.join(OUT, nome), encoding="utf-8") as f:
                return list(csv.DictReader(f))
        except FileNotFoundError:
            return []
    return (le("gems.csv"), le("carregam.csv"), le("falham.csv")) if continuar \
        else ([], [], [])


def main(continuar: bool = False) -> None:
    os.makedirs(OUT, exist_ok=True)
    mods, meta = defaultdict(list), {}
    with open(ENT, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            mods[r["gem"]].append(r)
            meta[(r["gem"], r["ficheiro"])] = r
    with open(PARSE, encoding="utf-8") as f:
        refs = {r["gem"]: (r["repo_usado"], r["etiqueta"], r["raiz_codigo"])
                for r in csv.DictReader(f)}

    linhas, ok_mods, mau_mods = _feito(continuar)
    refazer = {r["gem"] for r in linhas if r["erro_instalacao"] == "nao clonou"}
    linhas = [r for r in linhas if r["gem"] not in refazer]
    ok_mods = [r for r in ok_mods if r["gem"] not in refazer]
    mau_mods = [r for r in mau_mods if r["gem"] not in refazer]
    ja = {r["gem"] for r in linhas}
    gems = [g for g in sorted(mods) if g not in ja]
    if ja:
        print(f"a retomar: {len(ja)} feitas, faltam {len(gems)}")

    trabalho = tempfile.mkdtemp(prefix="marta_c6_")
    try:
        for i, gem in enumerate(gems):
            dest = os.path.join(trabalho, gem.replace("/", "_"))
            home = os.path.join(trabalho, f"g_{gem.replace('/', '_')}")
            bpath = os.path.join(trabalho, f"b_{gem.replace('/', '_')}")
            repo, tag, sub = refs.get(gem, ("", "", "."))
            reg = {"gem": gem, "modulos": len(mods[gem]), "deps": "",
                   "instalou": "", "instalou_a_propria": "", "usou_gemfile": "",
                   "ambiente": "", "erro_instalacao": "", "load_paths": "",
                   "entrada": "", "porta_abriu": "", "erro_porta": "",
                   "recuperados_pela_ordem": 0, "carregam": 0, "falham": 0}
            if not clona(repo, tag, dest):
                reg["erro_instalacao"] = "nao clonou"
                linhas.append(reg)
                mau_mods += [{**m, "erro": "gem nao clonou"} for m in mods[gem]]
                print(f"  [{i+1}/{len(gems)}] {gem}: NAO CLONOU", flush=True)
                continue

            raiz = os.path.join(dest, sub) if sub and sub != "." else dest
            base = subprocess.run([ruby(), "-e", "print Gem.default_dir"],
                                  capture_output=True, text=True).stdout
            deps = deps_runtime(gem)
            reg["deps"] = " ".join(deps or [])
            ok, err = instala(deps or [], home)
            reg["instalou"], reg["erro_instalacao"] = ok, "" if ok else err
            env = {**os.environ, "GEM_HOME": home, "GEM_PATH": home + ":" + base}
            caminhos = load_paths(raiz)
            reg["load_paths"] = " ".join(os.path.relpath(c, dest) for c in caminhos)
            entrada = nome_require(gem, caminhos)
            reg["entrada"] = entrada or "(sem porta)"
            lista = "\n".join(m["ficheiro"] for m in mods[gem])

            def corre():
                try:
                    return subprocess.run([ruby(), CARREGA, raiz, entrada, *caminhos],
                                          input=lista, capture_output=True, text=True,
                                          errors="replace", env=env, timeout=1800).stdout
                except subprocess.TimeoutExpired as e:
                    s = e.stdout or ""
                    return s.decode("utf-8", "replace") if isinstance(s, bytes) else s

            def porta_falhou(s):
                for ln in s.splitlines():
                    try:
                        d = json.loads(ln)
                    except json.JSONDecodeError:
                        continue
                    if isinstance(d, dict) and d.get("tipo") == "porta":
                        return not d["ok"]
                return True

            saida = corre()
            reg["ambiente"] = "deps do gemspec"
            if porta_falhou(saida):                       # degrau 2
                ok2, e2 = instala([gem], home)
                reg["instalou_a_propria"] = ok2
                if ok2:
                    saida = corre()
                    if not porta_falhou(saida):
                        reg["ambiente"] = "deps + a propria gem"
                else:
                    reg["erro_instalacao"] = (reg["erro_instalacao"] + " | propria: " + e2).strip(" |")
            if porta_falhou(saida):                       # degrau 3
                ok3, e3 = bundle(raiz, bpath)
                reg["usou_gemfile"] = ok3
                if ok3:
                    env = env_bundle(bpath, base)
                    saida = corre()
                    if not porta_falhou(saida):
                        reg["ambiente"] = "Gemfile do projeto"
                else:
                    reg["erro_instalacao"] = (reg["erro_instalacao"] + " | bundle: " + e3).strip(" |")

            vistos, bons, maus = set(), [], []
            for ln in saida.splitlines():
                try:
                    d = json.loads(ln)
                except json.JSONDecodeError:
                    continue
                if not isinstance(d, dict) or "tipo" not in d:
                    continue
                if d["tipo"] == "porta":
                    reg["porta_abriu"], reg["erro_porta"] = d["ok"], d.get("erro") or ""
                    continue
                vistos.add(d["ficheiro"])
                linha = dict(meta[(gem, d["ficheiro"])])
                if d["ok"]:
                    linha["modo"] = "isolado"
                    bons.append(linha)
                else:
                    linha["erro"] = d.get("erro") or ""
                    maus.append(linha)
            maus += [{**m, "erro": "sem resposta (processo morreu)"}
                     for m in mods[gem] if m["ficheiro"] not in vistos]

            if maus:                                      # segunda oportunidade
                mata = {m["ficheiro"] for m in maus
                        if m.get("erro", "").startswith(("saida abrupta", "timeout"))}
                try:
                    s2 = subprocess.run([ruby(), ORDEM, raiz, entrada, *caminhos],
                                        input="\n".join(m["ficheiro"] for m in mods[gem]
                                                        if m["ficheiro"] not in mata),
                                        capture_output=True, text=True,
                                        errors="replace", env=env, timeout=900).stdout
                except subprocess.TimeoutExpired as e:
                    s2 = e.stdout if isinstance(e.stdout, str) else ""
                carregados = set()
                for ln in s2.splitlines():
                    try:
                        d = json.loads(ln)
                    except json.JSONDecodeError:
                        continue
                    if isinstance(d, dict) and d.get("carregado"):
                        carregados.add(d["ficheiro"])
                rec = [m for m in maus if m["ficheiro"] in carregados]
                for m in rec:
                    m.pop("erro", None)
                    m["modo"] = "com a biblioteca carregada"
                bons += rec
                maus = [m for m in maus if m["ficheiro"] not in carregados]
                reg["recuperados_pela_ordem"] = len(rec)

            ok_mods += bons
            mau_mods += maus
            reg["carregam"], reg["falham"] = len(bons), len(maus)
            linhas.append(reg)
            print(f"  [{i+1}/{len(gems)}] {gem}: porta={reg['porta_abriu']} "
                  f"{len(bons)}/{len(mods[gem])} carregam", flush=True)
            for d in (dest, home, bpath):
                shutil.rmtree(d, ignore_errors=True)
    finally:
        shutil.rmtree(trabalho, ignore_errors=True)

    campos = list(next(iter(meta.values())).keys())
    for nome, dados, cs in (("carregam.csv", ok_mods, campos + ["modo"]),
                            ("falham.csv", mau_mods, campos + ["erro"]),
                            ("gems.csv", linhas, list(linhas[0].keys()))):
        with open(os.path.join(OUT, nome), "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=cs, extrasaction="ignore")
            w.writeheader()
            w.writerows(dados)

    funil = {"data": str(date.today()),
             "entram": len(ok_mods) + len(mau_mods),
             "carregam": len(ok_mods), "falham": len(mau_mods),
             "carregam_isolados": sum(1 for m in ok_mods if m.get("modo") == "isolado"),
             "carregam_so_com_a_biblioteca":
                 sum(1 for m in ok_mods if m.get("modo") != "isolado"),
             "ambiente_usado": {a: sum(1 for r in linhas if r["ambiente"] == a)
                                for a in ("deps do gemspec", "deps + a propria gem",
                                          "Gemfile do projeto")},
             "gems_no_fim": len({m["gem"] for m in ok_mods}),
             "categorias_no_fim": len({m["categoria"] for m in ok_mods}),
             "metodos": sum(int(m["metodos"]) for m in ok_mods)}
    json.dump(funil, open(f"{OUT}/funil.json", "w", encoding="utf-8"),
              indent=2, ensure_ascii=False)
    print("\n" + json.dumps(funil, indent=1))


if __name__ == "__main__":
    main(continuar="--continuar" in sys.argv)

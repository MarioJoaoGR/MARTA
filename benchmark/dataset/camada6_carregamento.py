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

DUAS FASES, e um modulo so fica certificado se passar nas duas:

  1. carrega num processo Ruby limpo (rb/carrega.rb, e rb/ordem.rb na segunda
     oportunidade);
  2. carrega no EXECUTOR DE TESTES da ferramenta: um spec trivial que so faz
     `require`, corrido pela mesma funcao que a MARTA usa, e a confirmacao de
     que o ficheiro aparece no relatorio de cobertura.

A fase 2 existe porque os dois carregadores nao sao a mesma coisa: o RSpec traz
os seus argumentos, ja esta carregado, e corre dentro da pasta do projeto. Ha
modulos que passam no primeiro e falham no segundo (um exemplo que instala gems
ao carregar, um `bundler/setup` que le o Gemfile da pasta, um generator que
precisa do Rails, um ficheiro que arranca o Minitest e recusa os argumentos do
RSpec). E nao falham sozinhos: carregados com os outros alvos da gem, apagam a
cobertura deles tambem. Saem para o `falham_rspec.csv`.

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
# MARTA_DATASET_DIR desvia os artefactos para outra pasta. Serve para verificar
# se uma camada reproduz o seu artefacto sem escrever por cima do que esta no
# repositorio (uma verificacao assim ja apanhou ficheiros por engano num commit).
D = os.environ.get("MARTA_DATASET_DIR") or \
    os.path.join(RAIZ, "apresentacao", "demo_dataset")
ENT = os.path.join(D, "5_desduplicacao", "representantes.csv")
PARSE = os.path.join(D, "2_parser", "parse.csv")
OUT = os.path.join(D, "6_carregamento")
_RB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rb")
CARREGA, ORDEM = os.path.join(_RB, "carrega.rb"), os.path.join(_RB, "ordem.rb")


SPEC_TRIVIAL = """require {req}
RSpec.describe {desc} do
  it "carrega" do
    expect(true).to eq(true)
  end
end
"""


def _poe_o_rspec_no_caminho() -> None:
    """O GEM_PATH da gem nao ve o rspec, que vive no venv de Ruby do repositorio.

    Sem isto, TODOS os modulos falhavam com "can't find gem rspec-core" e a camada
    barrava a populacao inteira por um erro de ambiente (aconteceu). O venv entra
    antes das bundled gems da distribuicao, como no prepare_ruby_projects.
    """
    venv = os.environ.get("MARTA_RUBY_ENV")
    if not venv:
        return
    partes = [x for x in os.environ.get("GEM_PATH", "").split(os.pathsep) if x]
    if venv in partes:
        return
    os.environ["GEM_PATH"] = os.pathsep.join(partes[:-1] + [venv] + partes[-1:]
                                             if partes else [venv])


def rspec_responde() -> str:
    """Um spec trivial numa pasta vazia: o executor de testes esta de pe?

    Corre-se ANTES de clonar seja o que for. A segunda fase da camada 6 depende
    dele, e um erro de ambiente aqui barraria a populacao toda em silencio.
    Devolve "" se responde, ou o erro.
    """
    sys.path.insert(0, RAIZ)
    _poe_o_rspec_no_caminho()
    from marta.ruby_backend import backend as bk
    pasta = tempfile.mkdtemp(prefix="marta_c6_smoke_")
    try:
        spec = os.path.join(pasta, "smoke_spec.rb")
        with open(spec, "w", encoding="utf-8") as f:
            f.write('RSpec.describe("smoke") { it("corre") { expect(1).to eq(1) } }\n')
        res = bk.RubyBackend().run_tests(spec, [], pasta)
        return "" if res.all_passed else " ".join((res.output or "sem saida").split())[:300]
    finally:
        shutil.rmtree(pasta, ignore_errors=True)


def certifica_no_rspec(raiz, caminhos, entrada, ficheiros_codigo, bons, biblioteca,
                       workers: int = 4):
    """Segunda fase: o modulo carrega TAMBEM pelo executor de testes da ferramenta?

    A primeira fase carrega cada modulo num processo Ruby limpo (rb/carrega.rb).
    A MARTA corre o RSpec: com os argumentos dele, com ele ja carregado, e dentro
    da pasta do projeto. Ha modulos que passam no primeiro e falham no segundo (um
    exemplo que instala gems ao carregar, um `bundler/setup` que le o Gemfile da
    pasta onde corre, um generator que precisa do Rails, um ficheiro que arranca o
    Minitest e recusa os argumentos do RSpec). Um modulo destes nao falha sozinho:
    carregado com os outros alvos da gem, apaga a cobertura deles tambem.

    Corre-se aqui porque e aqui que a gem esta clonada e as dependencias
    instaladas, no ambiente que a acabou de certificar. Devolve
    (certificados, barrados), com o erro de cada um dos barrados.
    """
    from concurrent.futures import ThreadPoolExecutor
    sys.path.insert(0, RAIZ)
    _poe_o_rspec_no_caminho()
    from marta.ruby_backend import coverage_runner as cov
    from marta.ruby_backend.project import RubyProject

    rel = [os.path.relpath(c, raiz) for c in caminhos]
    proj = RubyProject(root_dir=raiz, source_dir=".",
                       target_files=[m["ficheiro"] for m in bons],
                       load_paths=rel, preload=entrada or None,
                       code_files=ficheiros_codigo,
                       library_files=biblioteca or None,
                       library_targets=[m["ficheiro"] for m in bons
                                        if m.get("modo", "isolado") != "isolado"] or None,
                       ).discover()
    por_ficheiro = {}
    for t in proj.targets:
        por_ficheiro.setdefault(t.source_rel, t)

    pasta = tempfile.mkdtemp(prefix="marta_c6_rspec_")
    try:
        def um(m):
            t = por_ficheiro.get(m["ficheiro"])
            if t is None:      # modulo sem metodos-alvo: nada a certificar
                return m, ""
            spec = os.path.join(pasta, m["ficheiro"].replace("/", "__") + "_spec.rb")
            with open(spec, "w", encoding="utf-8") as f:
                f.write(SPEC_TRIVIAL.format(req=json.dumps(t.require_target),
                                            desc=json.dumps(f"carrega {m['ficheiro']}")))
            extra = proj._extra_requires_for(t)
            res = proj.backend.run_tests(spec, proj._load_path_list(), raiz,
                                         **({"requires_extra": extra} if extra else {}))
            if res.all_passed:
                return m, ""
            return m, " ".join((res.output or "sem saida").split())[:300]

        with ThreadPoolExecutor(max_workers=workers) as ex:
            resultados = list(ex.map(um, bons))
        certificados = [m for m, err in resultados if not err]
        barrados = [{**m, "erro_rspec": err} for m, err in resultados if err]

        # Depois de tirar os que falham, os que ficam TEM de aparecer na cobertura:
        # e a chave por onde a ferramenta procura o ficheiro. Sem ela, a cobertura
        # desse modulo sairia vazia sem dar erro.
        specs = [os.path.join(pasta, f) for f in sorted(os.listdir(pasta))
                 if f.endswith("_spec.rb")
                 and f[: -len("_spec.rb")].replace("__", "/")
                 in {m["ficheiro"] for m in certificados}]
        if specs:
            try:
                r = cov.run_line_coverage(".", specs, cwd=raiz, timeout=1800,
                                          isolated=True,
                                          load_paths=proj._load_path_list(),
                                          requires=([entrada] if entrada else [])
                                          + list(proj.backend.coverage_requires))
                chaves = set(r.files)
                sem_cobertura = [m for m in certificados if m["ficheiro"] not in chaves]
                if sem_cobertura:
                    fora = {m["ficheiro"] for m in sem_cobertura}
                    certificados = [m for m in certificados if m["ficheiro"] not in fora]
                    barrados += [{**m, "erro_rspec": "nao aparece na cobertura"}
                                 for m in sem_cobertura]
            except Exception as e:                       # noqa: BLE001
                print(f"    ! cobertura falhou: {repr(e)[:150]}", flush=True)
    finally:
        shutil.rmtree(pasta, ignore_errors=True)
    return certificados, barrados


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
    return (le("gems.csv"), le("carregam.csv"), le("falham.csv"),
            le("falham_rspec.csv")) if continuar else ([], [], [], [])


def main(continuar: bool = False) -> None:
    os.makedirs(OUT, exist_ok=True)
    erro = rspec_responde()
    if erro:
        raise SystemExit(f"o RSpec nao responde, a 2a fase barraria tudo: {erro}\n"
                         "(falta `source scripts/ruby_env.sh`?)")
    mods, meta = defaultdict(list), {}
    with open(ENT, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            mods[r["gem"]].append(r)
            meta[(r["gem"], r["ficheiro"])] = r
    with open(PARSE, encoding="utf-8") as f:
        refs = {r["gem"]: (r["repo_usado"], r["etiqueta"], r["raiz_codigo"])
                for r in csv.DictReader(f)}

    linhas, ok_mods, mau_mods, sem_rspec = _feito(continuar)
    refazer = {r["gem"] for r in linhas if r["erro_instalacao"] == "nao clonou"}
    linhas = [r for r in linhas if r["gem"] not in refazer]
    ok_mods = [r for r in ok_mods if r["gem"] not in refazer]
    mau_mods = [r for r in mau_mods if r["gem"] not in refazer]
    sem_rspec = [r for r in sem_rspec if r["gem"] not in refazer]
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
                   "recuperados_pela_ordem": 0, "barrados_no_rspec": 0,
                   "carregam": 0, "falham": 0}
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
            # O `ambiente` e o que ESTEVE EM VIGOR quando os modulos foram
            # carregados, mesmo que a porta nunca abra: e o ambiente que o
            # prepare tem de reproduzir no cluster. Registar o primeiro degrau
            # quando o carregamento correu no terceiro deixava o cluster com
            # outras gems (a doorkeeper, cuja porta rebenta, carregava com o
            # Gemfile mas ia registada como "deps do gemspec").
            if porta_falhou(saida):                       # degrau 2
                ok2, e2 = instala([gem], home)
                reg["instalou_a_propria"] = ok2
                if ok2:
                    saida = corre()
                    reg["ambiente"] = "deps + a propria gem"
                else:
                    reg["erro_instalacao"] = (reg["erro_instalacao"] + " | propria: " + e2).strip(" |")
            if porta_falhou(saida):                       # degrau 3
                ok3, e3 = bundle(raiz, bpath)
                reg["usou_gemfile"] = ok3
                if ok3:
                    env = env_bundle(bpath, base)
                    saida = corre()
                    reg["ambiente"] = "Gemfile do projeto"
                else:
                    reg["erro_instalacao"] = (reg["erro_instalacao"] + " | bundle: " + e3).strip(" |")

            vistos, bons, maus, mata = set(), [], [], set()
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
                mata |= {m["ficheiro"] for m in maus
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

            # Segunda fase: carrega TAMBEM pelo executor de testes da ferramenta?
            if bons:
                guardado = {k: os.environ.get(k) for k in ("GEM_HOME", "GEM_PATH",
                                                           "BUNDLE_APP_CONFIG", "BUNDLE_PATH")}
                os.environ.update({k: v for k, v in env.items() if k in guardado})
                try:
                    bons, barrados = certifica_no_rspec(
                        raiz, caminhos,
                        # A porta so entra se ABRIU: a doorkeeper tem porta que
                        # rebenta (NoMethodError: mattr_reader), e a camada
                        # certificou os modulos dela sem a carregar. Carrega-la a
                        # forca barrava a gem inteira por uma decisao nossa.
                        entrada if reg["porta_abriu"] is True else "",
                        [m["ficheiro"] for m in mods[gem]], bons,
                        [m["ficheiro"] for m in mods[gem] if m["ficheiro"] not in mata])
                finally:
                    for k, v in guardado.items():
                        if v is None:
                            os.environ.pop(k, None)
                        else:
                            os.environ[k] = v
                sem_rspec += barrados
                reg["barrados_no_rspec"] = len(barrados)

            ok_mods += bons
            mau_mods += maus
            reg["carregam"], reg["falham"] = len(bons), len(maus)
            linhas.append(reg)
            print(f"  [{i+1}/{len(gems)}] {gem}: porta={reg['porta_abriu']} "
                  f"{len(bons)}/{len(mods[gem])} carregam"
                  + (f", {reg['barrados_no_rspec']} barrados no RSpec"
                     if reg["barrados_no_rspec"] else ""), flush=True)
            for d in (dest, home, bpath):
                shutil.rmtree(d, ignore_errors=True)
    finally:
        shutil.rmtree(trabalho, ignore_errors=True)

    campos = list(next(iter(meta.values())).keys())
    for nome, dados, cs in (("carregam.csv", ok_mods, campos + ["modo"]),
                            ("falham.csv", mau_mods, campos + ["erro"]),
                            ("falham_rspec.csv", sem_rspec, campos + ["modo", "erro_rspec"]),
                            ("gems.csv", linhas, list(linhas[0].keys()))):
        with open(os.path.join(OUT, nome), "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=cs, extrasaction="ignore")
            w.writeheader()
            w.writerows(dados)

    funil = {"data": str(date.today()),
             # entram = carregam + nao carregam + barrados no RSpec (a camada 5 inteira)
             "entram": len(ok_mods) + len(mau_mods) + len(sem_rspec),
             "carregam": len(ok_mods), "falham": len(mau_mods),
             "barrados_no_rspec": len(sem_rspec),
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

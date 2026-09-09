"""Camada 2: as gems do universo leem-se com o nosso parser?

Uma pergunta so. Clona cada gem, corre o Prism sobre cada `.rb` que nao seja da
suite humana, conta o que falha, e apaga o clone. NAO exclui gems: regista.

Quatro decisoes que custaram gems reais e por isso estao aqui explicadas:

1. CLONA-SE A ETIQUETA DA VERSAO PUBLICADA, nao o ramo por omissao. E o codigo
   que as pessoas instalam, e uma etiqueta nao se move (o ramo sim). O
   `active_model_serializers` mostrou o custo do contrario: o `master` dele nao
   tem `lib/` nenhum, o codigo vive no ramo de manutencao.

2. ONDE VIVE O CODIGO nao se decide pela lista da comunidade nem pelo RubyGems,
   porque ambos envelhecem em direccoes diferentes (a `tilt` e a `kaminari`
   mudaram de casa; o `warden` declara no RubyGems o repo antigo). Juiz
   objectivo: quem tiver a etiqueta da versao publicada.

3. A SUITE HUMANA sai, e tem de casar a QUALQUER profundidade: nos monorepos
   esta em `fastlane/spec/`, `rspec-core/spec/`, nao na raiz. Sem isso entravam
   1182 ficheiros de teste como se fossem codigo.

4. NAO SE EXCLUI POR `lib/` nem por ser aplicacao/framework. O benchmark do
   CodaMosa, que seguimos, tem quase metade de aplicacoes (ansible, black,
   httpie, youtube-dl, e o thonny, que e um IDE). A restricao a bibliotecas nao
   e defensavel.

    python -m benchmark.dataset.camada2_parser
    python -m benchmark.dataset.camada2_parser --continuar   # retoma
"""
from __future__ import annotations

import csv
import gzip
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from collections import defaultdict
from datetime import date

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = os.path.join(RAIZ, "apresentacao", "demo_dataset")
OUT = os.path.join(D, "2_parser")
UNIVERSO = os.path.join(D, "1_universo", "universo.json")
DECLARADOS = os.path.join(D, "1_universo", "repos_declarados.csv")
LOTE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rb", "lote.rb")

# A suite humana e a linha de referencia contra a qual medimos, logo nao pode
# ser tambem o alvo. E a UNICA coisa que se poe de lado.
SUITE = {"spec", "test", "tests", "features"}
LIXO = {".git", "node_modules", "tmp", "coverage", "vendor"}


def ruby() -> str:
    """O Ruby do venv. Nao depender do PATH: sem o ambiente activo, o `ruby` do
    PATH no macOS e o 2.6, e tudo falha em silencio."""
    b = os.environ.get("MARTA_RUBY_BIN")
    if b and os.access(b, os.X_OK):
        return b
    alt = os.path.expanduser("~/.rbenv/versions/3.4.10/bin/ruby")
    return alt if os.access(alt, os.X_OK) else "ruby"


def _e_suite(rel: str) -> bool:
    return any(p in SUITE for p in rel.split(os.sep))


def _nao_ruby(rel: str) -> str:
    """Ficheiros `.rb` que nunca foram Ruby: moldes de gerador (levam ERB) e
    fixtures partidas de proposito. Sao lidos na mesma, para o erro ficar
    visivel no artefacto em vez de desaparecer."""
    partes = rel.split(os.sep)
    if "templates" in partes or os.path.basename(rel).endswith("_template.rb"):
        return "molde de gerador"
    if {"fixtures", "broken_files", "test_projects"} & set(partes):
        return "fixture de teste"
    return ""


def git(root: str, *args) -> str:
    try:
        return subprocess.run(["git", "-C", root, *args], capture_output=True,
                              text=True, errors="replace", timeout=30).stdout.strip()
    except Exception:
        return ""


def etiquetas(repo: str) -> list:
    try:
        r = subprocess.run(["git", "ls-remote", "--tags", "--refs",
                            f"https://github.com/{repo}"],
                           capture_output=True, text=True, errors="replace",
                           timeout=120)
        return [ln.split("refs/tags/", 1)[1].strip()
                for ln in r.stdout.splitlines() if "refs/tags/" in ln] \
            if r.returncode == 0 else []
    except Exception:
        return []


def escolhe_etiqueta(tags: list, versao: str) -> str:
    """A etiqueta que corresponde a versao publicada. Os projetos etiquetam de
    maneiras diferentes: v1.2.3, 1.2.3, rails-v1.2.3, gem/v1.2.3."""
    if not versao:
        return ""
    alvo = versao.strip()

    def norm(t):
        c = t.rsplit("/", 1)[-1]
        return c[1:] if c[:1].lower() == "v" else c

    for t in tags:
        if norm(t) == alvo:
            return t
    for t in tags:
        c = t.rsplit("/", 1)[-1]
        if c.endswith(alvo) and c[:-len(alvo)].rstrip("v-_") != c:
            return t
    return ""


def clona(repo: str, ref: str, dest: str, tentativas: int = 3) -> bool:
    """Com repeticao: o GitHub trava ao fim de muitas clonagens seguidas, e 68
    gems cairam de uma vez por isso. A falha e temporaria, nao definitiva."""
    for t in range(tentativas):
        cmd = ["git", "clone", "--depth", "1"]
        if ref:
            cmd += ["--branch", ref]
        cmd += [f"https://github.com/{repo}", dest]
        try:
            r = subprocess.run(cmd, capture_output=True, text=True,
                               errors="replace", timeout=300)
            if r.returncode == 0:
                return True
            if ref and "not found in upstream" in (r.stderr or ""):
                ref = ""                       # etiqueta ma: tenta o ramo
                continue
        except Exception:
            pass
        shutil.rmtree(dest, ignore_errors=True)
        if t < tentativas - 1:
            time.sleep(5 * (t + 1))
    return False


def lista_rb(root: str):
    alvos, suite, por_pasta = [], [], {}
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in LIXO and not d.startswith(".")]
        rel_dir = os.path.relpath(dp, root)
        topo = "." if rel_dir == "." else rel_dir.split(os.sep)[0]
        for fn in fns:
            if not fn.endswith(".rb"):
                continue
            p = os.path.join(dp, fn)
            por_pasta[topo] = por_pasta.get(topo, 0) + 1
            (suite if _e_suite(os.path.relpath(p, root)) else alvos).append(p)
    return alvos, suite, por_pasta


def analisa(paths: list) -> list:
    if not paths:
        return []
    p = subprocess.run([ruby(), LOTE], input="\n".join(paths),
                       capture_output=True, text=True, errors="replace",
                       timeout=1800)
    out = []
    for linha in p.stdout.splitlines():
        try:
            out.append(json.loads(linha))
        except json.JSONDecodeError:
            pass
    return out


def _declarados() -> dict:
    try:
        with open(DECLARADOS, encoding="utf-8") as f:
            return {x["gem"]: x["repo_declarado"] for x in csv.DictReader(f)
                    if x.get("repo_declarado")}
    except FileNotFoundError:
        return {}


def _feito(continuar: bool):
    def le(nome):
        try:
            with open(os.path.join(OUT, nome), encoding="utf-8") as f:
                return list(csv.DictReader(f))
        except FileNotFoundError:
            return []
    if not continuar:
        return [], [], []
    return le("parse.csv"), le("erros.csv"), le("onde_vive.csv")


def main(continuar: bool = False, limite=None) -> None:
    os.makedirs(OUT, exist_ok=True)
    gems = json.load(open(UNIVERSO, encoding="utf-8"))["gems"]
    declarado = _declarados()
    linhas, erros, onde = _feito(continuar)
    # Quem nao clonou nao esta feito: a falha era temporaria e tem de repetir.
    refazer = {r["gem"] for r in linhas if r.get("erro_clone") == "nao clonou"}
    linhas = [r for r in linhas if r["gem"] not in refazer]
    ja = {r["gem"] for r in linhas}
    if ja:
        print(f"a retomar: {len(ja)} feitas, faltam {len(gems) - len(ja)}")
    gems = [g for g in gems if g["gem"] not in ja]
    if limite:
        gems = gems[:limite]

    trabalho = tempfile.mkdtemp(prefix="marta_c2_")
    modo = "at" if continuar and ja else "wt"
    fcompleto = gzip.open(f"{OUT}/analise_completa.jsonl.gz", modo, encoding="utf-8")
    fmods = open(f"{OUT}/modulos.jsonl", "a" if modo == "at" else "w",
                 encoding="utf-8")
    try:
        for i, g in enumerate(gems):
            nome = g["gem"]
            base_repo = g["repo"].split("/tree/")[0]
            sub = g["repo"].split("/tree/master/")[1] if "/tree/master/" in g["repo"] else ""
            versao = g.get("versao") or ""
            dest = os.path.join(trabalho, nome.replace("/", "_"))

            # onde vive o codigo: quem tiver a etiqueta da versao publicada
            tag = escolhe_etiqueta(etiquetas(base_repo), versao)
            repo_usado, origem = base_repo, "lista"
            alt = declarado.get(nome, "")
            if not tag and alt and alt.lower() != base_repo.lower():
                t2 = escolhe_etiqueta(etiquetas(alt), versao)
                if t2:
                    repo_usado, origem, tag = alt, "declarado no RubyGems", t2

            reg = {"gem": nome, "repo": g["repo"], "categoria": g["categoria"],
                   "downloads": g["downloads"], "versao": versao,
                   "repo_usado": repo_usado, "origem_repo": origem,
                   "etiqueta": tag, "ref_usada": "", "erro_clone": "",
                   "ramo": "", "commit": "", "raiz_codigo": sub or ".",
                   "tem_lib": "", "rb_alvo": 0, "rb_suite": 0, "lidos": 0,
                   "com_erro": 0, "com_erro_real": 0, "taxa": "",
                   "metodos": 0, "classes": 0}

            ok = clona(repo_usado, tag, dest)
            reg["ref_usada"] = ("etiqueta" if tag else "ramo por omissao") if ok else ""
            if not ok:
                reg["erro_clone"] = "nao clonou"
                linhas.append(reg)
                print(f"  [{i+1}/{len(gems)}] {nome}: NAO CLONOU", flush=True)
                continue

            raiz = os.path.join(dest, sub) if sub and os.path.isdir(os.path.join(dest, sub)) else dest
            reg["ramo"] = git(dest, "rev-parse", "--abbrev-ref", "HEAD")
            reg["commit"] = git(dest, "rev-parse", "HEAD")[:12]
            reg["tem_lib"] = os.path.isdir(os.path.join(raiz, "lib"))
            alvos, suite, por_pasta = lista_rb(raiz)
            reg["rb_alvo"], reg["rb_suite"] = len(alvos), len(suite)
            for pasta, n in sorted(por_pasta.items(), key=lambda x: -x[1]):
                onde.append({"gem": nome, "pasta": pasta, "rb": n,
                             "e_suite": pasta in SUITE})

            n_err = n_real = 0
            for r in analisa(alvos):
                rel = os.path.relpath(r["path"], raiz)
                nr = _nao_ruby(rel)
                errs = [] if r.get("fatal") else (r.get("errors") or [])
                if r.get("fatal"):
                    erros.append({"gem": nome, "ficheiro": rel, "linha": "",
                                  "mensagem": r["fatal"], "nao_ruby": nr})
                for e in errs[:3]:
                    erros.append({"gem": nome, "ficheiro": rel,
                                  "linha": e.get("line"),
                                  "mensagem": e.get("message"), "nao_ruby": nr})
                if errs or r.get("fatal"):
                    n_err += 1
                    n_real += 0 if nr else 1
                if r.get("fatal"):
                    continue
                ms = r.get("methods") or []
                cls = r.get("classes") or []
                reg["metodos"] += len(ms)
                reg["classes"] += len(cls)
                comum = {"gem": nome, "categoria": g["categoria"],
                         "ficheiro": rel, "commit": reg["commit"]}
                fcompleto.write(json.dumps({**comum, "classes": cls,
                                            "metodos": ms, "erros": errs},
                                           ensure_ascii=False) + "\n")
                fmods.write(json.dumps({**comum, "erro": bool(errs),
                                        "nao_ruby": nr, "metodos": len(ms),
                                        "classes": len(cls),
                                        "singletons": sum(1 for m in ms if m.get("singleton"))},
                                       ensure_ascii=False) + "\n")
            reg["lidos"] = len(alvos)
            reg["com_erro"], reg["com_erro_real"] = n_err, n_real
            reg["taxa"] = f"{100*(len(alvos)-n_err)/len(alvos):.1f}" if alvos else ""
            linhas.append(reg)
            print(f"  [{i+1}/{len(gems)}] {nome}: {len(alvos)} rb, {n_err} com erro, "
                  f"{reg['metodos']} metodos", flush=True)
            shutil.rmtree(dest, ignore_errors=True)
    finally:
        fcompleto.close()
        fmods.close()
        shutil.rmtree(trabalho, ignore_errors=True)

    def grava(nome, dados, campos):
        with open(os.path.join(OUT, nome), "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore")
            w.writeheader()
            w.writerows(dados)

    grava("parse.csv", linhas, list(linhas[0].keys()))
    grava("erros.csv", erros, ["gem", "ficheiro", "linha", "mensagem", "nao_ruby"])
    grava("onde_vive.csv", sorted(onde, key=lambda r: (r["gem"], -int(r["rb"]))),
          ["gem", "pasta", "rb", "e_suite"])

    com_rb = [L for L in linhas if int(L["rb_alvo"] or 0) > 0]
    funil = {"data": str(date.today()),
             "1_universo": len(linhas),
             "2_clonaram": sum(1 for L in linhas if not L["erro_clone"]),
             "3_com_ficheiros_rb": len(com_rb),
             "4_leem_sem_um_unico_erro": sum(1 for L in com_rb if not int(L["com_erro"] or 0)),
             "4b_leem_sem_erro_ignorando_moldes_e_fixtures":
                 sum(1 for L in com_rb if not int(L["com_erro_real"] or 0)),
             "ficheiros_rb_alvo": sum(int(L["rb_alvo"]) for L in com_rb),
             "ficheiros_da_suite_humana": sum(int(L["rb_suite"]) for L in com_rb),
             "ficheiros_com_erro": sum(int(L["com_erro"]) for L in com_rb),
             "ficheiros_com_erro_que_sao_ruby": sum(int(L["com_erro_real"]) for L in com_rb),
             "metodos": sum(int(L["metodos"]) for L in com_rb),
             "clonadas_pela_etiqueta_da_versao":
                 sum(1 for L in linhas if L["ref_usada"] == "etiqueta"),
             "repo_corrigido_pelo_rubygems":
                 [L["gem"] for L in linhas if L["origem_repo"] != "lista"]}
    json.dump(funil, open(f"{OUT}/funil.json", "w", encoding="utf-8"),
              indent=2, ensure_ascii=False)
    print("\n" + json.dumps({k: v for k, v in funil.items()
                             if not isinstance(v, list)}, indent=1))


if __name__ == "__main__":
    lim = int(sys.argv[sys.argv.index("--limite") + 1]) if "--limite" in sys.argv else None
    main(continuar="--continuar" in sys.argv, limite=lim)

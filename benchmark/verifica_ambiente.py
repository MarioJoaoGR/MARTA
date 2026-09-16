"""Verifica que cada módulo do corpus carrega COM A FERRAMENTA, antes do cluster.

A camada 6 do dataset certificou que os 500 módulos carregam. Mas certificou-os
com o seu próprio carregador, e a MARTA-Ruby chama o RSpec. Se os dois ambientes
não forem o mesmo, um módulo certificado falha no cluster e o erro conta contra a
ferramenta, sem ser culpa dela.

Este verificador fecha essa distância. Por cada módulo-alvo escreve um spec
trivial que só faz `require` do módulo, e corre-o pela MESMA função que a
ferramenta usa (``backend.run_tests``), no ambiente que o ``prepare`` montou.
Não chama modelo nenhum e não gasta GPU.

No fim confirma ainda que o helper de cobertura devolve, para cada ficheiro-alvo,
a chave com que a ferramenta o procura (``MethodTarget.source_rel``) — senão a
cobertura desse módulo sairia vazia sem dar erro.

Correr duas vezes: aqui, e no nó de login do Deucalion depois do ``prepare``,
para provar que o ambiente offline também está de pé.

    python -m benchmark.verifica_ambiente --projects-dir /caminho/ruby_projects
    python -m benchmark.verifica_ambiente --projects-dir ... --projects puma,jwt
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import pathlib
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from benchmark import prepare_ruby_projects as prep  # noqa: E402


def log(msg: str) -> None:
    print(msg, flush=True)


SPEC = '''require {req}
RSpec.describe {desc} do
  it "carrega" do
    expect(true).to eq(true)
  end
end
'''


def verifica_gem(gem: str, p: dict, projects_dir: pathlib.Path, preparado: dict,
                 workers: int) -> list:
    """Uma linha por módulo-alvo. Sequencial por gem (o GEM_HOME é global ao
    processo), com os módulos em paralelo dentro da gem."""
    from marta.ruby_backend.project import RubyProject

    clone = projects_dir / gem
    raiz = prep.raiz_de(clone, p)
    os.environ.update(prep.gem_env(clone, preparado["gems"]))

    t0 = time.time()
    proj = RubyProject(root_dir=str(raiz), source_dir=".",
                       target_files=[a["ficheiro"] for a in p["alvos"]],
                       load_paths=p["load_paths"], preload=p["entrada"] or None,
                       code_files=p["ficheiros_codigo"]).discover()
    t_parse = time.time() - t0

    # Um alvo por FICHEIRO (o require é do ficheiro, não do método).
    por_ficheiro = {}
    for t in proj.targets:
        por_ficheiro.setdefault(t.source_rel, t)
    meta = {a["ficheiro"]: a for a in p["alvos"]}

    scratch = tempfile.mkdtemp(prefix=f"verif_{gem}_")

    def um(rel: str) -> dict:
        t = por_ficheiro[rel]
        spec = os.path.join(scratch, rel.replace("/", "__") + "_spec.rb")
        with open(spec, "w", encoding="utf-8") as f:
            f.write(SPEC.format(req=json.dumps(t.require_target),
                                desc=json.dumps(f"carrega {rel}")))
        t1 = time.time()
        res = proj.backend.run_tests(spec, proj._load_path_list(), str(raiz))
        a = meta.get(rel, {})
        erro = "" if res.all_passed else \
            " ".join((res.output or "").split())[:300] or "sem saída"
        return {"gem": gem, "ficheiro": rel, "require": t.require_target,
                "modo": a.get("modo", ""), "origem": a.get("origem", ""),
                "estado": "ok" if res.all_passed else "falha",
                "erro": "" if res.all_passed else erro,
                "segundos": round(time.time() - t1, 2)}

    try:
        with ThreadPoolExecutor(max_workers=workers) as ex:
            linhas = list(ex.map(um, sorted(por_ficheiro)))

        # A cobertura vê estes ficheiros com a chave que a ferramenta usa?
        from marta.ruby_backend import coverage_runner as cov
        specs = [os.path.join(scratch, f) for f in sorted(os.listdir(scratch))
                 if f.endswith("_spec.rb")]
        chaves = set()
        if specs:
            try:
                r = cov.run_line_coverage(
                    ".", specs, cwd=str(raiz), timeout=1800, isolated=True,
                    load_paths=proj._load_path_list(),
                    requires=[p["entrada"]] if p["entrada"] else None)
                chaves = set(r.files)
            except Exception as e:
                log(f"    ! cobertura falhou: {repr(e)[:150]}")
    finally:
        import shutil
        shutil.rmtree(scratch, ignore_errors=True)

    for linha in linhas:
        linha["na_cobertura"] = linha["ficheiro"] in chaves

    ok = sum(1 for x in linhas if x["estado"] == "ok")
    sem_cov = sum(1 for x in linhas if not x["na_cobertura"])
    log(f"  {gem}: {ok}/{len(linhas)} carregam"
        + (f", {sem_cov} sem cobertura" if sem_cov else "")
        + f"  (parse {t_parse:.0f}s, {len(proj.targets)} métodos-alvo)")
    return linhas


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--projects-dir", required=True)
    ap.add_argument("--manifest", default=str(prep.PROJETOS))
    ap.add_argument("--projects", default=None, help="subconjunto separado por vírgulas")
    ap.add_argument("--workers", type=int, default=4,
                    help="módulos em paralelo dentro de cada gem")
    ap.add_argument("--out", default=None, help="CSV de saída (default: <projects-dir>/verificacao.csv)")
    args = ap.parse_args()

    projetos = prep.carrega_projetos(pathlib.Path(args.manifest))
    projects_dir = pathlib.Path(args.projects_dir).resolve()
    manifest = projects_dir / "manifest.json"
    if not manifest.exists():
        sys.exit(f"❌ {manifest} não existe: correr primeiro o prepare_ruby_projects")
    preparados = {r["gem"]: r for r in json.loads(manifest.read_text())["projetos"]
                  if r["estado"] == "pronto"}

    gems = sorted(g for g in projetos if g in preparados)
    if args.projects:
        pedidas = {x.strip() for x in args.projects.split(",")}
        gems = [g for g in gems if g in pedidas]
    fora = sorted(set(projetos) - set(preparados))
    if fora:
        log(f"⚠️  {len(fora)} gem(s) do corpus não preparadas: "
            f"{', '.join(fora[:10])}{' …' if len(fora) > 10 else ''}")

    log(f"A verificar {len(gems)} gems, "
        f"{sum(len(projetos[g]['alvos']) for g in gems)} módulos …")
    linhas = []
    for gem in gems:
        try:
            linhas += verifica_gem(gem, projetos[gem], projects_dir, preparados[gem],
                                   args.workers)
        except Exception as e:
            log(f"  {gem}: ERRO {repr(e)[:200]}")
            linhas.append({"gem": gem, "ficheiro": "", "require": "", "modo": "",
                           "origem": "", "estado": "erro", "erro": repr(e)[:300],
                           "segundos": 0, "na_cobertura": False})

    out = pathlib.Path(args.out) if args.out else projects_dir / "verificacao.csv"
    campos = ["gem", "ficheiro", "require", "modo", "origem", "estado", "erro",
              "na_cobertura", "segundos"]
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore")
        w.writeheader()
        w.writerows(linhas)

    ok = sum(1 for x in linhas if x["estado"] == "ok")
    sem_cov = [x for x in linhas if x["estado"] == "ok" and not x["na_cobertura"]]
    falhas = [x for x in linhas if x["estado"] != "ok"]
    log(f"\n{ok}/{len(linhas)} módulos carregam pela ferramenta → {out}")
    if sem_cov:
        log(f"⚠️  {len(sem_cov)} carregam mas não aparecem na cobertura "
            f"(ex.: {sem_cov[0]['gem']}/{sem_cov[0]['ficheiro']})")
    if falhas:
        log(f"❌ {len(falhas)} falham. Primeiras:")
        for x in falhas[:10]:
            log(f"   {x['gem']}/{x['ficheiro']} [{x['modo']}]: {x['erro'][:160]}")
        sys.exit(1)
    log("✅ ambiente igual ao que o dataset certificou; pode ir para o cluster")


if __name__ == "__main__":
    main()

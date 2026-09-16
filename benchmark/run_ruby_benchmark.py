"""Harness do benchmark MARTA-Ruby.

Não adivinha nada. Lê dois ficheiros:
  - ``projetos.json`` (camada 7 do dataset): os alvos e o ambiente certificado
    de cada gem;
  - ``<projects-dir>/manifest.json`` (``prepare_ruby_projects``): o que ficou de
    facto preparado.
Só corre gems que estejam nos dois. Não há modo "sem alvos": sem eles a
ferramenta tomava a gem inteira como alvo (83 766 métodos em vez de 6 976).

Por gem, duas fases separáveis:
  generate   corre a MARTA-Ruby no ambiente certificado       (precisa de GPU)
  measure    cobertura só dos specs gerados, no MESMO ambiente (só CPU)
No Deucalion a medição vai para a conta de CPU; ``--phase all`` faz as duas.

Resume: ``state.json`` guarda o estado por gem e por fase; um restart salta o
que já está feito (essencial no Deucalion, onde o walltime obriga a encadear).

    python -m benchmark.run_ruby_benchmark --projects-dir /data/ruby_projects \\
        --out-dir /data/results --num 3 [--phase generate|measure|all]
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import shlex
import shutil
import signal
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from benchmark import prepare_ruby_projects as prep  # noqa: E402

PYTHON = os.environ.get("USER_PYTHON_PATH", sys.executable)


def log(msg: str) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"[{ts}] {msg}", flush=True)


def _grava_json(path: pathlib.Path, dados) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(dados, indent=2, ensure_ascii=False) + "\n")
    os.replace(tmp, path)


class Harness:
    def __init__(self, projects_dir, out_dir, num, limit, timeout, projetos,
                 preparados, fresh_specs=False):
        self.projects_dir = pathlib.Path(projects_dir).resolve()
        self.out_dir = pathlib.Path(out_dir).resolve()
        self.num, self.limit, self.timeout = num, limit, timeout
        self.projetos, self.preparados = projetos, preparados
        self.fresh_specs = fresh_specs
        self.harness_dir = self.out_dir / "harness"
        self.logs_dir = self.harness_dir / "logs"
        self.state_path = self.harness_dir / "state.json"
        self.harness_dir.mkdir(parents=True, exist_ok=True)
        self.logs_dir.mkdir(parents=True, exist_ok=True)
        self.state = json.loads(self.state_path.read_text()) if self.state_path.exists() else {}

    def save(self):
        _grava_json(self.state_path, self.state)

    def _clone(self, gem) -> pathlib.Path:
        return self.projects_dir / gem

    # ---------------------------------------------------------------- run --
    def _run(self, cmd, cwd, log_path, timeout, extra_env=None):
        env = os.environ.copy()
        if extra_env:
            env.update(extra_env)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        t0 = time.time()
        try:
            with open(log_path, "w") as out:
                out.write(f"# $ {' '.join(shlex.quote(c) for c in cmd)}\n# cwd: {cwd}\n"
                          f"# started: {datetime.now(timezone.utc).isoformat()}\n\n")
                out.flush()
                r = subprocess.run(cmd, cwd=str(cwd), env=env, stdout=out,
                                   stderr=subprocess.STDOUT, timeout=timeout)
            return ("ok" if r.returncode == 0 else "failed"), time.time() - t0, \
                   ("" if r.returncode == 0 else f"returncode={r.returncode}")
        except subprocess.TimeoutExpired:
            return "timeout", time.time() - t0, f"after {timeout}s"
        except Exception as e:
            return "failed", time.time() - t0, repr(e)[:200]

    def run_marta(self, gem) -> bool:
        """Gera specs com a MARTA-Ruby, uma execução por gem."""
        key = f"marta_ruby/{gem}"
        if self.state.get(key, {}).get("status") in ("ok", "failed"):
            log(f"  {gem}: geração já feita ({self.state[key]['status']}), a saltar")
            return self.state[key]["status"] == "ok"

        p, pr = self.projetos[gem], self.preparados[gem]
        raiz = prep.raiz_de(self._clone(gem), p)
        # Runs independentes (desenho experimental: N runs + Wilcoxon): sem isto a
        # run k reutilizaria os specs da run k-1. As caches de ANÁLISE ficam.
        if self.fresh_specs:
            spec_dir = self.out_dir / gem / "marta_specs"
            if spec_dir.is_dir():
                shutil.rmtree(spec_dir)
                log(f"  {gem}: marta_specs/ limpo (--fresh-specs)")

        ambiente = self.harness_dir / f"ambiente_{gem}.json"
        _grava_json(ambiente, {"load_paths": p["load_paths"],
                               "preload": p["entrada"] or None,
                               "code_files": p["ficheiros_codigo"]})
        alvos = self.harness_dir / f"alvos_{gem}.json"
        _grava_json(alvos, [a["ficheiro"] for a in p["alvos"]])

        cmd = [PYTHON, "-m", "marta.ruby_backend.start_react",
               "--project_path", str(raiz), "--source_path", ".",
               "--project_name", gem,
               "--targets", str(alvos), "--environment", str(ambiente),
               "--num", str(self.num), "--output_dir", str(self.out_dir)]
        if self.limit:
            cmd += ["--limit", str(self.limit)]

        extra = prep.gem_env(self._clone(gem), pr["gems"])
        pp = [str(REPO)] + ([os.environ["PYTHONPATH"]] if os.environ.get("PYTHONPATH") else [])
        extra["PYTHONPATH"] = os.pathsep.join(pp)

        log(f"  {gem}: a gerar ({len(p['alvos'])} módulos, num={self.num}) …")
        status, elapsed, err = self._run(cmd, REPO, self.logs_dir / f"{gem}.log",
                                         self.timeout, extra)
        self.state[key] = {"status": status, "elapsed_s": round(elapsed, 1), "err": err}
        self.save()
        log(f"  └─ {status} ({elapsed/60:.1f} min)")
        return status == "ok"

    def measure(self, gem):
        """Cobertura SÓ dos specs gerados (marta_specs/), no ambiente certificado."""
        key = f"coverage/{gem}"
        if self.state.get(key, {}).get("status") == "ok":
            return
        p, pr = self.projetos[gem], self.preparados[gem]
        clone = self._clone(gem)
        t0 = time.time()
        try:
            from marta.ruby_backend import coverage_runner as cov
            from marta.ruby_backend.project import GENERATED_SPEC_DIR, RubyProject

            out_root = self.out_dir / gem
            spec_root = out_root / GENERATED_SPEC_DIR
            specs = sorted(str(s) for s in spec_root.glob("**/*.rb")) \
                if spec_root.is_dir() else []
            if not specs:
                self.state[key] = {"status": "no_specs"}
                self.save()
                return

            os.environ.update(prep.gem_env(clone, pr["gems"]))
            proj = RubyProject(root_dir=str(prep.raiz_de(clone, p)), source_dir=".",
                               output_root=str(out_root),
                               target_files=[a["ficheiro"] for a in p["alvos"]],
                               load_paths=p["load_paths"], preload=p["entrada"] or None,
                               code_files=p["ficheiros_codigo"]).discover()

            # CÓPIA DESCARTÁVEL (porte do fix Python b8cb6ac7): os testes gerados
            # podem criar/apagar ficheiros no cwd; medir sobre uma cópia torna a
            # medição reprodutível. As gems ficam fora da cópia: o ambiente aponta
            # para as originais, que nada escreve durante a medição.
            scratch = tempfile.mkdtemp(prefix=f"cov_{gem}_",
                                       dir=os.getenv("COV_SCRATCH") or None)
            try:
                copia = pathlib.Path(scratch) / gem
                shutil.copytree(str(clone), str(copia), symlinks=True,
                                ignore=shutil.ignore_patterns(".git", ".gem_home", ".gem_bundle"))
                raiz_copia = prep.raiz_de(copia, p)
                # Carregar TODOS os ficheiros-alvo antes: um ficheiro sem nenhum
                # spec verde não aparecia no Coverage, e as linhas dele saíam do
                # denominador. A percentagem subia por haver menos testes.
                carrega = pathlib.Path(scratch) / "_marta_carrega_alvos_spec.rb"
                reqs = sorted({t.require_target for t in proj.targets})
                carrega.write_text("".join(
                    f"begin; require {json.dumps(r)}; rescue Exception; end\n" for r in reqs))
                result = cov.run_line_coverage(
                    ".", [str(carrega), *specs], cwd=str(raiz_copia), timeout=1800,
                    isolated=True, load_paths=p["load_paths"],
                    requires=[p["entrada"]] if p["entrada"] else None)
            finally:
                shutil.rmtree(scratch, ignore_errors=True)

            por_modulo = {a["ficheiro"]: a for a in p["alvos"]}
            linhas, tot = [], dict(exec=0, cob=0, cob_invocados=0, ramos=0, ramos_cob=0,
                                   invocados=0, carregados=0)
            for t in proj.targets:
                rel = t.source_rel
                a = por_modulo.get(rel, {})
                lines = result.files.get(rel)
                mc = cov.synthesize(t.method, lines, result.branches.get(rel),
                                    result.methods.get(rel)) if lines else None
                linha = {"metodo": t.method.qualified_name, "ficheiro": rel,
                         "origem": a.get("origem"), "modo": a.get("modo"),
                         "vizinhos_no_corpus": a.get("vizinhos_no_corpus"),
                         "carregado": mc is not None}
                if mc is not None:
                    linha.update(linhas_executaveis=mc.executable_lines,
                                 linhas_cobertas=mc.covered_lines,
                                 ramos=mc.total_branches, ramos_cobertos=mc.covered_branches,
                                 invocado=mc.invoked)
                    tot["exec"] += mc.executable_lines
                    tot["cob"] += mc.covered_lines
                    tot["ramos"] += mc.total_branches
                    tot["ramos_cob"] += mc.covered_branches
                    tot["carregados"] += 1
                    if mc.invoked:
                        tot["invocados"] += 1
                        tot["cob_invocados"] += mc.covered_lines
                linhas.append(linha)
            _grava_json(out_root / "cobertura_por_metodo.json", linhas)

            def pct(a, b):
                return round(100 * a / b, 2) if b else 0.0
            self.state[key] = {
                "status": "ok", "elapsed_s": round(time.time() - t0, 1),
                "spec_files": len(specs), "metodos_alvo": len(proj.targets),
                "metodos_carregados": tot["carregados"],
                "metodos_invocados": tot["invocados"],
                "linhas_executaveis": tot["exec"], "linhas_cobertas": tot["cob"],
                "cobertura_linhas_pct": pct(tot["cob"], tot["exec"]),
                # A mesma cobertura, mas só a contar métodos que chegaram a ser
                # chamados: tira o `def` executado ao carregar o ficheiro.
                "cobertura_linhas_so_invocados_pct": pct(tot["cob_invocados"], tot["exec"]),
                "ramos": tot["ramos"], "ramos_cobertos": tot["ramos_cob"],
                "cobertura_ramos_pct": pct(tot["ramos_cob"], tot["ramos"]),
            }
            s = self.state[key]
            log(f"  └─ cobertura: {s['cobertura_linhas_pct']}% linhas "
                f"({s['cobertura_linhas_so_invocados_pct']}% só invocados), "
                f"{s['cobertura_ramos_pct']}% ramos, "
                f"{tot['invocados']}/{len(proj.targets)} métodos invocados")
        except Exception as e:
            self.state[key] = {"status": "error", "err": repr(e)[:300],
                               "elapsed_s": round(time.time() - t0, 1)}
            log(f"  └─ erro na medição: {repr(e)[:150]}")
        self.save()

    def report(self):
        rows = {k.split("/", 1)[1]: v for k, v in self.state.items()
                if k.startswith("coverage/") and v.get("status") == "ok"}
        out = self.out_dir / "results.json"
        _grava_json(out, {"projetos": rows, "state": self.state})
        if rows:
            log("")
            log(f"{'gem':24s}{'specs':>7s}{'métodos':>9s}{'invoc.':>8s}{'linhas':>9s}{'ramos':>8s}")
            for n, v in sorted(rows.items()):
                log(f"{n:24s}{v['spec_files']:>7}{v['metodos_alvo']:>9}"
                    f"{v['metodos_invocados']:>8}{v['cobertura_linhas_pct']:>8}%"
                    f"{v['cobertura_ramos_pct']:>7}%")
        log(f"resultados → {out}")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--projects-dir", required=True, help="dir preparado (prepare_ruby_projects)")
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--manifest", default=str(prep.PROJETOS), help="projetos.json da camada 7")
    ap.add_argument("--projects", default=None, help="subconjunto separado por vírgulas")
    ap.add_argument("--phase", choices=("all", "generate", "measure"), default="all")
    ap.add_argument("--num", type=int, default=3, help="rondas do loop de cobertura")
    ap.add_argument("--limit", type=int, default=None, help="limitar métodos-alvo (smoke)")
    ap.add_argument("--timeout", type=int, default=0, help="timeout por gem (0 = sem limite)")
    ap.add_argument("--fresh-specs", action="store_true",
                    help="apaga marta_specs/ de cada gem antes de gerar "
                         "(runs independentes p/ o desenho N-runs+Wilcoxon)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--reset", action="store_true")
    args = ap.parse_args()

    projetos = prep.carrega_projetos(pathlib.Path(args.manifest))
    manifest = pathlib.Path(args.projects_dir) / "manifest.json"
    if not manifest.exists():
        sys.exit(f"❌ {manifest} não existe: correr primeiro "
                 f"`python -m benchmark.prepare_ruby_projects --out {args.projects_dir}`")
    preparados = {r["gem"]: r for r in json.loads(manifest.read_text())["projetos"]
                  if r["estado"] == "pronto"}

    gems = sorted(g for g in projetos if g in preparados
                  and preparados[g]["commit"] == projetos[g]["commit"])
    nao_prontas = sorted(set(projetos) - set(gems))
    if args.projects:
        pedidas = {x.strip() for x in args.projects.split(",")}
        desconhecidas = sorted(pedidas - set(projetos))
        if desconhecidas:
            sys.exit(f"❌ não estão no corpus: {', '.join(desconhecidas)}")
        nao_prontas = sorted(pedidas - set(gems))
        gems = [g for g in gems if g in pedidas]
    if nao_prontas:
        log(f"⚠️  {len(nao_prontas)} gem(s) do corpus não preparadas, ficam de fora: "
            f"{', '.join(nao_prontas[:10])}{' …' if len(nao_prontas) > 10 else ''}")

    h = Harness(args.projects_dir, args.out_dir, args.num, args.limit, args.timeout or None,
                projetos, preparados, fresh_specs=args.fresh_specs)
    if args.reset and h.state_path.exists():
        h.state_path.unlink()
        h.state = {}
        log("state.json apagado (reset)")

    modulos = sum(len(projetos[g]["alvos"]) for g in gems)
    log(f"MARTA-Ruby benchmark · {len(gems)} gems · {modulos} módulos · fase={args.phase} "
        f"· num={args.num} · modelo={os.environ.get('MODEL', '(default do .env)')}")
    if args.dry_run:
        for g in gems:
            p = projetos[g]
            log(f"  • {g}: {len(p['alvos'])} módulos, raiz={p['raiz']}, "
                f"{p['ambiente']}, porta={p['entrada'] or '(nenhuma)'}")
        log("(dry-run; a sair)")
        return

    # SLURM manda SIGTERM antes do walltime: gravar estado e sair limpo (o
    # script de job encadeia a continuação, que retoma via state.json).
    def _sigterm(signum, frame):
        log("SIGTERM recebido — estado gravado; a sair para encadear continuação")
        h.save()
        sys.exit(143)
    signal.signal(signal.SIGTERM, _sigterm)

    for gem in gems:
        log(f"▶ {gem}")
        if args.phase in ("all", "generate"):
            gerou = h.run_marta(gem)
        else:
            gerou = h.state.get(f"marta_ruby/{gem}", {}).get("status") == "ok"
            if not gerou:
                log(f"  {gem}: sem geração concluída, nada para medir")
        if gerou and args.phase in ("all", "measure"):
            h.measure(gem)
    h.report()


if __name__ == "__main__":
    main()

"""Harness do benchmark MARTA-Ruby (espelha scripts/run_benchmark.py).

Por projeto preparado (ver ``prepare_ruby_projects.py``):
  1. corre a MARTA-Ruby (``marta.ruby_backend.start_react``) → specs em marta_specs/
  2. mede a cobertura **só dos specs gerados** (isolada da suite humana)
  3. grava métricas por projeto e acumula em results.json

Resume: ``state.json`` guarda o estado por projeto; um restart salta o que já
está ``ok``/``failed`` (idêntico ao harness Python — essencial no Deucalion, onde
o walltime obriga a encadear jobs).

    python -m benchmark.run_ruby_benchmark --projects-dir /data/ruby_projects \\
        --out-dir /data/results --num 3
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import shlex
import signal
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone

REPO = pathlib.Path(__file__).resolve().parent.parent
PYTHON = os.environ.get("USER_PYTHON_PATH", sys.executable)
RUBY_BIN = os.environ.get("MARTA_RUBY_BIN", "ruby")


def log(msg: str) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"[{ts}] {msg}", flush=True)


def _gem_env(proj: pathlib.Path) -> dict:
    """GEM_HOME/GEM_PATH para correr os specs do projeto.

    GEM_PATH tem de incluir o ``.gem_home`` do projeto (deps do código sob teste,
    pré-instaladas offline) **E** o store global (onde vive o rspec). Apontar só
    para o do projeto escondia o rspec: `can't find gem rspec-core`.
    """
    gem_home = proj / ".gem_home"
    try:
        default_dir = subprocess.run([RUBY_BIN, "-e", "print Gem.default_dir"],
                                     capture_output=True, text=True, errors='replace', timeout=30).stdout.strip()
    except Exception:
        default_dir = ""
    paths = [str(gem_home)] + ([default_dir] if default_dir else [])
    if os.environ.get("GEM_PATH"):
        paths.append(os.environ["GEM_PATH"])
    return {"GEM_HOME": str(gem_home), "GEM_PATH": os.pathsep.join(paths)}


class Harness:
    def __init__(self, projects_dir, out_dir, num, limit, timeout, fresh_specs=False,
                 targets=None):
        self.projects_dir = pathlib.Path(projects_dir).resolve()
        self.out_dir = pathlib.Path(out_dir).resolve()
        self.num, self.limit, self.timeout = num, limit, timeout
        self.fresh_specs = fresh_specs
        self.targets = targets or {}
        self.harness_dir = self.out_dir / "harness"
        self.logs_dir = self.harness_dir / "logs"
        self.state_path = self.harness_dir / "state.json"
        self.harness_dir.mkdir(parents=True, exist_ok=True)
        self.logs_dir.mkdir(parents=True, exist_ok=True)
        self.state = json.loads(self.state_path.read_text()) if self.state_path.exists() else {}

    def save(self):
        self.state_path.write_text(json.dumps(self.state, indent=2) + "\n")

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

    def run_marta(self, name, info):
        """Gera specs com a MARTA-Ruby. Um run por projeto."""
        key = f"marta_ruby/{name}"
        if self.state.get(key, {}).get("status") in ("ok", "failed"):
            log(f"  {name}: já feito ({self.state[key]['status']}), a saltar")
            return self.state[key]["status"] == "ok"

        proj = self.projects_dir / name
        # Runs independentes (desenho experimental: N runs + Wilcoxon): sem
        # isto, a run k reutilizaria os specs da run k-1 (o skip resume-safe vê
        # os ficheiros no projeto e não regenera). As caches de ANÁLISE ficam —
        # são contexto determinístico, reutilizado entre runs também no Python.
        if self.fresh_specs:
            import shutil
            spec_dir = self.out_dir / name / "marta_specs"
            if spec_dir.is_dir():
                shutil.rmtree(spec_dir)
                log(f"  {name}: marta_specs/ limpo (--fresh-specs)")
        cmd = [PYTHON, "-m", "marta.ruby_backend.start_react",
               "--project_path", str(proj),
               "--source_path", info["source_path"],
               "--num", str(self.num),
               "--output_dir", str(self.out_dir)]
        if self.limit:
            cmd += ["--limit", str(self.limit)]
        # Seleção de ficheiros-alvo (benchmark/select_targets.py): escreve a
        # lista deste projeto num ficheiro temporário e passa-a ao CLI.
        if self.targets and name in self.targets:
            tf = self.harness_dir / f"targets_{name}.json"
            tf.write_text(json.dumps(self.targets[name]["files"], indent=2))
            cmd += ["--targets", str(tf)]

        extra = _gem_env(proj)
        pp = [str(REPO)] + ([os.environ["PYTHONPATH"]] if os.environ.get("PYTHONPATH") else [])
        extra["PYTHONPATH"] = os.pathsep.join(pp)

        log(f"  {name}: a gerar (num={self.num}) …")
        status, elapsed, err = self._run(cmd, REPO, self.logs_dir / f"{name}.log",
                                         self.timeout, extra)
        self.state[key] = {"status": status, "elapsed_s": round(elapsed, 1), "err": err}
        self.save()
        log(f"  └─ {status} ({elapsed/60:.1f} min)")
        return status == "ok"

    def measure(self, name, info):
        """Cobertura SÓ dos specs gerados (marta_specs/), isolada da suite humana."""
        key = f"coverage/{name}"
        if self.state.get(key, {}).get("status") == "ok":
            return
        proj = self.projects_dir / name
        try:
            sys.path.insert(0, str(REPO))
            from marta.ruby_backend import coverage_runner as cov
            from marta.ruby_backend.project import GENERATED_SPEC_DIR, RubyProject

            out_root = self.out_dir / name
            spec_root = out_root / GENERATED_SPEC_DIR
            specs = sorted(str(p) for p in spec_root.glob("**/*.rb")) \
                if spec_root.is_dir() else []
            if not specs:
                self.state[key] = {"status": "no_specs"}
                self.save()
                return

            os.environ.update(_gem_env(proj))  # deps do projeto + rspec global
            p = RubyProject(root_dir=str(proj), source_dir=info["source_path"],
                            output_root=str(out_root)).discover()

            # CÓPIA DESCARTÁVEL (porte do fix Python b8cb6ac7): os testes
            # gerados podem criar/apagar ficheiros no cwd. Medir com cwd no
            # diretório REAL do projeto deixava-o num estado diferente a cada
            # medição — no lado Python o mesmo projeto deu 27.7% numa execução e
            # 8.4% noutra com os MESMOS ficheiros. Medir sobre uma cópia torna a
            # medição reprodutível e impede que uma medição contamine a seguinte.
            scratch = tempfile.mkdtemp(prefix=f"cov_{name}_",
                                       dir=os.getenv("COV_SCRATCH") or None)
            try:
                proj_copy = os.path.join(scratch, proj.name)
                shutil.copytree(str(proj), proj_copy, symlinks=True)
                result = cov.run_line_coverage(info["source_path"], specs,
                                               cwd=proj_copy, timeout=1800,
                                               isolated=True)
            finally:
                shutil.rmtree(scratch, ignore_errors=True)
            tot_exec = tot_cov = fully = 0
            for t in p.targets:
                lines = result.files.get(t.source_rel)
                if not lines:
                    continue
                mc = cov.synthesize(t.method, lines)
                tot_exec += mc.executable_lines
                tot_cov += mc.covered_lines
                fully += 1 if mc.fully_covered and mc.executable_lines else 0
            pct = round(100 * tot_cov / tot_exec, 2) if tot_exec else 0.0
            self.state[key] = {"status": "ok", "spec_files": len(specs),
                               "target_methods": len(p.targets),
                               "methods_fully_covered": fully,
                               "covered_lines": tot_cov, "executable_lines": tot_exec,
                               "line_coverage_pct": pct}
            log(f"  └─ cobertura (só gerados): {pct}%  ({len(specs)} specs, "
                f"{fully}/{len(p.targets)} métodos 100%)")
        except Exception as e:
            self.state[key] = {"status": "error", "err": repr(e)[:300]}
            log(f"  └─ erro na medição: {repr(e)[:150]}")
        self.save()

    def report(self):
        rows = []
        for k, v in self.state.items():
            if k.startswith("coverage/") and v.get("status") == "ok":
                rows.append((k.split("/", 1)[1], v))
        out = self.out_dir / "results.json"
        out.write_text(json.dumps({"projects": dict(rows), "state": self.state}, indent=2) + "\n")
        if rows:
            log("")
            log(f"{'projeto':14s}{'specs':>7s}{'métodos':>9s}{'100%':>7s}{'cobertura':>11s}")
            for n, v in rows:
                log(f"{n:14s}{v['spec_files']:>7}{v['target_methods']:>9}"
                    f"{v['methods_fully_covered']:>7}{v['line_coverage_pct']:>10}%")
        log(f"resultados → {out}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--projects-dir", required=True, help="dir preparado (prepare_ruby_projects)")
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--projects", default=None, help="subset separado por vírgulas")
    ap.add_argument("--num", type=int, default=3, help="rondas do loop de cobertura")
    ap.add_argument("--limit", type=int, default=None, help="limitar métodos-alvo (smoke)")
    ap.add_argument("--timeout", type=int, default=0, help="timeout por projeto (0 = sem limite)")
    ap.add_argument("--targets", default=None,
                    help="targets.json do select_targets (limita os ficheiros-alvo)")
    ap.add_argument("--fresh-specs", action="store_true",
                    help="apaga marta_specs/ de cada projeto antes de gerar "
                         "(runs independentes p/ o desenho N-runs+Wilcoxon)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--reset", action="store_true")
    args = ap.parse_args()

    cfg_path = pathlib.Path(args.projects_dir) / "manifest.json"
    config = json.loads((REPO / "benchmark" / "ruby_projects.json").read_text())
    config = {k: v for k, v in config.items() if not k.startswith("_")}
    if cfg_path.exists():  # respeita o que foi realmente preparado
        prepared = {p["project"] for p in json.loads(cfg_path.read_text())["projects"]
                    if p["status"].startswith("ready")}
        config = {k: v for k, v in config.items() if k in prepared}
    if args.projects:
        wanted = {p.strip() for p in args.projects.split(",")}
        config = {k: v for k, v in config.items() if k in wanted}

    targets = None
    if args.targets:
        targets = json.loads(pathlib.Path(args.targets).read_text())["projects"]
    h = Harness(args.projects_dir, args.out_dir, args.num, args.limit,
                args.timeout or None, fresh_specs=args.fresh_specs, targets=targets)
    if args.reset and h.state_path.exists():
        h.state_path.unlink()
        h.state = {}
        log("state.json apagado (reset)")

    log(f"MARTA-Ruby benchmark · {len(config)} projetos · num={args.num} · "
        f"modelo={os.environ.get('MODEL', '(default do .env)')}")
    for n, i in config.items():
        log(f"  • {n} (source={i['source_path']}, suite humana={i['human_suite']})")
    if args.dry_run:
        log("(dry-run; a sair)")
        return

    # SLURM manda SIGTERM antes do walltime: gravar estado e sair limpo (o
    # script de job encadeia a continuação, que retoma via state.json).
    def _sigterm(signum, frame):
        log("SIGTERM recebido — estado gravado; a sair para encadear continuação")
        h.save()
        sys.exit(143)
    signal.signal(signal.SIGTERM, _sigterm)

    for name, info in config.items():
        log(f"▶ {name}")
        if h.run_marta(name, info):
            h.measure(name, info)
    h.report()


if __name__ == "__main__":
    main()

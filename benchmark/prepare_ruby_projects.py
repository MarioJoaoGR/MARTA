"""Prepara os projetos Ruby do benchmark (PASSO COM REDE — correr ANTES do job).

Os nós de computação do Deucalion não têm rede, por isso os projetos têm de vir
clonados e com as dependências instaladas — o análogo do que o .sif faz para o
benchmark Python (projetos pip-installed em build-time).

Por cada projeto de ``ruby_projects.json``:
  clone --> checkout do commit FIXADO --> instala runtime deps do gemspec num
  GEM_HOME local ao projeto (``.gem_home/``), sem tocar no gem-store do sistema.

O diretório resultante é auto-contido: copia-se/bind-monta-se no Deucalion e o
harness corre offline (basta GEM_HOME apontar para ``<proj>/.gem_home``).

    python -m benchmark.prepare_ruby_projects --out /caminho/para/ruby_projects
    python -m benchmark.prepare_ruby_projects --out ... --projects faker,fpm
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import pathlib
import subprocess
import sys
import time

REPO = pathlib.Path(__file__).resolve().parent.parent
CONFIG = REPO / "benchmark" / "ruby_projects.json"
RUBY_BIN = os.environ.get("MARTA_RUBY_BIN", "ruby")
_BIN = os.path.dirname(RUBY_BIN)
GEM_BIN = os.path.join(_BIN, "gem") if _BIN else "gem"
BUNDLE_BIN = os.path.join(_BIN, "bundle") if _BIN else "bundle"


def _run(cmd, cwd=None, timeout=600, env=None, quiet=True):
    try:
        r = subprocess.run(cmd, cwd=cwd, timeout=timeout, env=env,
                           capture_output=True, text=True, errors='replace')
        if r.returncode != 0 and not quiet:
            print(f"    ! {' '.join(cmd[:3])}: {(r.stderr or r.stdout)[-300:]}")
        return r.returncode == 0, (r.stderr or r.stdout)[-400:]
    except subprocess.TimeoutExpired:
        return False, "timeout"
    except Exception as e:
        return False, repr(e)[:200]


def prepare(name: str, info: dict, out_dir: pathlib.Path, timeout: int) -> dict:
    dest = out_dir / name
    res = {"project": name, "repo": info["repo"], "commit": info["commit"]}

    if not dest.exists():
        # Clone completo (precisamos de fazer checkout de um commit antigo, por
        # isso NÃO se pode usar --depth 1).
        ok, err = _run(["git", "clone", f"https://github.com/{info['repo']}", str(dest)],
                       timeout=timeout)
        if not ok:
            return {**res, "status": "clone_failed", "detail": err}

    ok, err = _run(["git", "-C", str(dest), "checkout", "--quiet", info["commit"]],
                   timeout=180)
    if not ok:
        return {**res, "status": "checkout_failed", "detail": err}

    src = dest / info["source_path"]
    if not src.is_dir():
        return {**res, "status": "no_source", "detail": f"{info['source_path']} nao existe"}

    # Runtime deps num GEM_HOME local ao projeto (auto-contido, portável).
    gem_home = dest / ".gem_home"
    gem_home.mkdir(exist_ok=True)
    env = {**os.environ, "GEM_HOME": str(gem_home), "GEM_PATH": str(gem_home)}

    specs = sorted(glob.glob(str(dest / "*.gemspec")))
    installed, detail = False, "sem gemspec na raiz"
    if specs:
        ok, err = _run([GEM_BIN, "build", os.path.basename(specs[0])],
                       cwd=str(dest), timeout=180, env=env)
        if ok:
            built = sorted(glob.glob(str(dest / "*.gem")))
            if built:
                installed, detail = _run(
                    [GEM_BIN, "install", os.path.basename(built[-1]),
                     "--install-dir", str(gem_home), "--no-document"],
                    cwd=str(dest), timeout=timeout, env=env)
        else:
            detail = f"gem build falhou: {err}"

    rb_files = len(glob.glob(str(src / "**" / "*.rb"), recursive=True))
    return {**res, "status": "ready" if installed else "ready_no_deps",
            "source_path": info["source_path"], "rb_files": rb_files,
            "gem_home": str(gem_home), "deps_detail": None if installed else detail}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True, help="diretório de saída (auto-contido)")
    ap.add_argument("--projects", default=None, help="subset separado por vírgulas")
    ap.add_argument("--timeout", type=int, default=900)
    args = ap.parse_args()

    cfg = {k: v for k, v in json.loads(CONFIG.read_text()).items() if not k.startswith("_")}
    if args.projects:
        wanted = {p.strip() for p in args.projects.split(",")}
        cfg = {k: v for k, v in cfg.items() if k in wanted}

    out_dir = pathlib.Path(args.out).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"A preparar {len(cfg)} projetos em {out_dir}\n")

    results = []
    for name, info in cfg.items():
        t0 = time.time()
        print(f"→ {name} ({info['repo']} @ {info['commit'][:10]}) ...", flush=True)
        r = prepare(name, info, out_dir, args.timeout)
        r["seconds"] = round(time.time() - t0, 1)
        results.append(r)
        extra = f" ({r['rb_files']} .rb)" if r.get("rb_files") else ""
        print(f"   {r['status']}{extra}  {r['seconds']}s")
        if r.get("deps_detail"):
            print(f"   nota deps: {str(r['deps_detail'])[:150]}")

    manifest = out_dir / "manifest.json"
    manifest.write_text(json.dumps({"projects": results}, indent=2) + "\n")
    ready = sum(1 for r in results if r["status"].startswith("ready"))
    print(f"\n{ready}/{len(results)} prontos. Manifesto: {manifest}")
    print("Copiar/bind-montar este diretório no Deucalion e apontar o harness com --projects-dir.")


if __name__ == "__main__":
    sys.exit(main())

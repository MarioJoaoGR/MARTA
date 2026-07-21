"""Portão final do corpus: instalabilidade isolada (o que a análise estática não vê).

Percorre a ordenação de diversidade (corpus_selection.json) e, por cada gem:
  clone raso (regista o SHA = pinning) -> `bundle install` ISOLADO em
  vendor/bundle dentro do clone (nada no gem-store global) -> confirma que
  instala sem extensões nativas pesadas -> APAGA o clone.
Mantém as TARGET primeiras que instalam limpo; as que falham (ex.: mysql2 precisa
de libmysqlclient) são o filtro de "sem deps nativas pesadas" a funcionar.

Restrição do utilizador: nada fica instalado no sistema, tudo em vendor/bundle
temporário, apagado no fim.

    python -m benchmark.finalize_corpus            # alvo 12
    python -m benchmark.finalize_corpus --target 12 --timeout 240
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import time

RUBY_BIN = os.environ.get("MARTA_RUBY_BIN", "ruby")
_BIN = os.path.dirname(RUBY_BIN)
GEM_BIN = os.path.join(_BIN, "gem") if _BIN else "gem"


def _run(cmd, cwd, timeout, env=None):
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                           timeout=timeout, env=env)
        return r.returncode == 0, (r.stderr or r.stdout)[-500:]
    except subprocess.TimeoutExpired:
        return False, "timeout"
    except Exception as e:
        return False, str(e)[:300]


import glob


def _has_native_ext(dest: str) -> bool:
    """Extensão C/nativa: precisa de compilação + libs de sistema — a 'dep nativa
    pesada' a evitar (não portável ao Deucalion). Sinal: ext/**/extconf.rb."""
    return bool(glob.glob(os.path.join(dest, "ext", "**", "extconf.rb"), recursive=True)) \
        or bool(glob.glob(os.path.join(dest, "ext", "**", "*.c"), recursive=True))


def try_install(repo_url: str, dest: str, timeout: int):
    ok, err = _run(["git", "clone", "--depth", "1", repo_url, dest], cwd=".", timeout=120)
    if not ok:
        return {"status": "clone_failed", "detail": err}
    sha = subprocess.run(["git", "-C", dest, "rev-parse", "HEAD"],
                         capture_output=True, text=True).stdout.strip()

    if _has_native_ext(dest):
        return {"status": "native_extension", "sha": sha}

    specs = glob.glob(os.path.join(dest, "*.gemspec"))
    if not specs:
        return {"status": "no_gemspec", "sha": sha}

    # Instalar SÓ as runtime deps do gemspec (não o Gemfile de dev do repo, que
    # arrasta tooling irrelevante e dava falsos install_failed). Tudo num GEM_HOME
    # isolado dentro do clone -> nada no store global, apagado com o clone.
    gem_home = os.path.join(dest, ".gem_home")
    env = {**os.environ, "GEM_HOME": gem_home, "GEM_PATH": gem_home}
    ok, err = _run([GEM_BIN, "build", os.path.basename(specs[0])], dest, 60, env)
    if not ok:
        return {"status": "build_failed", "sha": sha, "detail": err}
    built = sorted(glob.glob(os.path.join(dest, "*.gem")))
    if not built:
        return {"status": "build_failed", "sha": sha}
    ok, err = _run([GEM_BIN, "install", os.path.basename(built[-1]),
                    "--install-dir", gem_home, "--no-document"], dest, timeout, env)
    return {"status": "installed" if ok else "install_failed",
            "sha": sha, "detail": None if ok else err}


def main(target=12, timeout=240):
    sel = json.load(open("benchmark/results/corpus_selection.json", encoding="utf-8"))["selected"]
    work = tempfile.mkdtemp(prefix="marta_final_")
    final, results = [], []
    try:
        for s in sel:
            if len(final) >= target:
                break
            dest = os.path.join(work, s["gem"])
            t0 = time.time()
            r = try_install(s["clone"] if "clone" in s else f"https://github.com/{s['repo']}",
                            dest, timeout)
            r.update({"gem": s["gem"], "repo": s["repo"], "rank": s["rank"],
                      "seconds": round(time.time() - t0, 1)})
            results.append(r)
            mark = "OK" if r["status"] == "installed" else f"DROP ({r['status']})"
            print(f"  #{s['rank']:>2} {s['gem']:20s} {mark:28s} {r['seconds']}s", flush=True)
            if r["status"] == "installed":
                final.append({"gem": s["gem"], "repo": s["repo"], "sha": r["sha"],
                              "section": s["section"], "downloads": s["downloads"],
                              "metrics": s["metrics"], "code": s.get("code")})
            shutil.rmtree(dest, ignore_errors=True)  # limpa JA
    finally:
        shutil.rmtree(work, ignore_errors=True)  # limpeza total

    os.makedirs("benchmark/results", exist_ok=True)
    json.dump({"target": target, "corpus": final, "attempts": results},
              open("benchmark/results/corpus_final.json", "w", encoding="utf-8"), indent=2)
    print(f"\nCORPUS FINAL: {len(final)} gems instaladas limpas (de {len(results)} tentadas). "
          f"Clones apagados. -> benchmark/results/corpus_final.json")
    for c in final:
        print(f"  {c['gem']:20s} @ {c['sha'][:10]}  [{c['section']}]")


if __name__ == "__main__":
    tgt = int(sys.argv[sys.argv.index("--target") + 1]) if "--target" in sys.argv else 12
    tmo = int(sys.argv[sys.argv.index("--timeout") + 1]) if "--timeout" in sys.argv else 240
    main(target=tgt, timeout=tmo)

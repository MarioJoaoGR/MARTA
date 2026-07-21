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
BUNDLE_BIN = os.path.join(os.path.dirname(RUBY_BIN), "bundle") if os.path.dirname(RUBY_BIN) else "bundle"


def _run(cmd, cwd, timeout):
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)
        return r.returncode == 0, (r.stderr or r.stdout)[-500:]
    except subprocess.TimeoutExpired:
        return False, "timeout"
    except Exception as e:
        return False, str(e)[:300]


def try_install(repo_url: str, dest: str, timeout: int):
    ok, err = _run(["git", "clone", "--depth", "1", repo_url, dest], cwd=".", timeout=120)
    if not ok:
        return {"status": "clone_failed", "detail": err}
    sha = subprocess.run(["git", "-C", dest, "rev-parse", "HEAD"],
                         capture_output=True, text=True).stdout.strip()
    if not os.path.exists(os.path.join(dest, "Gemfile")):
        return {"status": "no_gemfile", "sha": sha}
    # Isolar: gems vão para vendor/bundle DENTRO do clone (nada no store global).
    _run([BUNDLE_BIN, "config", "set", "--local", "path", "vendor/bundle"], dest, 30)
    ok, err = _run([BUNDLE_BIN, "install", "--jobs", "4"], dest, timeout)
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

"""Diagnóstico de candidatas ao corpus MARTA-Ruby (sem LLM).

Para cada gem clonada mede, de forma reprodutível:
  * identidade      — commit pinado, framework de teste detetado
  * dimensão        — ficheiros .rb, métodos-alvo, classes, LOC
  * análise estática— arestas do call graph, erros de parse, targets com tipos
  * suite humana    — nº de testes, verde?, e **cobertura-base** dos métodos-alvo

A cobertura-base é o critério que a lição da `money` (99.8%) tornou obrigatório:
gems quase totalmente cobertas deixam pouca margem para a ferramenta demonstrar
ganho. Output em JSON + tabela markdown, para entrar direto no paper.

    python -m benchmark.diagnose sondagens/targets/money sondagens/targets/faker ...
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from typing import Optional

from marta.ruby_backend import coverage_runner as cov
from marta.ruby_backend.backend import MinitestBackend, detect_backend
from marta.ruby_backend.project import RubyProject
from marta.ruby_backend.ruby_ast import RubyParseError

SOURCE_CANDIDATES = ("lib", "src")


def _source_dir(root: str) -> Optional[str]:
    for d in SOURCE_CANDIDATES:
        if os.path.isdir(os.path.join(root, d)):
            return d
    return None


def _git(root: str, *args) -> str:
    try:
        return subprocess.run(["git", "-C", root, *args], capture_output=True,
                              text=True, timeout=30).stdout.strip()
    except Exception:
        return ""


def _loc(root: str, source_dir: str) -> int:
    total = 0
    for dirpath, _dirs, files in os.walk(os.path.join(root, source_dir)):
        for f in files:
            if f.endswith(".rb"):
                try:
                    with open(os.path.join(dirpath, f), "r", encoding="utf-8",
                              errors="ignore") as fh:
                        total += sum(1 for _ in fh)
                except OSError:
                    pass
    return total


def _human_suite_coverage(root: str, source_dir: str, proj: RubyProject,
                          minitest: bool) -> dict:
    """Corre a suite HUMANA sob Coverage e sintetiza cobertura dos métodos-alvo.

    Nota: aqui NÃO se isola a config do projeto (isolated=False) — a suite
    humana precisa do seu spec_helper/.rspec. É o oposto do que fazemos com os
    testes gerados.
    """
    test_dir = "test" if minitest else "spec"
    if not os.path.isdir(os.path.join(root, test_dir)):
        return {"error": f"sem {test_dir}/"}
    if minitest:
        # Minitest usa DUAS convenções de nome: `foo_test.rb` (i18n, rubyzip) e
        # `test_foo.rb` (faker). Apanhar só uma perde a suite inteira.
        found = []
        for dirpath, _d, files in os.walk(os.path.join(root, test_dir)):
            for f in files:
                if f.endswith("_test.rb") or (f.startswith("test_") and f.endswith(".rb")):
                    found.append(os.path.relpath(os.path.join(dirpath, f), root))
        if not found:
            return {"error": f"sem ficheiros de teste reconheciveis em {test_dir}/"}
        specs = sorted(found)[:400]
    else:
        specs = [test_dir]

    try:
        t0 = time.time()
        result = cov.run_line_coverage(source_dir, specs, cwd=root,
                                       timeout=900, isolated=False, minitest=minitest)
        dt = time.time() - t0
    except RubyParseError as e:
        return {"error": str(e)[:160]}

    total_exec = total_cov = fully = 0
    for t in proj.targets:
        lines = result.files.get(t.source_rel)
        if not lines:
            continue
        mc = cov.synthesize(t.method, lines)
        if mc.executable_lines == 0:
            continue
        total_exec += mc.executable_lines
        total_cov += mc.covered_lines
        if mc.fully_covered:
            fully += 1
    pct = round(100 * total_cov / total_exec, 1) if total_exec else None
    return {"files_measured": len(result.files), "line_coverage_pct": pct,
            "methods_fully_covered": fully, "executable_lines": total_exec,
            "seconds": round(dt, 1)}


def diagnose(root: str) -> dict:
    root = os.path.abspath(root.rstrip(os.sep))
    name = os.path.basename(root)
    out: dict = {"name": name, "path": root}

    source_dir = _source_dir(root)
    if source_dir is None:
        out["error"] = "sem lib/ nem src/"
        return out
    out["source_dir"] = source_dir
    out["commit"] = _git(root, "rev-parse", "HEAD")[:12]
    out["commit_date"] = _git(root, "log", "-1", "--format=%cs")

    backend = detect_backend(os.path.join(root, source_dir))
    minitest = isinstance(backend, MinitestBackend)
    out["framework"] = "minitest" if minitest else "rspec"

    t0 = time.time()
    proj = RubyProject(root_dir=root, source_dir=source_dir, backend=backend).discover()
    out["discover_seconds"] = round(time.time() - t0, 1)

    parse_errors = 0
    for f in proj.files:
        try:
            parse_errors += len(backend.parse_file(f).errors)
        except RubyParseError:
            parse_errors += 1
    out.update({
        "files": len(proj.files),
        "loc": _loc(root, source_dir),
        "target_methods": len(proj.targets),
        "classes": len([c for c in proj.type_index.classes.values() if c.kind == "class"]),
        "call_graph_edges": len(proj.call_graph.edges) if proj.call_graph else 0,
        "targets_with_types": sum(1 for t in proj.targets if t.judge),
        "parse_errors": parse_errors,
    })
    out["human_suite"] = _human_suite_coverage(root, source_dir, proj, minitest)
    return out


def main(paths):
    rows = []
    for p in paths:
        print(f"→ {p} ...", flush=True)
        try:
            rows.append(diagnose(p))
        except Exception as e:  # diagnóstico nunca deve abortar o lote
            rows.append({"name": os.path.basename(p.rstrip("/")), "error": f"{type(e).__name__}: {e}"[:200]})

    os.makedirs("benchmark/results", exist_ok=True)
    with open("benchmark/results/diagnose.json", "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2)

    hdr = ("| gem | fw | ficheiros | LOC | métodos | classes | arestas | "
           "erros parse | cobertura-base | métodos 100% |")
    sep = "|" + "---|" * 10
    lines = [hdr, sep]
    for r in rows:
        if "error" in r and "files" not in r:
            lines.append(f"| {r['name']} | — | ERRO: {r['error'][:60]} ||||||||")
            continue
        hs = r.get("human_suite", {})
        covp = hs.get("line_coverage_pct")
        covs = f"{covp}%" if covp is not None else f"n/d ({hs.get('error','?')[:28]})"
        lines.append(
            f"| {r['name']} | {r['framework']} | {r['files']} | {r['loc']} | "
            f"{r['target_methods']} | {r['classes']} | {r['call_graph_edges']} | "
            f"{r['parse_errors']} | {covs} | {hs.get('methods_fully_covered','—')} |"
        )
    table = "\n".join(lines)
    with open("benchmark/results/diagnose.md", "w", encoding="utf-8") as f:
        f.write("# Diagnóstico de candidatas ao corpus\n\n" + table + "\n")
    print("\n" + table)


if __name__ == "__main__":
    main(sys.argv[1:])

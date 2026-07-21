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
from marta.ruby_backend.project import RubyProject
from marta.ruby_backend.ruby_ast import RubyParseError

SOURCE_CANDIDATES = ("lib", "src")


def _human_suite_framework(root: str) -> str:
    """Framework da SUITE HUMANA do projeto — só para a medir (a MARTA gera
    sempre RSpec, independentemente disto). spec/ => rspec, test/ => minitest."""
    if os.path.isdir(os.path.join(root, "spec")):
        return "rspec"
    if os.path.isdir(os.path.join(root, "test")):
        return "minitest"
    return "rspec"


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


# Chamadas que denunciam metaprogramação — o que torna um projeto "difícil" e
# distinto (stress no parser/grafo/inferência estática). Contá-las caracteriza
# a especificidade do CÓDIGO (o que nos interessa), não a suite de testes.
METAPROG_CALLS = {
    "define_method", "define_singleton_method", "method_missing", "respond_to_missing?",
    "send", "__send__", "public_send", "instance_eval", "class_eval", "module_eval",
    "instance_exec", "const_get", "const_set", "instance_variable_get",
    "instance_variable_set", "define_delegator", "def_delegator", "delegate",
    "method_added", "included", "extended", "inherited",
}


def _code_metrics(proj) -> dict:
    """Métricas que caracterizam a DIVERSIDADE do código (agnóstico a testes).

    Cada uma mapeia para uma parte da MARTA que é exercida de forma diferente:
    tamanho de método (contexto do LLM), singletons/mixins/herança (inferência de
    tipos + grafo), metaprogramação (limite da análise estática), duck-typing
    (inferência de tipos por uso).
    """
    targets = proj.targets
    n = len(targets) or 1
    classes = [c for c in proj.type_index.classes.values()]
    real_classes = [c for c in classes if c.kind == "class"]
    modules = [c for c in classes if c.kind == "module"]

    method_locs = [t.method.end_line - t.method.start_line + 1 for t in targets]
    singletons = sum(1 for t in targets if t.method.singleton)
    duck = sum(1 for t in targets if any((t.method.param_members or {}).values()))
    mixins = sum(len(c.includes) + len(c.extends) + len(c.prepends) for c in classes)

    metaprog = 0
    for t in targets:
        for c in t.method.calls:
            if c["name"] in METAPROG_CALLS:
                metaprog += 1

    depths = []
    for c in real_classes:
        try:
            depths.append(len(proj.type_index.ancestors(c.qualified_name)))
        except Exception:
            pass

    return {
        "avg_method_loc": round(sum(method_locs) / n, 1),
        "max_method_loc": max(method_locs) if method_locs else 0,
        "pct_singleton": round(100 * singletons / n),
        "pct_duck_typed": round(100 * duck / n),
        "modules": len(modules),
        "mixins_per_class": round(mixins / (len(real_classes) or 1), 2),
        "max_ancestor_depth": max(depths) if depths else 0,
        "metaprog_calls": metaprog,
        "metaprog_per_100methods": round(100 * metaprog / n, 1),
    }


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


def diagnose(root: str, measure_coverage: bool = False) -> dict:
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
    out["human_framework"] = _human_suite_framework(root)

    t0 = time.time()
    proj = RubyProject(root_dir=root, source_dir=source_dir).discover()
    out["discover_seconds"] = round(time.time() - t0, 1)

    parse_errors = 0
    for f in proj.files:
        try:
            parse_errors += len(proj.backend.parse_file(f).errors)
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
    out["code"] = _code_metrics(proj)

    if measure_coverage:  # opcional (lento) — baseline de comparação, não seleção
        out["human_suite"] = _human_suite_coverage(
            root, source_dir, proj, out["human_framework"] == "minitest")
    return out


def main(paths, measure_coverage=False):
    rows = []
    for p in paths:
        print(f"→ {p} ...", flush=True)
        try:
            rows.append(diagnose(p, measure_coverage=measure_coverage))
        except Exception as e:  # diagnóstico nunca deve abortar o lote
            rows.append({"name": os.path.basename(p.rstrip("/")), "error": f"{type(e).__name__}: {e}"[:200]})

    os.makedirs("benchmark/results", exist_ok=True)
    with open("benchmark/results/diagnose.json", "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2)

    # Tabela focada na DIVERSIDADE do código (o critério de seleção).
    hdr = ("| gem | fw humana | métodos | classes | LOC | avg loc/mét | "
           "% singleton | % duck | mixins/cl | prof. herança | metaprog/100 | erros parse |")
    sep = "|" + "---|" * 12
    lines = [hdr, sep]
    for r in rows:
        if "files" not in r:
            lines.append(f"| {r['name']} | ERRO: {r.get('error','?')[:50]} |||||||||||")
            continue
        c = r["code"]
        lines.append(
            f"| {r['name']} | {r['human_framework']} | {r['target_methods']} | "
            f"{r['classes']} | {r['loc']} | {c['avg_method_loc']} | {c['pct_singleton']}% | "
            f"{c['pct_duck_typed']}% | {c['mixins_per_class']} | {c['max_ancestor_depth']} | "
            f"{c['metaprog_per_100methods']} | {r['parse_errors']} |"
        )
    table = "\n".join(lines)
    with open("benchmark/results/diagnose.md", "w", encoding="utf-8") as f:
        f.write("# Diagnóstico de candidatas — diversidade de código\n\n" + table + "\n")
    print("\n" + table)


if __name__ == "__main__":
    argv = [a for a in sys.argv[1:] if a != "--coverage"]
    main(argv, measure_coverage="--coverage" in sys.argv)
    main(sys.argv[1:])

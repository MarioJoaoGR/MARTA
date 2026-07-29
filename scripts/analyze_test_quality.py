#!/usr/bin/env python3
"""Qualidade dos ORÁCULOS das suites geradas — evidência para o paper.

A cobertura mede que linhas EXECUTAM; não mede se o teste VERIFICA alguma coisa.
Dois mecanismos conhecidos inflacionam a cobertura sem valor de deteção:

  • Test4Py (baseline): quando a reparação falha N vezes, aplica uma "heuristic
    reduction" que MINIMIZA o teste até passar (§3.4.2 do paper) — na prática
    trunca as assertions. O teste continua a executar código (conta para
    cobertura) mas deixa de verificar. → medimos aqui a % de testes SEM asserts.
  • Pynguin (SBST): gera assertions de REGRESSÃO (assert x == <valor observado>),
    que passam por construção e não codificam intenção. → medimos a % de asserts
    triviais (comparação com literal, isinstance, is not None, ...).

Métricas por (tool, projeto):
    n_tests            funções de teste (def test_*)
    asserts/test       média de assertions por teste
    %_zero_assert      testes SEM qualquer assertion  ← assert deletion
    %_trivial          assertions triviais / total     ← oráculos fracos
    %_mock             testes que usam mocks
    loc/test           linhas por teste (proxy de riqueza)

Uso:  python scripts/analyze_test_quality.py --results /data/results
"""
import argparse
import ast
import csv
import glob
import json
import os
import statistics as st
import collections

TOOL_DIRS = {
    "marta": "Results_MARTA",
    "test4py_baseline": "Results_Test4PyBaseline",
    "pynguin": "Results_Pynguin",
}
MOCK_NAMES = {"patch", "MagicMock", "Mock", "mocker", "monkeypatch", "AsyncMock"}


def _is_trivial(node):
    """Assertion ESTRUTURALMENTE fraca — não verifica comportamento do SUT.

    ⚠️ Critério deliberadamente CONSERVADOR. Comparar com um literal NÃO é
    trivial: `assert add(2,3) == 5` é precisamente um bom oráculo. Só contam
    como fracas as formas que não dizem nada sobre o que a função CALCULA:

      • assert True / assert 1                    (constante)
      • assert isinstance(x, T) / bool(x) / hasattr(...)   (estrutura, não valor)
      • assert type(x) == T  ou  f"{type(x).__module__}..." == "..."
            ← o padrão dominante do Pynguin
      • assert mock.called / m.call_count == N / m.assert_called_with(...)
            ← verifica o duplo de teste, não o código sob teste
    """
    t = node.test
    if isinstance(t, ast.Constant):
        return True
    if isinstance(t, ast.Call):
        name = getattr(t.func, "id", None) or getattr(t.func, "attr", None)
        if name in ("isinstance", "bool", "hasattr", "callable"):
            return True
        if name and name.startswith("assert_"):          # mock.assert_called_with
            return True
    if isinstance(t, ast.Attribute) and t.attr in ("called", "call_count"):
        return True
    if isinstance(t, ast.Compare):
        left = t.left
        # mock: x.call_count == N / x.called == True
        if isinstance(left, ast.Attribute) and left.attr in ("call_count", "called"):
            return True
        # type(x) == T  → verifica o tipo, não o valor
        if isinstance(left, ast.Call) and getattr(left.func, "id", None) == "type":
            return True
        # f-string sobre type(...) — a assinatura do Pynguin:
        #   assert f"{type(o).__module__}.{type(o).__qualname__}" == "pkg.Cls"
        if isinstance(left, ast.JoinedStr):
            for n in ast.walk(left):
                if isinstance(n, ast.Call) and getattr(n.func, "id", None) == "type":
                    return True
    return False


def analyze_file(path):
    try:
        tree = ast.parse(open(path, encoding="utf-8", errors="replace").read())
    except SyntaxError:
        return []
    uses_mock_module = any(
        (isinstance(n, ast.ImportFrom) and n.module and "mock" in n.module)
        or (isinstance(n, ast.Import) and any("mock" in a.name for a in n.names))
        for n in ast.walk(tree)
    )
    out = []
    for fn in ast.walk(tree):
        if not isinstance(fn, ast.FunctionDef) or not fn.name.startswith("test"):
            continue
        asserts = [n for n in ast.walk(fn) if isinstance(n, ast.Assert)]
        # pytest.raises / pytest.warns contam como oráculo (não-trivial)
        raises = sum(
            1 for n in ast.walk(fn)
            if isinstance(n, ast.withitem) or (
                isinstance(n, ast.Call) and getattr(n.func, "attr", "") in ("raises", "warns"))
        )
        mock_local = uses_mock_module or any(
            (getattr(n, "id", None) in MOCK_NAMES) or (getattr(n, "attr", None) in MOCK_NAMES)
            for n in ast.walk(fn)
        )
        loc = (fn.end_lineno or fn.lineno) - fn.lineno + 1
        out.append({
            "n_assert": len(asserts) + raises,
            "n_trivial": sum(1 for a in asserts if _is_trivial(a)),
            "zero": (len(asserts) + raises) == 0,
            "mock": bool(mock_local),
            "loc": loc,
        })
    return out


def find_tests(results, tool, proj):
    base = os.path.join(results, TOOL_DIRS[tool], proj)
    return sorted(f for f in glob.glob(os.path.join(base, "**", "test_*.py"), recursive=True)
                  if "OLD" not in f and "quarantine" not in f and "_cov_" not in f
                  and "_mut_tests" not in f)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", default="/data/results")
    ap.add_argument("--projects", default="/opt/marta/projects.json")
    args = ap.parse_args()
    targets = json.load(open(args.projects))

    rows = []
    for tool in TOOL_DIRS:
        for proj in sorted(targets):
            tests = []
            for f in find_tests(args.results, tool, proj):
                tests += analyze_file(f)
            if not tests:
                continue
            n = len(tests)
            rows.append({
                "tool": tool, "project": proj, "n_tests": n,
                "asserts_per_test": round(sum(t["n_assert"] for t in tests) / n, 2),
                "pct_zero_assert": round(100 * sum(t["zero"] for t in tests) / n, 1),
                "pct_trivial": round(
                    100 * sum(t["n_trivial"] for t in tests)
                    / max(1, sum(t["n_assert"] for t in tests)), 1),
                "pct_mock": round(100 * sum(t["mock"] for t in tests) / n, 1),
                "loc_per_test": round(sum(t["loc"] for t in tests) / n, 1),
            })

    hdr = f"{'tool':18} {'projeto':22} {'#tests':>7} {'asrt/t':>7} {'%0asrt':>7} {'%triv':>6} {'%mock':>6} {'loc/t':>6}"
    print(hdr); print("-" * len(hdr))
    for r in rows:
        print(f"{r['tool']:18} {r['project']:22} {r['n_tests']:>7} {r['asserts_per_test']:>7} "
              f"{r['pct_zero_assert']:>7} {r['pct_trivial']:>6} {r['pct_mock']:>6} {r['loc_per_test']:>6}")

    print("\n═══ AGREGADO POR TOOL (ponderado pelo nº de testes) ═══")
    agg = collections.defaultdict(lambda: collections.Counter())
    for r in rows:
        a = agg[r["tool"]]; n = r["n_tests"]
        a["n"] += n
        a["asr"] += r["asserts_per_test"] * n
        a["zero"] += r["pct_zero_assert"] * n
        a["triv"] += r["pct_trivial"] * n
        a["mock"] += r["pct_mock"] * n
        a["loc"] += r["loc_per_test"] * n
    for t, a in sorted(agg.items()):
        n = a["n"]
        print(f"  {t:18} {n:>6} testes | asserts/teste {a['asr']/n:4.2f} | "
              f"SEM assert {a['zero']/n:4.1f}% | triviais {a['triv']/n:4.1f}% | "
              f"mocks {a['mock']/n:4.1f}% | loc/teste {a['loc']/n:4.1f}")

    out = os.path.join(args.results, "test_quality.csv")
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    print(f"\nCSV: {out}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Extrai testes das 3 tools para a MESMA função — figura qualitativa do paper.

A MARTA e o Test4Py nomeiam os ficheiros por função (test_<mod>_<func>_<n>.py);
o Pynguin gera um ficheiro por MÓDULO (test_<mod>.py). Este script, dado um
projeto (e opcionalmente uma função), encontra funções cobertas pelas três e
imprime/escreve os testes lado a lado, prontos para a figura.

O CoverUp não entra: não foi possível executar a ferramenta, comparamos apenas
com os números publicados (ver threats to validity).

Uso:
  python scripts/compare_examples.py --results /data/results --project pyMonet
  python scripts/compare_examples.py --results /data/results --project pyMonet \
      --func maybe_Maybe_map --out /data/results/exemplo.md
"""
import argparse
import glob
import os
import re

TOOL_DIRS = {
    "MARTA": "Results_MARTA",
    "Test4Py (baseline)": "Results_Test4PyBaseline",
    "Pynguin": "Results_Pynguin",
}


def tests_of(results, dirname, proj):
    base = os.path.join(results, dirname, proj)
    return sorted(f for f in glob.glob(os.path.join(base, "**", "test_*.py"), recursive=True)
                  if "OLD" not in f and "quarantine" not in f and "_cov_" not in f
                  and "_mut_tests" not in f)


def stem_key(path):
    """'test_pymonet_maybe_Maybe_map_0.py' → 'pymonet_maybe_maybe_map' (sem ronda)."""
    b = os.path.basename(path)[len("test_"):-len(".py")]
    b = re.sub(r"_\d+$", "", b)          # sufixo de ronda/índice
    return b.lower()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", default="/data/results")
    ap.add_argument("--project", required=True)
    ap.add_argument("--func", help="filtro (substring do nome do ficheiro)")
    ap.add_argument("--max-lines", type=int, default=60)
    ap.add_argument("--out", help="escrever markdown para ficheiro")
    args = ap.parse_args()

    marta = {stem_key(p): p for p in tests_of(args.results, TOOL_DIRS["MARTA"], args.project)}
    base = {stem_key(p): p for p in tests_of(args.results, TOOL_DIRS["Test4Py (baseline)"], args.project)}
    pyn = tests_of(args.results, TOOL_DIRS["Pynguin"], args.project)

    common = sorted(set(marta) & set(base))
    if args.func:
        common = [k for k in common if args.func.lower() in k]
    if not common:
        print(f"sem funções em comum entre MARTA e baseline em {args.project}")
        print(f"  marta: {len(marta)} ficheiros | baseline: {len(base)} | pynguin: {len(pyn)}")
        if marta:
            print("  exemplos marta:", list(marta)[:5])
        return

    key = common[0]
    # ficheiro do pynguin do MESMO módulo (o nome do módulo é o prefixo da chave)
    pyn_match = next((p for p in pyn if os.path.basename(p)[5:-3].lower() in key),
                     pyn[0] if pyn else None)

    def block(title, path):
        if not path or not os.path.exists(path):
            return f"### {title}\n\n_(sem teste correspondente)_\n"
        code = open(path, encoding="utf-8", errors="replace").read().splitlines()
        trimmed = "\n".join(code[:args.max_lines])
        more = "" if len(code) <= args.max_lines else f"\n… (+{len(code)-args.max_lines} linhas)"
        return (f"### {title}\n`{os.path.basename(path)}`\n\n"
                f"```python\n{trimmed}{more}\n```\n")

    md = [f"# Testes gerados para `{key}` — projeto `{args.project}`\n",
          f"_Funções com teste nas 3 ferramentas: {len(common)}_\n",
          block("MARTA", marta[key]),
          block("Test4Py (baseline)", base[key]),
          block("Pynguin", pyn_match)]
    text = "\n".join(md)
    if args.out:
        open(args.out, "w", encoding="utf-8").write(text)
        print("escrito:", args.out)
    else:
        print(text)
    if len(common) > 1:
        print(f"\n(outras funções disponíveis: {', '.join(common[1:8])}…)")


if __name__ == "__main__":
    main()

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
import json
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


def stem_key(path, modules):
    """Nome canónico da FUNÇÃO testada, comparável entre as 3 ferramentas.

    Os formatos divergem:
      MARTA     test_<mod_path>_<Func>_<ronda>.py   → 'pymonet_box_Box___eq___0'
      Test4Py   test_<mod_path>_t<Func><n>.py       → 'pymonet_box_tBox___eq__0'
                (o dir do baseline é <ficheiro>_t, daí o 't' colado)
    Estratégia: retirar o prefixo do módulo (de projects.json, com '.'→'_'),
    tolerando o 't' extra do baseline, e limpar os índices finais.
    """
    b = os.path.basename(path)[len("test_"):-len(".py")]
    best, best_mod = "", ""
    for m in modules:                     # prefixo mais longo que casar
        p = m.replace(".", "_")
        for cand in (p + "_t", p + "_", p):
            if b.lower().startswith(cand.lower()) and len(cand) > len(best):
                best, best_mod = cand, m
    if best:
        b = b[len(best):]
    b = re.sub(r"[_\d]+$", "", b)          # índices de ronda / contador
    return best_mod, re.sub(r"[^a-z0-9]", "", b.lower())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", default="/data/results")
    ap.add_argument("--project", required=True)
    ap.add_argument("--func", help="filtro (substring do nome do ficheiro)")
    ap.add_argument("--max-lines", type=int, default=60)
    ap.add_argument("--out", help="escrever markdown para ficheiro")
    ap.add_argument("--projects", default="/opt/marta/projects.json")
    ap.add_argument("--rank", type=int, metavar="N",
                    help="lista as N funções onde a MARTA mais supera o baseline "
                         "em assertions não-triviais (baseline com asserts reais)")
    args = ap.parse_args()

    mods = json.load(open(args.projects)).get(args.project, [])
    marta = {stem_key(p, mods): p for p in tests_of(args.results, TOOL_DIRS["MARTA"], args.project)}
    base = {stem_key(p, mods): p for p in tests_of(args.results, TOOL_DIRS["Test4Py (baseline)"], args.project)}
    pyn = tests_of(args.results, TOOL_DIRS["Pynguin"], args.project)

    common = sorted(set(marta) & set(base))
    if args.func:
        common = [k for k in common if args.func.lower() in k[1]]
    if not common:
        print(f"sem funções em comum entre MARTA e baseline em {args.project}")
        print(f"  marta: {len(marta)} ficheiros | baseline: {len(base)} | pynguin: {len(pyn)}")
        if marta:
            print("  exemplos marta:", list(marta)[:5])
        return

    # ── MODO RANKING: encontrar o melhor exemplo com base nos DADOS ──────────
    # Critério: a MARTA tem mais assertions COM SIGNIFICADO (não-triviais) que o
    # baseline, E o baseline tem assertions reais (b_nt>0, sem assert deletion)
    # → o contraste é de qualidade de conteúdo, não de o baseline ter batota.
    if args.rank:
        from analyze_test_quality import analyze_file
        cand = []
        for k in common:
            m, b = analyze_file(marta[k]), analyze_file(base[k])
            if not m or not b:
                continue
            m_nt = sum(t["n_assert"] - t["n_trivial"] for t in m)
            b_nt = sum(t["n_assert"] - t["n_trivial"] for t in b)
            if b_nt < 1 or any(t["zero"] for t in b):
                continue                      # baseline sem asserts → não serve
            cand.append((m_nt - b_nt, m_nt, b_nt, len(m), len(b), k))
        cand.sort(reverse=True)
        print(f"{'Δnão-triv':>9} {'marta':>12} {'baseline':>12}  função")
        print(f"{'':>9} {'nt/tests':>12} {'nt/tests':>12}")
        print("-" * 62)
        for d, mnt, bnt, mt, bt, k in cand[:args.rank]:
            print(f"{d:>+9} {f'{mnt}/{mt}':>12} {f'{bnt}/{bt}':>12}  {k[0]}.{k[1]}")
        if cand:
            print(f"\nmelhor candidato:  --func {cand[0][5][1]}")
        else:
            print("nenhum candidato (baseline sem assertions em todas as funções comuns)")
        return

    key = common[0]
    mod, func = key
    # ficheiro do PYNGUIN do MESMO módulo (ele gera 1 ficheiro por módulo):
    # test_<modulo_com_underscores>.py — antes caía no primeiro ficheiro do
    # projeto e a figura mostrava um módulo diferente do das outras duas tools.
    want = "test_" + mod.replace(".", "_") + ".py"
    pyn_match = next((p for p in pyn if os.path.basename(p) == want), None)

    def block(title, path):
        if not path or not os.path.exists(path):
            return f"### {title}\n\n_(sem teste correspondente)_\n"
        code = open(path, encoding="utf-8", errors="replace").read().splitlines()
        trimmed = "\n".join(code[:args.max_lines])
        more = "" if len(code) <= args.max_lines else f"\n… (+{len(code)-args.max_lines} linhas)"
        return (f"### {title}\n`{os.path.basename(path)}`\n\n"
                f"```python\n{trimmed}{more}\n```\n")

    md = [f"# Testes gerados para `{mod}.{func}` — projeto `{args.project}`\n",
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
        print('\n(outras funções disponíveis: ' + ', '.join(f'{m}.{f}' for m, f in common[1:8]) + '…)')


if __name__ == "__main__":
    main()

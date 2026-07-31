#!/usr/bin/env python3
"""Eficiência de geração — a métrica que ISOLA a arquitetura de prompts.

Motivação (crítica externa): as duas manchetes do paper têm causas que NÃO são
o desacoplamento Planner/Assertion. O gap dos oráculos vem da política de
recuperação (salvage vs heuristic reduction) e o gap de custo vem do batching
ao ficheiro. Falta uma métrica a jusante que meça a QUALIDADE DO PROMPT e que
seja imune às duas: é isso que este script calcula.

Fonte: run_results/<projeto>.json de cada ferramenta. Os contadores são
incrementados DENTRO do ciclo de reparação (marta/testcase_react.py:92-115 é
chamado por message_react.py:1180, dentro de `for attempt in range(3)`), pelo
que são POR GERAÇÃO DO LLM, não por ficheiro.

  gerações       = syntax_pass + syntax_error
  validade sint. = syntax_pass / gerações        <- imune a salvage e a batching
  verde-à-1ª     = assertion_pass / gerações     <- ver AVISO DE UNIDADE
  resgatados     = assertion_fix_success         <- dependência do rescue
  retidos        = assertion_pass + assertion_fix_success

AVISO DE UNIDADE (tem de constar do paper): uma geração da MARTA produz UM
ficheiro com N testes (uma função); uma geração do baseline produz UM ficheiro
com UM teste (um cenário). A validade sintática é comparável (uma chamada ->
um ficheiro) e é, se alguma coisa, MAIS exigente para a MARTA. A taxa de verde
NÃO é comparável de forma limpa, porque a MARTA exige que os N testes passem
todos. Reportar ambas, com a ressalva.

Os campos `first_*` são os mesmos contadores restritos à PRIMEIRA RONDA
(first_run=False no fim da ronda 0: marta/start_react.py:68 e
test4dt/start.py:49), com semântica idêntica nas duas ferramentas.

Uso:  python scripts/generation_efficiency.py --results <dir>
"""
import argparse
import glob
import json
import os

TOOLS = ["marta", "test4py_baseline"]
LABEL = {"marta": "MARTA", "test4py_baseline": "Test4Py"}
DIRS = {"marta": "Results_MARTA", "test4py_baseline": "Results_Test4PyBaseline"}
KEYS = ["syntax_pass", "syntax_error", "assertion_pass", "assertion_error",
        "assertion_fix_success", "llm_calls", "prompt_tokens", "completion_tokens"]


def load(results, tool):
    """Soma os contadores de todos os projetos; devolve (total, ronda1, por-projeto)."""
    tot = {k: 0 for k in KEYS}
    r1 = {k: 0 for k in KEYS}
    per = {}
    for f in sorted(glob.glob(os.path.join(results, DIRS[tool], "**", "run_results", "*.json"),
                            recursive=True)):
        try:
            d = json.load(open(f))
        except Exception:
            continue
        proj = os.path.basename(f)[:-5]
        per[proj] = d
        for k in KEYS:
            tot[k] += d.get(k) or 0
            r1[k] += d.get("first_" + k, d.get(k) if k not in (
                "llm_calls", "prompt_tokens", "completion_tokens") else 0) or 0
    return tot, r1, per


def discards(results, tool):
    """Ficheiros retidos vs postos em quarentena (só a MARTA tem quarentena)."""
    base = os.path.join(results, DIRS[tool])
    kept = len([f for f in glob.glob(os.path.join(base, "**", "test_*.py"), recursive=True)
                if "OLD" not in f and "quarantine" not in f and "_cov_" not in f])
    quar = len(glob.glob(os.path.join(base, "**", "*quarantine*", "*.py"), recursive=True))
    return kept, quar


def row(name, c):
    gen = c["syntax_pass"] + c["syntax_error"]
    if not gen:
        return f"{name:24} {'— sem dados':>12}"
    keep = c["assertion_pass"] + c["assertion_fix_success"]
    return (f"{name:24} {gen:>10,} {100*c['syntax_pass']/gen:>9.1f}% "
            f"{100*c['assertion_pass']/gen:>9.1f}% "
            f"{c['assertion_fix_success']:>9,} "
            f"{(gen/keep if keep else float('nan')):>9.2f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", required=True)
    ap.add_argument("--csv")
    a = ap.parse_args()

    print("═══ EFICIÊNCIA DE GERAÇÃO (por chamada ao LLM) ═══\n")
    print(f"{'':24} {'gerações':>10} {'sintaxe ok':>10} {'verde':>10} "
          f"{'resgatados':>10} {'ger./retido':>10}")
    print("─" * 78)
    store = {}
    for t in TOOLS:
        tot, r1, per = load(a.results, t)
        store[t] = (tot, r1, per)
        print(row(LABEL[t] + " (todas as rondas)", tot))
        print(row(LABEL[t] + "   └ só ronda 1", r1))
    print("\nAVISO DE UNIDADE: 1 geração da MARTA = 1 ficheiro com N testes; "
          "1 geração do\nbaseline = 1 ficheiro com 1 teste. 'sintaxe ok' é "
          "comparável (e mais exigente\npara a MARTA); 'verde' não é, porque a "
          "MARTA exige que os N testes passem todos.")

    print("\n\n═══ DESCARTE ═══\n")
    print(f"{'':24} {'retidos':>10} {'quarentena':>12} {'taxa descarte':>14}")
    print("─" * 62)
    for t in TOOLS:
        kept, quar = discards(a.results, t)
        tx = f"{100*quar/(kept+quar):.1f}%" if (kept + quar) else "—"
        print(f"{LABEL[t]:24} {kept:>10,} {quar:>12,} {tx:>14}")
    print("\nNOTA: só a MARTA arquiva o que descarta (testcase_react.py:415); o "
          "baseline\napaga. Para o baseline a grandeza equivalente sai dos "
          "contadores acima\n(assertion_error vs assertion_pass+fix_success) e "
          "é por TESTE, não por ficheiro.")

    print("\n\n═══ DEPENDÊNCIA DO MECANISMO DE RECUPERAÇÃO ═══\n")
    for t in TOOLS:
        tot = store[t][0]
        keep = tot["assertion_pass"] + tot["assertion_fix_success"]
        if keep:
            print(f"{LABEL[t]:24} {100*tot['assertion_fix_success']/keep:>6.1f}% "
                  f"dos ficheiros retidos só sobreviveram por recuperação")
    print("\nSão mecanismos QUALITATIVAMENTE distintos, não graus do mesmo: o "
          "salvage da\nMARTA remove TESTES inteiros e nunca transforma um teste "
          "com assertion num\nsem assertion; a heuristic reduction do Test4Py "
          "(§3.4.2) remove ASSERTIONS\naté o teste passar. É esta diferença de "
          "tipo — e não o volume de recuperação —\nque explica o gap dos oráculos.")

    if a.csv:
        import csv as _csv
        with open(a.csv, "w", newline="") as fh:
            w = _csv.writer(fh)
            w.writerow(["tool", "project", "scope"] + KEYS)
            for t in TOOLS:
                for proj, d in sorted(store[t][2].items()):
                    w.writerow([t, proj, "all"] + [d.get(k) or 0 for k in KEYS])
                    w.writerow([t, proj, "round1"] +
                               [d.get("first_" + k, d.get(k) or 0) or 0 for k in KEYS])
        print(f"\n>>> escrito: {a.csv}")


if __name__ == "__main__":
    main()

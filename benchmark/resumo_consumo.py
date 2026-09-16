"""Consumo medido de uma execução, e a extrapolação para o corpus inteiro.

Lê os ``run_results/<gem>.json`` que a ferramenta escreve (a telemetria por fase)
e responde às perguntas que decidem o orçamento:

  - quanto custou cada fase, em chamadas, tokens e horas;
  - quanto custa um método, em média, na Fase 1 e na geração;
  - quantas respostas vieram cortadas pelo limite ou falharam;
  - quanto custaria o corpus inteiro, e o braço da ablação, a este ritmo.

A extrapolação usa o número de métodos do corpus (``ablacao.json``: alvos e
afetados). Custo por método × métodos. É uma estimativa, e diz isso: um piloto
de poucas gems não representa todas as gems, por isso também se mostra a
dispersão entre gems.

Horas de parede são horas de GPU: o job tem 1 GPU reservada o tempo todo,
esteja o modelo a trabalhar ou o RSpec a correr.

    python -m benchmark.resumo_consumo --results /projects/.../results_ruby/deepseek-coder-v2_16b
"""
from __future__ import annotations

import argparse
import json
import pathlib
import statistics
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
ABLACAO = REPO / "apresentacao" / "demo_dataset" / "7_selecao" / "ablacao.json"

FASE1 = ("sumarios_passagem1", "sumarios_passagem2", "what_todo_raiz",
         "what_todo_propagado", "what_todo_fallback", "sumario_final",
         "sumarios_de_classe", "rag")
GERACAO = ("plano", "dev_primeira", "dev_reparacao")


def _metodos_gerados(dados: dict) -> int:
    """Métodos distintos com geração nesta execução: a 1ª ronda tem um plano por
    método, por isso as chamadas do plano na ronda 0 contam métodos. Sem isso,
    usa-se o total de planos a dividir pelas rondas."""
    cob = dados.get("coverage") or []
    if cob and isinstance(cob[0], dict):
        return len(cob[0])
    return dados.get("por_fase", {}).get("plano", {}).get("chamadas", 0)


def le_execucoes(pasta: pathlib.Path) -> dict:
    """gem (com sufixo _sem_grafo no braço da ablação) -> run_results."""
    fora = {}
    for f in sorted(pasta.glob("*/run_results/*.json")):
        if f.name.endswith(".eventos.jsonl"):
            continue
        try:
            dados = json.loads(f.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        if "por_fase" in dados:
            fora[f.parent.parent.name] = dados
    return fora


def resume(execucoes: dict) -> dict:
    tot = {"horas": 0.0, "metodos": 0, "chamadas": 0, "tokens_in": 0, "tokens_out": 0,
           "cortadas": 0, "erros": 0, "fase1_h": 0.0, "geracao_h": 0.0,
           "subprocessos_h": 0.0}
    por_fase, por_gem = {}, {}
    for gem, d in execucoes.items():
        n = _metodos_gerados(d)
        h = d.get("time", 0) / 3600
        tot["horas"] += h
        tot["metodos"] += n
        tot["chamadas"] += d.get("llm_calls", 0)
        tot["tokens_in"] += d.get("prompt_tokens", 0)
        tot["tokens_out"] += d.get("completion_tokens", 0)
        tot["cortadas"] += d.get("llm_cortadas", 0)
        tot["erros"] += d.get("llm_erros", 0)
        for nome, f in d.get("por_fase", {}).items():
            a = por_fase.setdefault(nome, {"chamadas": 0, "tokens_in": 0, "tokens_out": 0,
                                           "horas": 0.0})
            a["chamadas"] += f.get("chamadas", 0)
            a["tokens_in"] += f.get("prompt_tokens", 0)
            a["tokens_out"] += f.get("completion_tokens", 0)
            a["horas"] += f.get("segundos_total", 0) / 3600
            if nome in FASE1:
                tot["fase1_h"] += f.get("segundos_total", 0) / 3600
            elif nome in GERACAO:
                tot["geracao_h"] += f.get("segundos_total", 0) / 3600
        for s in d.get("subprocessos", {}).values():
            tot["subprocessos_h"] += s.get("segundos", 0) / 3600
        if n:
            por_gem[gem] = {"metodos": n, "horas": h, "s_por_metodo": 3600 * h / n}
    return {"total": tot, "por_fase": por_fase, "por_gem": por_gem}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--results", required=True, help="pasta de resultados de um modelo")
    ap.add_argument("--ablacao", default=str(ABLACAO))
    args = ap.parse_args()

    execucoes = le_execucoes(pathlib.Path(args.results))
    if not execucoes:
        sys.exit("nenhum run_results com telemetria por fase nesta pasta")
    normal = {g: d for g, d in execucoes.items() if not g.endswith("_sem_grafo")}
    sem_grafo = {g: d for g, d in execucoes.items() if g.endswith("_sem_grafo")}

    corpus = json.loads(pathlib.Path(args.ablacao).read_text())
    alvos, afetados = corpus["total_alvos"], corpus["total_afetados"]

    for nome, grupo, universo in (("EXECUÇÃO NORMAL", normal, alvos),
                                  ("BRAÇO SEM GRAFO", sem_grafo, afetados)):
        if not grupo:
            continue
        r = resume(grupo)
        t = r["total"]
        print(f"\n=== {nome}: {len(grupo)} gems, {t['metodos']} métodos ===")
        print(f"  tempo           {t['horas']:.2f} h   "
              f"(Fase 1 {t['fase1_h']:.2f} h, geração {t['geracao_h']:.2f} h, "
              f"subprocessos Ruby {t['subprocessos_h']:.2f} h)")
        print(f"  chamadas        {t['chamadas']}   tokens {t['tokens_in']} in / "
              f"{t['tokens_out']} out")
        print(f"  cortadas        {t['cortadas']}   erros {t['erros']}")
        print("  por fase:")
        for fase, f in sorted(r["por_fase"].items(), key=lambda kv: -kv[1]["horas"]):
            print(f"    {fase:22s} {f['horas']:6.2f} h  {f['chamadas']:6d} chamadas  "
                  f"{f['tokens_in']:>9d} in {f['tokens_out']:>8d} out")
        if t["metodos"]:
            s_metodo = 3600 * t["horas"] / t["metodos"]
            dispersao = [v["s_por_metodo"] for v in r["por_gem"].values()]
            print(f"  por método      {s_metodo:.1f} s "
                  f"(entre gems: {min(dispersao):.1f} a {max(dispersao):.1f} s"
                  + (f", desvio {statistics.pstdev(dispersao):.1f}" if len(dispersao) > 1 else "")
                  + ")")
            print(f"  EXTRAPOLAÇÃO    {universo} métodos × {s_metodo:.1f} s = "
                  f"{universo * s_metodo / 3600:.0f} GPU-h")


if __name__ == "__main__":
    main()

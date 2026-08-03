#!/usr/bin/env python3
"""Prepara as suites publicadas do CoverUp para medição com o NOSSO pipeline.

PORQUÊ: a §5.5 compara-nos com os números publicados do CoverUp, o que é uma
comparação não controlada em três eixos ao mesmo tempo — modelo (GPT-4o vs
open-weights local), granularidade (eles reportam por FUNÇÃO, nós por MÓDULO) e
pipeline de medição. O repositório de replicação deles (plasma-umass/coverup-eval)
publica os ficheiros de teste que geraram. Medindo ESSES ficheiros com o nosso
`measure_coverage.py`, sobre os nossos módulos-alvo, dois dos três eixos
desaparecem e sobra o modelo — que é declarável.

NÃO é re-execução do CoverUp. É medição do artefacto publicado.

Cobertura do corpus: eles publicam 24 projetos, nós temos 27. Ficam de fora
mimesis, sanic e thefuck.

Uso (no nó de login do Deucalion, que tem rede):
  git clone --depth 1 https://github.com/plasma-umass/coverup-eval /tmp/coverup-eval
  python scripts/stage_coverup.py --src /tmp/coverup-eval --results <RES>
"""
import argparse
import json
import os
import shutil
import sys

# Os nomes deles usam underscores e minúsculas; os nossos vêm do projects.json.
# blib2to3 é o pacote-alvo do black — o diretório deles tem o nome do pacote,
# não o do projeto. Os outros dois perdem o prefixo `python-`.
EXPLICIT = {
    "blib2to3": "black",
    "semantic_release": "python-semantic-release",
    "string_utils": "python-string-utils",
}


def norm(n):
    return n.lower().replace("-", "").replace("_", "")


def resolve(theirs, ours):
    """EXPLICIT, depois igualdade normalizada, depois sufixo (`python-` e afins)."""
    if theirs in EXPLICIT:
        return EXPLICIT[theirs]
    t = norm(theirs)
    if t in ours:
        return ours[t]
    cands = [v for k, v in ours.items() if k.endswith(t) or t.endswith(k)]
    return cands[0] if len(cands) == 1 else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True, help="clone de plasma-umass/coverup-eval")
    ap.add_argument("--results", required=True, help="raiz dos resultados (RES)")
    ap.add_argument("--config", default="output/cm.gpt4o-v2",
                    help="configuração a usar (default: a principal do paper FSE'25)")
    ap.add_argument("--projects", default="/opt/marta/projects.json")
    a = ap.parse_args()

    targets = json.load(open(a.projects))
    ours = {norm(p): p for p in targets}
    src_root = os.path.join(a.src, a.config)
    if not os.path.isdir(src_root):
        sys.exit(f"não existe: {src_root}")

    dst_root = os.path.join(a.results, "Results_CoverUp")
    matched, missing, unmatched = [], [], []

    for theirs in sorted(os.listdir(src_root)):
        tests_dir = os.path.join(src_root, theirs, "coverup-tests")
        if not os.path.isdir(tests_dir):
            continue
        ourname = resolve(theirs, ours)
        if not ourname:
            unmatched.append(theirs)
            continue
        files = [f for f in os.listdir(tests_dir) if f.startswith("test_") and f.endswith(".py")]
        if not files:
            continue
        dst = os.path.join(dst_root, ourname, "coverup_tests")
        os.makedirs(dst, exist_ok=True)
        for f in files:
            shutil.copy2(os.path.join(tests_dir, f), os.path.join(dst, f))
        matched.append((theirs, ourname, len(files)))

    have = {m[1] for m in matched}
    missing = sorted(p for p in targets if p not in have)

    print(f"{'deles':22} -> {'nosso':26} {'#testes':>8}")
    print("-" * 60)
    for t, o, n in matched:
        print(f"{t:22} -> {o:26} {n:>8}")
    print("-" * 60)
    print(f"{len(matched)} projetos preparados em {dst_root}")
    if unmatched:
        print(f"\nSEM correspondência no nosso projects.json: {', '.join(unmatched)}")
    if missing:
        print(f"\nNOSSOS projetos sem suite do CoverUp ({len(missing)}): {', '.join(missing)}")
        print("  -> a comparação tem de ser feita SÓ nos projetos em comum,")
        print("     senão estes contariam 0% e enviesavam contra o CoverUp.")


if __name__ == "__main__":
    main()

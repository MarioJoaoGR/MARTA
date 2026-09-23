#!/bin/bash
# Prepara e VERIFICA os projetos Ruby no Deucalion. Correr no nó de LOGIN (tem
# rede), depois do setup_ruby.sh:
#
#     PROJECTS=aasm,commander bash deucalion/prepara_corpus.sh   # só essas gems
#     bash deucalion/prepara_corpus.sh                           # o corpus inteiro
#
# Corre dentro do container e com as MESMAS montagens dos jobs (/opt/marta,
# /opt/ruby, /data/pydeps, /data/ruby_projects). Assim as gems com extensões em C
# compilam contra a glibc do container, e os caminhos que o bundler e o
# RubyGems gravam são os que o job vai ver. Verificar noutro sítio não provava
# nada sobre o job.
#
# Três passos, e pára no primeiro que falhe:
#   1. os pydeps têm as versões do requirements.txt
#   2. prepare: clona cada gem na etiqueta e instala pelo degrau da camada 6
#   3. verificador: cada módulo carrega pela ferramenta e aparece na cobertura
set -euo pipefail

BASE=/projects/F202407648IACDCF2/mario
SIF="$BASE/containers/marta_benchmark.sif"
MARTA_ROOT="$BASE/MARTA"
RUBY_ROOT="${RUBY_ROOT:-$BASE/ruby-3.4.10}"
RUBY_PROJECTS="$BASE/ruby_projects"
PROJECTS="${PROJECTS:-}"

[ -x "$RUBY_ROOT/bin/ruby" ] || { echo "❌ falta o Ruby em $RUBY_ROOT: correr deucalion/setup_ruby.sh"; exit 2; }
mkdir -p "$RUBY_PROJECTS"

singularity exec \
    --bind "$MARTA_ROOT:/opt/marta" \
    --bind "$BASE/pydeps:/data/pydeps" \
    --bind "$RUBY_PROJECTS:/data/ruby_projects" \
    --bind "$RUBY_ROOT:/opt/ruby" \
    --bind "/usr/share/zoneinfo:/usr/share/zoneinfo:ro" \
    --env "PROJECTS=$PROJECTS" \
    "$SIF" bash -c '
        set -euo pipefail
        cd /opt/marta
        unset GEM_HOME GEM_PATH RUBYOPT BUNDLE_GEMFILE
        export LANG=C.UTF-8 LC_ALL=C.UTF-8   # o container não tem locale UTF-8 por omissão
        export HOME=/data/ruby_projects/.home XDG_CACHE_HOME=/data/ruby_projects/.home/.cache   # o $HOME da conta está cheio
        mkdir -p "$HOME"
        export PATH="/opt/ruby/bin:$PATH"
        export MARTA_RUBY_BIN=/opt/ruby/bin/ruby MARTA_RSPEC_BIN=/opt/ruby/bin/rspec
        export PYTHONPATH="/data/pydeps/marta:/opt/marta" PYTHONUNBUFFERED=1
        PY=/opt/conda/envs/test4py_env/bin/python
        SUB=""
        [ -n "$PROJECTS" ] && SUB="--projects $PROJECTS"

        echo "=== 1. pydeps"
        $PY deucalion/verifica_pydeps.py requirements.txt

        echo "=== 2. prepare"
        $PY -m benchmark.prepare_ruby_projects --out /data/ruby_projects --continuar $SUB

        echo "=== 3. verificador"
        $PY -m benchmark.verifica_ambiente --projects-dir /data/ruby_projects $SUB
    '

#!/bin/bash
# Instala o Ruby da MARTA-Ruby no Deucalion. Correr UMA vez, no nó de LOGIN (tem
# rede):
#
#     bash deucalion/setup_ruby.sh
#
# Porque é assim:
#  - A mesma versão que certificou o dataset (3.4.10) e o mesmo RSpec (3.13.x),
#    com as versões exatas, para o ambiente do cluster ser o que foi verificado.
#  - Compila-se DENTRO do container, com o prefixo /opt/ruby, que é onde os jobs
#    o montam. Assim as bibliotecas e as gems com extensões em C ficam ligadas à
#    glibc do container, e os caminhos dentro do Ruby são os que os jobs veem.
#  - O container não tem os cabeçalhos do libyaml (o `gem` e o `bundler` precisam
#    do psych) nem do libffi. Não se instala nada no sistema: vêm do conda-forge,
#    com o conda do próprio container, para dentro da pasta do Ruby (deps/).
#  - Tudo fica em $RUBY_ROOT, em /projects. Apagar a pasta desfaz tudo.
set -euo pipefail

BASE=/projects/F202407648IACDCF2/mario
SIF="$BASE/containers/marta_benchmark.sif"
RUBY_ROOT="${RUBY_ROOT:-$BASE/ruby-3.4.10}"
BUILD="$BASE/ruby-build"

mkdir -p "$RUBY_ROOT" "$BUILD"
singularity exec \
    --bind "$RUBY_ROOT:/opt/ruby" \
    --bind "$BUILD:/data/build" \
    --bind "$(cd "$(dirname "$0")" && pwd):/data/deucalion" \
    "$SIF" bash /data/deucalion/instala_ruby_no_container.sh

rm -rf "$BUILD"
echo "Ruby pronto em $RUBY_ROOT (montado como /opt/ruby nos jobs)."

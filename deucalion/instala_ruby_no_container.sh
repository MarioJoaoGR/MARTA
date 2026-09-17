#!/bin/bash
# Corre DENTRO do container (chamado pelo setup_ruby.sh). Espera /opt/ruby e
# /data/build graváveis, e rede.
set -euo pipefail

VERSAO=3.4.10
SHA256=ecee2d072a14f2d14347dd56dfd8fe5c3130abf5117bfaacbda0f4ef9cc429ec
DEPS=/opt/ruby/deps
unset GEM_HOME GEM_PATH RUBYOPT BUNDLE_GEMFILE
# O container não tem locale UTF-8 por omissão; sem isto o Ruby lê texto como ASCII.
export LANG=C.UTF-8 LC_ALL=C.UTF-8

# 1. libyaml (no conda-forge chama-se "yaml") e libffi, para dentro da pasta do Ruby
if [ ! -f "$DEPS/include/yaml.h" ] || [ ! -f "$DEPS/include/ffi.h" ]; then
    echo "→ libyaml e libffi (conda-forge) em $DEPS"
    CONDA_PKGS_DIRS=/data/build/conda_pkgs /opt/conda/bin/conda create -y -q \
        -p "$DEPS" --override-channels -c conda-forge yaml libffi
fi

# 2. o código do Ruby, confirmado pelo checksum publicado
cd /data/build
if [ ! -x /opt/ruby/bin/ruby ]; then
    echo "→ Ruby $VERSAO: descarregar e confirmar"
    curl -fsSL -o ruby.tar.gz "https://cache.ruby-lang.org/pub/ruby/3.4/ruby-$VERSAO.tar.gz"
    echo "$SHA256  ruby.tar.gz" | sha256sum -c -
    tar xzf ruby.tar.gz
    cd "ruby-$VERSAO"
    echo "→ configurar e compilar (demora uns minutos)"
    ./configure --prefix=/opt/ruby --disable-install-doc \
        --with-opt-dir="$DEPS" \
        LDFLAGS="-L$DEPS/lib -Wl,-rpath,$DEPS/lib" > /data/build/configure.log 2>&1 \
        || { tail -30 /data/build/configure.log; exit 1; }
    make -j4 > /data/build/make.log 2>&1 || { tail -40 /data/build/make.log; exit 1; }
    make install > /data/build/install.log 2>&1 || { tail -30 /data/build/install.log; exit 1; }
fi

export PATH="/opt/ruby/bin:$PATH"

# 3. o RSpec, nas versões que certificaram o dataset (ver o setup_ruby_env.sh)
echo "→ RSpec nas versões do dataset"
for g in diff-lcs:1.6.2 rspec-support:3.13.7 rspec-core:3.13.6 \
         rspec-expectations:3.13.5 rspec-mocks:3.13.8; do
    gem install --no-document "$g"
done
gem install --no-document --conservative rspec:3.13.2

# 4. confirmar
echo "→ verificação"
ruby -v
ruby -e '
  %w[prism psych openssl zlib json coverage].each do |b|
    begin; require b; puts "  ok  #{b}"; rescue LoadError => e; puts "  FALTA #{b}: #{e.message}"; exit 1; end
  end
  begin; require "fiddle"; puts "  ok  fiddle"; rescue LoadError; puts "  (sem fiddle: a ferramenta nao o usa)"; end
  puts "  prism #{Prism::VERSION}"
'
rspec --version
esperadas="diff-lcs (1.6.2) rspec (3.13.2) rspec-core (3.13.6) rspec-expectations (3.13.5) rspec-mocks (3.13.8) rspec-support (3.13.7)"
for e in "diff-lcs (1.6.2)" "rspec (3.13.2)" "rspec-core (3.13.6)" "rspec-expectations (3.13.5)" \
         "rspec-mocks (3.13.8)" "rspec-support (3.13.7)"; do
    gem list --local | grep -qxF "$e" || { echo "  versão errada, esperava só: $e"; gem list --local | grep -E "^(rspec|diff-lcs)"; exit 1; }
done
echo "  versões do RSpec certas: $esperadas"
echo "  bundler $(bundle --version)"

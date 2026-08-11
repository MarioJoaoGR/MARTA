#!/bin/bash
# Cria o venv de Ruby da MARTA e instala lá dentro o que a ferramenta precisa.
# Não instala NADA no store global do rbenv (ver scripts/ruby_env.sh).
#
#   ./scripts/setup_ruby_env.sh
#
# Idempotente: correr outra vez não estraga nada. Para recomeçar do zero, apaga
# a pasta `.ruby_env/` — não há mais estado nenhum em lado nenhum.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUBY="${MARTA_RBENV_RUBY:-$HOME/.rbenv/versions/3.4.10/bin/ruby}"
GEM="$(dirname "$RUBY")/gem"
VENV="$REPO/.ruby_env"

[ -x "$RUBY" ] || { echo "não encontrei o Ruby em $RUBY (define MARTA_RBENV_RUBY)" >&2; exit 1; }

DEF="$("$RUBY" -e 'print Gem.default_dir')"
mkdir -p "$VENV"
echo "venv: $VENV"
echo "ruby: $("$RUBY" --version)"
echo

# --install-dir força a escrita no venv mesmo que a gem já esteja visível no
# store global — sem isto, enquanto o global ainda tiver rspec, o `gem install`
# considera as deps satisfeitas e o venv fica sem o executável `bin/rspec`.
echo "a instalar o rspec no venv…"
GEM_HOME="$VENV" GEM_PATH="$VENV:$DEF" \
  "$GEM" install rspec --no-document --install-dir "$VENV"

echo
echo "=== verificação ==="
GEM_HOME="$VENV" GEM_PATH="$VENV:$DEF" "$RUBY" -e '
  ok = true
  %w[json prism coverage minitest rspec/core].each do |g|
    begin; require g; puts "  OK      #{g}"
    rescue LoadError; puts "  FALHA   #{g}"; ok = false; end
  end
  exit(ok ? 0 : 1)
'
[ -x "$VENV/bin/rspec" ] && echo "  OK      bin/rspec" || { echo "  FALHA   bin/rspec"; exit 1; }

echo
echo "Pronto. Activa com:  source scripts/ruby_env.sh"

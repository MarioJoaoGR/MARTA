#!/bin/bash
# Devolve o store global do rbenv ao estado de uma instalação limpa do Ruby.
#
# Remove duas coisas:
#   1. as 40 gems que entraram a 19-20 jul — dependências de DESENVOLVIMENTO das
#      gems clonadas nas sondagens, instaladas antes de a isolação por GEM_HOME
#      estar apertada. Nunca deviam lá ter estado;
#   2. o rspec (+deps) e o simplecov, que passam a viver no venv `.ruby_env/`.
#      O simplecov nem sequer é usado — medimos com o módulo Coverage nativo.
#
# NÃO toca no Ruby 3.4.10 nem nas bundled gems da distribuição (minitest, rake,
# ...): essas são o equivalente à stdlib do Python e têm de lá ficar.
#
#   ./scripts/limpar_gems_globais.sh            # só mostra (dry-run)
#   ./scripts/limpar_gems_globais.sh --apagar   # apaga
set -uo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUBY="${MARTA_RBENV_RUBY:-$HOME/.rbenv/versions/3.4.10/bin/ruby}"
GEM="$(dirname "$RUBY")/gem"
VENV="$REPO/.ruby_env"

# Fugas das sondagens de 19-20 jul.
FUGAS=(
  ast:2.4.3 bigdecimal:4.1.2 coderay:1.1.3 concurrent-ruby:1.3.7
  concurrent-ruby:1.3.8 erb:6.0.5 i18n:1.15.2 io-console:0.8.2 json:2.21.1
  language_server-protocol:3.17.0.6 lint_roller:1.1.0 logger:1.7.0
  method_source:1.1.0
  minitest:5.27.0 mocha:2.1.0 parallel:2.1.0 parser:3.3.12.0 prism:1.9.0
  pry:0.16.0 rainbow:3.1.1 rake:13.4.2 rbs:4.0.3 rdoc:8.0.0 redcarpet:3.6.1
  regexp_parser:2.12.0 reline:0.6.3 rubocop:1.86.2 rubocop-ast:1.50.0
  rubocop-performance:1.26.1 rubocop-rake:0.7.1 rubocop-rspec:3.8.0
  ruby-progressbar:1.13.0 ruby2_keywords:0.0.5 simplecov:1.0.2
  test_declarative:0.0.6 tsort:0.2.0 typeprof:0.32.0
  unicode-display_width:3.2.0 unicode-emoji:4.2.0 yard:0.9.45
)
# Passam a viver no venv.
MUDAM_PARA_VENV=(
  rspec:3.13.2 rspec-core:3.13.6 rspec-expectations:3.13.5 rspec-mocks:3.13.8
  rspec-support:3.13.7 diff-lcs:1.6.2 simplecov:1.0.0
)
TODAS=("${FUGAS[@]}" "${MUDAM_PARA_VENV[@]}")

if [ "${1:-}" != "--apagar" ]; then
  echo "DRY-RUN — nada será apagado. Correr com --apagar para executar."
  echo
  echo "fugas das sondagens (${#FUGAS[@]}):"
  printf '%s\n' "${FUGAS[@]}" | tr ':' ' ' | awk '{printf "    %-30s %s\n", $1, $2}'
  echo
  echo "passam para o venv (${#MUDAM_PARA_VENV[@]}):"
  printf '%s\n' "${MUDAM_PARA_VENV[@]}" | tr ':' ' ' | awk '{printf "    %-30s %s\n", $1, $2}'
  echo
  echo "total: ${#TODAS[@]}. Ruby e bundled gems não são tocados."
  exit 0
fi

# GUARDA: nunca remover o rspec do global sem o venv já a funcionar, senão a
# ferramenta fica sem rspec nenhum. Env explícito para não depender do shell.
DEF="$("$RUBY" -e 'print Gem.default_dir')"
if ! GEM_HOME="$VENV" GEM_PATH="$VENV" "$RUBY" -e 'require "rspec/core"' 2>/dev/null \
   || [ ! -x "$VENV/bin/rspec" ]; then
  echo "ABORTADO: o venv em $VENV não tem um rspec funcional." >&2
  echo "          corre primeiro:  ./scripts/setup_ruby_env.sh" >&2
  exit 1
fi

# CRÍTICO: forçar o alvo no store GLOBAL. Sem isto, correr este script com o
# venv activo (`source scripts/ruby_env.sh`) herdava GEM_HOME=.ruby_env e o
# `gem uninstall` ia esvaziar o VENV em vez do global — foi o que aconteceu à
# primeira. O nome do script promete "globais": tem de o garantir sozinho.
export GEM_HOME="$DEF"
export GEM_PATH="$DEF"

echo "venv verificado (rspec funcional). A limpar o global em $DEF …"
echo

n_rm=0; n_skip=0
for g in "${TODAS[@]}"; do
  name="${g%%:*}"; ver="${g##*:}"
  # Verificar a presença ANTES: `gem uninstall --force` devolve 0 mesmo quando a
  # gem não existe, por isso confiar no seu código de saída fazia o relatório
  # dizer "removida" para dezenas de gems já ausentes.
  if [ ! -f "$DEF/specifications/$name-$ver.gemspec" ]; then
    n_skip=$((n_skip+1)); continue
  fi
  # -x remove executáveis, -I ignora dependências (evita prompts interactivos),
  # --force não aborta se outra gem ainda a declarar como dep.
  if "$GEM" uninstall "$name" -v "$ver" -x -I --force >/dev/null 2>&1 \
     && [ ! -f "$DEF/specifications/$name-$ver.gemspec" ]; then
    echo "  removida  $name $ver"; n_rm=$((n_rm+1))
  else
    echo "  FALHOU    $name $ver (ainda presente)"
  fi
done
echo
echo "  $n_rm removidas, $n_skip já ausentes."

# O shim do rspec fica pendurado depois de o remover do global.
command -v rbenv >/dev/null && rbenv rehash 2>/dev/null

echo
echo "=== verificação: o venv continua inteiro? ==="
venv_ok=1
GEM_HOME="$VENV" GEM_PATH="$VENV:$DEF" "$RUBY" -e '
  ok = true
  %w[json prism coverage minitest rspec/core].each do |g|
    begin; require g; puts "  OK      #{g}"
    rescue LoadError; puts "  FALHA   #{g}"; ok = false; end
  end
  exit(ok ? 0 : 1)' || venv_ok=0
if [ "$venv_ok" -eq 0 ] || [ ! -x "$VENV/bin/rspec" ]; then
  echo
  echo "!!! O VENV FICOU PARTIDO. Recupera com:  ./scripts/setup_ruby_env.sh" >&2
  exit 1
fi
echo
echo "=== o que sobra no store global (deve ser só a distribuição do Ruby) ==="
du -sh "$DEF/gems"
echo
echo "Agora: source scripts/ruby_env.sh"

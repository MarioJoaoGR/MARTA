# Ativa o "venv" de Ruby da MARTA — o equivalente ao `source venv/bin/activate`.
#
#   source scripts/ruby_env.sh
#
# REGRA (a mesma do Python: nunca `pip install` fora do venv): tudo o que for
# instalado vai para `.ruby_env/`, NUNCA para o store global do rbenv. O que se
# instalar sem isto activo suja a máquina e não é reprodutível.
#
# Porque é que o GEM_PATH inclui o `Gem.default_dir` além do venv: as *bundled
# gems* do Ruby (minitest, rake, ...) vivem lá e fazem parte da distribuição —
# são o equivalente à stdlib do Python, não algo que nós instalámos. Sem elas,
# `require "minitest"` falha e a medição das suites humanas em Minitest (faker,
# jekyll, fluentd) deixa de funcionar. LER de lá é correto; ESCREVER lá não.

_marta_repo="$(cd "$(dirname "${BASH_SOURCE[0]:-${(%):-%x}}")/.." && pwd)"
_marta_ruby="${MARTA_RBENV_RUBY:-$HOME/.rbenv/versions/3.4.10/bin/ruby}"

if [ ! -x "$_marta_ruby" ]; then
  echo "ruby_env: não encontrei o Ruby em $_marta_ruby" >&2
  echo "          define MARTA_RBENV_RUBY para o caminho certo." >&2
  return 1 2>/dev/null || exit 1
fi

export MARTA_RUBY_ENV="$_marta_repo/.ruby_env"
export MARTA_RUBY_BIN="$_marta_ruby"
export MARTA_RSPEC_BIN="$MARTA_RUBY_ENV/bin/rspec"

# GEM_HOME = para onde os `gem install` escrevem. Só o venv, sempre.
export GEM_HOME="$MARTA_RUBY_ENV"
# GEM_PATH = de onde se lê. Venv + distribuição do Ruby (ver comentário acima).
export GEM_PATH="$MARTA_RUBY_ENV:$("$_marta_ruby" -e 'print Gem.default_dir')"
export PATH="$MARTA_RUBY_ENV/bin:$(dirname "$_marta_ruby"):$PATH"

echo "ruby_env activo: $MARTA_RUBY_ENV"
if [ -x "$MARTA_RSPEC_BIN" ]; then
  echo "  rspec: $("$MARTA_RSPEC_BIN" --version 2>/dev/null | head -1)"
else
  echo "  (venv por criar — corre: ./scripts/setup_ruby_env.sh)"
fi

unset _marta_repo _marta_ruby

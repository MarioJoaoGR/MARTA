#!/bin/bash
# Regenera os artefactos da demo a partir dos dois ficheiros em 1_codigo/.
# Nada aqui e escrito a mao: 2_prism/ e a saida do parser, 3_grafo/ e a saida
# do construtor do grafo.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/../.."
source scripts/ruby_env.sh >/dev/null
PY=/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/bin/python
D=apresentacao/demo

for f in carteira movimento; do
  "$MARTA_RUBY_BIN" marta/ruby_backend/rb/marta_parse.rb "$D/1_codigo/$f.rb" \
    | "$PY" -m json.tool > "$D/2_prism/$f.json"
done

"$PY" - <<'EOF'
import sys, os, json
sys.path.insert(0, os.getcwd())
from marta.ruby_backend.backend import RubyBackend
b = RubyBackend()
cg = b.build_call_graph(b.discover_files(os.path.abspath("apresentacao/demo/1_codigo")))
json.dump(cg.to_json(), open("apresentacao/demo/3_grafo/grafo.json", "w"), indent=2)
open("apresentacao/demo/3_grafo/grafo.dot", "w").write(cg.to_dot("demo"))
for e in cg.edges:
    print(f"  {e.caller:22s} -> {e.callee:22s} [{e.kind}]")
EOF

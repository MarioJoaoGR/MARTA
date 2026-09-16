"""Cobertura convencional por ficheiro: a regra do coverage.py.

Confirmado a 2026-09-16 com o coverage.py 7.6.1 num módulo Python só importado
(import, constante, classe com três métodos, nenhum chamado): 12 instruções, 6
executadas — o import, a constante, a linha `class` e as três linhas `def`
(linhas 1, 3, 6, 7, 13, 16) — 50%. O denominador é o ficheiro inteiro, não só as
linhas de dentro dos métodos. Estes testes prendem a mesma regra do lado Ruby.
"""
import pytest

from marta.ruby_backend import coverage_runner as cov, runner
from marta.ruby_backend.ruby_ast import RubyParseError


def _toolchain_ok():
    try:
        return runner.syntax_check("def x; end") is None
    except RubyParseError:
        return False


precisa = pytest.mark.skipif(not _toolchain_ok(), reason="no Ruby/RSpec toolchain")


def test_regra_sobre_o_array_de_linhas():
    # null = não executável, 0 = não correu, >0 = correu
    fc = cov.file_coverage([1, None, 3, 0, 0, None, 1], [[2, 1], [4, 0]])
    assert fc.executable_lines == 5
    assert fc.covered_lines == 3
    assert round(fc.pct, 1) == 60.0
    assert fc.total_branches == 2 and fc.covered_branches == 1


def test_ficheiro_nao_carregado_da_zero_e_nao_rebenta():
    fc = cov.file_coverage(None)
    assert fc.executable_lines == 0 and fc.pct == 0.0


@precisa
def test_mesmo_ficheiro_que_o_do_coverage_py(tmp_path):
    """O equivalente Ruby do módulo medido com o coverage.py: só carregado, nenhum
    método chamado. Contam as linhas que correm ao carregar (require, constante,
    class, def) sobre TODAS as executáveis do ficheiro."""
    (tmp_path / "lib").mkdir()
    (tmp_path / "lib" / "parents.rb").write_text(
        'require "set"\n'                         # 1  corre ao carregar
        "\n"                                      # 2
        'SEPARADOR = "-"\n'                       # 3  corre ao carregar
        "\n"                                      # 4
        "class Parents\n"                         # 5  corre ao carregar
        "  def parent\n"                          # 6  corre ao carregar (def)
        "    segmentos = tag.split(SEPARADOR)\n"  # 7
        "    return nil if segmentos.size < 2\n"  # 8
        "    segmentos[0..-2].join(SEPARADOR)\n"  # 9
        "  end\n"                                 # 10
        "\n"                                      # 11
        "  def self_and_parents\n"                # 12 corre ao carregar (def)
        "    [self] + parents\n"                  # 13
        "  end\n"                                 # 14
        "\n"                                      # 15
        "  def parents\n"                         # 16 corre ao carregar (def)
        "    [parent]\n"                          # 17
        "  end\n"                                 # 18
        "end\n")                                  # 19
    spec = tmp_path / "so_carrega_spec.rb"
    spec.write_text('require "parents"\nRSpec.describe("x") { it("y") { expect(1).to eq(1) } }\n')

    res = cov.run_line_coverage(".", [str(spec)], cwd=str(tmp_path), isolated=True,
                                load_paths=["lib"])
    fc = cov.file_coverage(res.files["lib/parents.rb"])

    corridas = [n + 1 for n, h in enumerate(res.files["lib/parents.rb"]) if h]
    assert corridas == [1, 3, 5, 6, 12, 16]
    assert fc.covered_lines == 6
    # o denominador inclui os corpos dos métodos, que nunca correram
    assert fc.executable_lines > fc.covered_lines

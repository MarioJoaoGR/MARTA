"""O ambiente de execução certificado pelo dataset (camadas 6 e 7).

A camada 6 certificou que cada módulo carrega com TODAS as pastas de carregamento
da gem e com a porta de entrada já carregada. Se a ferramenta correr os specs de
outra maneira, módulos certificados falham por causa do ambiente. Estes testes
prendem as quatro peças: o nome do `require`, a lista de `-I`, o `-r` da porta de
entrada, e a invocação de métodos na cobertura.
"""
import pytest

from marta.ruby_backend import coverage_runner as cov, runner
from marta.ruby_backend.project import RubyProject
from marta.ruby_backend.ruby_ast import RubyParseError


def _toolchain_ok():
    try:
        return runner.syntax_check("def x; end") is None
    except RubyParseError:
        return False


precisa = pytest.mark.skipif(not _toolchain_ok(), reason="no Ruby/RSpec toolchain")


class _M:
    """Só o que o synthesize lê de um método."""
    def __init__(self, start, end):
        self.start_line, self.end_line = start, end


# --- nome do require e ficheiros analisados -------------------------------- #
@precisa
def test_require_tira_o_prefixo_da_pasta_de_carregamento(tmp_path):
    """No fastlane o alvo é `deliver/lib/deliver/setup.rb` e o require é
    `deliver/setup` — o caminho inteiro dava LoadError."""
    (tmp_path / "deliver" / "lib" / "deliver").mkdir(parents=True)
    (tmp_path / "deliver" / "lib" / "deliver" / "setup.rb").write_text(
        "class Setup\n  def run(x)\n    x\n  end\nend\n")
    (tmp_path / "fora.rb").write_text("class Fora\n  def a\n    1\n  end\nend\n")

    proj = RubyProject(root_dir=str(tmp_path), source_dir=".",
                       load_paths=["deliver/lib"], preload="fastlane",
                       code_files=["deliver/lib/deliver/setup.rb"],
                       target_files=["deliver/lib/deliver/setup.rb"]).discover()

    t = proj.targets[0]
    assert t.require_target == "deliver/setup"
    # a chave da cobertura continua a ser o caminho do ficheiro
    assert t.source_rel == "deliver/lib/deliver/setup.rb"
    # só os ficheiros do manifesto são analisados (o fora.rb existe e não entra)
    assert len(proj.files) == 1


@precisa
def test_raiz_entra_no_load_path_mas_nao_no_require(tmp_path):
    """A camada 6 punha a raiz no $LOAD_PATH, e é por isso que ficheiros fora de
    qualquer lib/ (o setup.rb da kramdown) carregam. Mas o nome do require só usa
    as pastas declaradas."""
    (tmp_path / "lib").mkdir()
    (tmp_path / "lib" / "a.rb").write_text("class A\n  def x\n    1\n  end\nend\n")
    (tmp_path / "setup.rb").write_text("class S\n  def y\n    2\n  end\nend\n")

    proj = RubyProject(root_dir=str(tmp_path), source_dir=".", load_paths=["lib"],
                       code_files=["lib/a.rb", "setup.rb"],
                       target_files=["lib/a.rb", "setup.rb"]).discover()

    reqs = {t.source_rel: t.require_target for t in proj.targets}
    assert reqs["lib/a.rb"] == "a"
    assert reqs["setup.rb"] == "setup"
    assert proj._load_path_list() == ["lib", "."]


@precisa
def test_sem_ambiente_o_comportamento_e_o_de_sempre(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "calc.rb").write_text("class Calc\n  def add(a, b) = a + b\nend\n")
    proj = RubyProject(root_dir=str(tmp_path), source_dir="src").discover()
    t = proj.targets[0]
    assert t.require_target == "calc" and t.source_rel == "calc.rb"
    assert proj._load_path_list() == ["src"]
    assert proj.backend.requires == []


# --- porta de entrada ------------------------------------------------------ #
@precisa
def test_run_rspec_carrega_a_porta_de_entrada(tmp_path):
    (tmp_path / "porta.rb").write_text("PORTA = 7\n")
    spec = tmp_path / "x_spec.rb"
    spec.write_text('RSpec.describe "porta" do\n  it "vem carregada" do\n'
                    '    expect(PORTA).to eq(7)\n  end\nend\n')

    sem = runner.run_rspec(str(spec), load_paths=["."], cwd=str(tmp_path))
    assert not sem.all_passed

    com = runner.run_rspec(str(spec), load_paths=["."], cwd=str(tmp_path),
                           requires=["porta"])
    assert com.all_passed


# --- cobertura: pastas, porta e invocação ---------------------------------- #
@precisa
def test_cobertura_com_pastas_porta_e_invocacao(tmp_path):
    (tmp_path / "sub" / "lib").mkdir(parents=True)
    (tmp_path / "sub" / "lib" / "bar.rb").write_text(
        "class Bar\n"          # 1
        "  def hi\n"           # 2
        "    :hi\n"            # 3
        "  end\n"              # 4
        "  def nunca\n"        # 5
        "    :n\n"             # 6
        "  end\n"              # 7
        "end\n")               # 8
    (tmp_path / "porta.rb").write_text("PORTA = true\n")
    spec = tmp_path / "bar_spec.rb"
    spec.write_text('require "bar"\nRSpec.describe Bar do\n  it "x" do\n'
                    '    expect(PORTA).to eq(true)\n'
                    '    expect(Bar.new.hi).to eq(:hi)\n  end\nend\n')

    res = cov.run_line_coverage(".", [str(spec)], cwd=str(tmp_path), isolated=True,
                                load_paths=["sub/lib", "."], requires=["porta"])

    rel = "sub/lib/bar.rb"
    assert rel in res.files, "a pasta de carregamento extra não chegou ao helper"
    linhas, metodos = res.files[rel], res.methods[rel]

    hi = cov.synthesize(_M(2, 4), linhas, res.branches.get(rel), metodos)
    nunca = cov.synthesize(_M(5, 7), linhas, res.branches.get(rel), metodos)
    assert hi.invoked is True
    assert nunca.invoked is False
    # E a razão de `invoked` existir: na métrica convencional o método que nunca
    # foi chamado já conta a linha do `def`, executada ao carregar o ficheiro.
    assert nunca.covered_lines >= 1


def test_synthesize_sem_dados_de_metodos_deixa_invoked_indefinido():
    mc = cov.synthesize(_M(1, 3), [1, 0, None])
    assert mc.invoked is None
    assert mc.covered_lines == 1 and mc.missing_lines == [2]

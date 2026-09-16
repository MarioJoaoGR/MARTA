"""A ablação do grafo: `enrich=False` desliga os dois sítios, e só esses.

O grafo entra na Fase 1 em dois pontos — a 2ª passagem do `done_what` (junta o
que os métodos chamados fazem) e a propagação do `what_todo` (um método herda a
perspetiva de quem o chama). O braço da ablação tem de desligar os DOIS: desligar
só um mediria meia coisa e o resultado não diria nada.

As fases do recorder são o que prova isso sem depender de prompts.
"""
import asyncio

import pytest

from marta.ruby_backend import runner
from marta.ruby_backend.project import RubyProject
from marta.ruby_backend.ruby_ast import RubyParseError


def _toolchain_ok():
    try:
        return runner.syntax_check("def x; end") is None
    except RubyParseError:
        return False


precisa = pytest.mark.skipif(not _toolchain_ok(), reason="no Ruby/RSpec toolchain")

# `dobro` chama `soma`: uma aresta entre dois métodos que são ambos alvo, que é
# a condição para o grafo mudar alguma coisa.
CODIGO = """class Calc
  def dobro(x)
    soma(x, x)
  end

  def soma(a, b)
    a + b
  end
end
"""


def _projeto(tmp_path):
    (tmp_path / "lib").mkdir()
    (tmp_path / "lib" / "calc.rb").write_text(CODIGO)
    return RubyProject(root_dir=str(tmp_path), source_dir="lib").discover()


async def _ask(system, user):
    return "um resumo qualquer"


@precisa
def test_com_grafo_ha_segunda_passagem_e_propagacao(tmp_path):
    proj = _projeto(tmp_path)
    r = proj._recorder()
    asyncio.run(proj.analyze_summaries(ask=_ask, use_cache=False, enrich=True))

    fases = r.score.por_fase
    assert fases["sumarios_passagem1"]["chamadas"] == 2
    # o `dobro` chama o `soma`, logo paga a 2ª passagem
    assert fases["sumarios_passagem2"]["chamadas"] == 1
    # o `soma` é chamado, logo o what_todo dele vem do chamador e não do README
    assert fases["what_todo_propagado"]["chamadas"] == 1
    assert fases["what_todo_raiz"]["chamadas"] >= 1


@precisa
def test_sem_grafo_os_dois_pontos_ficam_desligados(tmp_path):
    proj = _projeto(tmp_path)
    r = proj._recorder()
    asyncio.run(proj.analyze_summaries(ask=_ask, use_cache=False, enrich=False))

    fases = r.score.por_fase
    # a 2ª passagem nem chega a existir
    assert "sumarios_passagem2" not in fases
    # e ninguém tem chamadores: todos são raiz, nada se propaga
    assert fases.get("what_todo_propagado", {}).get("chamadas", 0) == 0
    assert fases["what_todo_raiz"]["chamadas"] == 2
    # o resto do fluxo fica igual: uma passagem 1 e um sumário final por método
    assert fases["sumarios_passagem1"]["chamadas"] == 2
    assert fases["sumario_final"]["chamadas"] == 2


@precisa
def test_filtro_por_metodo(tmp_path):
    """O braço da ablação só repete os métodos que o grafo afeta: o ficheiro
    continua alvo, mas só esses métodos geram specs."""
    (tmp_path / "lib").mkdir()
    (tmp_path / "lib" / "calc.rb").write_text(CODIGO)
    proj = RubyProject(root_dir=str(tmp_path), source_dir="lib",
                       method_names=["Calc#soma"]).discover()
    assert [t.method.qualified_name for t in proj.targets] == ["Calc#soma"]
    # o ficheiro continua a ser analisado: o grafo e o índice de tipos precisam
    assert len(proj.files) == 1


@precisa
def test_os_dois_bracos_nao_partilham_cache(tmp_path, monkeypatch):
    """Sem ficheiros de cache separados, um braço lia os sumários do outro e a
    ablação não media nada."""
    monkeypatch.setenv("MODEL", "modelo_de_teste")
    proj = _projeto(tmp_path)
    asyncio.run(proj.analyze_summaries(ask=_ask, use_cache=True, enrich=True))
    asyncio.run(proj.analyze_summaries(ask=_ask, use_cache=True, enrich=False))

    caches = sorted(p.name for p in (tmp_path / ".marta_ruby_cache").glob("analysis_*.json"))
    assert caches == ["analysis_modelo_de_teste.json",
                      "analysis_modelo_de_teste_sem_grafo.json"]

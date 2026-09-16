"""Telemetria da execução: fases, eventos por chamada, cortes e erros.

O total de tokens não responde a "onde foi o tempo" nem a "quantas respostas
vieram cortadas". Estes testes prendem o que o recorder passou a medir.
"""
import asyncio
import json

from marta.ruby_backend import recorder as rec


def _ask_fake(tokens=(100, 40), resposta="resp"):
    """Imita o que o gptapi faz numa chamada real: credita o singleton."""
    from marta.recorder import recoder as py_recoder

    async def ask(system, user):
        py_recoder.score.add_tokens(*tokens)
        return resposta
    return ask


def test_chamadas_sao_separadas_por_fase():
    r = rec.RubyRecorder()
    ask = rec.token_tracking_ask(_ask_fake(), r.score, r)

    async def fluxo():
        with r.fase("plano"):
            await ask("s", "u")
        with r.fase("dev"):
            await ask("s", "u")
            await ask("s", "u")

    asyncio.run(fluxo())
    por_fase = r.score.por_fase
    assert por_fase["plano"]["chamadas"] == 1
    assert por_fase["dev"]["chamadas"] == 2
    assert por_fase["dev"]["prompt_tokens"] == 200
    assert por_fase["dev"]["completion_tokens"] == 80
    # o tempo de parede da fase é medido mesmo quando o modelo é de mentira
    assert por_fase["dev"]["segundos_total"] >= 0.0
    assert r.score.llm_calls == 3


def test_eventos_ficam_no_jsonl_com_metodo_e_ronda(tmp_path):
    caminho = tmp_path / "eventos.jsonl"
    r = rec.RubyRecorder(caminho_eventos=str(caminho))
    ask = rec.token_tracking_ask(_ask_fake(), r.score, r)

    async def fluxo():
        with r.contexto(metodo="Calc#add", ronda=1):
            with r.fase("plano"):
                await ask("s", "u")

    asyncio.run(fluxo())
    linhas = [json.loads(x) for x in caminho.read_text().splitlines()]
    assert len(linhas) == 1
    e = linhas[0]
    assert e["tipo"] == "llm" and e["fase"] == "plano"
    assert e["metodo"] == "Calc#add" and e["ronda"] == 1
    assert e["prompt_tokens"] == 100 and e["completion_tokens"] == 40


def test_resposta_cortada_pelo_limite_e_contada(monkeypatch):
    monkeypatch.setattr(rec, "_detalhe_da_ultima_chamada",
                        lambda: {"finish_reason": "length", "erro": None})
    r = rec.RubyRecorder()
    ask = rec.token_tracking_ask(_ask_fake(), r.score, r)
    asyncio.run(ask("s", "u"))
    assert r.score.llm_cortadas == 1 and r.score.llm_erros == 0


def test_erro_do_modelo_e_contado(monkeypatch):
    """O gptapi devolve "" quando a chamada falha; sem isto era uma chamada
    normal com resposta vazia."""
    monkeypatch.setattr(rec, "_detalhe_da_ultima_chamada",
                        lambda: {"finish_reason": None, "erro": "Timeout"})
    r = rec.RubyRecorder()
    ask = rec.token_tracking_ask(_ask_fake(resposta=""), r.score, r)
    asyncio.run(ask("s", "u"))
    assert r.score.llm_erros == 1
    assert r.score.por_fase["?"]["erros"] == 1


def test_subprocessos_ruby_sao_cronometrados(tmp_path):
    r = rec.RubyRecorder(caminho_eventos=str(tmp_path / "e.jsonl"))
    with r.fase("dev"):
        with r.medir("rspec"):
            pass
        with r.medir("rspec"):
            pass
        with r.medir("ruby -c"):
            pass
    assert r.score.subprocessos["rspec"]["execucoes"] == 2
    assert r.score.subprocessos["ruby -c"]["execucoes"] == 1
    tipos = [json.loads(x)["tipo"] for x in (tmp_path / "e.jsonl").read_text().splitlines()]
    assert tipos == ["rspec", "rspec", "ruby -c"]


def test_contexto_persistente_marca_a_ronda(tmp_path):
    """A ronda dura um ciclo inteiro: fixa-se uma vez e fica em todos os eventos
    seguintes, sem reindentar o ciclo."""
    caminho = tmp_path / "e.jsonl"
    r = rec.RubyRecorder(caminho_eventos=str(caminho))
    r.define_contexto(ronda=0)
    with r.medir("rspec"):
        pass
    r.define_contexto(ronda=1)
    with r.contexto(metodo="Calc#add"):
        with r.medir("rspec"):
            pass
    eventos = [json.loads(x) for x in caminho.read_text().splitlines()]
    assert [e["ronda"] for e in eventos] == [0, 1]
    assert "metodo" not in eventos[0] and eventos[1]["metodo"] == "Calc#add"


def test_json_final_mantem_as_chaves_antigas():
    """O formato do run_results não pode partir: o que existia continua lá."""
    r = rec.RubyRecorder()
    r.score.add_syntax_pass()
    r.score.add_llm_call(10, 5, fase="plano", segundos=0.5)
    d = r.to_json()
    for chave in ("time", "times", "syntax_pass", "prompt_tokens", "completion_tokens",
                  "llm_calls", "total_tokens", "coverage", "assertion_error_types"):
        assert chave in d
    assert d["total_tokens"] == 15
    assert d["por_fase"]["plano"]["chamadas"] == 1

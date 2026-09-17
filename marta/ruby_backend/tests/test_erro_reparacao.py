"""O texto do erro que volta ao modelo na reparação tem de caber no prompt."""
from marta.ruby_backend import prompts


def test_erro_curto_fica_igual():
    assert prompts.resumir_erro("Failure/Error: x\nexpected 1") == "Failure/Error: x\nexpected 1"


def test_backtrace_repetido_de_uma_recursao_passa_a_uma_linha():
    texto = "SystemStackError:\n  stack level too deep\n" + "# ./spec.rb:3:in 'a'\n" * 20000 + "1 example, 1 failure"
    r = prompts.resumir_erro(texto)
    assert "[linha repetida 20000 vezes]" in r
    assert r.startswith("SystemStackError:") and r.endswith("1 example, 1 failure")
    assert len(r) < 200


def test_texto_longo_guarda_o_inicio_e_o_fim():
    texto = "MENSAGEM\n" + "\n".join(f"linha {i}" for i in range(50000)) + "\nRESUMO FINAL"
    r = prompts.resumir_erro(texto)
    assert len(r) <= prompts.LIMITE_ERRO + 100
    assert r.startswith("MENSAGEM") and r.endswith("RESUMO FINAL")
    assert "caracteres omitidos" in r


def test_o_prompt_de_reparacao_usa_o_resumo():
    enorme = "x\n" * 10 + "y" * 100000
    assert len(prompts.repair_dev_instruction(enorme)) < prompts.LIMITE_ERRO + 500

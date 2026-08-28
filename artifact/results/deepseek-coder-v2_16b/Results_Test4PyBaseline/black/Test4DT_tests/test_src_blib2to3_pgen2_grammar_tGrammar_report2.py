# Module: blib2to3.pgen2.grammar
import pytest
from blib2to3.pgen2.grammar import Grammar

def test_initialization():
    grammar = Grammar()
    assert isinstance(grammar, Grammar)
    assert grammar.symbol2number == {}
    assert grammar.number2symbol == {}
    assert grammar.states == []
    assert grammar.dfas == {}
    assert grammar.labels == [(0, "EMPTY")]
    assert grammar.keywords == {}
    assert grammar.tokens == {}
    assert grammar.symbol2label == {}
    assert grammar.start == 256
    assert not grammar.async_keywords

def test_report():
    grammar = Grammar()
    # Since the report method is supposed to print to stdout, we can't directly check its output in a unit test.
    # However, we can ensure that it runs without errors and doesn't crash when called.
    try:
        grammar.report()
    except Exception as e:
        pytest.fail(f"Unexpected error occurred: {e}")

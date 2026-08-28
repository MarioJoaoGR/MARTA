
import pytest
from blib2to3.pgen2.grammar import Grammar

# Test the initialization of the Grammar class
def test_grammar_initialization():
    grammar = Grammar()
    assert isinstance(grammar, Grammar)
    assert grammar.symbol2number == {}
    assert grammar.number2symbol == {}
    assert grammar.states == []
    assert grammar.dfas == {}
    assert grammar.labels == [(0, "EMPTY")]
    assert grammar.keywords == {}
    assert grammar.tokens == {}
    assert grammar.start == 256
    assert not grammar.async_keywords

# Test the report method of the Grammar class
def test_grammar_report(capsys):
    grammar = Grammar()
    grammar.report()
    captured = capsys.readouterr()
    assert "s2n" in captured.out
    assert "n2s" in captured.out
    assert "states" in captured.out
    assert "dfas" in captured.out
    assert "labels" in captured.out
    assert "start 256" in captured.out

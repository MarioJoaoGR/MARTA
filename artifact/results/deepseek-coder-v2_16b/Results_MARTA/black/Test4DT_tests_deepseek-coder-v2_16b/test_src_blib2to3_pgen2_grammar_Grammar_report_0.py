
import pytest
from blib2to3.pgen2.grammar import Grammar

def test_init():
    grammar = Grammar()
    assert hasattr(grammar, 'symbol2number')
    assert isinstance(grammar.symbol2number, dict)
    assert hasattr(grammar, 'number2symbol')
    assert isinstance(grammar.number2symbol, dict)
    assert hasattr(grammar, 'states')
    assert isinstance(grammar.states, list)
    assert hasattr(grammar, 'dfas')
    assert isinstance(grammar.dfas, dict)
    assert hasattr(grammar, 'labels')
    assert isinstance(grammar.labels, list)
    assert hasattr(grammar, 'keywords')
    assert isinstance(grammar.keywords, dict)
    assert hasattr(grammar, 'tokens')
    assert isinstance(grammar.tokens, dict)
    assert hasattr(grammar, 'symbol2label')
    assert isinstance(grammar.symbol2label, dict)
    assert hasattr(grammar, 'start')
    assert isinstance(grammar.start, int)
    assert hasattr(grammar, 'async_keywords')
    assert isinstance(grammar.async_keywords, bool)

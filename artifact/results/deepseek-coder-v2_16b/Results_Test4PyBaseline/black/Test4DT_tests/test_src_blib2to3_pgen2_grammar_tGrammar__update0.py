
# Module: blib2to3.pgen2.grammar
# test_grammar.py
from blib2to3.pgen2.grammar import Grammar
import pytest

@pytest.fixture
def grammar():
    return Grammar()

def test_default_initialization(grammar):
    assert isinstance(grammar.symbol2number, dict)
    assert isinstance(grammar.number2symbol, dict)
    assert isinstance(grammar.states, list)
    assert isinstance(grammar.dfas, dict)
    assert isinstance(grammar.labels, list)
    assert isinstance(grammar.keywords, dict)
    assert isinstance(grammar.tokens, dict)
    assert isinstance(grammar.symbol2label, dict)
    assert grammar.start == 256
    assert not grammar.async_keywords

def test_update_attributes(grammar):
    attrs = {
        "symbol2number": {"S": 256, "NP": 257, "VP": 258},
        "number2symbol": {256: "S", 257: "NP", 258: "VP"},
        # Other attributes can be updated similarly
    }
    grammar._update(attrs)
    assert grammar.symbol2number == {"S": 256, "NP": 257, "VP": 258}
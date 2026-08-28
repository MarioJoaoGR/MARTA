
import pytest
from pathlib import Path
import pickle
from blib2to3.pgen2.grammar import Grammar

# Test initialization of the Grammar class
def test_grammar_initialization():
    grammar = Grammar()
    assert isinstance(grammar.symbol2number, dict)
    assert isinstance(grammar.number2symbol, dict)
    assert isinstance(grammar.states, list)
    assert isinstance(grammar.dfas, dict)
    assert isinstance(grammar.labels, list)
    assert isinstance(grammar.keywords, dict)
    assert isinstance(grammar.tokens, dict)
    assert isinstance(grammar.symbol2label, dict)
    assert grammar.start == 256
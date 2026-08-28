
import pytest
from blib2to3.pgen2.grammar import Grammar
import pickle

@pytest.fixture
def valid_grammar():
    grammar = Grammar()
    pkl = pickle.dumps(grammar)
    return (grammar, pkl)

def test_valid_input(valid_grammar):
    grammar, pkl = valid_grammar
    with pytest.raises(AttributeError):
        grammar.loads(pkl)

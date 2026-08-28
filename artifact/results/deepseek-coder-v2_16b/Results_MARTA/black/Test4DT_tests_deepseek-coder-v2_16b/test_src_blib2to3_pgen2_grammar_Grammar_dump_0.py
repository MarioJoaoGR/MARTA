
import pytest
from blib2to3.pgen2.grammar import Grammar

def test_edge_case():
    grammar = Grammar()
    with pytest.raises(AttributeError):
        # Attempt to call a method that should raise AttributeError
        grammar.method_that_does_not_exist()

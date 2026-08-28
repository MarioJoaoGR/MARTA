
import pytest
from pathlib import Path
import pickle
from blib2to3.pgen2.grammar import Grammar

@pytest.fixture(scope="module")
def grammar():
    grammar = Grammar()
    yield grammar
    # Teardown if necessary

def test_valid_input(grammar):
    valid_file_path = Path(__file__).parent / "test_grammar.pkl"
    with open(valid_file_path, "wb") as f:
        pickle.dump({}, f)
    
    grammar.load(valid_file_path)
    assert grammar.symbol2number == {}
    assert grammar.number2symbol == {}
    assert grammar.states == []
    assert grammar.dfas == {}
    assert grammar.labels == [(0, "EMPTY")]
    assert grammar.keywords == {}
    assert grammar.tokens == {}
    assert grammar.start == 256
    assert grammar.async_keywords is False


import pytest
from pathlib import Path
import pickle
from src.blib2to3.pgen2.grammar import Grammar

@pytest.fixture(name="non_existent_grammar")
def fixture_non_existent_grammar():
    return Grammar()

@pytest.fixture(name="empty_grammar")
def fixture_empty_grammar():
    grammar = Grammar()
    # Simulate an empty grammar by not loading any data
    return grammar

def test_invalid_input(non_existent_grammar):
    with pytest.raises(FileNotFoundError) as excinfo:
        non_existent_grammar.load(Path("nonexistentfile.pkl"))
    assert isinstance(excinfo.value, FileNotFoundError), "Expected FileNotFoundError"

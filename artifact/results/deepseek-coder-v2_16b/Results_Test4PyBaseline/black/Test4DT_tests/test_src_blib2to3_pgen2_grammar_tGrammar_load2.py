
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
    assert not grammar.async_keywords

# Test loading the grammar tables from a pickle file
def test_load_from_pickle():
    # Create a temporary pickle file with sample data
    sample_data = {
        'symbol2number': {'START': 256},
        'number2symbol': {256: 'START'},
        'states': [],
        'dfas': {},
        'labels': [(0, "EMPTY")],
        'keywords': {},
        'tokens': {},
        'symbol2label': {}
    }
    with open('temp_grammar.pkl', 'wb') as f:
        pickle.dump(sample_data, f)
    
    # Load the grammar tables from the temporary file
    grammar = Grammar()
    grammar.load(Path('temp_grammar.pkl'))
    
    assert grammar.symbol2number == {'START': 256}
    assert grammar.number2symbol == {256: 'START'}
    assert grammar.states == []
    assert grammar.dfas == {}
    assert grammar.labels == [(0, "EMPTY")]
    assert grammar.keywords == {}
    assert grammar.tokens == {}
    assert grammar.symbol2label == {}
    
    # Clean up the temporary file
    Path('temp_grammar.pkl').unlink()

# Test dumping the grammar tables to a pickle file
def test_dump_to_pickle():
    # Create an instance of Grammar with sample data
    grammar = Grammar()
    grammar.symbol2number = {'START': 256}
    grammar.number2symbol = {256: 'START'}
    grammar.states = []
    grammar.dfas = {}
    grammar.labels = [(0, "EMPTY")]
    grammar.keywords = {}
    grammar.tokens = {}
    grammar.symbol2label = {}
    
    # Dump the grammar tables to a temporary file
    grammar.dump(Path('temp_grammar.pkl'))
    
    # Load and check the contents of the temporary file
    with open('temp_grammar.pkl', 'rb') as f:
        loaded_data = pickle.load(f)
        

import pytest
from ansible.vars.manager import VarsWithSources

# Assuming _vars_sources is a global dictionary used in the function for tracking sources
_vars_sources = {}

def combine_vars(data, new_data):
    combined = data.copy()
    combined.update(new_data)
    return combined

def test_valid_input():
    data = {'a': 1, 'b': 2}
    new_data = {'b': 3, 'c': 4}
    source = 'example_source'
    
    result = _combine_and_track(data, new_data, source)
    
    assert result == {'a': 1, 'b': 3, 'c': 4}
    assert _vars_sources == {'b': 'example_source', 'c': 'example_source'}

def test_edge_case_none():
    data = None
    new_data = None
    source = None
    
    result = _combine_and_track(data, new_data, source)
    
    assert result == {}
    assert _vars_sources == {}

def test_invalid_input():
    with pytest.raises(TypeError):
        data = 'not a dict'
        new_data = 123
        source = 'invalid'
        
        _combine_and_track(data, new_data, source)

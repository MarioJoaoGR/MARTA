
import pytest
from ansible.utils.vars import merge_hash

def test_valid_inputs():
    x = {'a': 1, 'b': {'c': 2}}
    y = {'b': {'d': 3}, 'e': 4}
    result = merge_hash(x, y)
    assert result == {'a': 1, 'b': {'d': 3}, 'e': 4}

def test_edge_cases():
    x = {'a': [1, 2]}
    y = {'a': None, 'b': {'c': []}}
    with pytest.raises(TypeError):
        merge_hash(x, y)

def test_invalid_inputs():
    x = {}
    y = {}
    with pytest.raises(ValueError):
        merge_hash(x, y, list_merge='unknown_option')

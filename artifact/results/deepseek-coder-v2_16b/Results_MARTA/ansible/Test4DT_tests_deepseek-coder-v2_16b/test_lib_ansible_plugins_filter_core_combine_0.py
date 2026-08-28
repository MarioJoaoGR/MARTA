
import pytest
from ansible.plugins.filter.core import combine

def test_valid_inputs():
    dict1 = {'a': 1, 'b': [2]}
    dict2 = {'b': [3], 'c': 4}
    dict3 = {'d': 5}
    dict4 = {'e': 6}
    
    result = combine(dict1, dict2)
    assert result == {'a': 1, 'b': [3], 'c': 4}
    
    result_recursive = combine(dict1, dict2, recursive=True)
    assert result_recursive == {'a': 1, 'b': [2, 3], 'c': 4}
    
    result_list_combine = combine(dict1, dict2, list_merge='combine')
    assert result_list_combine == {'a': 1, 'b': [2, 3], 'c': 4}
    
    result_list_append = combine(dict1, dict2, list_merge='append')
    assert result_list_append == {'a': 1, 'b': [2, 3, 4], 'c': 4}

def test_edge_cases():
    dict1 = {}
    dict2 = {'a': None}
    dict3 = {'b': []}
    dict4 = {'c': 0}
    
    result = combine(dict1, dict2, dict3, dict4)
    assert result == {'a': None, 'b': [], 'c': 0}
    
    with pytest.raises(ValueError):
        combine(dict2, extra=1)

def test_invalid_inputs():
    dict1 = {}
    dict2 = {'a': 1, 'b': [2]}
    
    with pytest.raises(ValueError):
        combine(dict2, extra=1)

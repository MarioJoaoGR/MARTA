
import pytest
from copy import deepcopy
from ansible.module_utils.common.dict_transformations import dict_merge

# Test cases for dict_merge function
def test_dict_merge_non_dict():
    a = {'a': 1, 'b': {'c': 2}}
    b = {'b': "not a dictionary"}
    expected = {'a': 1, 'b': "not a dictionary"}
    assert dict_merge(a, b) == expected

def test_dict_merge_none():
    a = None
    b = {'a': 1}
    with pytest.raises(TypeError):
        dict_merge(a, b)

def test_dict_merge_empty():
    a = {}
    b = {'a': 1}
    expected = {'a': 1}
    assert dict_merge(a, b) == expected

def test_dict_merge_nested():
    a = {'a': 1, 'b': {'c': 2}}
    b = {'b': {'d': 3}, 'e': 4}
    expected = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4}
    assert dict_merge(a, b) == expected

def test_dict_merge_recursive():
    a = {'a': 1, 'b': {'c': 2}}
    b = {'b': {'d': 3, 'e': 5}, 'f': 6}
    expected = {'a': 1, 'b': {'c': 2, 'd': 3, 'e': 5}, 'f': 6}
    assert dict_merge(a, b) == expected

def test_dict_merge_overwrite():
    a = {'a': 1, 'b': {'c': 2}}
    b = {'b': {'c': 3, 'd': 4}, 'e': 5}
    expected = {'a': 1, 'b': {'c': 3, 'd': 4}, 'e': 5}
    assert dict_merge(a, b) == expected

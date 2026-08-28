
import pytest
from copy import deepcopy
from ansible.module_utils.common.dict_transformations import dict_merge

# Test cases for dict_merge function
def test_dict_merge_simple():
    a = {'a': 1, 'b': {'c': 2}}
    b = {'b': {'d': 3}, 'e': 4}
    expected = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4}
    assert dict_merge(a, b) == expected

def test_dict_merge_nested():
    a = {'a': 1, 'b': {'c': 2}}
    b = {'b': {'d': 3}, 'e': 4}
    expected = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4}
    assert dict_merge(a, b) == expected

def test_dict_merge_non_dict():
    a = {'a': 1, 'b': {'c': 2}}
    b = {'b': "not a dictionary"}
    expected = {'a': 1, 'b': "not a dictionary"}
    assert dict_merge(a, b) == expected

def test_dict_merge_empty():
    a = {}
    b = {'a': 1}
    expected = {'a': 1}
    assert dict_merge(a, b) == expected

def test_dict_merge_none():
    a = None
    b = {'a': 1}
    with pytest.raises(TypeError):
        dict_merge(a, b)

# Additional test cases to cover uncovered lines (116-121, 123-124)
def test_dict_merge_invalid_input():
    a = "not a dictionary"
    b = {'a': 1}
    with pytest.raises(TypeError):
        dict_merge(a, b)

def test_dict_merge_same_key_different_types():
    a = {'a': 1}
    b = {'a': {'b': 2}}
    expected = {'a': {'b': 2}}
    assert dict_merge(a, b) == expected

def test_dict_merge_multiple_nested_merges():
    a = {'a': 1, 'b': {'c': 2}}
    b = {'b': {'d': 3}, 'e': 4}
    c = {'f': 5}
    expected = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4, 'f': 5}
    assert dict_merge(dict_merge(a, b), c) == expected

def test_dict_merge_deepcopy():
    a = {'a': deepcopy({'b': 1})}
    b = {'a': {'c': 2}}
    expected = {'a': {'b': 1, 'c': 2}}
    assert dict_merge(a, b) == expected

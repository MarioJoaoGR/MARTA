
import pytest
from ansible.module_utils.common.dict_transformations import recursive_diff

def test_recursive_diff_basic():
    dict1 = {'a': 1, 'b': {'c': 2, 'd': 3}}
    dict2 = {'a': 1, 'b': {'c': 4, 'e': 5}}
    result = recursive_diff(dict1, dict2)
    assert result == ({'b': {'d': 3, 'c': 2}}, {'b': {'c': 4, 'e': 5}})

def test_recursive_diff_no_differences():
    dict1 = {'x': 10, 'y': 20}
    dict2 = {'x': 10, 'y': 20}
    result = recursive_diff(dict1, dict2)
    assert result is None

def test_recursive_diff_nested_structures():
    dict1 = {'a': 1, 'b': {'c': 2}}
    dict2 = {'a': 1, 'b': {'c': 3, 'd': 4}}
    result = recursive_diff(dict1, dict2)
    assert result == ({'b': {'c': 2}}, {'b': {'c': 3, 'd': 4}})

def test_recursive_diff_one_empty():
    dict1 = {}
    dict2 = {'a': 1, 'b': {'c': 3, 'd': 4}}
    result = recursive_diff(dict1, dict2)
    assert result == ({}, {'a': 1, 'b': {'c': 3, 'd': 4}})

def test_recursive_diff_both_empty():
    dict1 = {}
    dict2 = {}
    result = recursive_diff(dict1, dict2)
    assert result is None

def test_recursive_diff_different_data_types():
    dict1 = {'a': 1, 'b': [1, 2, 3]}
    dict2 = {'a': 1, 'b': [1, 4, 5]}
    result = recursive_diff(dict1, dict2)
    assert result == ({'b': [1, 2, 3]}, {'b': [1, 4, 5]})

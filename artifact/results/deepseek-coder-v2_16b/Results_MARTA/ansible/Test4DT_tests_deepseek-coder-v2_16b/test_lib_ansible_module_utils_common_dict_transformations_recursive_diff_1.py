
import pytest
from ansible.module_utils.common.dict_transformations import recursive_diff

# Scenario 1: Basic Usage
def test_basic_usage():
    dict1 = {'a': 1, 'b': {'c': 2, 'd': 3}}
    dict2 = {'a': 1, 'b': {'c': 4, 'e': 5}}
    result = recursive_diff(dict1, dict2)
    assert result == ({'b': {'d': 3, 'c': 2}}, {'b': {'c': 4, 'e': 5}})

# Scenario 2: No Differences
def test_no_differences():
    dict1 = {'x': 10, 'y': 20}
    dict2 = {'x': 10, 'y': 20}
    result = recursive_diff(dict1, dict2)
    assert result is None

# Scenario 3: Different Nested Structures
def test_different_nested_structures():
    dict1 = {'a': 1, 'b': {'c': 2}}
    dict2 = {'a': 1, 'b': {'c': 3, 'd': 4}}
    result = recursive_diff(dict1, dict2)
    assert result == ({'b': {'c': 2}}, {'b': {'c': 3, 'd': 4}})

# Scenario 4: One Dictionary is Empty
def test_one_dictionary_is_empty():
    dict1 = {}
    dict2 = {'a': 1, 'b': {'c': 3, 'd': 4}}
    result = recursive_diff(dict1, dict2)
    assert result == ({}, {'a': 1, 'b': {'c': 3, 'd': 4}})

# Scenario 5: Both Dictionaries are Empty
def test_both_dictionaries_are_empty():
    dict1 = {}
    dict2 = {}
    result = recursive_diff(dict1, dict2)
    assert result is None

# Scenario 6: Different Data Types
def test_different_data_types():
    dict1 = {'a': 1, 'b': [1, 2, 3]}
    dict2 = {'a': 1, 'b': [1, 4, 5]}
    result = recursive_diff(dict1, dict2)
    assert result == ({'b': [1, 2, 3]}, {'b': [1, 4, 5]})

# Module: ansible.module_utils.common.parameters
import pytest
from ansible.module_utils.common.parameters import sanitize_keys
from collections import deque
from typing import Union, Dict, List, Set, Tuple, MutableSequence, Mapping, MutableSet

# Helper function to simulate the behavior of _sanitize_keys_conditions and _remove_values_conditions
def _sanitize_keys_conditions(obj: Union[Dict, List, Set, Tuple], no_log_strings: set, ignore_keys: frozenset, deferred_removals: deque):
    if isinstance(obj, dict):
        new_dict = {}
        for key, value in obj.items():
            if key not in ignore_keys and any(no_log in key for no_log in no_log_strings):
                new_key = "********"  # Placeholder for sanitized keys
                deferred_removals.append(({key: value}, {new_key: value}))
                new_dict[new_key] = value
            else:
                new_dict[key] = value
        return new_dict
    elif isinstance(obj, (list, set)):
        new_container = type(obj)()  # Maintain the same type as obj (list or set)
        for item in obj:
            if isinstance(item, dict):
                sanitized_item = _sanitize_keys_conditions(item, no_log_strings, ignore_keys, deferred_removals)
                new_container.add(sanitized_item)
            else:
                new_container.add(item)
        return new_container
    elif isinstance(obj, tuple):
        new_tuple = []
        for item in obj:
            if isinstance(item, dict):
                sanitized_item = _sanitize_keys_conditions(item, no_log_strings, ignore_keys, deferred_removals)
                new_tuple.append(sanitized_item)
            else:
                new_tuple.append(item)
        return tuple(new_tuple)
    else:
        return obj

# Test cases for sanitize_keys function
def test_sanitize_keys_dictionary():
    my_dict = {'key1': 'value1', 'key2': 'sensitive info'}
    result = sanitize_keys(my_dict, no_log_strings={"info"})
    assert result == {'key1': 'value1', 'key2': '********'}

def test_sanitize_keys_list_of_dictionaries():
    my_list = [{"a": "sensitive info"}, {"b": "another sensitive"}]
    result = sanitize_keys(my_list, no_log_strings={"info", "another"})
    assert result == [{'a': '********'}, {'b': '********'}]

def test_sanitize_keys_set():
    my_set = {"sensitive info", "another sensitive"}
    result = sanitize_keys(my_set, no_log_strings={"info", "another"})
    assert set(result) == {'********', '********'}

def test_sanitize_keys_tuple_of_dictionaries():
    my_tuple = ({'a': 'sensitive info'}, {'b': 'another sensitive'})
    result = sanitize_keys(my_tuple, no_log_strings={"info", "another"})
    assert list(result) == [{'a': '********'}, {'b': '********'}]

def test_sanitize_keys_nested_structure():
    my_nested = {
        'outer_key1': 'value',
        'outer_key2': [
            {'inner_key1': 'sensitive info'},
            {'inner_key2': 'another sensitive'}
        ]
    }
    result = sanitize_keys(my_nested, no_log_strings={"info", "another"})
    assert result == {'outer_key1': 'value', 'outer_key2': [{'inner_key1': '********'}, {'inner_key2': '********'}]}

def test_sanitize_keys_with_specific_keys_to_ignore():
    my_dict = {'key1': 'value1', 'key2': 'sensitive info'}
    result = sanitize_keys(my_dict, no_log_strings={"info"}, ignore_keys={'key1'})
    assert result == {'key1': 'value1', 'key2': '********'}

# Add more test cases as needed to cover different scenarios and edge cases.

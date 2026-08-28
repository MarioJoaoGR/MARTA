
import pytest
from ansible.vars.clean import module_response_deepcopy
import copy
import six

# Test deep copying a dictionary
def test_module_response_deepcopy_dict():
    original_dict = {'key1': 'value1', 'key2': [1, 2, 3]}
    copied_dict = module_response_deepcopy(original_dict)
    assert copied_dict == original_dict
    assert copied_dict is not original_dict

# Test deep copying a list
def test_module_response_deepcopy_list():
    original_list = [{'subkey1': 'subvalue1'}, {'subkey2': 'subvalue2'}]
    copied_list = module_response_deepcopy(original_list)
    assert copied_list == original_list
    assert copied_list is not original_list

# Test handling of unsupported data types (should return the original value)
def test_module_response_deepcopy_unsupported():
    unsupported_value = set([1, 2, 3])
    result = module_response_deepcopy(unsupported_value)
    assert result == unsupported_value

# Test deep copying a dictionary with nested structures
def test_module_response_deepcopy_nested_dict():
    original_nested_dict = {'key1': 'value1', 'key2': {'subkey1': 'subvalue1'}}
    copied_nested_dict = module_response_deepcopy(original_nested_dict)
    assert copied_nested_dict == original_nested_dict
    assert copied_nested_dict is not original_nested_dict
    assert copied_nested_dict['key2'] is not original_nested_dict['key2']

# Test deep copying a list with nested structures
def test_module_response_deepcopy_nested_list():
    original_nested_list = [{'subkey1': 'subvalue1'}, {'subkey2': [1, 2, 3]}]
    copied_nested_list = module_response_deepcopy(original_nested_list)
    assert copied_nested_list == original_nested_list
    assert copied_nested_list is not original_nested_list
    assert copied_nested_list[1]['subkey2'] is not original_nested_list[1]['subkey2']

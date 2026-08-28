# Module: ansible.plugins.filter.core
import pytest
from collections import Mapping
from ansible.plugins.filter.core import dict_to_list_of_dict_key_value_elements
from ansible.errors import AnsibleFilterTypeError

# Test cases for dict_to_list_of_dict_key_value_elements function

def test_basic_usage():
    my_dict = {'a': 1, 'b': 2}
    result = dict_to_list_of_dict_key_value_elements(my_dict)
    assert result == [{'key': 'a', 'value': 1}, {'key': 'b', 'value': 2}]

def test_custom_key_names():
    my_dict = {'foo': 3, 'bar': 4}
    result = dict_to_list_of_dict_key_value_elements(my_dict, key_name='k', value_name='v')
    assert result == [{'k': 'foo', 'v': 3}, {'k': 'bar', 'v': 4}]

def test_empty_dictionary():
    my_dict = {}
    result = dict_to_list_of_dict_key_value_elements(my_dict)
    assert result == []

def test_non_dictionary_input():
    with pytest.raises(AnsibleFilterTypeError):
        non_dict_input = "not a dictionary"
        dict_to_list_of_dict_key_value_elements(non_dict_input)

# Module: httpie.utils
import pytest
from httpie.utils import repr_dict
from pprint import pformat

# Test cases for repr_dict function

def test_basic_usage():
    my_dict = {'key1': 'value1', 'key2': [1, 2, 3]}
    expected_output = pformat(my_dict)
    assert repr_dict(my_dict) == expected_output

def test_empty_dictionary():
    empty_dict = {}
    expected_output = pformat(empty_dict)
    assert repr_dict(empty_dict) == expected_output

def test_nested_structure():
    nested_dict = {'key1': 'value1', 'key2': {'innerKey': 'innerValue'}}
    expected_output = pformat(nested_dict)
    assert repr_dict(nested_dict) == expected_output

def test_special_characters():
    special_chars_dict = {'key!': 'value!', 'key@': [1, '@']}
    expected_output = pformat(special_chars_dict)
    assert repr_dict(special_chars_dict) == expected_output

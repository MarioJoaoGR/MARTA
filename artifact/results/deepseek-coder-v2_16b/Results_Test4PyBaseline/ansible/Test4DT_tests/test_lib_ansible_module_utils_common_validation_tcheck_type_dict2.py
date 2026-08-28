
import pytest
from ansible.module_utils.common.validation import check_type_dict
import json
from types import *

# Test cases for valid dictionary input (already covered)
def test_valid_dictionary():
    assert check_type_dict({'key1': 'value1', 'key2': 'value2'}) == {'key1': 'value1', 'key2': 'value2'}

# Test cases for JSON string input (already covered)
def test_json_string():
    json_str = '{"key1": "value1", "key2": "value2"}'
    assert check_type_dict(json_str) == {'key1': 'value1', 'key2': 'value2'}

# Test cases for key=value string without quotes (already covered)
def test_key_value_string():
    kv_str = 'key1=value1, key2=value2'
    assert check_type_dict(kv_str) == {'key1': 'value1', 'key2': 'value2'}

# Test cases for key=value string with single quotes and double quotes (already covered)
def test_quoted_key_value_string():
    kv_str = "key1='value1', key2=\"value2\""
    assert check_type_dict(kv_str) == {'key1': 'value1', 'key2': 'value2'}

# Test cases for invalid dictionary string to trigger a TypeError (already covered)
def test_invalid_dictionary_string():
    with pytest.raises(TypeError) as excinfo:
        check_type_dict("invalid dictionary string")
    assert str(excinfo.value) == "dictionary requested, could not parse JSON or key=value"

# Test cases for non-string and non-dictionary input to trigger a TypeError (already covered)
def test_non_string_and_non_dictionary():
    with pytest.raises(TypeError) as excinfo:
        check_type_dict(12345)

# New test cases for uncovered lines

# Test case for value being None, which should raise a TypeError
def test_none_input():
    with pytest.raises(TypeError):
        check_type_dict(None)

# Test case for value being a list, which should raise a TypeError
def test_list_input():
    with pytest.raises(TypeError):
        check_type_dict(['key1', 'value1'])

# Test case for value being an int, which should raise a TypeError
def test_int_input():
    with pytest.raises(TypeError):
        check_type_dict(12345)

# Test case for value being a float, which should raise a TypeError
def test_float_input():
    with pytest.raises(TypeError):
        check_type_dict(123.45)

# Test case for value being a bool, which should raise a TypeError
def test_bool_input():
    with pytest.raises(TypeError):
        check_type_dict(True)

# Test case for value being a set, which should raise a TypeError
def test_set_input():
    with pytest.raises(TypeError):
        check_type_dict({1, 2, 3})

# Test case for value being a tuple, which should raise a TypeError
def test_tuple_input():
    with pytest.raises(TypeError):
        check_type_dict(('key1', 'value1'))

# Test case for value being a complex number, which should raise a TypeError
def test_complex_input():
    with pytest.raises(TypeError):
        check_type_dict(1j)


import pytest
from ansible.module_utils.common.validation import check_type_dict
import json

def test_check_type_dict_with_none():
    value = None
    with pytest.raises(TypeError):
        check_type_dict(value)

def test_check_type_dict_with_empty_string():
    value = ''
    with pytest.raises(TypeError):
        check_type_dict(value)

def test_check_type_dict_with_malformed_json_string():
    json_str = '{"key1": "value1'  # Missing closing brace
    with pytest.raises(TypeError):
        check_type_dict(json_str)

def test_check_type_dict_with_valid_dict():
    value = {'key1': 'value1'}
    assert check_type_dict(value) == value

def test_check_type_dict_with_valid_json_string():
    json_str = '{"key1": "value1"}'
    expected_result = {"key1": "value1"}
    assert check_type_dict(json_str) == expected_result

def test_check_type_dict_with_valid_key_value_string():
    key_value_str = 'key1=value1, key2=value2'
    expected_result = {'key1': 'value1', 'key2': 'value2'}
    assert check_type_dict(key_value_str) == expected_result

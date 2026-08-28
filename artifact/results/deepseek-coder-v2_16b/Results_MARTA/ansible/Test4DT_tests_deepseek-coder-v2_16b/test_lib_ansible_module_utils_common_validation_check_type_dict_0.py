
import pytest
from ansible.module_utils.common.validation import check_type_dict
import json

def test_valid_dictionary():
    value = {'key1': 'value1'}
    result = check_type_dict(value)
    assert isinstance(result, dict), "Expected a dictionary but got {}".format(type(result))

def test_valid_json_string():
    value = '{"key1": "value1"}'
    result = check_type_dict(value)
    assert isinstance(result, dict), "Expected a dictionary but got {}".format(type(result))
    assert result == {'key1': 'value1'}, "Expected dictionary content does not match the actual content."

def test_valid_key_value_string():
    value = 'key1=value1, key2=value2'
    result = check_type_dict(value)
    assert isinstance(result, dict), "Expected a dictionary but got {}".format(type(result))
    assert result == {'key1': 'value1', 'key2': 'value2'}, "Expected dictionary content does not match the actual content."

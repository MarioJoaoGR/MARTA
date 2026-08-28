
import pytest
from datetime import datetime
from collections import deque
from ansible.module_utils.common.parameters import remove_values, to_native

# Test scenarios
def test_valid_input_string():
    result = remove_values("hello world", {"world"})
    assert result == 'hello *'

def test_valid_input_dict():
    result = remove_values({"username": "admin", "password": "secret"}, {"admin", "secret"})
    assert result == {'username': '*', 'password': '*'}

def test_valid_input_list():
    result = remove_values([1, 2, 3], {2})
    assert result == [1, 3]

def test_valid_input_datetime():
    now = datetime.now()
    result = remove_values(now, {"datetime"})
    # Assuming the datetime object is converted to a string representation in ISO format
    assert isinstance(result, str) and len(result) > 0

def test_valid_input_nested_dict():
    data = {"level1": {"level2": {"sensitive_key": "sensitive_value"}}}
    result = remove_values(data, {"sensitive_value"})
    assert result == {'level1': {'level2': {}}}

def test_edge_case_none():
    result = remove_values(None, set())
    assert result is None

def test_edge_case_empty_list():
    result = remove_values([], {'item'})
    assert isinstance(result, list) and len(result) == 0

def test_error_handling_invalid_type():
    with pytest.raises(TypeError):
        remove_values([1, 'string', None], {None})

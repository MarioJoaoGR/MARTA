
import json
from unittest import TestCase, mock
import pytest
from typing import Union, Any

def json_decode(value: Union[str, bytes]) -> Any:
    """Returns Python objects for the given JSON string.

    Supports both `str` and `bytes` inputs.
    """
    return json.loads(to_basestring(value))

# Helper function to convert bytes to a basestring (either str or bytes)
def to_basestring(value: Union[str, bytes]) -> Union[str, bytes]:
    if isinstance(value, bytes):
        return value.decode('utf-8')
    return value

# Test cases
def test_valid_input_string():
    with mock.patch('json.loads', return_value={'key': 'value'}):
        result = json_decode('{"key": "value"}')
        assert result == {'key': 'value'}

def test_valid_input_bytes():
    byte_data = b'{"key": "value"}'
    with mock.patch('json.loads', return_value={'key': 'value'}):
        result = json_decode(byte_data)
        assert result == {'key': 'value'}

def test_invalid_input():
    byte_data = b'{"key": "value'  # Invalid JSON string
    with pytest.raises(json.JSONDecodeError):
        json_decode(byte_data)

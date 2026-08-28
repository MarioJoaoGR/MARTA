
import pytest
import json
from typing import Union, Any

def json_decode(value: Union[str, bytes]) -> Any:
    """Returns Python objects for the given JSON string.

    Supports both `str` and `bytes` inputs.
    """
    return json.loads(to_basestring(value))

# Helper function to convert bytes to a basestring (for compatibility with Python 2)
def to_basestring(value: Union[str, bytes]) -> str:
    if isinstance(value, bytes):
        return value.decode('utf-8')
    return value

@pytest.fixture
def valid_json_string():
    return '{"key": "value"}'

@pytest.fixture
def valid_json_bytes():
    return b'{"key": "value"}'

@pytest.fixture
def invalid_input():
    return 'not a JSON'

# Test for valid JSON string input
def test_valid_json_string(valid_json_string):
    result = json_decode(valid_json_string)
    assert result == {"key": "value"}

# Test for valid JSON bytes input
def test_valid_json_bytes(valid_json_bytes):
    result = json_decode(valid_json_bytes)
    assert result == {"key": "value"}

# Test handling invalid input (non-JSON string)
def test_invalid_input(invalid_input):
    with pytest.raises(json.JSONDecodeError):
        json_decode(invalid_input)

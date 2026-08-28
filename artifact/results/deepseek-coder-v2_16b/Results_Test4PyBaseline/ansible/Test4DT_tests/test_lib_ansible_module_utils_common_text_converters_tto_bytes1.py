
import pytest
from ansible.module_utils.common.text.converters import to_bytes

# Test cases for basic usage with UTF-8 encoding
def test_to_bytes_basic():
    result = to_bytes("Hello, World!")
    assert isinstance(result, bytes)
    assert result == b'Hello, World!'

# Test cases for handling errors with surrogate escape
def test_to_bytes_errors_surrogate_or_strict():
    result = to_bytes("Hello, World!", errors='surrogate_or_strict')
    if hasattr(result, 'decode'):  # Python 3
        assert isinstance(result, bytes)
        assert result == b'Hello, World!'
    else:  # Python 2
        assert isinstance(result, str)
        assert result == "Hello, World!"

# Test cases for using different nonstring strategies
def test_to_bytes_nonstring_simplerepr():
    result = to_bytes("Hello", nonstring='simplerepr')
    assert isinstance(result, bytes)
    assert result == b'Hello'

def test_to_bytes_nonstring_empty():
    result = to_bytes("", nonstring='empty')
    assert isinstance(result, bytes)
    assert result == b''

# Test cases for handling byte strings directly
def test_to_bytes_byte_string():
    input_str = b'Hello, World!'
    result = to_bytes(input_str)
    assert isinstance(result, bytes)
    assert result == b'Hello, World!'

# Test cases for handling non-string objects with different strategies
def test_to_bytes_nonstring_passthru():
    input_obj = "Hello"
    result = to_bytes(input_obj, nonstring='passthru')
    assert isinstance(result, bytes)
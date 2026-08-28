
import pytest
from ansible.module_utils.common.text.converters import to_bytes

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

# Test cases for handling text strings with different encodings
def test_to_bytes_different_encoding():
    input_str = "Hello, World!".encode('latin-1')
    result = to_bytes(input_str, encoding='latin-1')
    assert isinstance(result, bytes)
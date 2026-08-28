
import pytest
from tornado import escape

def utf8(value):
    if isinstance(value, str):
        return value.encode('utf-8')
    elif isinstance(value, bytes):
        return value
    elif value is None:
        return None
    else:
        raise TypeError("Expected bytes, unicode, or None; got %s" % type(value).__name__)

# Test cases for utf8 function
def test_valid_utf8_string():
    value = 'Hello'
    result = utf8(value)
    assert isinstance(result, bytes), f"Expected bytes but got {type(result)}"

def test_existing_bytes():
    value = b'World'
    result = utf8(value)
    assert isinstance(result, bytes), f"Expected bytes but got {type(result)}"

def test_invalid_input():
    with pytest.raises(TypeError):
        value = 12345
        utf8(value)

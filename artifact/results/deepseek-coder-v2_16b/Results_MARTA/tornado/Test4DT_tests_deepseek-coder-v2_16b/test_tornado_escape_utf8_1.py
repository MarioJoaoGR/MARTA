
import pytest
from tornado.escape import utf8

def test_valid_utf8_string():
    value = 'Hello'
    result = utf8(value)
    assert isinstance(result, bytes), "Expected a byte string"

def test_existing_bytes():
    value = b'World'
    result = utf8(value)
    assert result is value, "Expected the same input if it is already in bytes"

def test_invalid_input_type():
    with pytest.raises(TypeError):
        value = 12345
        utf8(value)

# Module: tornado.escape
import pytest
from typing import Optional, Union
from tornado.escape import utf8  # Assuming the module is correctly imported as in the provided documentation

# Test cases for utf8 function
def test_utf8_none():
    result = utf8(None)
    assert result is None

def test_utf8_unicode_string():
    value = "Hello"
    expected_output = b'Hello'
    result = utf8(value)
    assert result == expected_output

def test_utf8_byte_string():
    value = b"Hello"
    expected_output = b'Hello'
    result = utf8(value)
    assert result == expected_output

def test_utf8_unsupported_type():
    with pytest.raises(TypeError) as excinfo:
        utf8(123)
    assert str(excinfo.value) == "Expected bytes, unicode, or None; got <class 'int'>"

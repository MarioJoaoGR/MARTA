
import pytest
from tornado import escape

def test_valid_byte_string():
    value = b"Hello"
    result = escape.to_unicode(value)
    assert isinstance(result, str), f"Expected a string but got {type(result)}"


def test_invalid_input():
    value = 12345
    with pytest.raises(TypeError):
        escape.to_unicode(value)
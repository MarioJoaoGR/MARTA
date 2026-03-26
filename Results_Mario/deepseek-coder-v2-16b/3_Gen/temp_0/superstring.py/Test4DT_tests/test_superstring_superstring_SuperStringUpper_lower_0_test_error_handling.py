
import pytest
from superstring.superstring import SuperStringUpper

def test_error_handling():
    try:
        str_upper = SuperStringUpper(123)
    except Exception as e:
        assert isinstance(e, TypeError), "Expected a TypeError but got a different exception"

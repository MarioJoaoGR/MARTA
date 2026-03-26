
import pytest
from typing import Any

def is_string(obj: Any) -> bool:
    """
    Checks if an object is a string.

    *Example:*

    >>> is_string('foo') # returns true
    >>> is_string(b'foo') # returns false

    :param obj: Object to test.
    :return: True if string, false otherwise.
    """
    return isinstance(obj, str)

def test_valid_string():
    assert is_string('foo') == True
    assert is_string("bar") == True
    assert is_string("") == True
    assert is_string("123") == True
    assert is_string(b'foo') == False
    assert is_string(123) == False
    assert is_string([1, 2, 3]) == False
    assert is_string({'key': 'value'}) == False

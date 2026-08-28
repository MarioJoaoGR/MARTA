
import pytest
from string_utils.validation import is_full_string

def is_isogram(input_string: str) -> bool:
    """
    Checks if the string is an isogram (https://en.wikipedia.org/wiki/Isogram).

    *Examples:*

    >>> is_isogram('dermatoglyphics') # returns true
    >>> is_isogram('hello') # returns false

    :param input_string: String to check.
    :type input_string: str
    :return: True if isogram, false otherwise.
    """
    return is_full_string(input_string) and len(set(input_string.lower())) == len(input_string)

def test_is_isogram_basic():
    assert is_isogram('dermatoglyphics') == True
    assert is_isogram('hello') == False
    assert is_isogram('') == False
    assert is_isogram(' ') == False

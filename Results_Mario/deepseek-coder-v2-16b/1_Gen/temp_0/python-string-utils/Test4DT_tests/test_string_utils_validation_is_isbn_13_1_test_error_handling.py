
import re
import pytest
from string_utils.validation import __ISBNChecker

def is_isbn_13(input_string: str, normalize: bool = True) -> bool:
    """
    Checks if the given string represents a valid ISBN 13 (International Standard Book Number).
    By default hyphens in the string are ignored, so digits can be separated in different ways, by calling this
    function with `normalize=False` only digit-only strings will pass the validation.

    *Examples:*

    >>> is_isbn_13('9780312498580') # returns true
    >>> is_isbn_13('978-0312498580') # returns true
    >>> is_isbn_13('978-0312498580', normalize=False) # returns false

    :param input_string: String to check.
    :param normalize: True to ignore hyphens ("-") in the string (default), false otherwise.
    :return: True if valid ISBN 13, false otherwise.
    """
    checker = __ISBNChecker(input_string, normalize)
    return checker.is_isbn_13()

def test_error_handling():
    # Test for None input
    with pytest.raises(TypeError):
        is_isbn_13(None)
    
    # Test for empty string
    assert not is_isbn_13("")


import pytest
from string_utils.validation import is_full_string

def is_pangram(input_string: str) -> bool:
    """
    Checks if the string is a pangram (https://en.wikipedia.org/wiki/Pangram).

    *Examples:*

    >>> is_pangram('The quick brown fox jumps over the lazy dog') # returns true
    >>> is_pangram('hello world') # returns false

    :param input_string: String to check.
    :type input_string: str
    :return: True if the string is a pangram, False otherwise.
    """
    if not is_full_string(input_string):
        return False

    import string
    from re import sub as SPACES_RE
    
    cleaned_string = SPACES_RE('', '', input_string).lower()
    return set(cleaned_string).issuperset(set(string.ascii_lowercase))

def test_empty_string():
    assert not is_pangram('')

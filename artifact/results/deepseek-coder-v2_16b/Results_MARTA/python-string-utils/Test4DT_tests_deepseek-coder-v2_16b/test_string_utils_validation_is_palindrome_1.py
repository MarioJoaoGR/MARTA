
import pytest
from string_utils.validation import is_palindrome

def is_full_string(input_string: str) -> bool:
    return isinstance(input_string, str) and len(input_string.strip()) > 0

# Test for None input

# Test for non-string input

# Test for palindrome string without ignoring case or spaces
def test_simple_palindrome():
    assert is_palindrome('LOL') == True

# Test for non-palindrome string
def test_non_palindrome():
    assert is_palindrome('ROTFL') == False

# Test for palindrome with case differences, ignoring case
def test_case_insensitive_palindrome():
    assert is_palindrome('Lol', ignore_case=True) == True

# Test for palindrome string with spaces, ignoring spaces
def test_ignore_spaces_palindrome():
    assert is_palindrome('i topi non avevano nipoti', ignore_spaces=True) == True
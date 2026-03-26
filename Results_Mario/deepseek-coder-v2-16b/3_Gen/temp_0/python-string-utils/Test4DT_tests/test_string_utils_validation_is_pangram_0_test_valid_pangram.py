
import pytest
from string_utils.validation import is_full_string, SPACES_RE  # Assuming this module exists and has these items
import string

def is_pangram(input_string: str) -> bool:
    if not is_full_string(input_string):
        return False

    return set(SPACES_RE.sub('', input_string)).issuperset(set(string.ascii_lowercase))

def test_valid_pangram():
    # Test a pangram string
    assert is_pangram('The quick brown fox jumps over the lazy dog') == True
    
    # Test a non-pangram string
    assert is_pangram('hello world') == False


import pytest
from string_utils.validation import is_full_string

def test_valid_input():
    # Test with a non-empty string containing at least one non-space character
    assert is_full_string('hello') == True
    
    # Test with an empty string
    assert is_full_string('') == False
    
    # Test with a string that consists only of whitespace characters
    assert is_full_string(' ') == False
    
    # Test with None, which should return False as per the function's logic
    assert is_full_string(None) == False

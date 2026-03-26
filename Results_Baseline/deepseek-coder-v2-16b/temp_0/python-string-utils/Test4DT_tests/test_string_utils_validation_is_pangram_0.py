# Module: string_utils.validation
# test_string_utils.py
from string_utils.validation import is_pangram
import re
import string

def test_is_pangram():
    # Test a pangram string
    assert is_pangram('The quick brown fox jumps over the lazy dog') == True, "Expected True for a pangram"
    
    # Test not a pangram string
    assert is_pangram('hello world') == False, "Expected False for a non-pangram"
    
    # Test empty string
    assert is_pangram('') == False, "Expected False for an empty string"
    
    # Test string with numbers and special characters (should still be considered a pangram)
    assert is_pangram('The quick brown fox jumps over the lazy dog123!@#') == True, "Expected True for a string containing all letters of the alphabet at least once"

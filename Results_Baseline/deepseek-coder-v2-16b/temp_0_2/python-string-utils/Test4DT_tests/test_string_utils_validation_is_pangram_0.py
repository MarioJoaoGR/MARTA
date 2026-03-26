
# Module: string_utils.validation
# test_string_utils.py
from string_utils.validation import is_pangram
import string

def test_is_pangram():
    # Test a pangram
    assert is_pangram('The quick brown fox jumps over the lazy dog') == True, "Expected True for a pangram"
    
    # Test not a pangram
    assert is_pangram('hello world') == False, "Expected False for not a pangram"
    
    # Test edge case: empty string
    assert is_pangram('') == False, "Expected False for an empty string"
    
    # Test case insensitivity
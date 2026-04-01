
import re
from string_utils.validation import is_full_string

def test_valid_input():
    # Test None input
    assert not is_full_string(None)
    
    # Test empty string
    assert not is_full_string('')
    
    # Test string with only whitespace characters
    assert not is_full_string('     ')
    
    # Test valid non-empty string
    assert is_full_string('hello')

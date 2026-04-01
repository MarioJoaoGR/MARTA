
import pytest
from string_utils.validation import is_full_string

def test_empty_input():
    # Test when input is None
    assert not is_full_string(None)
    
    # Test when input is an empty string
    assert not is_full_string('')
    
    # Test when input consists only of whitespace characters
    assert not is_full_string(' ')
    
    # Test when input contains at least one non-space character
    assert is_full_string('hello')


import pytest
from string_utils.validation import is_full_string

def test_is_full_string():
    # Test None input
    assert not is_full_string(None)
    
    # Test empty string
    assert not is_full_string('')
    
    # Test whitespace-only string
    assert not is_full_string(' ')
    assert not is_full_string('   ')
    
    # Test non-empty string
    assert is_full_string('hello')
    assert is_full_string(' hello ')

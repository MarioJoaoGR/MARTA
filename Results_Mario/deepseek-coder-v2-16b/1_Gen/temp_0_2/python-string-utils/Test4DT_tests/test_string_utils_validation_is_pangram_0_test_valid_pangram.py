
import pytest
from string_utils.validation import is_pangram

def test_valid_pangram():
    # Test a valid pangram
    assert is_pangram('The quick brown fox jumps over the lazy dog') == True
    
    # Test a non-pangram sentence
    assert is_pangram('hello world') == False

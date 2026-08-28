
import pytest
from unittest.mock import patch
from string_utils.validation import is_isbn_13

# Test valid ISBN-13 numbers with normalization enabled and disabled
def test_valid_isbn_13():
    # Valid normalized ISBN-13 number
    assert is_isbn_13('9780312498580') == True
    
    # Valid non-normalized ISBN-13 number, normalization enabled by default
    assert is_isbn_13('978-0312498580') == True
    
    # Valid non-normalized ISBN-13 number, normalization explicitly set to False
    assert is_isbn_13('978-0312498580', normalize=False) == False

# Test invalid ISBN-13 numbers
def test_invalid_isbn_13():
    # Invalid ISBN number, normalization does not affect the result as it is a different format
    assert is_isbn_13('978045145052') == False

# Test edge cases including None, empty strings, and non-string inputs
def test_edge_cases():
    # None input should return False
    with pytest.raises(TypeError):
        is_isbn_13(None)
    
    # Empty string should return False
    assert is_isbn_13('') == False
    
    # Non-string input should raise a TypeError
    with pytest.raises(TypeError):
        is_isbn_13(12345)

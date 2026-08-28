
import pytest
from string_utils.manipulation import roman_encode

def test_roman_encode_with_integer():
    """Test that `roman_encode` correctly encodes an integer."""
    assert roman_encode(37) == 'XXXVII'

def test_roman_encode_with_string():
    """Test that `roman_encode` correctly encodes a string representation of an integer."""
    assert roman_encode('2020') == 'MMXX'

def test_roman_encode_with_max_value():
    """Test that `roman_encode` correctly encodes the maximum allowed value (3999)."""
    assert roman_encode(3999) == 'MMMCMXCIX'

def test_roman_encode_invalid_input():
    """Test that `roman_encode` raises an error for invalid input."""
    with pytest.raises(ValueError):
        roman_encode(-1)  # Negative numbers are not valid inputs

def test_roman_encode_non_integer_string():
    """Test that `roman_encode` raises an error for non-integer string representations."""
    with pytest.raises(ValueError):
        roman_encode('abc')  # Non-numeric strings are not valid inputs

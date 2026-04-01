
import re
from string_utils.validation import is_decimal

def test_invalid_inputs():
    # Test cases for invalid inputs
    assert not is_decimal('abc')  # Invalid input should return False
    assert not is_decimal('123abc')  # Invalid input should return False
    assert not is_decimal('12.')  # Invalid input should return False
    assert not is_decimal('.')  # Invalid input should return False
    assert not is_decimal('E-4')  # Invalid input should return False
    assert not is_decimal('-E+4')  # Invalid input should return False
    assert not is_decimal('1.23E')  # Invalid input should return False
    assert not is_decimal('1..23')  # Invalid input should return False
    
    # Test cases for valid inputs
    assert is_decimal('42.0')  # Valid decimal number should return True
    assert not is_decimal('42')  # Integer should return False


import pytest
from isort._vendored.tomli._parser import is_unicode_scalar_value

def test_valid_input_happy_path():
    # Test cases for valid Unicode scalar values
    assert is_unicode_scalar_value(65)  # ASCII 'A'
    assert is_unicode_scalar_value(1048575)  # U+FFFFF
    
    # Negative value should return False
    assert not is_unicode_scalar_value(-5)
    
    # Out of range values should return False
    assert not is_unicode_scalar_value(1114112)  # U+10FFFF + 1

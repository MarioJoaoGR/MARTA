
import pytest
from isort._vendored.tomli._parser import is_unicode_scalar_value

def test_valid_case_high_boundary():
    # Test a valid Unicode scalar value within the range of U+0000 to U+D7FF, inclusive
    assert is_unicode_scalar_value(55295) == True
    
    # Test another valid Unicode scalar value within the range of U+E000 to U+10FFFF, inclusive
    assert is_unicode_scalar_value(1114111) == True
    
    # Test an invalid Unicode scalar value outside the ranges
    assert is_unicode_scalar_value(55296) == False
    assert is_unicode_scalar_value(1114112) == False


import pytest
from your_module import is_unicode_scalar_value  # Replace 'your_module' with the actual module name where the function is defined.

def test_valid_input_happy_path():
    # Test cases for valid Unicode scalar values within the specified ranges
    assert is_unicode_scalar_value(65) == True  # ASCII 'A'
    assert is_unicode_scalar_value(1048575) == True  # U+FFFFF
    assert is_unicode_scalar_value(55296) == True  # First valid Unicode scalar value in the high range
    assert is_unicode_scalar_value(1114111) == True  # Last valid Unicode scalar value in the high range
    
    # Test cases for invalid Unicode scalar values outside the specified ranges
    assert is_unicode_scalar_value(-5) == False  # Negative value
    assert is_unicode_scalar_value(1114112) == False  # Out of range (U+10FFFF + 1)
    assert is_unicode_scalar_value(110592) == False  # Invalid high surrogate range

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_is_unicode_scalar_value_0_test_valid_input_happy_path
isort/Test4DT_tests/test_isort__vendored_tomli__parser_is_unicode_scalar_value_0_test_valid_input_happy_path.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""
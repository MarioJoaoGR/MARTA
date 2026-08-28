
# Module: string_utils.validation
import pytest
from string_utils.validation import is_number

# Test cases for valid numbers
def test_valid_positive_integer():
    assert is_number('42') == True

def test_valid_negative_decimal():
    assert is_number('-9.12') == True

def test_valid_scientific_notation():
    assert is_number('1e3') == True

# Test cases for invalid inputs that are not numbers
def test_invalid_string():
    assert is_number('1 2 3') == False

def test_non_string_input():
    with pytest.raises(TypeError):  # Corrected the error type to match the function's expected exception
        is_number(42)

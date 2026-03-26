# Module: string_utils.validation
import pytest
from string_utils.validation import is_number

# Test cases for the is_number function
def test_valid_integer():
    assert is_number('42') == True

def test_valid_float():
    assert is_number('19.99') == True

def test_signed_number():
    assert is_number('-9.12') == True

def test_scientific_notation():
    assert is_number('1e3') == True

def test_invalid_string():
    assert is_number('1 2 3') == False

# Additional test case for non-string input type
def test_non_string_input():
    with pytest.raises(TypeError):
        is_number(42)

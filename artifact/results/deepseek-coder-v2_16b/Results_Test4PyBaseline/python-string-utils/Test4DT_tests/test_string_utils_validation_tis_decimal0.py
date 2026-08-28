# Module: string_utils.validation
import pytest
from string_utils.validation import is_decimal

# Test cases for the `is_decimal` function
def test_valid_decimal():
    assert is_decimal('42.0') == True, "Expected '42.0' to be recognized as a decimal number."

def test_integer():
    assert is_decimal('42') == False, "Expected '42' to not be recognized as a decimal number."

def test_signed_decimal():
    assert is_decimal('-19.99') == True, "Expected '-19.99' to be recognized as a decimal number."

def test_scientific_notation():
    assert is_decimal('+3.14e2') == True, "Expected '+3.14e2' to be recognized as a decimal number using scientific notation."

def test_invalid_string():
    assert is_decimal('abc') == False, "Expected 'abc' to not be recognized as a decimal number."

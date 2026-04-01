
import pytest
from string_utils import validation  # Assuming this module contains is_decimal and possibly is_number

def test_valid_decimals():
    assert validation.is_decimal('42.0') == True
    assert validation.is_decimal('-123.45e6') == True
    assert validation.is_decimal('+78.9') == True

def test_invalid_decimals():
    assert validation.is_decimal('abc') == False
    assert validation.is_decimal('123') == False

# Additional tests for edge cases can be added here

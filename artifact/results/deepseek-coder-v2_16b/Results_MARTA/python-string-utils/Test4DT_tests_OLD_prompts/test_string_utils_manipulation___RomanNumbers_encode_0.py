
import pytest
from unittest.mock import patch
from string_utils.manipulation import __RomanNumbers

# Test encoding a valid integer input

# Test encoding an invalid integer input (outside the range 1 to 3999)
def test_encode_invalid_integer_input():
    with pytest.raises(ValueError):
        __RomanNumbers.encode(input_number=4000)

# Test encoding a valid string input
def test_encode_valid_string_input():
    assert __RomanNumbers.encode(input_number='3') == 'III'
    assert __RomanNumbers.encode(input_number='42') == 'XLII'
    assert __RomanNumbers.encode(input_number='1987') == 'MCMLXXXVII'

# Test encoding an invalid string input (not a valid integer)
def test_encode_invalid_string_input():
    with pytest.raises(ValueError):
        __RomanNumbers.encode(input_number='invalid')
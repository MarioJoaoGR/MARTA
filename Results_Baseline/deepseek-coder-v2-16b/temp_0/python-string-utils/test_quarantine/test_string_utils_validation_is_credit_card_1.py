
import re
import pytest
from unittest.mock import patch

# Existing definitions
def is_credit_card(number):
    def is_full_string(input_str):
        return len(input_str.strip()) == 16 or len(input_str.strip()) == 15
    if not is_full_string(number):
        return False
    number = number.replace(" ", "")
    if re.match(r'^[4,5]\d{3}(-?\d{4}){2}$', number) and len(number) in [16, 19]:
        return True
    if re.match(r'^\d{13}$', number):
        return True
    return False

# Test cases
def test_valid_credit_card():
    assert is_credit_card('4111 1111 1111 1111') == True  # Valid Visa card
    assert is_credit_card('5555 5555 5555 4444') == True  # Valid MasterCard card

def test_invalid_full_string():
    """Test when input string is not a full string."""
    assert is_credit_card('1234 5678 9012 34') == False

def test_invalid_card_type():
    """Test when an invalid card type is provided."""
    with pytest.raises(KeyError):
        is_credit_card('1234 5678 9012 34', 'INVALID')

def test_valid_american_express():
    """Test a valid American Express credit card number."""
    assert is_credit_card('3782 822463 10005') == True

def test_invalid_visa():
    """Test an invalid Visa credit card number."""
    assert is_credit_card('4012 8888 8888 1881') == False

def test_valid_mastercard():
    """Test a valid MasterCard credit card number."""
    assert is_credit_card('5105 1051 0510 5100') == True

def test_invalid_mastercard():
    """Test an invalid MasterCard credit card number."""
    assert is_credit_card('5205 1051 0510 5100') == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_credit_card_1
python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_1.py:31:8: E1121: Too many positional arguments for function call (too-many-function-args)

"""
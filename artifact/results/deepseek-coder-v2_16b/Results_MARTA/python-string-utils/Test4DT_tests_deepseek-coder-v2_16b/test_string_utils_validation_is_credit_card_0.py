
import pytest
from string_utils.validation import is_credit_card




def test_invalid_amex_card():
    input_string = '3782 822463 10006'  # Invalid American Express card number
    assert is_credit_card(input_string) == False, f"Expected {input_string} to be an invalid American Express card number."

def test_invalid_mastercard():
    input_string = '5555 5555 5555 4444'  # Invalid MasterCard card number
    assert is_credit_card(input_string) == False, f"Expected {input_string} to be an invalid MasterCard card number."
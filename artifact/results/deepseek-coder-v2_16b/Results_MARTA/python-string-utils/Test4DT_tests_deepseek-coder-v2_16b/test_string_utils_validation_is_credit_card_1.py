
import pytest
from string_utils.validation import is_credit_card




def test_invalid_credit_card():
    input_string = '1234-5678-9012-3456'
    assert is_credit_card(input_string) == False, "Expected an invalid card format to return False"

def test_empty_credit_card():
    input_string = ''
    assert is_credit_card(input_string) == False, "Expected an empty string to return False"
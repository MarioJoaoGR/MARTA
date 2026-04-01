
import re
import pytest
from string_utils.validation import is_credit_card, CREDIT_CARDS

def test_invalid_credit_card():
    input_string = '1234567890123456'
    assert not is_credit_card(input_string), "Expected False for an invalid credit card number"

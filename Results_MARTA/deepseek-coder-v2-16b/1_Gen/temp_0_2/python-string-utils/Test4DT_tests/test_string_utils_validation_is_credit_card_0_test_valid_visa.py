
import re
import pytest
from string_utils.validation import is_credit_card, CREDIT_CARDS

def test_valid_visa():
    input_string = '4532790782910562'
    assert is_credit_card(input_string) == True

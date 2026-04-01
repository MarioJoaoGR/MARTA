
from string_utils.validation import is_credit_card
import re

def test_empty_string():
    assert not is_credit_card("")  # Test an empty string

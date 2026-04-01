
import re
import pytest
from string_utils.validation import is_email

def test_invalid_multiple_at_signs():
    input_string = '@gmail.com'
    assert not is_email(input_string), f"Expected False for input '{input_string}', but got True"

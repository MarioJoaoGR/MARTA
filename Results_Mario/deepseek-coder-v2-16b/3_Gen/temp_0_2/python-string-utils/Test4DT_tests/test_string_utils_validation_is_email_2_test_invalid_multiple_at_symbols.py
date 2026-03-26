
import re
import pytest
from string_utils.validation import is_email, EMAIL_RE, ESCAPED_AT_SIGN

def test_invalid_multiple_at_symbols():
    input_string = 'multiple@@example.com'
    assert not is_email(input_string), "Expected False for invalid email with multiple '@' symbols"

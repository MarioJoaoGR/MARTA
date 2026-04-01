
import re
import pytest
from string_utils.validation import is_email, EMAIL_RE, ESCAPED_AT_SIGN

def test_invalid_start_with_dot():
    input_string = '.invalid@example.com'
    assert not is_email(input_string)

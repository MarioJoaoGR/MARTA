
import re
import pytest
from string_utils.validation import is_email, EMAIL_RE, ESCAPED_AT_SIGN

def test_invalid_length_head():
    input_string = 'a' * 65 + '@gmail.com'
    assert not is_email(input_string), "Expected False for too long head part"

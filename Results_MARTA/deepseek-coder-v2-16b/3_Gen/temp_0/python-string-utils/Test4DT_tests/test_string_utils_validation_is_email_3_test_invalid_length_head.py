
import re
import pytest
from string_utils.validation import is_email, EMAIL_RE, ESCAPED_AT_SIGN

def test_invalid_length_head():
    # Test an invalid email due to too long a head part
    assert not is_email('a' * 65 + '@gmail.com')

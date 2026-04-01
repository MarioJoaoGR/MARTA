
import re
import pytest
from string_utils.validation import is_email, EMAIL_RE, ESCAPED_AT_SIGN

def test_invalid_multiple_at_signs():
    # Test case for an invalid email due to multiple "@" signs
    assert not is_email('@gmail.com')


import re
import pytest
from string_utils.validation import is_email, EMAIL_RE, ESCAPED_AT_SIGN

def test_invalid_starts_with_dot():
    assert not is_email('.invalid@example.com')

# Additional tests for edge cases and valid emails can be added here

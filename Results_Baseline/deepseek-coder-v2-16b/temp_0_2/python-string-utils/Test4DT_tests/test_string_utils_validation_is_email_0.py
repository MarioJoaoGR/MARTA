
import pytest
from string_utils.validation import is_email

# Test cases for valid emails
def test_valid_emails():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('user+mailbox@example.co.in') == True  # Example from RFC 3696
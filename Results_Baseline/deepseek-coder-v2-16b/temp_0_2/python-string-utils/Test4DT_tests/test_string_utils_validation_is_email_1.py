
import pytest
from string_utils.validation import is_email
import re

# Define a regex pattern for email validation (assuming this is defined somewhere in the module)
EMAIL_RE = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

# Test cases for valid emails (existing test case is sufficient, so no new test case here)
def test_valid_emails():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('user+mailbox@example.co.in') == True  # Example from RFC 3696

# Test cases for invalid emails based on the uncovered lines
def test_invalid_emails():
    # Line 21: it must be a non-empty string with max len 320 and cannot start with a dot
    assert is_email('') == False  # Empty string
    assert is_email('a' * 321) == False  # String too long
    assert is_email('.invalid@example.com') == False  # Starts with a dot

    # Line 29: head's size must be <= 64, tail <= 255, head must not start with a dot or contain multiple consecutive dots
    assert is_email('a' * 65 + '@example.com') == False  # Head too long
    assert is_email('@example.com') == False  # No head part
    assert is_email('..head@example.com') == False  # Head starts with a dot
    assert is_email('head..@example.com') == False  # Head contains multiple dots
    assert is_email('"quoted head"@example.com') == True  # Valid head with quotes and spaces removed

    # Line 34: removes escaped spaces, so that later on the test regex will accept the string
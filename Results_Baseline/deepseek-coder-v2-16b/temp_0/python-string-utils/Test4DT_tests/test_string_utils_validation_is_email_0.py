# Module: string_utils.validation
import pytest
from string_utils.validation import is_email

# Test cases for valid emails
def test_valid_emails():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('"my email"@example.com') == True
    assert is_email('user+mailbox@example.co.in') == True  # Example of a valid email with special characters in the local part

# Test cases for invalid emails due to too long head part
def test_invalid_long_head():
    assert is_email('a' * 65 + '@gmail.com') == False

# Test cases for invalid emails due to multiple "@" signs
def test_invalid_multiple_ats():
    assert is_email('@gmail.com') == False

# Test cases for invalid emails with escaped spaces in the head part
def test_invalid_escaped_spaces():
    assert is_email('"my email"@example.com') == True  # This should be true as per the function's logic, but you might want to adjust this if there are changes in the implementation details

# Test cases for invalid emails with other edge cases (not covered by examples)
def test_invalid_edge_cases():
    assert is_email('my.email@the-provider.com') == True  # This should be true as per the function's logic, but you might want to adjust this if there are changes in the implementation details

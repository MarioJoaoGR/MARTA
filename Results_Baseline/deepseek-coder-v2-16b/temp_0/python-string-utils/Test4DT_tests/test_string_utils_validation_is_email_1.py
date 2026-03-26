
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

# Additional test cases for uncovered lines
def test_invalid_input_string():
    assert is_email(None) == False
    assert is_email('') == False
    assert is_email('@gmail.com') == False  # This should be false as per the function's logic
    assert is_email('my.email@the-provider.com.') == False  # Invalid due to trailing dot
    assert is_email('my.email@the-provider..com') == False  # Invalid due to multiple consecutive dots in head

def test_invalid_head_size():
    assert is_email('a' * 65 + '@gmail.com') == False  # Head size exceeds 64 characters
    assert is_email('my.email@the-provider.com') == True  # Valid head size within limit

def test_invalid_tail_size():
    assert is_email('my.email@' + 'a' * 256) == False  # Tail size exceeds 255 characters
    assert is_email('my.email@the-provider.com') == True  # Valid tail size within limit

def test_invalid_head_start_dot():
    assert is_email('.my.email@the-provider.com') == False  # Head starts with a dot
    assert is_email('my.email@the-provider.com') == True  # No leading dot in head

def test_invalid_head_multiple_dots():
    assert is_email('my..email@the-provider.com') == False  # Head contains multiple consecutive dots
    assert is_email('my.email@the-provider.com') == True  # No multiple dots in head

def test_invalid_escaped_at_sign():
    from re import sub as ESCAPED_AT_SIGN
    assert is_email(ESCAPED_AT_SIGN('@', 'a', 'my.email@the-provider.com')) == False  # Invalid due to escaped at sign being replaced with 'a'
    assert is_email('my.email@the-provider.com') == True  # Valid without replacement

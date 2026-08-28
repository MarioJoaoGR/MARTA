
import re
from unittest.mock import patch
import pytest

# Assuming the regex and escaped signs are defined somewhere in a module named string_utils.validation
EMAIL_RE = re.compile(r'^[^@]+@[^@]+\.[^@]+$')
ESCAPED_AT_SIGN = re.compile(r'\\@')

def is_full_string(input_string: str) -> bool:
    return isinstance(input_string, str) and len(input_string) > 0

def is_email(input_string: str) -> bool:
    if not is_full_string(input_string) or len(input_string) > 320 or input_string.startswith('.'):
        return False

    try:
        head, tail = input_string.split('@')

        if len(head) > 64 or len(tail) > 255 or head.endswith('.') or ('..' in head):
            return False

        head = head.replace('\\ ', '')
        if head.startswith('"') and head.endswith('"'):
            head = head.replace(' ', '')[1:-1]

        return EMAIL_RE.match(head + '@' + tail) is not None

    except ValueError:
        if ESCAPED_AT_SIGN.search(input_string) is not None:
            return is_email(ESCAPED_AT_SIGN.sub('a', input_string))

        return False

# Test cases for valid email addresses
def test_valid_email():
    assert is_email('my.email@the-provider.com') == True

# Test case for invalid email address that starts with a dot
def test_invalid_email_starts_with_dot():
    assert is_email('.invalid@example.com') == False

# Test case for invalid email address containing multiple '@' signs
def test_invalid_email_multiple_atsign():
    assert is_email('user@domain@example.com') == False

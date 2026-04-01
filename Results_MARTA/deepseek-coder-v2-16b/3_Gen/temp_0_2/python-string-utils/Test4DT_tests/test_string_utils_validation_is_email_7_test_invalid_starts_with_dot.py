
import re
import pytest
from string_utils.validation import is_email

# Assuming EMAIL_RE and ESCAPED_AT_SIGN are defined in string_utils.validation module
EMAIL_RE = re.compile(r'^[^@]+@[^@]+\.[^@]+$')
ESCAPED_AT_SIGN = re.compile(r'\\@')

def test_invalid_starts_with_dot():
    input_string = '.invalid@example.com'
    assert is_email(input_string) == False

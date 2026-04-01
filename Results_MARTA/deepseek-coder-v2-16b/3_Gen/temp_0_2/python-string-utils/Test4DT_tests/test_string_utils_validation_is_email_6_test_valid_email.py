
import re
import pytest
from string_utils.validation import is_email

# Assuming EMAIL_RE and ESCAPED_AT_SIGN are defined in string_utils.validation module
EMAIL_RE = re.compile(r'^[^@]+@[^@]+\.[^@]+$')
ESCAPED_AT_SIGN = re.compile(r'\\@')

def test_valid_email():
    input_string = 'my.email@the-provider.com'
    assert is_email(input_string) == True

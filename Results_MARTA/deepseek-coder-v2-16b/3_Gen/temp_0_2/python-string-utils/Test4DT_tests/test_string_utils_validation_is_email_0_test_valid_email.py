
import re
import pytest
from string_utils.validation import is_email

# Define regular expressions and constants used in the is_email function
EMAIL_RE = re.compile(r'^[^@]+@[^@]+\.[^@]+$')
ESCAPED_AT_SIGN = re.compile(r'\\ @')

def test_valid_email():
    input_string = 'my.email@the-provider.com'
    assert is_email(input_string) == True, "Expected valid email to return True"


import re
import pytest
from string_utils.validation import is_email

# Define regular expressions for validation
EMAIL_RE = re.compile(r'^[^@]+@[^@]+\.[^@]+$')
ESCAPED_AT_SIGN = re.compile(r'\\@')

def test_invalid_multiple_ats():
    # Test case with multiple '@' symbols
    assert not is_email('multiple@@example.com')

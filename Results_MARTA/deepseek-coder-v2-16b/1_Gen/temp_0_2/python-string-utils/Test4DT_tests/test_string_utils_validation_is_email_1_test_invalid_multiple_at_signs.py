
import re
import pytest
from string_utils.validation import is_email

# Assuming EMAIL_RE and ESCAPED_AT_SIGN are defined somewhere in string_utils.validation module
EMAIL_RE = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
ESCAPED_AT_SIGN = re.compile(r'\\@')

def test_invalid_multiple_at_signs():
    assert not is_email('my@email@provider.com')  # This should return False

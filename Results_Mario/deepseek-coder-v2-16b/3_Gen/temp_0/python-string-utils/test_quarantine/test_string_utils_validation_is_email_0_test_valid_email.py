
import re
import pytest
from string_utils.validation import is_email

# Assuming EMAIL_RE and ESCAPED_AT_SIGN are defined in string_utils.validation module
EMAIL_RE = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
ESCAPED_AT_SIGN = re.compile(r'\\"[^"]+"|\\\'[^']+\'')

def test_valid_email():
    input_string = 'my.email@the-provider.com'
    assert is_email(input_string) == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_email_0_test_valid_email
python-string-utils/Test4DT_tests/test_string_utils_validation_is_email_0_test_valid_email.py:8:49: E0001: Parsing failed: 'closing parenthesis ']' does not match opening parenthesis '(' (Test4DT_tests.test_string_utils_validation_is_email_0_test_valid_email, line 8)' (syntax-error)


"""
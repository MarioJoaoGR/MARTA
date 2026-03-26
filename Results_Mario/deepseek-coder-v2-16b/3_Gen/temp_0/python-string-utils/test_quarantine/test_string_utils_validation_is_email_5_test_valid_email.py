
import re
import pytest
from string_utils.validation import is_full_string, EMAIL_RE, ESCAPED_AT_SIGN

def test_valid_email():
    # Valid emails
    assert is_email('my.email@the-provider.com') == True
    assert is_email('"my email"@example.com') == True
    assert is_email('user@domain.co') == True
    
    # Invalid emails due to too long a head part
    assert is_email('a' * 65 + '@gmail.com') == False
    
    # Invalid emails due to multiple "@" signs
    assert is_email('@gmail.com') == False
    
    # Valid emails with escaped spaces in the head part
    assert is_email('"my email"@example.com') == True
    
    # Edge cases for invalid emails
    assert is_email('invalid-email') == False
    assert is_email('user@domain..co') == False
    assert is_email('user@domain.c') * 65 + '@gmail.com') == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_email_5_test_valid_email
python-string-utils/Test4DT_tests/test_string_utils_validation_is_email_5_test_valid_email.py:24:57: E0001: Parsing failed: 'unmatched ')' (Test4DT_tests.test_string_utils_validation_is_email_5_test_valid_email, line 24)' (syntax-error)


"""

import pytest
from string_utils.validation import is_email

# Assuming EMAIL_RE and ESCAPED_AT_SIGN are defined in string_utils.validation
EMAIL_RE = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
ESCAPED_AT_SIGN = re.compile(r'\\@')

def test_valid_email():
    # Valid email
    assert is_email('my.email@the-provider.com') == True
    
    # Invalid email due to too long a local part
    assert is_email('a' * 65 + '@gmail.com') == False
    
    # Invalid email due to multiple "@" signs
    assert is_email('my@email@provider.com') == False
    
    # Invalid email due to starting with a dot
    assert is_email('.myemail@provider.com') == False
    
    # Valid email with escaped spaces in the local part
    assert is_email('my\.email@the-provider.com') == True
    
    # Borderline case with escaped "@" sign
    assert is_email('my\@email@provider.com') == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_email_0_test_valid_email
python-string-utils/Test4DT_tests/test_string_utils_validation_is_email_0_test_valid_email.py:6:11: E0602: Undefined variable 're' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_email_0_test_valid_email.py:7:18: E0602: Undefined variable 're' (undefined-variable)


"""
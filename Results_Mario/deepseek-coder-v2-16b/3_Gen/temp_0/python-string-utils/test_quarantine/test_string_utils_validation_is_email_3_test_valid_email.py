
import re
from string_utils.validation import is_email

# Define the regular expression for email validation
EMAIL_RE = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
ESCAPED_AT_SIGN = re.compile(r'\\ @')

def test_valid_email():
    # Test cases for valid emails
    assert is_email('my.email@the-provider.com')  # returns True
    assert is_email('a' * 64 + '@gmail.com')      # returns True, as length constraint is not checked here
    assert is_email('"my email"@example.com')     # returns True, handles escaped spaces
    assert is_email('my.email@subdomain.example.com')  # returns True, tests subdomains
    assert is_email('user+mailbox@example.co.uk')   # returns True, tests plus sign in local part
    assert is_email('"very.unusual.@.unusual.com"@example.com')  # returns True, handles unusual characters
    assert is_email('admin@mailserver1.subdomain.example.com')  # returns True, tests multiple subdomains

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_email_3_test_valid_email.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_email _______________________________

    def test_valid_email():
        # Test cases for valid emails
        assert is_email('my.email@the-provider.com')  # returns True
        assert is_email('a' * 64 + '@gmail.com')      # returns True, as length constraint is not checked here
        assert is_email('"my email"@example.com')     # returns True, handles escaped spaces
        assert is_email('my.email@subdomain.example.com')  # returns True, tests subdomains
        assert is_email('user+mailbox@example.co.uk')   # returns True, tests plus sign in local part
        assert is_email('"very.unusual.@.unusual.com"@example.com')  # returns True, handles unusual characters
>       assert is_email('admin@mailserver1.subdomain.example.com')  # returns True, tests multiple subdomains
E       AssertionError: assert False
E        +  where False = is_email('admin@mailserver1.subdomain.example.com')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_email_3_test_valid_email.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_email_3_test_valid_email.py::test_valid_email
============================== 1 failed in 0.03s ===============================
"""
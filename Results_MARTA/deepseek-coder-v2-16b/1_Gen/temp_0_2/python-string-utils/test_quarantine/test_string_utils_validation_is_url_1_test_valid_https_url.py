
import pytest
from string_utils.validation import is_url

@pytest.mark.parametrize("input_string, expected", [
    ('https://mysite.com', True),
    ('http://mysite.com', False),  # HTTP should not be allowed
    ('https://www.mysite.com', True),
    ('.mysite.com', False),         # No scheme provided
    ('ftp://example.com', False),   # FTP is not in the allowed schemes
    ('https://mysite.com', True)     # Valid HTTPS URL should return True
])
def test_valid_https_url(input_string, expected):
    assert is_url(input_string, allowed_schemes=['http', 'https']) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 6 items

python-string-utils/Test4DT_tests/test_string_utils_validation_is_url_1_test_valid_https_url.py . [ 16%]
F....                                                                    [100%]

=================================== FAILURES ===================================
________________ test_valid_https_url[http://mysite.com-False] _________________

input_string = 'http://mysite.com', expected = False

    @pytest.mark.parametrize("input_string, expected", [
        ('https://mysite.com', True),
        ('http://mysite.com', False),  # HTTP should not be allowed
        ('https://www.mysite.com', True),
        ('.mysite.com', False),         # No scheme provided
        ('ftp://example.com', False),   # FTP is not in the allowed schemes
        ('https://mysite.com', True)     # Valid HTTPS URL should return True
    ])
    def test_valid_https_url(input_string, expected):
>       assert is_url(input_string, allowed_schemes=['http', 'https']) == expected
E       AssertionError: assert True == False
E        +  where True = is_url('http://mysite.com', allowed_schemes=['http', 'https'])

python-string-utils/Test4DT_tests/test_string_utils_validation_is_url_1_test_valid_https_url.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_url_1_test_valid_https_url.py::test_valid_https_url[http:/mysite.com-False]
========================= 1 failed, 5 passed in 0.03s ==========================
"""
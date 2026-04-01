
import pytest
from string_utils.validation import is_url

@pytest.mark.parametrize("input_string, allowed_schemes, expected", [
    ('http://example.com', ['http', 'https', 'ftp'], True),
    ('https://example.com', ['http', 'https', 'ftp'], True),
    ('ftp://example.com', ['http', 'https', 'ftp'], True),
    ('http://example.com', ['https', 'ftp'], False),
    ('https://example.com', ['http', 'ftp'], False),
    ('ftp://example.com', ['http', 'https'], False),
    ('.mysite.com', None, False),  # Invalid URL without schemes specified
])
def test_valid_url_with_allowed_schemes(input_string, allowed_schemes, expected):
    assert is_url(input_string, allowed_schemes) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 7 items

python-string-utils/Test4DT_tests/test_string_utils_validation_is_url_7_test_valid_url_with_allowed_schemes.py . [ 14%]
...F..                                                                   [100%]

=================================== FAILURES ===================================
_ test_valid_url_with_allowed_schemes[https://example.com-allowed_schemes4-False] _

input_string = 'https://example.com', allowed_schemes = ['http', 'ftp']
expected = False

    @pytest.mark.parametrize("input_string, allowed_schemes, expected", [
        ('http://example.com', ['http', 'https', 'ftp'], True),
        ('https://example.com', ['http', 'https', 'ftp'], True),
        ('ftp://example.com', ['http', 'https', 'ftp'], True),
        ('http://example.com', ['https', 'ftp'], False),
        ('https://example.com', ['http', 'ftp'], False),
        ('ftp://example.com', ['http', 'https'], False),
        ('.mysite.com', None, False),  # Invalid URL without schemes specified
    ])
    def test_valid_url_with_allowed_schemes(input_string, allowed_schemes, expected):
>       assert is_url(input_string, allowed_schemes) == expected
E       AssertionError: assert True == False
E        +  where True = is_url('https://example.com', ['http', 'ftp'])

python-string-utils/Test4DT_tests/test_string_utils_validation_is_url_7_test_valid_url_with_allowed_schemes.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_url_7_test_valid_url_with_allowed_schemes.py::test_valid_url_with_allowed_schemes[https:/example.com-allowed_schemes4-False]
========================= 1 failed, 6 passed in 0.03s ==========================
"""
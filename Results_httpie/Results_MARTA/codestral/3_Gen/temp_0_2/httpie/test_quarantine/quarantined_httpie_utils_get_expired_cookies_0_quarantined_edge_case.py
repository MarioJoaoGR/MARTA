
import pytest
from httpie.utils import get_expired_cookies
from unittest.mock import patch

def test_edge_case():
    with patch('httpie.utils.time.time', return_value=1672502400):  # Example timestamp for testing edge case
        expired_cookies = get_expired_cookies(
            'cookie1=value1; Max-Age=3600, cookie2=value2; Expires=1672502400',
            now=None
        )
    assert len(expired_cookies) == 2

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_codestral/test_httpie_utils_get_expired_cookies_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        with patch('httpie.utils.time.time', return_value=1672502400):  # Example timestamp for testing edge case
            expired_cookies = get_expired_cookies(
                'cookie1=value1; Max-Age=3600, cookie2=value2; Expires=1672502400',
                now=None
            )
>       assert len(expired_cookies) == 2
E       assert 0 == 2
E        +  where 0 = len([])

httpie/Test4DT_tests_codestral/test_httpie_utils_get_expired_cookies_0_test_edge_case.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_utils_get_expired_cookies_0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.19s ===============================
"""
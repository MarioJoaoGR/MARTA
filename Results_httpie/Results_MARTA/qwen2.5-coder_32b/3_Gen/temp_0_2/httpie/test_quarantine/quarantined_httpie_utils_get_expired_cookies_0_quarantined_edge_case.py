
import time
from httpie.utils import get_expired_cookies, parse_ns_headers, split_cookies
from typing import List, Optional, Tuple, Dict
from unittest.mock import patch

def test_get_expired_cookies():
    # Test case for expired cookies
    cookies_str = 'session=12345; Max-Age=60; path=/, user_token=abcde; Expires=1700000000'
    now = 1690000000.0  # Example current time for testing expired cookies
    
    with patch('httpie.utils.time.time', return_value=now):
        expired_cookies = get_expired_cookies(cookies_str, now)
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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_utils_get_expired_cookies_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
___________________________ test_get_expired_cookies ___________________________

    def test_get_expired_cookies():
        # Test case for expired cookies
        cookies_str = 'session=12345; Max-Age=60; path=/, user_token=abcde; Expires=1700000000'
        now = 1690000000.0  # Example current time for testing expired cookies
    
        with patch('httpie.utils.time.time', return_value=now):
            expired_cookies = get_expired_cookies(cookies_str, now)
>           assert len(expired_cookies) == 2
E           assert 0 == 2
E            +  where 0 = len([])

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_utils_get_expired_cookies_0_test_edge_case.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_utils_get_expired_cookies_0_test_edge_case.py::test_get_expired_cookies
============================== 1 failed in 0.15s ===============================
"""
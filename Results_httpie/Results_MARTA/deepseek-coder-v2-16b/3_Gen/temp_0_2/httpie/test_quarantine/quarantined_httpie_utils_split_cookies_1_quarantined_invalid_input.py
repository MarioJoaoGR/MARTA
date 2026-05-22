
import pytest
from unittest.mock import patch
from httpie.utils import split_cookies, RE_COOKIE_SPLIT

def test_invalid_input():
    with patch('builtins.isinstance', return_value=False):
        assert split_cookies(123) == []

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_split_cookies_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with patch('builtins.isinstance', return_value=False):
>           assert split_cookies(123) == []

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_split_cookies_1_test_invalid_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cookies = 123

    def split_cookies(cookies):
        """
        When ``requests`` stores cookies in ``response.headers['Set-Cookie']``
        it concatenates all of them through ``, ``.
    
        This function splits cookies apart being careful to not to
        split on ``, `` which may be part of cookie value.
        """
        if not cookies:
            return []
>       return RE_COOKIE_SPLIT.split(cookies)
E       TypeError: expected string or bytes-like object, got 'int'

httpie/httpie/utils.py:153: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_split_cookies_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.13s ===============================
"""
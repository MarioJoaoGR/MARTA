
import pytest
from unittest.mock import patch
from httpie.utils import get_expired_cookies, parse_ns_headers, split_cookies, _max_age_to_expires

def test_valid_input():
    cookies = 'session=12345; Max-Age=600; path=/, user_token=abcde; Expires=1700000000'
    expected_output = [{'name': 'session', 'path': '/'}, {'name': 'user_token', 'path': '/'}]
    
    with patch('httpie.utils.parse_ns_headers', side_effect=lambda x: [(('name1', 'value1'), ('expires', 1700000000)), (('name2', 'value2'), ('expires', None))]):
        with patch('httpie.utils.split_cookies', side_effect=lambda x: [('session', '12345; Max-Age=600; path=/'), ('user_token', 'abcde; Expires=1700000000')]):
            with patch('httpie.utils._max_age_to_expires', side_effect=_max_age_to_expires):
                result = get_expired_cookies(cookies)
    
    assert result == expected_output

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_get_expired_cookies_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        cookies = 'session=12345; Max-Age=600; path=/, user_token=abcde; Expires=1700000000'
        expected_output = [{'name': 'session', 'path': '/'}, {'name': 'user_token', 'path': '/'}]
    
        with patch('httpie.utils.parse_ns_headers', side_effect=lambda x: [(('name1', 'value1'), ('expires', 1700000000)), (('name2', 'value2'), ('expires', None))]):
            with patch('httpie.utils.split_cookies', side_effect=lambda x: [('session', '12345; Max-Age=600; path=/'), ('user_token', 'abcde; Expires=1700000000')]):
                with patch('httpie.utils._max_age_to_expires', side_effect=_max_age_to_expires):
                    result = get_expired_cookies(cookies)
    
>       assert result == expected_output
E       AssertionError: assert [{'name': 'na... 'path': '/'}] == [{'name': 'se... 'path': '/'}]
E         
E         At index 0 diff: {'name': 'name1', 'path': '/'} != {'name': 'session', 'path': '/'}
E         Right contains one more item: {'name': 'user_token', 'path': '/'}
E         Use -v to get more diff

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_get_expired_cookies_0_test_valid_input.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_get_expired_cookies_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.11s ===============================
"""
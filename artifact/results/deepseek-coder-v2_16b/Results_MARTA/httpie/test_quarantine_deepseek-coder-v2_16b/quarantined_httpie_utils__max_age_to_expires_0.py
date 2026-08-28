
import pytest
from httpie.utils import _max_age_to_expires



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils__max_age_to_expires_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        valid_cookies = [
            {'expires': 1701676800.0, 'max-age': '86400', 'name': 'session', 'value': 'abc123'},
            {'expires': 'some_expiry_time', 'name': 'user_token', 'value': 'xyz789'}
        ]
        now = 1701590400.0  # Example timestamp for January 2, 2024, 00:00:00
    
        _max_age_to_expires(valid_cookies, now)
    
        assert valid_cookies[0]['expires'] == 1701590400.0 + 86400.0
>       assert valid_cookies[1]['expires'] is None
E       AssertionError: assert 'some_expiry_time' is None

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils__max_age_to_expires_0.py:15: AssertionError
_____________________________ test_missing_max_age _____________________________

    def test_missing_max_age():
        cookies = [
            {'name': 'session', 'value': 'abc123'},
            {'name': 'user_token', 'value': 'xyz789', 'max-age': '3600'}
        ]
        now = 1701590400.0  # Example timestamp for January 2, 2024, 00:00:00
    
        _max_age_to_expires(cookies, now)
    
>       assert cookies[0]['expires'] is None
E       KeyError: 'expires'

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils__max_age_to_expires_0.py:26: KeyError
_____________________________ test_invalid_max_age _____________________________

    def test_invalid_max_age():
        cookies = [
            {'name': 'session', 'value': 'abc123', 'max-age': 'invalid'},
            {'name': 'user_token', 'value': 'xyz789'}
        ]
        now = 1701590400.0  # Example timestamp for January 2, 2024, 00:00:00
    
        _max_age_to_expires(cookies, now)
    
>       assert cookies[0]['expires'] is None
E       KeyError: 'expires'

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils__max_age_to_expires_0.py:38: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils__max_age_to_expires_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils__max_age_to_expires_0.py::test_missing_max_age
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils__max_age_to_expires_0.py::test_invalid_max_age
============================== 3 failed in 0.14s ===============================
"""
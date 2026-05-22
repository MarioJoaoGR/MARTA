
import pytest
from httpie.utils import get_expired_cookies
from unittest.mock import patch, MagicMock

def test_invalid_input():
    with pytest.raises(ValueError):
        get_expired_cookies("")  # Test empty string input
        get_expired_cookies("session=12345; Max-Age=600; path=/")  # Test missing 'now' parameter

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

httpie/Test4DT_tests_codestral/test_httpie_utils_get_expired_cookies_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

httpie/Test4DT_tests_codestral/test_httpie_utils_get_expired_cookies_0_test_invalid_input.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_utils_get_expired_cookies_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.20s ===============================
"""
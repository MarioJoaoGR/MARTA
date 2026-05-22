
import pytest
from unittest.mock import patch
from httpie.utils import unwrap_context

def test_invalid_input():
    with patch('httpie.utils.unwrap_context', side_effect=Exception("Invalid input")):
        with pytest.raises(Exception) as exc_info:
            raise Exception("Root error") from FileNotFoundError("Related error")
        assert str(exc_info.value) == "Invalid input"

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_unwrap_context_3_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with patch('httpie.utils.unwrap_context', side_effect=Exception("Invalid input")):
            with pytest.raises(Exception) as exc_info:
                raise Exception("Root error") from FileNotFoundError("Related error")
>           assert str(exc_info.value) == "Invalid input"
E           AssertionError: assert 'Root error' == 'Invalid input'
E             
E             - Invalid input
E             + Root error

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_unwrap_context_3_test_invalid_input.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_unwrap_context_3_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.17s ===============================
"""

import pytest
from unittest.mock import patch
from flutes.log import set_console_logging_function, _CONSOLE_LOG_FN

def test_none_input():
    with patch('flutes.log._CONSOLE_LOG_FN', new=None):
        assert _CONSOLE_LOG_FN is None
        set_console_logging_function(lambda x: print(x))
        assert _CONSOLE_LOG_FN is not None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_log_set_console_logging_function_0_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        with patch('flutes.log._CONSOLE_LOG_FN', new=None):
>           assert _CONSOLE_LOG_FN is None
E           assert _CONSOLE_LOG_FN is None

flutes/Test4DT_tests/test_flutes_log_set_console_logging_function_0_test_none_input.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_set_console_logging_function_0_test_none_input.py::test_none_input
============================== 1 failed in 0.09s ===============================
"""
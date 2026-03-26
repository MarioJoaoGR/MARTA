
from flutes.log import _get_console_logging_function, _CONSOLE_LOG_FN
from unittest.mock import patch
import pytest

def test_invalid_input():
    with patch('flutes.log._CONSOLE_LOG_FN', None):
        log_function = _get_console_logging_function()
        assert callable(log_function), "Expected a callable object but got something else."

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

flutes/Test4DT_tests/test_flutes_log__get_console_logging_function_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with patch('flutes.log._CONSOLE_LOG_FN', None):
            log_function = _get_console_logging_function()
>           assert callable(log_function), "Expected a callable object but got something else."
E           AssertionError: Expected a callable object but got something else.
E           assert False
E            +  where False = callable(None)

flutes/Test4DT_tests/test_flutes_log__get_console_logging_function_1_test_invalid_input.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log__get_console_logging_function_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.09s ===============================
"""
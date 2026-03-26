
from flutes.log import set_console_logging_function, _CONSOLE_LOG_FN
from unittest.mock import Mock
import pytest

def test_none_input():
    # Create a mock function
    mock_fn = Mock()
    
    # Call the function with None
    set_console_logging_function(None)
    
    # Check that _CONSOLE_LOG_FN is None
    assert _CONSOLE_LOG_FN is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_log_set_console_logging_function_0_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        # Create a mock function
        mock_fn = Mock()
    
        # Call the function with None
        set_console_logging_function(None)
    
        # Check that _CONSOLE_LOG_FN is None
>       assert _CONSOLE_LOG_FN is None
E       assert _CONSOLE_LOG_FN is None

flutes/Test4DT_tests/test_flutes_log_set_console_logging_function_0_test_none_input.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_set_console_logging_function_0_test_none_input.py::test_none_input
============================== 1 failed in 0.11s ===============================
"""
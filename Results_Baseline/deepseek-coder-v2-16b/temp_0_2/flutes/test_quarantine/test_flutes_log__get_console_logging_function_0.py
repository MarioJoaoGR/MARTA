
import pytest
from flutes.log import _get_console_logging_function

# Test case to check if the function returns the current console logging function
def test_get_console_logging_function():
    # Assuming _CONSOLE_LOG_FN is a mock function for testing purposes
    from unittest.mock import MagicMock
    
    # Create a mock function
    mock_log_function = MagicMock()
    
    # Assign the mock function to _CONSOLE_LOG_FN
    global _CONSOLE_LOG_FN
    _CONSOLE_LOG_FN = mock_log_function  # pylint: disable=E0602
    
    # Call the function and check if it returns the mock function
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

flutes/Test4DT_tests/test_flutes_log__get_console_logging_function_0.py F [100%]

=================================== FAILURES ===================================
______________________ test_get_console_logging_function _______________________

    def test_get_console_logging_function():
        # Assuming _CONSOLE_LOG_FN is a mock function for testing purposes
        from unittest.mock import MagicMock
    
        # Create a mock function
        mock_log_function = MagicMock()
    
        # Assign the mock function to _CONSOLE_LOG_FN
        global _CONSOLE_LOG_FN
        _CONSOLE_LOG_FN = mock_log_function  # pylint: disable=E0602
    
        # Call the function and check if it returns the mock function
>       assert _get_console_logging_function() == mock_log_function
E       AssertionError: assert functools.partial(<built-in function print>, flush=True) == <MagicMock id='140489108953168'>
E        +  where functools.partial(<built-in function print>, flush=True) = _get_console_logging_function()

flutes/Test4DT_tests/test_flutes_log__get_console_logging_function_0.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log__get_console_logging_function_0.py::test_get_console_logging_function
============================== 1 failed in 0.09s ===============================
"""
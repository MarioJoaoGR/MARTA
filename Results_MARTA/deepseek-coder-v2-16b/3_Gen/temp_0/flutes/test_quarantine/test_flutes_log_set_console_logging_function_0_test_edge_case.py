
from flutes.log import set_console_logging_function, _CONSOLE_LOG_FN
from unittest.mock import Mock
import pytest

def test_edge_case():
    # Create a mock logging function
    mock_log_fn = Mock()
    
    # Set the console logging function to None
    set_console_logging_function(None)
    
    # Assert that _CONSOLE_LOG_FN is now None
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

flutes/Test4DT_tests/test_flutes_log_set_console_logging_function_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        # Create a mock logging function
        mock_log_fn = Mock()
    
        # Set the console logging function to None
        set_console_logging_function(None)
    
        # Assert that _CONSOLE_LOG_FN is now None
>       assert _CONSOLE_LOG_FN is None
E       assert _CONSOLE_LOG_FN is None

flutes/Test4DT_tests/test_flutes_log_set_console_logging_function_0_test_edge_case.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_set_console_logging_function_0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.08s ===============================

"""
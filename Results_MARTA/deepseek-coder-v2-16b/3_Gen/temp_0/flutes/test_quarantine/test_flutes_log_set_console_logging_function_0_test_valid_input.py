
from flutes.log import _CONSOLE_LOG_FN, set_console_logging_function
from unittest.mock import Mock

def test_valid_input():
    mock_log_fn = Mock()
    set_console_logging_function(mock_log_fn)
    assert _CONSOLE_LOG_FN == mock_log_fn

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_log_set_console_logging_function_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        mock_log_fn = Mock()
        set_console_logging_function(mock_log_fn)
>       assert _CONSOLE_LOG_FN == mock_log_fn
E       AssertionError: assert _CONSOLE_LOG_FN == <Mock id='140369383270928'>

flutes/Test4DT_tests/test_flutes_log_set_console_logging_function_0_test_valid_input.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_set_console_logging_function_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.10s ===============================
"""
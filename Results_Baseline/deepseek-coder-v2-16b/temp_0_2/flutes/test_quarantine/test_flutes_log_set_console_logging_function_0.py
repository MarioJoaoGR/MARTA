
# Module: flutes.log
import pytest
from typing import Callable

# Import the function from its module
global _CONSOLE_LOG_FN
try:
    from flutes.log import set_console_logging_function as target_function
except ImportError:
    # If the import fails, assume the function is in the same module and adjust accordingly
    from .flutes.log import set_console_logging_function as target_function

# Test cases for set_console_logging_function
def test_set_console_logging_function_basic():
    def mock_log_fn(log: str):
        pass
    
    # Call the function with a mock log function
    target_function(mock_log_fn)
    
    # Assert that _CONSOLE_LOG_FN is set to the mock log function
    assert _CONSOLE_LOG_FN == mock_log_fn

def test_set_console_logging_function_multiple_calls():
    def first_mock_log_fn(log: str):
        pass
    
    def second_mock_log_fn(log: str):
        pass
    
    # Call the function with a mock log function, then another one
    target_function(first_mock_log_fn)
    assert _CONSOLE_LOG_FN == first_mock_log_fn
    
    target_function(second_mock_log_fn)
    assert _CONSOLE_LOG_FN == second_mock_log_fn

def test_set_console_logging_function_none():
    # Call the function with None, which should reset _CONSOLE_LOG_FN to None
    target_function(None)
    
    # Assert that _CONSOLE_LOG_FN is set to None
    assert _CONSOLE_LOG_FN is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_log_set_console_logging_function_0
flutes/Test4DT_tests/test_flutes_log_set_console_logging_function_0.py:23:11: E0602: Undefined variable '_CONSOLE_LOG_FN' (undefined-variable)
flutes/Test4DT_tests/test_flutes_log_set_console_logging_function_0.py:34:11: E0602: Undefined variable '_CONSOLE_LOG_FN' (undefined-variable)
flutes/Test4DT_tests/test_flutes_log_set_console_logging_function_0.py:37:11: E0602: Undefined variable '_CONSOLE_LOG_FN' (undefined-variable)
flutes/Test4DT_tests/test_flutes_log_set_console_logging_function_0.py:44:11: E0602: Undefined variable '_CONSOLE_LOG_FN' (undefined-variable)


"""
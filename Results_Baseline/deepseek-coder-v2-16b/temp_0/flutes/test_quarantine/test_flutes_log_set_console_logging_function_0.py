
# Module: flutes.log
import pytest
from typing import Callable

# Import the function from the module
def set_console_logging_function(log_fn: Callable[[str], None]) -> None:
    r"""Set the console logging function **for current process only**."""
    global _CONSOLE_LOG_FN
    _CONSOLE_LOG_FN = log_fn

# Test cases for set_console_logging_function
def test_set_console_logging_function_with_valid_log_fn():
    def mock_log_fn(message: str):
        print(f"Logged message: {message}")
    
    set_console_logging_function(mock_log_fn)
    assert _CONSOLE_LOG_FN == mock_log_fn

def test_set_console_logging_function_without_log_fn():
    with pytest.raises(TypeError):
        set_console_logging_function()

def test_set_console_logging_function_with_invalid_log_fn():
    with pytest.raises(AssertionError):
        set_console_logging_function("not a callable")

# Additional edge cases can be added to cover more scenarios

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_log_set_console_logging_function_0
flutes/Test4DT_tests/test_flutes_log_set_console_logging_function_0.py:22:8: E1120: No value for argument 'log_fn' in function call (no-value-for-parameter)


"""
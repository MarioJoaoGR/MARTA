
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
    assert _CONSOLE_LOG_FN == mock_log_fn, f"Expected _CONSOLE_LOG_FN to be {mock_log_fn}, but got {_CONSOLE_LOG_FN}"
    # Additional assertions can be added to check the behavior of the logging function

def test_set_console_logging_function_with_none():
    set_console_logging_function(None)
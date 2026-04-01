
import pytest
from unittest.mock import patch
from flutes.log import _get_console_logging_function, _CONSOLE_LOG_FN

@pytest.mark.unit
def test_valid_input():
    # Mock the console logging function to return a dummy callable
    with patch('flutes.log._CONSOLE_LOG_FN', return_value=lambda x: print(x)):
        log_function = _get_console_logging_function()
        assert callable(log_function)
        # Test the logging functionality by calling it with a sample message
        log_function("This is a test message.")

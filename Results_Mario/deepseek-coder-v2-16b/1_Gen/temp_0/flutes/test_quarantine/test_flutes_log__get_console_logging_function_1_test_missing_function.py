
from flutes.log import _get_console_logging_function, _CONSOLE_LOG_FN
from unittest.mock import patch

def dummy_log_function(message):
    raise NotImplementedError("This is a mock log function and should not be called.")

def test_missing_function():
    with patch('flutes.log._CONSOLE_LOG_FN', None):
        # Mock _CONSOLE_LOG_FN to return the dummy function
        with patch('flutes.log._CONSOLE_LOG_FN', new=dummy_log_function):
            log_function = _get_console_logging_function()
            assert callable(log_function), "Expected a callable object, but got something else."

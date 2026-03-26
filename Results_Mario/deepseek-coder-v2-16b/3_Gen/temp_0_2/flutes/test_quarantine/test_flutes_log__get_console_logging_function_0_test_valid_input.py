
from unittest.mock import patch, MagicMock
import pytest
from flutes.log import _get_console_logging_function, _CONSOLE_LOG_FN

def test_valid_input():
    # Mock a callable object as _CONSOLE_LOG_FN
    mock_log_fn = MagicMock()
    with patch('flutes.log._CONSOLE_LOG_FN', return_value=mock_log_fn):
        # Call the function to be tested
        log_function = _get_console_logging_function()
        assert callable(log_function)

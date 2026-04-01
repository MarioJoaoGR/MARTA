
import pytest
from unittest.mock import patch
from flutes.log import _get_console_logging_function, _CONSOLE_LOG_FN

def test_no_console_logging():
    with patch('flutes.log._CONSOLE_LOG_FN', None):
        log_function = _get_console_logging_function()
        assert log_function is None

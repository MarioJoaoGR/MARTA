
import pytest
from unittest.mock import patch
from flutes.log import _CONSOLE_LOG_FN, _get_console_logging_function

@pytest.mark.skip(reason="This test is not yet implemented")
def test_none_input():
    with patch('flutes.log._CONSOLE_LOG_FN', None):
        log_function = _get_console_logging_function()
        assert callable(log_function)


import pytest
from unittest.mock import patch
from flutes.log import _get_console_logging_function, _CONSOLE_LOG_FN

@pytest.mark.parametrize("input_value", [None])
def test_none_input(input_value):
    with patch('flutes.log._CONSOLE_LOG_FN', return_value=lambda x: print(x)):
        log_function = _get_console_logging_function()
        assert callable(log_function)

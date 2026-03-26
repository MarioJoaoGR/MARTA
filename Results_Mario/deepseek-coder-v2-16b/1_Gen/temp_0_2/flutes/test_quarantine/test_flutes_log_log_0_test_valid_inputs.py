
import pytest
from flutes.log import log, LOGGING_MAP, LEVEL_MAP, _CONSOLE_LOGGING_LEVEL, COLOR_MAP, LOGGER
from unittest.mock import patch

@pytest.mark.parametrize("msg, level, force_console, timestamp, include_proc_id", [
    ("This is an info message.", "info", False, True, True),
    ("An error occurred.", "error", False, True, True),
    ("A warning message.", "warning", False, True, True),
    ("Success message.", "success", False, True, True),
    ("Message without timestamp.", "info", False, False, True),
    ("Message without process ID.", "info", False, True, False)
])
def test_valid_inputs(msg, level, force_console, timestamp, include_proc_id):
    with patch('flutes.log._CONSOLE_LOG_FN', side_effect=print), \
         patch('flutes.log.LOGGER.hasHandlers', return_value=True), \
         patch('flutes.log.get_worker_id', return_value=123):
        log(msg, level, force_console, timestamp, include_proc_id)

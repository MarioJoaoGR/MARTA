
import pytest
from flutes.log import log, LOGGING_MAP, LEVEL_MAP, _CONSOLE_LOGGING_LEVEL, COLOR_MAP, LOGGER
from unittest.mock import patch

@pytest.mark.parametrize("msg", ["Test message 1", "Another test message"])
@pytest.mark.parametrize("level", ["info", "warning", "error", "success"])
@pytest.mark.parametrize("force_console", [True, False])
@pytest.mark.parametrize("timestamp", [True, False])
@pytest.mark.parametrize("include_proc_id", [True, False])
def test_log_valid_inputs(msg, level, force_console, timestamp, include_proc_id):
    with patch('flutes.log._CONSOLE_LOG_FN', side_effect=print), \
         patch('flutes.log.LOGGER.hasHandlers', return_value=True), \
         patch('flutes.log.get_worker_id', return_value=123):
        log(msg, level=level, force_console=force_console, timestamp=timestamp, include_proc_id=include_proc_id)

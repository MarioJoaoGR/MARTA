
import pytest
from flutes.log import log, LOGGING_MAP, LEVEL_MAP, _CONSOLE_LOGGING_LEVEL, COLOR_MAP
from unittest.mock import patch

# Mocking the logger and console output
@patch('flutes.log._CONSOLE_LOG_FN')
@patch('flutes.log.LOGGER')
def test_invalid_inputs(mock_logger, mock_console):
    with pytest.raises(ValueError):
        log("Test message", level="invalid")

# Test cases for other levels should be added here if necessary

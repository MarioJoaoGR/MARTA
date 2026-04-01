
import pytest
from flutes.log import log, LoggingLevel, LEVEL_MAP, _CONSOLE_LOGGING_LEVEL, LOGGING_MAP, COLOR_MAP, LOGGER, get_worker_id, colored, _CONSOLE_LOG_FN

def test_edge_cases():
    with pytest.raises(ValueError):
        log("Test message", level="invalid_level")

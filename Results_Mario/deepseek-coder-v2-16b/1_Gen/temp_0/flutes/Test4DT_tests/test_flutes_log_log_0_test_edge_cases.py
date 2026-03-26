
import pytest
from flutes.log import log, LoggingLevel, LEVEL_MAP, _CONSOLE_LOGGING_LEVEL, COLOR_MAP, LOGGING_MAP, LOGGER
from unittest.mock import patch

def test_edge_cases():
    with pytest.raises(ValueError):
        # Test case where level is not in LOGGING_MAP
        log("Test message", level="invalid_level")

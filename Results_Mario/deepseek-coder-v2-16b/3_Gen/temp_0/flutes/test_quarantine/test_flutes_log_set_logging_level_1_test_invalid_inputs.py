
import pytest
from unittest.mock import patch, MagicMock
from flutes.log import set_logging_level, LEVEL_MAP, _CONSOLE_LOGGING_LEVEL, LOGGER

# Define a mock for the LEVEL_MAP dictionary
@pytest.fixture(autouse=True)
def mock_level_map():
    with patch('flutes.log.LEVEL_MAP', {'DEBUG': 10}):
        yield

# Test case to check invalid logging level input
def test_invalid_inputs():
    with pytest.raises(ValueError):
        set_logging_level('INVALID_LEVEL', console=True, file=True)

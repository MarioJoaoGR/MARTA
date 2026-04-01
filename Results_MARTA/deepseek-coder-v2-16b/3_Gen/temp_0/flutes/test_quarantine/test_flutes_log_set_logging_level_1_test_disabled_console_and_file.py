
import pytest
from unittest.mock import patch, DEFAULT
from flutes.log import set_logging_level, LEVEL_MAP, _CONSOLE_LOGGING_LEVEL, LOGGER

@pytest.fixture(autouse=True)
def mock_logger():
    with patch('flutes.log.LOGGER', autospec=True):
        yield

def test_set_logging_level_disabled_console_and_file():
    with pytest.raises(ValueError):
        set_logging_level('INVALID_LEVEL', console=False, file=False)

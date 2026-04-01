
import pytest
from flutes.log import set_logging_level, LEVEL_MAP, _CONSOLE_LOGGING_LEVEL, LOGGER

def test_invalid_input():
    with pytest.raises(ValueError):
        set_logging_level('INVALID_LEVEL', console=True, file=True)

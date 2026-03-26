
import pytest
from flutes.log import set_logging_level, LEVEL_MAP, _CONSOLE_LOGGING_LEVEL, LOGGER

def test_valid_inputs():
    # Assuming LEVEL_MAP, _CONSOLE_LOGGING_LEVEL, and LOGGER are properly defined in the flutes.log module
    
    with pytest.raises(ValueError):
        set_logging_level('INVALID', console=True, file=True)

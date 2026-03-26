
import pytest
from flutes.log import set_logging_level, LEVEL_MAP

def test_invalid_inputs():
    with pytest.raises(ValueError):
        # Test with an unknown logging level
        set_logging_level('UNKNOWN_LEVEL')
        
    with pytest.raises(ValueError):
        # Test with a None value
        set_logging_level(None)


import pytest
from flutes.log import set_logging_level, LEVEL_MAP

def test_invalid_inputs():
    with pytest.raises(ValueError):
        set_logging_level('INVALID_LEVEL')

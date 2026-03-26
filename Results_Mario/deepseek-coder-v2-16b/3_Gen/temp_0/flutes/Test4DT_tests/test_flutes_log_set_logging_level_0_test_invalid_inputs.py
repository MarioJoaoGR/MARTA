
import pytest
from flutes.log import set_logging_level, LEVEL_MAP
from unittest.mock import patch

def test_invalid_inputs():
    with pytest.raises(ValueError):
        # Test with an invalid logging level
        set_logging_level('INVALID_LEVEL')
        
    with pytest.raises(ValueError):
        # Test with a valid but unsupported logging level (e.g., 'NOTSET')
        set_logging_level('NOTSET')

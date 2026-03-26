
import pytest
from flutes.log import log  # Assuming the module is named 'flutes.log'

def test_invalid_inputs():
    with pytest.raises(ValueError):
        # Test with an invalid logging level
        log("Test message", level="invalid_level")

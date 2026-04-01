
import pytest
from flutes.log import log  # Assuming this is the correct module path

def test_invalid_inputs():
    with pytest.raises(ValueError):
        log("Test message", level="invalid_level")


import pytest
from flutes.log import log  # Assuming this is the correct module and you have access to it

def test_invalid_logging_level():
    with pytest.raises(ValueError):
        log("Test message", level="invalid_level")

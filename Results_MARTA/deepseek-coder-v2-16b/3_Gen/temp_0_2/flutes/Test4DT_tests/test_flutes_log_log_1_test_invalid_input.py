
import pytest
from flutes.log import log, LoggingLevel

def test_invalid_input():
    with pytest.raises(ValueError):
        log("Test message", level="invalid_level")

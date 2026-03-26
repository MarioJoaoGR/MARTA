
import pytest
from flutes.log import log, LoggingLevel  # Importing from the correct module

def test_edge_case_none():
    with pytest.raises(ValueError):
        log("Test message", level="invalid_level")  # Invalid level should raise ValueError

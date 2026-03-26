
import pytest
from flutes.log import log  # Assuming 'flutes.log' is correctly imported

def test_log_edge_cases():
    with pytest.raises(ValueError):
        # Test with an incorrect logging level
        log("Test message", level="invalid_level")


import pytest
from flutes.log import log  # Assuming the module is correctly imported from 'flutes.log'

def test_edge_cases():
    with pytest.raises(ValueError):
        log("Test message", level="invalid_level")

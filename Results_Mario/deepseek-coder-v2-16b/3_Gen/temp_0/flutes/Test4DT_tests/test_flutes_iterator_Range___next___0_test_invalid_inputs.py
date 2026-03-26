
import pytest
from flutes.iterator import Range

def test_invalid_inputs():
    with pytest.raises(ValueError):
        # Test case for invalid input - no arguments
        r = Range()
    
    with pytest.raises(ValueError):
        # Test case for invalid input - more than three arguments
        r = Range(1, 2, 3, 4)

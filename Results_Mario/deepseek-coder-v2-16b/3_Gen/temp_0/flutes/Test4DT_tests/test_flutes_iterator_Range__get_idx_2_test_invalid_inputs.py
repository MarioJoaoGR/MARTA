
import pytest
from flutes.iterator import Range

def test_invalid_inputs():
    with pytest.raises(ValueError):
        # No arguments provided
        r = Range()
    
    with pytest.raises(ValueError):
        # More than three arguments provided
        r = Range(1, 2, 3, 4)


import pytest
from flutes.iterator import Range

def test_invalid_inputs():
    with pytest.raises(ValueError):
        # Test case 1: No arguments provided
        r = Range()
        
        # Test case 2: More than three arguments provided
        r = Range(1, 2, 3, 4)

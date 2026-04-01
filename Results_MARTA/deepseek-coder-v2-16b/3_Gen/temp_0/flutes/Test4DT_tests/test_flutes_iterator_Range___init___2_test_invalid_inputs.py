
import pytest
from flutes.iterator import Range

def test_invalid_inputs():
    with pytest.raises(ValueError):
        # Test case for no arguments provided
        r = Range()
        
        # Test case for more than three arguments provided
        r = Range(1, 2, 3, 4)

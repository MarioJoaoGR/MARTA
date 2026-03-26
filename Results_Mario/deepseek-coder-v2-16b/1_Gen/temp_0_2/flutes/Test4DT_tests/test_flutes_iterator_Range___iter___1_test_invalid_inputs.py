
import pytest
from flutes.iterator import Range

def test_invalid_inputs():
    # Test cases for invalid inputs
    with pytest.raises(ValueError):
        Range()  # No arguments provided
    
    with pytest.raises(ValueError):
        Range(1, 2, 3, 4)  # More than three arguments provided

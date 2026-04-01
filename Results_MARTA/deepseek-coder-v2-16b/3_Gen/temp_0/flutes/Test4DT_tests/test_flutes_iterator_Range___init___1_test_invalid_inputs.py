
import pytest
from flutes.iterator import Range

def test_invalid_inputs():
    # Test when no arguments are provided
    with pytest.raises(ValueError):
        Range()
    
    # Test when more than three arguments are provided
    with pytest.raises(ValueError):
        Range(1, 2, 3, 4)

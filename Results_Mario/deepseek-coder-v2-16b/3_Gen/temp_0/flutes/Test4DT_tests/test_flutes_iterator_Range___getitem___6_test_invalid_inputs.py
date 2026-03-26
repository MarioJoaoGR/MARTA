
import pytest
from flutes.iterator import Range

def test_invalid_inputs():
    with pytest.raises(ValueError):
        # Test without any arguments
        r = Range()
        
    with pytest.raises(ValueError):
        # Test with more than three arguments
        r = Range(1, 2, 3, 4)

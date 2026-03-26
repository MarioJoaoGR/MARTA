
import pytest
from flutes.iterator import Range

def test_invalid_inputs():
    with pytest.raises(ValueError):
        # Invalid number of arguments
        r = Range()
    
    with pytest.raises(ValueError):
        # More than three arguments
        r = Range(1, 2, 3, 4)

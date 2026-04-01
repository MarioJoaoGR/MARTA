
import pytest
from flutes.iterator import Range

def test_invalid_inputs():
    with pytest.raises(ValueError):
        # Invalid: no arguments provided
        r = Range()
    
    with pytest.raises(ValueError):
        # Invalid: more than three arguments provided
        r = Range(1, 2, 3, 4)

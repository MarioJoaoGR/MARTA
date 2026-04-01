
import pytest
from flutes.iterator import Range

def test_invalid_inputs():
    with pytest.raises(ValueError):
        r = Range()  # No arguments provided
    
    with pytest.raises(ValueError):
        r = Range(1, 2, 3, 4)  # More than three arguments provided
    
    with pytest.raises(TypeError):
        r = Range(1, "end")  # Invalid type for end argument

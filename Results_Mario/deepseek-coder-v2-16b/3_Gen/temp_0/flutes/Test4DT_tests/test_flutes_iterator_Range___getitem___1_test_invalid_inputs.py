
import pytest
from flutes.iterator import Range

def test_invalid_inputs():
    with pytest.raises(ValueError):
        r = Range()  # No arguments provided
        r = Range(1, 2, 3, 4)  # More than three arguments provided
        r = Range(1)  # Only one argument provided

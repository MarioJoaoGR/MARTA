
import pytest
from flutes.iterator import Range  # Assuming this is the correct module path

def test_invalid_inputs():
    with pytest.raises(ValueError):
        r = Range()          # No arguments, should raise ValueError
        r = Range(1, 2, 3, 4) # More than three arguments, should raise ValueError
        r = Range(1)         # One argument, should raise ValueError
        r = Range(1, 2, 3, 4, 5) # Even more arguments, should raise ValueError

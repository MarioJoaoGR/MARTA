
import pytest
from unittest.mock import Mock, patch
from pymonet.utils import memoize  # Assuming this module exists and contains the memoize function

def test_invalid_input():
    # Create a mock function to be memoized
    def add(x):
        return x + 1
    
    # Memoize the mock function
    memoized_add = memoize(add)
    
    # Test with invalid input (e.g., not hashable types like list or dict)
    with pytest.raises(TypeError):  # Expect a TypeError because of invalid input
        memoized_add([1, 2, 3])  # This should raise a TypeError due to the argument being mutable and unhashable

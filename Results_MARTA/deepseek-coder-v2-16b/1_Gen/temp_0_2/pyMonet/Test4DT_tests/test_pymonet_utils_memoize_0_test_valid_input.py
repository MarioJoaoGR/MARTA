
# Import necessary modules
from typing import Callable, List, Any
from pymonet.utils import memoize, eq  # Assuming this is the correct import path for the module
import pytest

# Define a sample function to be memoized
def add(x):
    return x + 1

# Test case for valid input
@pytest.mark.parametrize("input_value", [2, 3, 4])
def test_valid_input(input_value):
    # Memoize the sample function
    memoized_add = memoize(add)
    
    # First call should compute and cache the result
    assert memoized_add(input_value) == input_value + 1
    
    # Second call with the same argument should retrieve the cached result
    assert memoized_add(input_value) == input_value + 1

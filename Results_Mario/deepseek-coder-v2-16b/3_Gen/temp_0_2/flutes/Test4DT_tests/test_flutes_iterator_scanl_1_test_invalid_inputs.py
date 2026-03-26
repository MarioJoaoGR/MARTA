
import pytest
from flutes.iterator import scanl
from typing import Callable, Iterable

# Define a simple add function for testing
def add(x: int, y: int) -> int:
    return x + y

# Test invalid inputs and error handling
def test_invalid_inputs():
    # Test with None as func
    with pytest.raises(TypeError):
        list(scanl(None, [1, 2, 3], 0))
    
    # Test with None as iterable
    with pytest.raises(TypeError):
        list(scanl(add, None, 0))
    
    # Test with None as initial value
    with pytest.raises(TypeError):
        list(scanl(add, [1, 2, 3], None))
    
    # Test with non-callable func
    with pytest.raises(TypeError):
        list(scanl("not_a_function", [1, 2, 3], 0))
    
    # Test with non-iterable iterable
    with pytest.raises(TypeError):
        list(scanl(add, 12345, 0))

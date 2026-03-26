
import pytest
from flutes.multiproc import DummyPool

def test_valid_inputs():
    def example_function(x):
        return x * 2
    
    # Create a DummyPool instance with single-threaded execution
    pool = DummyPool(processes=0)
    
    # Apply the function using the pool
    result = pool.apply(example_function, args=(5,))
    
    # Assert that the result is correct
    assert result == 10

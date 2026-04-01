
import pytest
from flutes.multiproc import DummyPool

def test_dummy_pool_map():
    # Create a DummyPool instance with processes set to 0
    pool = DummyPool(processes=0)
    
    # Define a function to be mapped over an iterable
    def multiply_by_two(x):
        return x * 2
    
    # Test the map method with a range of numbers
    result = pool.map(multiply_by_two, range(5))
    
    # Check if the results are as expected
    assert result == [0, 2, 4, 6, 8]

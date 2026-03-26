
import pytest
from flutes.multiproc import DummyPool

def test_dummy_pool():
    # Create an instance of DummyPool with processes set to 0, which means it will use single-threaded execution
    pool = DummyPool(processes=0)
    
    # Define a sample function and iterable for testing the starmap method
    def sample_function(a, b):
        return a + b
    
    iterable = [(1, 2), (3, 4)]
    
    # Use the starmap method to apply the sample function to each tuple in the iterable
    results = pool.starmap(sample_function, iterable)
    
    # Assert that the results are as expected
    assert results == [3, 7]

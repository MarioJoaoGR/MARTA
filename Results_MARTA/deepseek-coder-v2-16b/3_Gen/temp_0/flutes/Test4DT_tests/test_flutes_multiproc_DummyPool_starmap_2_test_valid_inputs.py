
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

def test_valid_inputs():
    # Create a DummyPool instance with processes set to 0, which means single-threaded execution
    dummy_pool = DummyPool(processes=0)
    
    # Define a sample function and iterable for testing
    def sample_function(a, b):
        return a + b
    
    data = [(1, 2), (3, 4)]
    
    # Use the starmap method of DummyPool to apply the sample function to the data
    results = dummy_pool.starmap(sample_function, data)
    
    # Assert that the results are as expected
    assert results == [3, 7]

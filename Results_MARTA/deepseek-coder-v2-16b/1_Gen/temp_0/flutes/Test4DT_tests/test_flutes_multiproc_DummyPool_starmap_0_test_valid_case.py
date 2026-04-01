
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

def test_valid_case():
    # Create a DummyPool instance with processes set to 0
    dummy_pool = DummyPool(processes=0)
    
    # Ensure that the pool is an instance of DummyPool and not multiprocessing.Pool directly
    assert isinstance(dummy_pool, DummyPool), "Expected DummyPool instance"
    
    # Example function to test with starmap
    def example_func(a, b):
        return a + b
    
    # Create an iterable of tuples for the starmap method
    data = [(1, 2), (3, 4)]
    
    # Use the starmap method to apply the function across the iterable
    results = dummy_pool.starmap(example_func, data)
    
    # Assert that the results are as expected
    assert results == [3, 7], "Expected results do not match"

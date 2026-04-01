
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

def test_dummy_pool_starmap_async():
    pool = DummyPool(processes=0)  # Create a DummyPool with zero processes, which means single-threaded execution
    
    def multiply(a, b):
        return a * b
    
    args = [(2, 3), (4, 5)]
    result = pool.starmap_async(multiply, args)
    
    assert result.get() == [6, 20]  # Check if the results match the expected values


import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

def test_valid_inputs():
    # Test creating a DummyPool with processes set to 0 (single-threaded execution)
    pool = DummyPool(processes=0)
    assert isinstance(pool, DummyPool), "Expected an instance of DummyPool"
    
    # Test creating a DummyPool with default parameters
    pool_default = DummyPool()
    assert isinstance(pool_default, DummyPool), "Expected an instance of DummyPool"
    
    # Test creating a DummyPool with initializer and initargs
    def initializer_func(*args):
        pass  # Placeholder for actual initialization logic
    
    pool_with_initializer = DummyPool(processes=0, initializer=initializer_func, initargs=(1, "arg2"))
    assert isinstance(pool_with_initializer, DummyPool), "Expected an instance of DummyPool"

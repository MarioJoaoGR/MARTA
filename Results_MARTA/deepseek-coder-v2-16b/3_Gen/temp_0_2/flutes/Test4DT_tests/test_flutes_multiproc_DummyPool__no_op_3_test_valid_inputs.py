
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

def test_valid_inputs():
    # Test creating a DummyPool with processes set to 0 (single-threaded execution)
    pool = DummyPool(processes=0)
    assert isinstance(pool, DummyPool), "Expected an instance of DummyPool"
    
    # Test creating a DummyPool with a custom initializer function and arguments
    def my_initializer(*args):
        print("Initializer called with args:", args)
    
    pool = DummyPool(processes=0, initializer=my_initializer, initargs=(1, "arg2"))
    assert isinstance(pool, DummyPool), "Expected an instance of DummyPool"

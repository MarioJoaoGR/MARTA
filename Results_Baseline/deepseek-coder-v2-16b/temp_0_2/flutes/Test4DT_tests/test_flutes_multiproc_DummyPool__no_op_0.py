
import pytest
from flutes.multiproc import DummyPool
import multiprocessing as mp  # Importing the module explicitly to avoid undefined variable error

# Test creating a DummyPool instance with no additional initialization
def test_dummy_pool_no_initializer():
    pool = DummyPool(processes=0)
    assert pool._state == mp.pool.RUN

# Test creating a DummyPool instance with an initializer function and arguments
def test_dummy_pool_with_initializer():
    def initializer_func(arg):
        assert arg == 42
    
    pool = DummyPool(processes=0, initializer=initializer_func, initargs=(42,))
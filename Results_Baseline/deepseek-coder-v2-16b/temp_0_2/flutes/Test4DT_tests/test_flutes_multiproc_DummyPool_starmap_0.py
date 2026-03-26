
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

# Test Case 1: Creating a pool with no additional initialization
def test_dummy_pool_no_init():
    pool = DummyPool(processes=0)
    results = list(pool.imap(lambda x: x * x, range(5)))
    assert results == [0, 1, 4, 9, 16]

# Test Case 2: Initializing each worker process with a custom function and argument
def initializer_func(arg):
    print(f"Initializing with arg: {arg}")

def test_dummy_pool_with_init():
    pool = DummyPool(processes=0, initializer=initializer_func, initargs=(42,))
    results = list(pool.imap(lambda x: x * 2, range(5)))
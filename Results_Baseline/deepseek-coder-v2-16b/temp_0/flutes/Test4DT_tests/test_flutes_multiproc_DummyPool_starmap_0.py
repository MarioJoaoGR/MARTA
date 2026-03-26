
import pytest
from multiprocessing import Pool
from typing import Callable, Iterable, List, Tuple, Any
from flutes.multiproc import DummyPool

# Test cases for the DummyPool class
def test_dummy_pool_init():
    pool = DummyPool(processes=0)
    assert isinstance(pool, DummyPool), "Instance should be a DummyPool"

def test_dummy_pool_starmap():
    def multiply(a, b):
        return a * b
    
    pool = DummyPool(processes=0)
    results = pool.starmap(multiply, [(1, 2), (3, 4)])
    assert results == [2, 12], "Expected results to be [2, 12]"

def test_dummy_pool_apply():
    def add_one(x):
        return x + 1
    
    pool = DummyPool(processes=0)
    result = pool.apply(add_one, args=(1,))
    assert result == 2, "Expected result to be 2"

def test_dummy_pool_imap():
    def increment(x):
        return x + 1
    
    pool = DummyPool(processes=0)
    results = list(pool.imap(increment, [1, 2, 3, 4]))
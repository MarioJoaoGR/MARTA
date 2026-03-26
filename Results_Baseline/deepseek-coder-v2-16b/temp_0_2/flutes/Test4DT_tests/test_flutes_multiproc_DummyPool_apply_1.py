
import pytest
from multiprocessing import Pool
from typing import Callable, Iterable, Any, Dict
from flutes.multiproc import DummyPool

# Define the initializer function for testing
def initializer_func(arg):
    print(f"Initializing with arg: {arg}")

# Test cases for DummyPool class
@pytest.fixture
def dummy_pool():
    return DummyPool(processes=0)

def test_dummy_pool_without_initializer(dummy_pool):
    def square(x):
        return x * x
    
    results = list(dummy_pool.imap(square, range(5)))
    assert results == [0, 1, 4, 9, 16]

def test_dummy_pool_with_initializer(dummy_pool):
    def square(x):
        return x * x
    
    pool = DummyPool(processes=0, initializer=initializer_func, initargs=(42,))
    results = list(pool.imap(square, range(5)))
    assert results == [0, 1, 4, 9, 16]

def test_dummy_pool_apply_function(dummy_pool):
    def square(x):
        return x * x
    
    result = dummy_pool.apply(square, args=(5,))
    assert result == 25

def test_dummy_pool_starmap_function(dummy_pool):
    def square(x):
        return x * x
    
    results = list(dummy_pool.starmap(square, [(0,), (1,), (2,), (3,), (4,)]))
    assert results == [0, 1, 4, 9, 16]

# New test cases to cover line 103
def test_dummy_pool_local_state_update(dummy_pool):
    def fn_with_state(x, __state__=None):
        if __state__ is not None:
            assert __state__ == "initialized"
        return x * x
    
    # Test without state update
    result = dummy_pool.apply(fn_with_state, args=(5,))
    assert result == 25
    
    # Test with state update
    pool = DummyPool(processes=0)
    pool._process_state = "initialized"
    result = pool.apply(fn_with_state, args=(5,))
    assert result == 25

def test_dummy_pool_local_state_update_not_triggered(dummy_pool):
    def fn_without_state(x):
        return x * x
    
    # Test without state update
    result = dummy_pool.apply(fn_without_state, args=(5,))
    assert result == 25
    
    # Test with state update (should not affect the function)
    pool = DummyPool(processes=0)
    pool._process_state = "initialized"
    result = pool.apply(fn_without_state, args=(5,))
    assert result == 25

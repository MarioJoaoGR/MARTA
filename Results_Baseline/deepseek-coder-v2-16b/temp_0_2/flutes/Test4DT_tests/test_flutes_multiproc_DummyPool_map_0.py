# Module: flutes.multiproc
import pytest
from multiprocessing import Pool as MPPool
from typing import Callable, Iterable, List, Optional, Any
from flutes.multiproc import DummyPool

# Helper function for testing
def square(x):
    return x * x

@pytest.fixture
def pool():
    return DummyPool(processes=0)

def test_map_no_initializer(pool):
    results = list(pool.map(square, range(5)))
    assert results == [0, 1, 4, 9, 16]

def test_map_with_initializer(pool):
    def initializer_func(arg):
        print(f"Initializing with arg: {arg}")
    
    pool = DummyPool(processes=0, initializer=initializer_func, initargs=(42,))
    results = list(pool.map(square, range(5)))
    assert results == [0, 1, 4, 9, 16]

def test_imap_no_initializer(pool):
    results = list(pool.imap(square, range(5)))
    assert results == [0, 1, 4, 9, 16]

def test_imap_with_initializer(pool):
    def initializer_func(arg):
        print(f"Initializing with arg: {arg}")
    
    pool = DummyPool(processes=0, initializer=initializer_func, initargs=(42,))
    results = list(pool.imap(square, range(5)))
    assert results == [0, 1, 4, 9, 16]

def test_map_async_no_initializer(pool):
    results_async = pool.map_async(square, range(5))
    # Wait for the results to be ready and then print them
    assert list(results_async.get()) == [0, 1, 4, 9, 16]

def test_map_async_with_initializer(pool):
    def initializer_func(arg):
        print(f"Initializing with arg: {arg}")
    
    pool = DummyPool(processes=0, initializer=initializer_func, initargs=(42,))
    results_async = pool.map_async(square, range(5))
    # Wait for the results to be ready and then print them
    assert list(results_async.get()) == [0, 1, 4, 9, 16]

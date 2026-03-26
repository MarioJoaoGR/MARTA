
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool
from typing import Callable, Iterable, Tuple, List

# Test Case 3: Verifying the initialization of process state in starmap method
def initializer_func(arg):
    print(f"Initializing with arg: {arg}")

def test_dummy_pool_starmap_with_init():
    pool = DummyPool(processes=1)  # Using a single process for predictable results
    def multiply(a, b):
        return a * b
    
    iterable = [(2, 3), (4, 5)]
    results = list(pool.starmap(multiply, iterable, initargs=(42,)))
    assert results == [6, 20]

# Test Case 4: Handling the process state in starmap method
def test_dummy_pool_starmap_with_state():
    pool = DummyPool(processes=1)
    def multiply(a, b):
        return a * b
    
    iterable = [(2, 3), (4, 5)]
    results = list(pool.starmap(multiply, iterable))
    assert results == [6, 20]

# Test Case 5: Verifying the initialization of process state in starmap method with different initargs
def initializer_func_diff(arg):
    print(f"Initializing with arg: {arg}")

def test_dummy_pool_starmap_with_different_init():
    pool = DummyPool(processes=1)  # Using a single process for predictable results
    def multiply(a, b):
        return a * b
    
    iterable = [(2, 3), (4, 5)]
    results = list(pool.starmap(multiply, iterable, initargs=(78,)))
    assert results == [6, 20]

# Module: flutes.multiproc
import pytest
from multiprocessing import Pool
from typing import Callable, Iterable, Any, Dict
import flutes.multiproc as mp

# Assuming the module name is 'flutes.multiproc' and the class is defined in this module

@pytest.fixture(scope="module")
def pool():
    return mp.DummyPool(processes=0)

def test_map(pool):
    def multiply_by_two(x):
        return x * 2

    results = pool.map(multiply_by_two, range(1, 6))
    assert results == [2, 4, 6, 8, 10]

def test_apply(pool):
    def square(x):
        return x ** 2

    result = pool.apply(square, args=(3,))
    assert result == 9

def test_imap(pool):
    def multiply_by_two(x):
        return x * 2

    results_iterator = pool.imap(multiply_by_two, range(1, 6))
    results = [result for result in results_iterator]
    assert results == [2, 4, 6, 8, 10]

def test_starmap(pool):
    def multiply(x, y):
        return x * y

    results = pool.starmap(multiply, [(1, 2), (3, 4), (5, 6)])
    assert results == [2, 12, 30]

def test_apply_async(pool):
    def add(x, y):
        return x + y

    result = pool.apply_async(add, args=(1, 2))
    assert result.get() == 3

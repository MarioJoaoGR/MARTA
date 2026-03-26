
# Module: flutes.multiproc
# test_multiproc.py
from multiprocessing import Pool
import pytest
from typing import Callable, Iterable, Any, Mapping, Iterator

def square(x):
    return x ** 2

def process(x):
    return x * x

def multiply(a, b):
    return a * b

@pytest.fixture
def pool():
    with Pool() as p:
        yield p

def test_imap_unordered(pool):
    results = list(pool.imap_unordered(square, range(10), chunksize=2))
    assert results == [x ** 2 for x in range(10)]

def test_imap_unordered_with_process(pool):
    results = list(pool.imap_unordered(process, range(10), chunksize=2))
    assert results == [x * x for x in range(10)]

def test_starmap(pool):
    results = pool.starmap(multiply, [(1, 2), (3, 4), (5, 6)])
    assert list(results) == [2, 12, 30]

def test_apply(pool):
    result = pool.apply(square, args=(5,))
    assert result == 25

def test_apply_async(pool):
    result = pool.apply_async(process, (5,), callback=lambda x: print(f"Result: {x}"))
    result.wait()
    assert result.get() == 25

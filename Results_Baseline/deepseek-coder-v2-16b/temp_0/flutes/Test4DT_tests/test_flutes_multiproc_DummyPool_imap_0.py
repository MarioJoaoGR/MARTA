# Module: flutes.multiproc
import pytest
from multiprocessing import Pool
from typing import Callable, Iterable, Iterator, Optional, Any, TypeVar

T = TypeVar('T')
R = TypeVar('R')

# Assuming the DummyPool class is defined in the flutes.multiproc module
from flutes.multiproc import DummyPool

def multiply_by_two(x):
    return x * 2

@pytest.fixture
def pool():
    return DummyPool(processes=0)

def test_imap(pool: DummyPool):
    results = list(pool.imap(multiply_by_two, range(5)))
    assert results == [0, 2, 4, 6, 8]

def test_map(pool: DummyPool):
    results = list(pool.map(multiply_by_two, range(5)))
    assert results == [0, 2, 4, 6, 8]

def test_imap_unordered(pool: DummyPool):
    results = list(pool.imap_unordered(multiply_by_two, range(5)))
    # The order may vary due to unordered nature
    assert set(results) == {0, 2, 4, 6, 8}

def test_starmap(pool: DummyPool):
    results = list(pool.starmap(multiply_by_two, [(1,), (2,), (3,), (4,)]))
    assert results == [2, 4, 6, 8]

def test_apply(pool: DummyPool):
    result = pool.apply(multiply_by_two, args=(1,))
    assert result == 2

def test_apply_async(pool: DummyPool):
    result = pool.apply_async(multiply_by_two, args=(1,)).get()
    assert result == 2

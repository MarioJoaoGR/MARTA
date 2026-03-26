
# Module: flutes.multiproc
# test_multiproc.py
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

def square(x):
    return x * x

@pytest.fixture
def pool():
    return DummyPool(processes=0)

def test_apply(pool):
    result = pool.apply(square, args=(5,))
    assert result == 25

def test_apply_async(pool):
    result = pool.apply_async(square, args=(5,))
    assert result.get() == 25

def test_map(pool):
    results = list(pool.map(square, range(5)))
    assert results == [0, 1, 4, 9, 16]

def test_imap(pool):
    results = list(pool.imap(square, range(5)))
    assert results == [0, 1, 4, 9, 16]

def test_starmap(pool):
    results = list(pool.starmap(lambda x, y: x * y, [(1, 2), (3, 4)]))
    assert results == [2, 12]

def test_map_async(pool):
    result = pool.map_async(square, range(5))
    assert list(result.get()) == [0, 1, 4, 9, 16]

def test_starmap_async(pool):
    result = pool.starmap_async(lambda x, y: x * y, [(1, 2), (3, 4)])
    assert list(result.get()) == [2, 12]

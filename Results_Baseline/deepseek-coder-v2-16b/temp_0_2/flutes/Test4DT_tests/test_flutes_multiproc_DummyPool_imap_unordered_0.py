
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

# Example function to test with the pool
def square(x):
    return x * x

# Test cases for DummyPool class
@pytest.fixture
def dummy_pool():
    return DummyPool(processes=0)

def test_imap_unordered(dummy_pool):
    results = list(dummy_pool.imap_unordered(square, range(5)))
    assert len(results) == 5
    for i in range(5):
        assert results[i] == square(i)

def test_imap(dummy_pool):
    results = list(dummy_pool.imap(square, range(5)))
    assert len(results) == 5
    for i in range(5):
        assert results[i] == square(i)

def test_map(dummy_pool):
    results = list(dummy_pool.map(square, range(5), chunksize=1))
    assert len(results) == 5
    for i in range(5):
        assert results[i] == square(i)

def test_apply(dummy_pool):
    result = dummy_pool.apply(square, args=(5,))
    assert result == square(5)

def test_apply_async(dummy_pool):
    async_result = dummy_pool.apply_async(square, args=(5,), error_callback=lambda x: print("Error:", x))
    async_result.wait()
    assert async_result.get() == square(5)

def test_starmap(dummy_pool):
    results = list(dummy_pool.starmap(square, [(0,), (1,), (2,), (3,), (4,)]))
    assert len(results) == 5
    for i in range(5):
        assert results[i] == square(i)

def test_starmap_async(dummy_pool):
    async_result = dummy_pool.starmap_async(square, [(0,), (1,), (2,), (3,), (4,)], callback=lambda x: print("Callback:", x))
    async_result.wait()
    assert len(async_result.get()) == 5
    for i in range(5):
        assert async_result.get()[i] == square(i)

def test_map_async(dummy_pool):
    async_result = dummy_pool.map_async(square, range(5), callback=lambda x: print("Callback:", x))
    async_result.wait()
    assert len(async_result.get()) == 5
    for i in range(5):
        assert async_result.get()[i] == square(i)

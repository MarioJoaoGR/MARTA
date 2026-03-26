
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

# Example function to apply
def my_function(x):
    return x * 2

@pytest.fixture
def pool():
    return DummyPool(processes=0)

def test_map(pool):
    results = list(pool.map(my_function, range(5)))
    assert results == [0, 2, 4, 6, 8]

def test_imap(pool):
    results = list(pool.imap(my_function, range(5)))
    assert results == [0, 2, 4, 6, 8]

def test_apply(pool):
    result = pool.apply(my_function, args=(1,))
    assert result == 2

def test_apply_async(pool):
    result = pool.apply_async(my_function, args=(5,), callback=lambda x: print("Callback:", x))
    assert result.get() == 10

def test_starmap(pool):
    results = list(pool.starmap(my_function, [(1,), (2,), (3,), (4,)]))
    assert results == [2, 4, 6, 8]

def test_imap_unordered(pool):
    results = list(pool.imap_unordered(my_function, range(5)))
    # Order may vary, so we check the elements are in the result
    assert set(results) == {0, 2, 4, 6, 8}

def test_starmap_async(pool):
    result = pool.starmap_async(my_function, [(1,), (2,), (3,), (4,)], callback=lambda x: print("Async Callback:", x))
    assert result.get() == [2, 4, 6, 8]

def test_gather(pool):
    def my_function_iterator(x):
        for i in range(x):
            yield i * 2
    results = list(pool.gather(my_function_iterator, range(5)))
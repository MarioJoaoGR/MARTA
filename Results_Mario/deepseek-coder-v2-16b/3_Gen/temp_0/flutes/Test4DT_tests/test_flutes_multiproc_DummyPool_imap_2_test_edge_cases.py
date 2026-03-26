
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

@pytest.fixture(scope="module")
def dummy_pool():
    return DummyPool(processes=0)

def test_dummy_pool_imap(dummy_pool):
    def multiply_by_two(x):
        return x * 2

    iterable = [1, 2, 3, 4]
    results = list(dummy_pool.imap(multiply_by_two, iterable))
    
    assert results == [2, 4, 6, 8]

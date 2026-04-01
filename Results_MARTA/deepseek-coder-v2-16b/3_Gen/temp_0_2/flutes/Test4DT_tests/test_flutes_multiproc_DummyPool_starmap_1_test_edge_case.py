
import pytest
from multiprocessing import Pool, cpu_count
from flutes.multiproc import DummyPool

@pytest.fixture(scope="module")
def dummy_pool():
    return DummyPool(processes=cpu_count())

def test_dummy_pool_starmap(dummy_pool):
    def multiply(a, b):
        return a * b

    results = dummy_pool.starmap(multiply, [(2, 3), (4, 5)])
    assert results == [6, 20]

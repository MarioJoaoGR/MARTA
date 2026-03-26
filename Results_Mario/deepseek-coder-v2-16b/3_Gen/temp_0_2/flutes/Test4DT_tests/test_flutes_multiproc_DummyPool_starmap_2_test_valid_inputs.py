
import pytest
from multiprocessing import Pool, cpu_count
from flutes.multiproc import DummyPool

@pytest.fixture(scope="module")
def dummy_pool():
    return DummyPool(processes=cpu_count())

def test_valid_inputs(dummy_pool):
    def func(arg1, arg2):
        return arg1 + arg2

    results = dummy_pool.starmap(func, [(1, 2), (3, 4)])
    assert results == [3, 7]

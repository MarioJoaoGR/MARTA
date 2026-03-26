
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

@pytest.fixture(scope="module")
def dummy_pool():
    return DummyPool(processes=0)

def test_valid_case(dummy_pool):
    def func(arg1, arg2):
        return arg1 + arg2
    
    args = [(1, 2), (3, 4)]
    results = dummy_pool.starmap(func, args)
    
    assert results == [3, 7]

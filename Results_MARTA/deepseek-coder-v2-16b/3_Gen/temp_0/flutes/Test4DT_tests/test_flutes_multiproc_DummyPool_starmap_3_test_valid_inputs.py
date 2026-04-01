
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

@pytest.fixture(scope="module")
def dummy_pool():
    return DummyPool(processes=0)

def test_valid_inputs(dummy_pool):
    def func(a, b):
        return a + b
    
    iterable = [(1, 2), (3, 4)]
    args = ()
    kwds = {}
    
    results = dummy_pool.starmap(func, iterable, args=args, kwds=kwds)
    
    assert results == [3, 7]

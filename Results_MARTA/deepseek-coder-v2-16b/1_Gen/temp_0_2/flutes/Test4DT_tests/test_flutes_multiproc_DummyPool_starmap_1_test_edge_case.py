
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

def initializer_func(arg1, arg2):
    # Your initialization code here
    pass

@pytest.fixture
def dummy_pool():
    return DummyPool(processes=0, initializer=initializer_func, initargs=(1, 2))

def test_dummy_pool_starmap(dummy_pool):
    def func(a, b):
        return a + b
    
    iterable = [(1, 2), (3, 4)]
    results = dummy_pool.starmap(func, iterable)
    
    assert results == [3, 7]

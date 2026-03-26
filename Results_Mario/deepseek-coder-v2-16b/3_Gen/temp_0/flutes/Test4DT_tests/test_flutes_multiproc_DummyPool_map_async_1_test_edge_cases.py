
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool, DummyApplyResult

@pytest.fixture(scope="module")
def dummy_pool():
    return DummyPool(processes=0)

def test_map_async(dummy_pool):
    def my_function(x):
        return x * 2
    
    iterable = [1, 2, 3, 4]
    result = dummy_pool.map_async(my_function, iterable)
    
    assert isinstance(result, DummyApplyResult)
    assert list(result.get()) == [2, 4, 6, 8]

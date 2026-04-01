
import multiprocessing as mp
from flutes.multiproc import DummyPool
import pytest

@pytest.fixture(scope="module")
def dummy_pool():
    return DummyPool(processes=0)

def test_dummy_pool_apply_async(dummy_pool):
    def my_function(a, b):
        return a + b
    
    result = dummy_pool.apply_async(my_function, args=(1, 2))
    assert result.get() == 3

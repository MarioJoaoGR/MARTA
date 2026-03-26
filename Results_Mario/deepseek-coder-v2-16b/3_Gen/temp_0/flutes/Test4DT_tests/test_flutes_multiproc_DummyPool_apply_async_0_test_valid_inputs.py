
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

@pytest.fixture(scope="module")
def dummy_pool():
    return DummyPool(processes=0)

def test_valid_inputs(dummy_pool):
    def my_function(a, b):
        return a + b
    
    result = dummy_pool.apply_async(my_function, args=(1, 2))
    assert result.get() == 3

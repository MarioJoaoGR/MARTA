
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

@pytest.fixture(scope="module")
def dummy_pool():
    return DummyPool(processes=0)

def test_dummy_pool_apply_async(dummy_pool):
    # Define a function to be applied asynchronously
    def add(x, y):
        return x + y
    
    # Apply the function asynchronously
    result = dummy_pool.apply_async(add, args=(1, 2))
    
    # Assert that the result is correct
    assert result.get() == 3


import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool, DummyApplyResult

# Fixture to create a DummyPool instance for testing
@pytest.fixture
def dummy_pool():
    return DummyPool(processes=0)

# Test cases for the starmap method of DummyPool class
def test_starmap_async_basic(dummy_pool):
    def square(x):
        return x * x
    
    # Create an iterable with tuples of arguments
    iterable = [(1,), (2,), (3,)]
    
    # Call starmap_async method
    result = dummy_pool.starmap_async(square, iterable)
    
    # Check if the results are correct
    assert isinstance(result, DummyApplyResult)
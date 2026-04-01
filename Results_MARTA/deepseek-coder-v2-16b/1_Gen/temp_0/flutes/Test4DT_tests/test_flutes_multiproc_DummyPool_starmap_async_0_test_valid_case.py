
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

@pytest.fixture(scope="module")
def dummy_pool():
    return DummyPool(processes=0)

def test_valid_case(dummy_pool):
    # Assuming you have a function to test with and an iterable for the starmap method
    def example_function(a, b):
        return a + b

    data = [(1, 2), (3, 4)]
    
    result = dummy_pool.starmap_async(example_function, data).get()
    assert result == [3, 7]

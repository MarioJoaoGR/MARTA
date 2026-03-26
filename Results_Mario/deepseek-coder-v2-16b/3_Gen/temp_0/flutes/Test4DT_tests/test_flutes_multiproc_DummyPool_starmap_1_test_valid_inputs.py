
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

@pytest.fixture(scope="module")
def dummy_pool():
    return DummyPool(processes=0)

def test_valid_inputs(dummy_pool):
    # Define a sample function to be tested with starmap
    def sample_function(a, b):
        return a + b
    
    # Create an iterable of inputs for the starmap method
    input_iterable = [(1, 2), (3, 4), (5, 6)]
    
    # Call the starmap method with the sample function and input iterable
    results = dummy_pool.starmap(sample_function, input_iterable)
    
    # Assert that the results match the expected values
    assert results == [3, 7, 11]


import pytest
from flutes.multiproc import DummyPool

def func(a, b):
    return a + b

@pytest.fixture
def dummy_pool():
    return DummyPool(processes=0)

def test_valid_inputs(dummy_pool):
    inputs = [(1, 2), (3, 4)]
    results = dummy_pool.starmap(func, inputs)
    
    assert len(results) == len(inputs)
    for result in results:
        assert isinstance(result, int)
        
    # Check if the results match the expected values
    expected_results = [3, 7]
    assert results == expected_results

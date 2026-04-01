
import pytest
from flutes.multiproc import DummyPool  # Adjust the import path based on your project structure

@pytest.fixture
def dummy_pool():
    return DummyPool(processes=0)

def test_valid_inputs(dummy_pool):
    def multiply(a, b):
        return a * b

    inputs = [(2, 3), (4, 5)]
    results = dummy_pool.starmap(multiply, inputs)
    
    assert len(results) == 2
    assert results[0] == 6
    assert results[1] == 20

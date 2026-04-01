
import pytest
from multiprocessing import Pool, dummy as mp_dummy

# Assuming DummyPool is defined in the multiproc module
from flutes.multiproc import DummyPool

@pytest.fixture(scope="module")
def pool():
    return DummyPool(processes=0)

def test_valid_inputs(pool):
    def multiply_by_two(x):
        return x * 2
    
    # Test with a list of numbers
    results = pool.imap(multiply_by_two, range(5))
    expected_results = [0, 2, 4, 6, 8]
    assert list(results) == expected_results

    # Test with an iterable that yields values directly
    def yield_values():
        for i in range(5):
            yield i
    
    results = pool.imap(multiply_by_two, yield_values())
    assert list(results) == expected_results


import pytest
from multiprocessing import Pool, cpu_count
from flutes.multiproc import safe_pool

def square(x):
    return x * x

@pytest.fixture
def pool():
    with safe_pool(processes=cpu_count()) as pool:
        yield pool

def test_valid_input(pool):
    results = pool.map(square, range(10))
    assert results == [i**2 for i in range(10)]

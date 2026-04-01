
import pytest
from multiprocessing import Pool, Queue
from typing import Callable, List, Iterable, Any, Optional

def square(x):
    return x * x

@pytest.fixture(scope="module")
def pool():
    with Pool() as pool:
        yield pool

def test_valid_case(pool):
    result = pool.starmap_async(square, [[1], [2], [3]])
    while not result.ready():
        pass  # Wait for the results to be ready
    
    assert result.get() == [1, 4, 9]

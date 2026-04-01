
import pytest
from multiprocessing import Pool, Queue
from typing import Callable, Iterable, List, Optional, Any, Mapping
import flutes.multiproc  # Assuming this is the correct module path

def square(x):
    return x * x

@pytest.fixture
def pool():
    with Pool() as p:
        yield p

def test_starmap_async(pool):
    result = pool.starmap_async(square, [[1], [2], [3]])
    while not result.ready():
        pass  # Wait for the results to be ready
    assert result.get() == [1, 4, 9]

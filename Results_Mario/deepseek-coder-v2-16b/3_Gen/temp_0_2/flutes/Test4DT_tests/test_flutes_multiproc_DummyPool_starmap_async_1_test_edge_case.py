
import pytest
from flutes.multiproc import DummyPool

@pytest.fixture
def pool():
    return DummyPool(processes=0)

def test_edge_case(pool):
    def func(x, y):
        return x + y

    iterable = [(1, 2), (3, 4)]
    result = pool.starmap_async(func, iterable).get()
    
    assert result == [3, 7]

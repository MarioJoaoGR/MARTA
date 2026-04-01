
import pytest
from multiprocessing import Pool
from flutes.multiproc import PoolWrapper

def square(x):
    return x * x

@pytest.fixture
def pool_wrapper():
    return PoolWrapper()

def test_map(pool_wrapper):
    results = list(pool_wrapper.map(square, [1, 2, 3, 4]))
    assert results == [1, 4, 9, 16]

def test_map_async(pool_wrapper):
    pool = Pool()
    async_result = pool_wrapper.map_async(square, [1, 2, 3, 4])
    results = list(async_result.get())
    assert results == [1, 4, 9, 16]


import pytest
from flutes.multiproc import PoolWrapper

@pytest.fixture(scope="module")
def pool_wrapper():
    return PoolWrapper()

def test_imap(pool_wrapper):
    with pytest.raises(TypeError, match="'function' object is not iterable"):
        result = list(pool_wrapper.imap([1, 2, 3], lambda x: x * x))

def test_imap_unordered(pool_wrapper):
    with pytest.raises(TypeError, match="'function' object is not iterable"):
        result = list(pool_wrapper.imap_unordered([1, 2, 3], lambda x: x * x))

def test_map(pool_wrapper):
    with pytest.raises(TypeError, match="'function' object is not iterable"):
        result = list(pool_wrapper.map([1, 2, 3], lambda x: x * x))

def test_map_async(pool_wrapper):
    with pytest.raises(TypeError, match="'function' object is not iterable"):
        async_result = pool_wrapper.map_async([1, 2, 3], lambda x: x * x)

def test_starmap(pool_wrapper):
    with pytest.raises(TypeError, match="'function' object is not iterable"):
        result = list(pool_wrapper.starmap([(1,), (2,), (3,)], lambda x: x * x))

def test_starmap_async(pool_wrapper):
    with pytest.raises(TypeError, match="'function' object is not iterable"):
        async_result = pool_wrapper.starmap_async([(1,), (2,), (3,)], lambda x: x * x)

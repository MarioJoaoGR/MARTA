
import pytest
from multiprocessing import Pool
from flutes.multiproc import PoolWrapper

def square(x):
    return x * x

@pytest.fixture
def pool_wrapper():
    return PoolWrapper()

def test_none_args(pool_wrapper):
    with pytest.raises(TypeError):
        pool_wrapper.map(square, None)

def test_empty_list(pool_wrapper):
    results = pool_wrapper.map(square, [])
    assert results == []

def test_boundary_values(pool_wrapper):
    results = pool_wrapper.map(square, [0, 1, 2, 3])
    expected = [0**2, 1**2, 2**2, 3**2]
    assert results == expected

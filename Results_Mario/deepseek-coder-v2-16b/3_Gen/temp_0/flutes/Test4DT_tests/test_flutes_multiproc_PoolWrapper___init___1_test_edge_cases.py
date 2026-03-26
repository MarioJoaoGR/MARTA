
import pytest
from multiprocessing import Pool, TimeoutError
from flutes.multiproc import PoolWrapper

def square(x):
    return x * x

@pytest.fixture
def pool_wrapper():
    return PoolWrapper()

def test_none_input(pool_wrapper):
    with pytest.raises(TypeError):
        pool_wrapper.map(square, None)

def test_empty_list_input(pool_wrapper):
    results = pool_wrapper.map(square, [])
    assert results == []

def test_boundary_values(pool_wrapper):
    # Test with boundary values such as very large numbers or small negative numbers
    results = pool_wrapper.map(square, [10**9, -10, 0, 3])
    expected_results = [10**18, 100, 0, 9]
    assert results == expected_results

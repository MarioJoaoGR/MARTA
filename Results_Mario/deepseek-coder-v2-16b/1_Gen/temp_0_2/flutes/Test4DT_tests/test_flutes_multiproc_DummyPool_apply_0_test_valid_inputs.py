
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

def initializer_func(*args):
    pass

@pytest.fixture(scope="module")
def dummy_pool():
    return DummyPool(processes=0, initializer=initializer_func, initargs=())

def test_apply_valid_inputs(dummy_pool):
    result = dummy_pool.apply(lambda x, y: x + y, args=(1, 2))
    assert result == 3

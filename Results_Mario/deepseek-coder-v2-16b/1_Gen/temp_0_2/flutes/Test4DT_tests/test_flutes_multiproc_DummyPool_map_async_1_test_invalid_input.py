
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

@pytest.fixture(scope="module")
def dummy_pool():
    return DummyPool(processes=0)

def test_invalid_input(dummy_pool):
    with pytest.raises(TypeError):
        # This should raise a TypeError because the initializer function is not callable
        dummy_pool.map_async("not_a_function", [1, 2, 3])

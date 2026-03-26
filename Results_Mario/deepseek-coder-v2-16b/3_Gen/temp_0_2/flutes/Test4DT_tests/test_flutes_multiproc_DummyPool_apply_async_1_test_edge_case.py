
import pytest
from flutes.multiproc import DummyPool

@pytest.fixture
def pool():
    return DummyPool(processes=0)

def test_apply_async_with_initializer(pool):
    def initializer_func(*args):
        pass  # Placeholder for actual initialization logic
    
    pool = DummyPool(processes=0, initializer=initializer_func, initargs=((),))
    result = pool.apply_async(lambda x: x * 2, args=(5,))
    assert result.get() == 10

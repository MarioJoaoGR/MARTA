
import pytest
from flutes.multiproc import DummyPool

def my_initializer(*args):
    pass

@pytest.fixture
def valid_pool():
    return DummyPool(processes=4, initializer=my_initializer, initargs=())

def test_valid_inputs(valid_pool):
    assert isinstance(valid_pool, DummyPool)

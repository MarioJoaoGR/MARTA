
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

@pytest.fixture(scope="module")
def dummy_pool():
    return DummyPool(processes=0)

def test_dummy_pool_enter(dummy_pool):
    assert isinstance(dummy_pool.__enter__(), DummyPool)

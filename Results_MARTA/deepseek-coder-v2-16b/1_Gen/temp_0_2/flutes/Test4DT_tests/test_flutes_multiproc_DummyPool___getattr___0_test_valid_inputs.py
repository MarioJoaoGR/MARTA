
import pytest
from unittest.mock import patch, MagicMock
from multiprocessing import Pool
from flutes.multiproc import DummyPool

@pytest.fixture(autouse=True)
def mock_mp():
    with patch('flutes.multiproc.DummyPool._no_op', return_value=MagicMock()):
        yield

def test_valid_inputs():
    pool = DummyPool(processes=0)
    assert isinstance(pool, DummyPool)

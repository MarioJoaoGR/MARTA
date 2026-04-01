
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

def test_valid_input():
    # Test creating a DummyPool with valid parameters, including processes set to 0 for single-threaded execution
    pool = DummyPool(processes=0)
    assert isinstance(pool, DummyPool), "Expected an instance of DummyPool"

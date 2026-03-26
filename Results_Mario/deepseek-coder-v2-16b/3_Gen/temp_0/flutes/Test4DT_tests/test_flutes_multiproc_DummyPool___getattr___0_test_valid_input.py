
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

def test_valid_input():
    pool = DummyPool(processes=0)
    assert isinstance(pool, DummyPool), "Expected a DummyPool instance"


import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

def test_valid_case():
    # Test that the DummyPool can be instantiated with valid parameters
    pool = DummyPool(processes=4)
    assert isinstance(pool, DummyPool), "Expected a DummyPool instance"

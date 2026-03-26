
import pytest
from flutes.multiproc import DummyPool

def test_valid_inputs():
    # Test that the pool can be created with valid inputs and processes set to 0
    pool = DummyPool(processes=0)
    assert isinstance(pool, DummyPool), "Expected a DummyPool instance"

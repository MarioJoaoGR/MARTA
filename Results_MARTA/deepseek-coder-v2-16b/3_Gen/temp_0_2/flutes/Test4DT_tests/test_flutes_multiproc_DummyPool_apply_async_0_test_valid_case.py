
import pytest
from flutes.multiproc import DummyPool

def test_valid_case():
    pool = DummyPool(processes=0)
    assert isinstance(pool, DummyPool)


import pytest
from pytutils.sets import MetaSet
import attr
import random

@pytest.fixture(scope="module")
def meta_set():
    ms = MetaSet()
    yield ms

def test_valid_inputs(meta_set):
    # Test adding a list of valid inputs
    lst = [1, 2, 3]
    meta_set.update(lst)
    assert len(meta_set._store) == 3

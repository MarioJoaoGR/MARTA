
import pytest
from pytutils.sets import MetaSet
import random
import attr

@pytest.fixture(scope="module")
def meta_set():
    return MetaSet()

def test_valid_inputs(meta_set):
    lst = [1, 2, 3]
    meta_set.update(lst)
    assert len(meta_set._store) == 3

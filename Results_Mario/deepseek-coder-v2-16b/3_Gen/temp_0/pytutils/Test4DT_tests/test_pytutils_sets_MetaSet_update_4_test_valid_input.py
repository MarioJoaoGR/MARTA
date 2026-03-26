
import pytest
from pytutils.sets import MetaSet
import attr
import random

@pytest.fixture
def meta_set():
    return MetaSet()

def test_valid_input(meta_set):
    lst = [1, 2, 3, 4]
    meta_set.update(lst)
    assert set(lst) == meta_set._store

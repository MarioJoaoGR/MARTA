
import pytest
from pytutils.sets import MetaSet
import attr
import random

# Mocking the consume function (assuming it's not available in standard library)
def consume(iterator):
    for _ in iterator:
        pass

@pytest.fixture
def meta_set():
    return MetaSet()

def test_valid_input(meta_set):
    lst = [1, 2, 3, 4]
    meta_set.update(lst)
    assert set(lst) == meta_set._store

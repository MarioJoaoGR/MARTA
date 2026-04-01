
import pytest
from pytutils.sets import MetaSet
import attr
import random

@pytest.fixture
def meta_set():
    return MetaSet()

def test_update_with_none(meta_set):
    with pytest.raises(TypeError):
        meta_set.update(None)

def test_update_with_empty_list(meta_set):
    meta_set.update([])
    assert len(meta_set._store) == 0

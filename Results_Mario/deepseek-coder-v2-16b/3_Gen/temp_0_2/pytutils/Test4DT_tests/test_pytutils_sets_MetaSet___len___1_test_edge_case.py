
import pytest
from pytutils.sets import MetaSet

@pytest.fixture
def meta_set():
    return MetaSet()

def test_len(meta_set):
    assert len(meta_set) == 0
    meta_set._store.add("example_value")
    assert len(meta_set) == 1

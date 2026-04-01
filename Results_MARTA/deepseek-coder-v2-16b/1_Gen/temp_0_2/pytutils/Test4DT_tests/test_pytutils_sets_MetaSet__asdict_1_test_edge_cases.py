
import pytest
from pytutils.sets import MetaSet

@pytest.fixture
def meta_set():
    return MetaSet()

def test_edge_cases(meta_set):
    assert hasattr(meta_set, '_store')
    assert isinstance(meta_set._store, set)
    assert hasattr(meta_set, '_meta')
    assert isinstance(meta_set._meta, dict)
    assert meta_set._initial is None

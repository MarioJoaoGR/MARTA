
import pytest
from pytutils.sets import MetaSet

@pytest.fixture
def meta_set():
    return MetaSet()

def test_update(meta_set):
    lst = [1, 2, 3, 4]
    meta_set._initial = lst
    meta_set.__attrs_post_init__()
    
    assert len(meta_set._store) == len(lst), f"Expected store length to be {len(lst)}, but got {len(meta_set._store)}"

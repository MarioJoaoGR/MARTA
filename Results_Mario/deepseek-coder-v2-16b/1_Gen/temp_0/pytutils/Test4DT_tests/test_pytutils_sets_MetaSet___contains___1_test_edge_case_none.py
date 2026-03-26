
import pytest
from pytutils.sets import MetaSet

@pytest.fixture
def meta_set():
    return MetaSet()

def test_edge_case_none(meta_set):
    # Add an item to the set
    meta_set._store.add(1)
    
    # Check if the item is in the set
    assert 1 in meta_set
    
    # Check if a non-existing item is not in the set
    assert None not in meta_set

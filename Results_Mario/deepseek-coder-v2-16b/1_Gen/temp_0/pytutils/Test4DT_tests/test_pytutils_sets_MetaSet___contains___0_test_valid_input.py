
import pytest
from pytutils.sets import MetaSet

@pytest.fixture
def meta_set():
    return MetaSet()

def test_valid_input(meta_set):
    # Add an item to the set
    meta_set._store.add(1)
    
    # Check if the item is in the set
    assert 1 in meta_set

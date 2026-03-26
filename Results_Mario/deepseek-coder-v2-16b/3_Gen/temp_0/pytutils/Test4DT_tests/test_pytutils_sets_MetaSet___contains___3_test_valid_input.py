
import pytest
from pytutils.sets import MetaSet

@pytest.fixture
def meta_set():
    return MetaSet()

def test_valid_input(meta_set):
    # Add an item to the set
    meta_set.add(1)
    
    # Check if the item is in the set
    assert 1 in meta_set
    
    # Check if a different item is not in the set
    assert 2 not in meta_set

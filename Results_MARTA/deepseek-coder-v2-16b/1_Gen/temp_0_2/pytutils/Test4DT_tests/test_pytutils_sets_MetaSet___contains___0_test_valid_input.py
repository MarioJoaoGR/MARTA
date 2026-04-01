
import pytest
from pytutils.sets import MetaSet

@pytest.fixture(scope="module")
def meta_set():
    return MetaSet()

def test_valid_input(meta_set):
    # Add an item to the set
    meta_set.add(1)
    
    # Check if the item is in the set
    assert 1 in meta_set
    
    # Remove the item from the set
    meta_set.remove(1)
    
    # Check if the item is not in the set after removal
    assert 1 not in meta_set

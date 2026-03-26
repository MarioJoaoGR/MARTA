
import pytest
from pytutils.sets import MetaSet
import attr
import random

@pytest.fixture
def meta_set():
    return MetaSet()

def test_valid_input(meta_set):
    # Add a value to the set
    meta_set._store.add(1)
    meta_set._meta[1] = 0  # Assign a timestamp for the added value
    
    # Check that the value is in the set and its metadata exists
    assert 1 in meta_set._store
    assert 1 in meta_set._meta
    
    # Discard the value
    meta_set.discard(1)
    
    # Check that the value has been removed from the set and its metadata has been deleted
    assert 1 not in meta_set._store
    with pytest.raises(KeyError):
        meta_set._meta.pop(1)


import pytest
from pytutils.sets import MetaSet
import random
import attr

@pytest.fixture
def meta_set():
    return MetaSet()

def test_valid_input(meta_set):
    # Add a value to the set
    value = 1
    meta_set._store.add(value)
    meta_set._meta[value] = random.randint(0, 1)
    
    # Discard the value
    meta_set.discard(value)
    
    # Check if the value is removed from both _store and _meta
    assert value not in meta_set._store
    assert value not in meta_set._meta

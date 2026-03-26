
import pytest
from pytutils.sets import MetaSet
import random
import attr

@pytest.fixture
def meta_set():
    return MetaSet()

def test_missing_value(meta_set):
    # Add a value to the set
    value = 10
    meta_set._store.add(value)
    meta_set._meta[value] = random.randint(0, 1)
    
    # Attempt to discard a value that is not in the set
    meta_set.discard(20)
    
    # Check if the value was actually discarded
    assert value in meta_set._store
    assert value in meta_set._meta

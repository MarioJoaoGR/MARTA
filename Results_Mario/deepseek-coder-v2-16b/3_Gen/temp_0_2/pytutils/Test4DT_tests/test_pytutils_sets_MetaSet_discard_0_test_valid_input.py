
import pytest
from pytutils.sets import MetaSet
import attr
import random

@pytest.fixture
def meta_set():
    return MetaSet()

def test_valid_input(meta_set):
    # Add a value to the set
    initial_value = "test_value"
    meta_set._store.add(initial_value)
    assert initial_value in meta_set._store
    
    # Discard the added value
    meta_set.discard(initial_value)
    assert initial_value not in meta_set._store
    assert initial_value not in meta_set._meta

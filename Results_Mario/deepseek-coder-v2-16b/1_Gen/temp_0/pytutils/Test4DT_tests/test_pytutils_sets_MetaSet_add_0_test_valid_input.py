
import pytest
from pytutils.sets import MetaSet
import random
import attr

@pytest.fixture
def meta_set():
    return MetaSet()

def test_valid_input(meta_set):
    # Add a value to the MetaSet
    initial_value = 10
    meta_set.add(initial_value)
    
    # Check if the value is in the store and metadata dictionary
    assert initial_value in meta_set._store
    assert initial_value in meta_set._meta
    
    # Check if the metadata for the added value matches the output of _meta_func
    assert isinstance(meta_set._meta[initial_value], int)
    assert 0 <= meta_set._meta[initial_value] <= 1

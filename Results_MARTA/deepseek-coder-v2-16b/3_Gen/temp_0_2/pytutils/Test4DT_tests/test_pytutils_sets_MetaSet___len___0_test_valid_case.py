
import pytest
from pytutils.sets import MetaSet
import attr
import random

@pytest.fixture
def meta_set():
    return MetaSet()

def test_valid_case(meta_set):
    # Add a value to the set and check if it is added correctly
    initial_value = "example_value"
    meta_set._initial = initial_value
    meta_set.add(initial_value)
    
    # Check that the length of the set has increased by 1
    assert len(meta_set) == 1
    
    # Check that the value is in the set with the correct metadata
    assert initial_value in meta_set._store
    assert meta_set._meta[initial_value] is not None

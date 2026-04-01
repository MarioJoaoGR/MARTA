
import pytest
from pytutils.sets import MetaSet
import attr
import random

@pytest.fixture
def meta_set():
    return MetaSet()

def test_valid_input(meta_set):
    # Add a valid value to the set
    meta_set.add("example_value")
    
    # Check that the length of the set has increased by 1
    assert len(meta_set) == 1
    
    # Optionally, you can add more assertions to check specific properties of the MetaSet instance
    # For example, checking if the added value is in the store and has a timestamp:
    assert "example_value" in meta_set._store
    assert meta_set._meta["example_value"] is not None

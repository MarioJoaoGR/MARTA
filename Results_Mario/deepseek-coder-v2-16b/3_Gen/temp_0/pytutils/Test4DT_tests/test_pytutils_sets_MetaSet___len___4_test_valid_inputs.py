
import pytest
from pytutils.sets import MetaSet
import attr
import random

@pytest.fixture
def meta_set():
    return MetaSet()

def test_valid_inputs(meta_set):
    assert len(meta_set) == 0
    
    # Add some values to the set
    meta_set.add("value1")
    meta_set.add("value2")
    meta_set.add("value3")
    
    # Check if the length is correctly calculated
    assert len(meta_set) == 3

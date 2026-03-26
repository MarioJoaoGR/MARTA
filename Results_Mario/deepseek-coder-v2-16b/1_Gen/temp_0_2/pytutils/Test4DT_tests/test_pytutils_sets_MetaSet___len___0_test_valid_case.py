
import pytest
from pytutils.sets import MetaSet
import attr
import random

@pytest.fixture
def meta_set():
    return MetaSet()

def test_valid_case(meta_set):
    assert len(meta_set) == 0
    
    # Add an element to the set
    meta_set.add(1)
    assert len(meta_set) == 1
    
    # Add another element to the set
    meta_set.add(2)
    assert len(meta_set) == 2
    
    # Remove an element from the set
    meta_set.remove(1)
    assert len(meta_set) == 1

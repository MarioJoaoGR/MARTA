
import pytest
from pytutils.sets import MetaSet
import attr
import random

@pytest.fixture
def meta_set():
    return MetaSet()

def test_edge_case(meta_set):
    # Test with an empty set
    assert len(meta_set._store) == 0
    
    # Test adding a None value
    meta_set.add(None)
    assert None in meta_set
    
    # Test removing the None value
    meta_set.remove(None)
    assert None not in meta_set

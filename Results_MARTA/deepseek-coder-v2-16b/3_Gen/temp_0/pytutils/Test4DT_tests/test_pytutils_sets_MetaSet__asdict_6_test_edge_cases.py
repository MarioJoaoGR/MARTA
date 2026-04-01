
import pytest
from pytutils.sets import MetaSet
import random
import copy

@pytest.fixture(scope="module")
def meta_set():
    ms = MetaSet()
    return ms

def test_edge_cases(meta_set):
    # Add some values to the MetaSet
    value1 = 10
    value2 = 20
    meta_set._store.add(value1)
    meta_set._meta[value1] = random.randint(0, 1)
    meta_set._store.add(value2)
    meta_set._meta[value2] = random.randint(0, 1)
    
    # Check the metadata dictionary
    expected_metadata = {value1: meta_set._meta[value1], value2: meta_set._meta[value2]}
    assert meta_set._asdict() == expected_metadata

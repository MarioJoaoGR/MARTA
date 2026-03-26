
import pytest
from pytutils.sets import MetaSet
import random
import copy

@pytest.fixture
def meta_set():
    ms = MetaSet()
    return ms

def test_edge_cases(meta_set):
    # Add a value to the set and check if it is in the metadata dictionary
    initial_value = 10
    meta_set._store.add(initial_value)
    assert initial_value not in meta_set._meta
    
    # Generate a timestamp for the added value
    random.seed(0)  # Seed to ensure reproducibility for testing purposes
    expected_timestamp = random.randint(0, 1)
    meta_set._meta[initial_value] = expected_timestamp
    
    # Check if the metadata dictionary now contains the added value with its timestamp
    assert initial_value in meta_set._meta
    assert meta_set._meta[initial_value] == expected_timestamp
    
    # Test the _asdict method to ensure it returns a shallow copy of the internal `_meta` dictionary
    metadata_copy = meta_set._asdict()
    assert isinstance(metadata_copy, dict)
    assert len(metadata_copy) == 1
    assert list(metadata_copy.keys())[0] == initial_value


import pytest
import attr
import random
import copy
from pytutils.sets import MetaSet

@pytest.fixture(scope="module")
def meta_set():
    return MetaSet()

def test_valid_inputs(meta_set):
    # Add some values to the set
    meta_set._store = {1, 2, 3}
    meta_set._meta = {1: "timestamp1", 2: "timestamp2", 3: "timestamp3"}
    
    # Call _asdict method and get a shallow copy of _meta dictionary
    meta_copy = meta_set._asdict()
    
    # Check if the copied dictionary is indeed a shallow copy
    assert meta_copy == {1: "timestamp1", 2: "timestamp2", 3: "timestamp3"}
    assert meta_copy is not meta_set._meta
    assert all(isinstance(key, int) for key in meta_copy.keys())

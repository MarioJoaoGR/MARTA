
import pytest
import attr
import random
import copy
from pytutils.sets import MetaSet

@pytest.fixture
def meta_set():
    return MetaSet()

def test_valid_inputs(meta_set):
    # Add some values to the set
    meta_set._store = {1, 2, 3}
    meta_set._meta = {1: 'timestamp1', 2: 'timestamp2', 3: 'timestamp3'}
    
    # Call _asdict method and check if it returns a shallow copy of the internal _meta dictionary
    meta_dict = meta_set._asdict()
    assert isinstance(meta_dict, dict)
    assert len(meta_dict) == len(meta_set._meta)
    for key in meta_dict:
        assert key in meta_set._meta

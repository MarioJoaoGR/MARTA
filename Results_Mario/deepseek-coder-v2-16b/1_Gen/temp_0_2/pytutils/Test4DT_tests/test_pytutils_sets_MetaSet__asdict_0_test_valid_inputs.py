
import pytest
from pytutils.sets import MetaSet
import attr
import random
import copy

@pytest.fixture
def meta_set():
    return MetaSet()

def test_valid_inputs(meta_set):
    # Add a few valid inputs to the MetaSet
    meta_set.add(1)
    meta_set.add(2)
    
    # Check if the metadata dictionary has been updated correctly
    assert len(meta_set._meta) == 2
    assert all(isinstance(value, int) for value in meta_set._meta.values())
    
    # Check if the _asdict method returns a copy of the metadata dictionary
    meta_dict = meta_set._asdict()
    assert len(meta_dict) == 2
    assert all(isinstance(value, int) for value in meta_dict.values())

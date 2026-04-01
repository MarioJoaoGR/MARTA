
import pytest
from pytutils.sets import MetaSet
import random
import attr

@pytest.fixture
def meta_set():
    return MetaSet()

def test_valid_input(meta_set):
    # Seed the random number generator to ensure reproducibility
    random.seed(0)
    
    value = 1
    meta_set.add(value)
    
    assert value in meta_set._store
    assert value in meta_set._meta
    assert isinstance(meta_set._meta[value], int)
    assert 0 <= meta_set._meta[value] <= 1

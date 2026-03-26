
import pytest
from pytutils.sets import MetaSet
import attr
import random

@pytest.fixture
def meta_set():
    return MetaSet()

def test_valid_inputs(meta_set):
    # Add some values to the MetaSet
    meta_set.add(1)
    meta_set.add(2)
    
    # Check that the iteration works correctly
    expected_values = {1, 2}
    actual_values = set()
    
    for value in meta_set:
        actual_values.add(value)
    
    assert actual_values == expected_values

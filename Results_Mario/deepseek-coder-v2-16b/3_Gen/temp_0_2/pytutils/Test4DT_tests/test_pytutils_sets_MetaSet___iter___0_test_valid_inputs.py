
import pytest
from pytutils.sets import MetaSet

def test_valid_inputs():
    meta_set = MetaSet()
    values = [1, 2, 3]
    
    for value in values:
        meta_set.add(value)
    
    iterated_values = []
    for value in meta_set:
        iterated_values.append(value)
    
    assert sorted(iterated_values) == sorted(values)

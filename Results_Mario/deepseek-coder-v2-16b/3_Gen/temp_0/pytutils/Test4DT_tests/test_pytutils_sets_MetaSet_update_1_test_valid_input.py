
import pytest
from pytutils.sets import MetaSet

def test_valid_input():
    meta_set = MetaSet()
    lst = [1, 2, 3, 4]
    meta_set.update(lst)
    
    assert set(lst).issubset(meta_set._store)

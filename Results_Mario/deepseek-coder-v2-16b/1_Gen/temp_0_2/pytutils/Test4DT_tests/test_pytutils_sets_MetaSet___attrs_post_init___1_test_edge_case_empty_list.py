
import pytest
from pytutils.sets import MetaSet

def test_edge_case_empty_list():
    meta_set = MetaSet()
    lst = []
    meta_set.update(lst)
    assert len(meta_set._store) == 0, "Expected the set to be empty after updating with an empty list"


import pytest
from pytutils.sets import MetaSet

def test_edge_case():
    meta_set = MetaSet()
    # Adding None to the set, it should be ignored
    meta_set.discard(None)
    
    assert len(meta_set._store) == 0, "The set should not contain any elements after discarding None"

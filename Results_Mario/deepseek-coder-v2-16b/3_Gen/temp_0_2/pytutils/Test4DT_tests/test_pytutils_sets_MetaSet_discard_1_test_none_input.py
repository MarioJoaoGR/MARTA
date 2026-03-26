
import pytest
from pytutils.sets import MetaSet

def test_none_input():
    meta_set = MetaSet()
    
    # Attempt to discard None, which should not raise an error and do nothing
    meta_set.discard(None)
    
    # Check that the set is still empty
    assert len(meta_set._store) == 0
    # Check that the metadata dictionary has no entries
    assert len(meta_set._meta) == 0

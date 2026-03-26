
import pytest
from pytutils.sets import MetaSet

# Test initialization of MetaSet
def test_init_metaset():
    meta_set = MetaSet()
    assert hasattr(meta_set, '_store'), "MetaSet instance should have a _store attribute"
    assert isinstance(meta_set._store, set), "_store should be an instance of set"
    assert hasattr(meta_set, '_meta'), "MetaSet instance should have a _meta attribute"
    assert isinstance(meta_set._meta, dict), "_meta should be an instance of dict"
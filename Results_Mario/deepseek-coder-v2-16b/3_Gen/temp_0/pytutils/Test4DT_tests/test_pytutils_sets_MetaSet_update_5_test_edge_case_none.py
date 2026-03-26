
import pytest
from pytutils.sets import MetaSet

def test_edge_case_none():
    meta_set = MetaSet()
    
    with pytest.raises(TypeError):
        meta_set.update(None)

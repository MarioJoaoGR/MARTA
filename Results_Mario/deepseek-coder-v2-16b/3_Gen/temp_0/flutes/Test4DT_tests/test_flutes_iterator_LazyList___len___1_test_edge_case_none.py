
import pytest
from flutes.iterator import LazyList

def test_edge_case_none():
    with pytest.raises(TypeError):
        lazy_list = LazyList(None)

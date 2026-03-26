
import pytest
from flutes.iterator import LazyList

def test_edge_case_none():
    lazy_list = LazyList([])
    with pytest.raises(IndexError):
        lazy_list[0]


import pytest
from flutes.iterator import LazyList

def test_edge_case_empty_list():
    lazy_list = LazyList([])
    with pytest.raises(StopIteration):
        next(iter(lazy_list))

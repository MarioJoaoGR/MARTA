
import pytest
from flutes.iterator import LazyList

def test_edge_case_empty_list():
    lazy_list = LazyList([])
    with pytest.raises(IndexError):
        assert lazy_list[0]  # This should raise an IndexError because the list is empty

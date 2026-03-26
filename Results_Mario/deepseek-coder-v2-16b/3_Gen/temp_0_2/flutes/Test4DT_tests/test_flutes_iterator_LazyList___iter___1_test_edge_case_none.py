
from flutes.iterator import LazyList  # Importing LazyList from the correct module path
import pytest

def test_edge_case_none():
    lazy_list = LazyList([])
    iterator = iter(lazy_list)
    with pytest.raises(StopIteration):
        while True:
            next(iterator)

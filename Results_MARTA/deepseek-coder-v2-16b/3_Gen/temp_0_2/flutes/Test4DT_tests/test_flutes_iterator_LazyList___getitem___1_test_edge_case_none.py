
import pytest
from flutes.iterator import LazyList  # Assuming this is the correct module path

def test_edge_case_none():
    lazy_list = LazyList([])
    with pytest.raises(IndexError):
        item = lazy_list[0]  # This should raise an IndexError because the list is empty

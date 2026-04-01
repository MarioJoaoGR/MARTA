
import pytest
from flutes.iterator import LazyList

@pytest.fixture
def lazy_list():
    return LazyList([1, 2, 3, 4])

def test_edge_case_none(lazy_list):
    # Fetch until index None (which means fetch all elements)
    lazy_list._fetch_until(None)
    
    # Check if the list contains all elements
    assert len(lazy_list.list) == 4
    assert lazy_list.list == [1, 2, 3, 4]

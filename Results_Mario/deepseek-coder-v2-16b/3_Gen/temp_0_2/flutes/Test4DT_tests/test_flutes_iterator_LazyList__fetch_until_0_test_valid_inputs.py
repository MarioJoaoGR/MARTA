
import pytest
from flutes.iterator import LazyList  # Adjust the import according to your module structure

# Example iterable for testing
@pytest.fixture
def example_iterable():
    return [1, 2, 3, 4]

def test_lazy_list_fetch_until(example_iterable):
    lazy_list = LazyList(example_iterable)
    
    # Fetch until index 0 (should fetch only up to index 0)
    lazy_list._fetch_until(0)
    
    # Check if the list has been fetched correctly
    assert len(lazy_list.list) == 1
    assert lazy_list.list[0] == 1

def test_lazy_list_fetch_beyond(example_iterable):
    lazy_list = LazyList(example_iterable)
    
    # Fetch until beyond the last index (should fetch all elements)
    lazy_list._fetch_until(5)  # Asking for an index that doesn't exist, so it should fetch everything
    
    # Check if the list has been fetched correctly
    assert len(lazy_list.list) == 4
    assert lazy_list.list == [1, 2, 3, 4]

def test_lazy_list_fetch_negative_index(example_iterable):
    lazy_list = LazyList(example_iterable)
    
    # Fetch until a negative index (should be ignored and fetch normally)
    lazy_list._fetch_until(-1)  # Negative index should be ignored
    
    # Check if the list has been fetched correctly
    assert len(lazy_list.list) == 4
    assert lazy_list.list == [1, 2, 3, 4]

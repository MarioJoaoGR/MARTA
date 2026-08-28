
import pytest
from flutes.iterator import LazyList

def my_generator():
    for i in range(5):
        yield i * i

# Test case to cover line 268 where idx is negative
def test_negative_index_handling_in_fetch_until():
    lazy_list = LazyList(my_generator())
    
    # Access an element with a negative index after exhausting the list
    assert list(lazy_list) == [0, 1, 4, 9, 16]
    assert lazy_list[-1] == 16
    
    # Ensure that the internal list has only fetched up to the required elements
    assert len(lazy_list.list) == 5

# Test case to ensure that accessing a negative index does not fetch more than necessary
def test_negative_index_fetches_minimal_elements():
    lazy_list = LazyList(my_generator())
    
    # Access an element with a negative index after exhausting the list
    assert list(lazy_list) == [0, 1, 4, 9, 16]
    assert lazy_list[-2] == 9
    
    # Ensure that the internal list has only fetched up to the required elements
    assert len(lazy_list.list) == 5

# Test case to ensure that accessing a very large negative index fetches all elements
def test_large_negative_index_fetches_all_elements():
    lazy_list = LazyList(my_generator())
    
    # Access an element with a very large negative index after exhausting the list
    assert list(lazy_list) == [0, 1, 4, 9, 16]
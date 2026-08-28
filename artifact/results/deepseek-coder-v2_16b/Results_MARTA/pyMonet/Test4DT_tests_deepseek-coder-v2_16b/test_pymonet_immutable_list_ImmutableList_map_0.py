
import pytest
from pymonet.immutable_list import ImmutableList

# Test edge case where ImmutableList is empty

# Test mapping over a list with one element
def test_mapping_one_element():
    my_list = ImmutableList(head=2)
    
    def square(x):
        return x * x
    
    mapped_list = my_list.map(square)
    assert isinstance(mapped_list, ImmutableList)
    assert not mapped_list.is_empty
    assert mapped_list.head == 4
    assert mapped_list.tail is None

# Test mapping over a list with multiple elements
def test_mapping_multiple_elements():
    sub_list = ImmutableList(head=2, tail=ImmutableList(head=3))
    my_list = ImmutableList(head=1, tail=sub_list)
    
    def square(x):
        return x * x
    
    mapped_list = my_list.map(square)
    assert isinstance(mapped_list, ImmutableList)
    assert not mapped_list.is_empty
    assert mapped_list.head == 1
    assert mapped_list.tail.head == 4
    assert mapped_list.tail.tail.head == 9
    assert mapped_list.tail.tail.tail is None
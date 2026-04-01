
import pytest
from pymonet.immutable_list import ImmutableList

def test_edge_cases():
    # Test with None, empty list, and boundary values
    empty_list = ImmutableList()
    
    # Append to an empty list
    new_list = empty_list.append(None)
    assert new_list.is_empty is False
    assert new_list.head is None
    
    # Append to a non-empty list
    list_with_one_element = ImmutableList(head=1)
    new_list = list_with_one_element.append(2)
    assert not new_list.is_empty
    assert new_list.head == 1
    assert new_list.tail.head == 2
    
    # Append to a non-empty list with multiple elements
    list_with_multiple_elements = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    new_list = list_with_multiple_elements.append(4)
    assert not new_list.is_empty
    assert new_list.head == 1
    assert new_list.tail.head == 2
    assert new_list.tail.tail.head == 3
    assert new_list.tail.tail.tail.head == 4
    
    # Append to a non-empty list with multiple elements and check immutability
    original = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    appended = original.append(4)
    assert original.tail.tail.head == 3  # Ensure the original list remains unchanged


# Module: pymonet.immutable_list
import pytest
from pymonet import ImmutableList

# Test the empty method to ensure it returns an empty instance of ImmutableList
def test_empty():
    empty_list = ImmutableList.empty()
    assert empty_list is not None, "Empty list should be created"
    assert empty_list.is_empty(), "The empty list should have is_empty set to True"
    assert empty_list.head is None, "The head of an empty list should be None"
    assert empty_list.tail is None, "The tail of an empty list should be None"

# Test the map method with a simple function that squares each element
def test_map():
    # Create a sample ImmutableList with elements 1, 2, and 3
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    
    # Define a function that squares its input
    def square(x):
        return x * x if x is not None else None
    
    # Apply the map function to the list
    mapped_list = list1.map(square)
    
    # Check that the new list has each element squared
    assert mapped_list.head == 1, "The head of the mapped list should be 1"
    assert mapped_list.tail.head == 4, "The second element in the mapped list should be 4 (2^2)"
    assert mapped_list.tail.tail.head == 9, "The third element in the mapped list should be 9 (3^2)"
    assert mapped_list.tail.tail.tail is None, "The tail of the last element in the mapped list should be None"

# Test the map method with a function that returns None for None inputs
def test_map_with_none():
    # Create a sample ImmutableList with elements 1 and None
    list_with_none = ImmutableList(head=1, tail=ImmutableList(head=None, tail=None))
    
    # Define a function that squares its input but returns None for None inputs
    def square_or_none(x):
        return x * x if x is not None else None
    
    # Apply the map function to the list
    mapped_list = list_with_none.map(square_or_none)
    
    # Check that the new list has each element squared and None remains None
    assert mapped_list.head == 1, "The head of the mapped list should be 1"
    assert mapped_list.tail.head is None, "The second element in the mapped list should still be None"
    assert mapped_list.tail.tail is None, "The tail of the last element in the mapped list should be None"

# Test the map method with an empty list
def test_map_with_empty_list():
    # Create an empty ImmutableList
    empty_list = ImmutableList()
    
    # Define a function that squares its input (which won't be used since the list is empty)
    def square(x):
        return x * x if x is not None else None
    
    # Apply the map function to the empty list
    mapped_list = empty_list.map(square)
    
    # Check that the new list remains empty and unchanged
    assert mapped_list.is_empty(), "The mapped list should still be empty"
    assert mapped_list.head is None, "The head of an empty mapped list should remain None"
    assert mapped_list.tail is None, "The tail of an empty mapped list should remain None"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList_map_0
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_map_0.py:4:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""
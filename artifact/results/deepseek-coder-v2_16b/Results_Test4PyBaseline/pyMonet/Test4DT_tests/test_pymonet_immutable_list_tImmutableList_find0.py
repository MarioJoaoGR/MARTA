# Module: pymonet.immutable_list
import pytest
from pymonet.immutable_list import ImmutableList

# Test cases for the find method in ImmutableList class
def test_find_element():
    # Create an immutable list with elements [1, 2, 3]
    lst = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    
    # Find the first element greater than 2
    result = lst.find(lambda x: x > 2)
    
    # Assert that the result is the expected value
    assert result == 3

def test_find_no_element():
    # Create an immutable list with elements [1, 2, 3]
    lst = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    
    # Find the first element greater than 3 (should not find any)
    result = lst.find(lambda x: x > 3)
    
    # Assert that the result is None
    assert result is None

def test_find_empty_list():
    # Create an empty immutable list
    lst = ImmutableList()
    
    # Find any element (should not find any in an empty list)
    result = lst.find(lambda x: True)
    
    # Assert that the result is None
    assert result is None

def test_find_single_element():
    # Create an immutable list with a single element [1]
    lst = ImmutableList(head=1)
    
    # Find any element (should find the only element in the list)
    result = lst.find(lambda x: True)
    
    # Assert that the result is 1
    assert result == 1

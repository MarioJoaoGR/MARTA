
import pytest
from pymonet.immutable_list import ImmutableList  # Assuming the module is named correctly

def test_reduce_edge_case():
    # Create an empty ImmutableList instance
    empty_list = ImmutableList()
    
    # Define a reducer function that adds elements
    def add(acc, x): return acc + x
    
    # Test reduce on an empty list
    assert empty_list.reduce(add, 0) == 0
    
    # Create a non-empty ImmutableList instance
    lst = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, is_empty=False)))
    
    # Test reduce on the list [1, 2, 3]
    assert lst.reduce(add, 0) == 6  # 1 + 2 + 3 = 6

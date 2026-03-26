
import pytest
from pymonet.immutable_list import ImmutableList

def test_edge_case():
    # Test edge cases for __len__ method
    
    # Empty list should have length 0
    empty_list = ImmutableList()
    assert len(empty_list) == 0
    
    # List with one element should have length 1
    single_element_list = ImmutableList(head=1)
    assert len(single_element_list) == 1
    
    # List with multiple elements should have correct length
    multi_element_list = ImmutableList(head=1, tail=ImmutableList(head=2))
    assert len(multi_element_list) == 2

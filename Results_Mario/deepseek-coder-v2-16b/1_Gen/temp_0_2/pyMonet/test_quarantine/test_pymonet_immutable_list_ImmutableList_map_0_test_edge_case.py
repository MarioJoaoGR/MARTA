
from pymonet import ImmutableList
import pytest

def test_map():
    # Create an immutable list with elements 1, 2, 3
    my_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, is_empty=False)))
    
    # Map the function that doubles each element
    mapped_list = my_list.map(lambda x: x * 2)
    
    # Check if the head and elements in the tail are doubled correctly
    assert mapped_list.head == 2
    assert mapped_list.tail.head == 4
    assert mapped_list.tail.tail.head == 6
    assert mapped_list.tail.tail.is_empty is False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList_map_0_test_edge_case
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_map_0_test_edge_case.py:2:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""
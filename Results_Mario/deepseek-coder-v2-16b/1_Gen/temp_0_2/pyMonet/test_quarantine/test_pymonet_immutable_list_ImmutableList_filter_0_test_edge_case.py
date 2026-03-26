
from pymonet import ImmutableList
import pytest

def test_filter_edge_case():
    # Create an empty list
    empty_list = ImmutableList()
    
    # Filtering on an empty list should return an empty list
    filtered_empty_list = empty_list.filter(lambda x: True)
    assert isinstance(filtered_empty_list, ImmutableList)
    assert filtered_empty_list.is_empty is True

    # Create a non-empty list with elements 1, 2, 3
    my_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, is_empty=False)))
    
    # Filtering out even numbers should result in an empty list
    filtered_list = my_list.filter(lambda x: x % 2 != 0)
    assert isinstance(filtered_list, ImmutableList)
    assert filtered_list.is_empty is True

    # Create a non-empty list with elements 1, 2, 3, 4
    my_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=ImmutableList(head=4, is_empty=False))))
    
    # Filtering out odd numbers should result in a list with elements 2 and 4
    filtered_list = my_list.filter(lambda x: x % 2 == 0)
    assert isinstance(filtered_list, ImmutableList)
    assert filtered_list.head == 2
    assert filtered_list.tail.head == 4
    assert filtered_list.tail.is_empty is False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList_filter_0_test_edge_case
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_filter_0_test_edge_case.py:2:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""
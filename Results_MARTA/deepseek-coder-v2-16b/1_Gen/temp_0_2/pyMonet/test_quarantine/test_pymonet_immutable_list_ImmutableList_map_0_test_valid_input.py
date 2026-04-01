
import pytest
from pymonet import ImmutableList  # Assuming the module name is correctly imported as 'pymonet'

def test_valid_input():
    # Create an immutable list with elements 1, 2, 3
    my_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, is_empty=False)))
    
    # Map a function over the list
    mapped_list = my_list.map(lambda x: x * 2)
    
    # Check that the original list remains unchanged
    assert my_list.head == 1
    assert my_list.tail.head == 2
    assert my_list.tail.tail.head == 3
    
    # Check that the mapped list has the correct elements
    assert mapped_list.head == 2
    assert mapped_list.tail.head == 4
    assert mapped_list.tail.tail.head == 6

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList_map_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_map_0_test_valid_input.py:3:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""
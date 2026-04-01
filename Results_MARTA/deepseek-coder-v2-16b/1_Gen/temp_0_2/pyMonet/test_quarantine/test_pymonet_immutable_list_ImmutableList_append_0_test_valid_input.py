
import pytest
from pymonet import ImmutableList

def test_valid_input():
    # Create an empty list
    my_list = ImmutableList.empty()
    
    # Append a new element to the list
    new_list = my_list.append(1)
    
    # Check if the new list has the appended element
    assert not new_list.is_empty
    assert new_list.head == 1
    assert isinstance(new_list.tail, ImmutableList)
    assert new_list.tail.is_empty

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList_append_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_append_0_test_valid_input.py:3:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""
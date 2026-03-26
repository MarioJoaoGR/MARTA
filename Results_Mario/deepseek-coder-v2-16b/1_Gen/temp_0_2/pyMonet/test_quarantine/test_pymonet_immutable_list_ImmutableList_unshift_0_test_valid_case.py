
from pymonet import ImmutableList

def test_unshift_valid_case():
    # Create an initial immutable list with elements 1, 2, 3
    my_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, is_empty=False)))
    
    # Prepend a new element (0) to the list
    new_list = my_list.unshift(0)
    
    # Check if the new list has the correct structure and elements
    assert new_list.head == 0
    assert new_list.tail.head == 1
    assert new_list.tail.tail.head == 2
    assert new_list.tail.tail.tail.is_empty is False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList_unshift_0_test_valid_case
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_unshift_0_test_valid_case.py:2:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""
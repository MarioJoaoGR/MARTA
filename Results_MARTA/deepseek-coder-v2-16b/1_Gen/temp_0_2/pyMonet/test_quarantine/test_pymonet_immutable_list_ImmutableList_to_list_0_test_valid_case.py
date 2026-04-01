
from pymonet import ImmutableList
import pytest

def test_to_list_valid_case():
    # Create an immutable list with elements 1, 2, 3
    my_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, is_empty=False)))
    
    # Convert to a Python built-in list and check the result
    assert my_list.to_list() == [1, 2, 3]

def test_to_list_empty_case():
    # Create an empty immutable list
    empty_list = ImmutableList(is_empty=True)
    
    # Convert to a Python built-in list and check the result
    assert empty_list.to_list() == []

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList_to_list_0_test_valid_case
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_to_list_0_test_valid_case.py:2:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""
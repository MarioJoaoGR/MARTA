
from pymonet import ImmutableList
import pytest

def test_to_list_empty():
    empty_list = ImmutableList(is_empty=True)
    assert empty_list.to_list() == []

def test_to_list_single_element():
    single_element_list = ImmutableList(head=1, is_empty=False)
    assert single_element_list.to_list() == [1]

def test_to_list_multiple_elements():
    multiple_elements_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, is_empty=False)))
    assert multiple_elements_list.to_list() == [1, 2, 3]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList_to_list_0_test_edge_case
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_to_list_0_test_edge_case.py:2:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""
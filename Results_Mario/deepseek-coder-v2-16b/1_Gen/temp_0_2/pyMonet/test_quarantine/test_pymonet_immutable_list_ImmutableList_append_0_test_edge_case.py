
import pytest
from pymonet import ImmutableList

def test_append_to_empty_list():
    empty_list = ImmutableList()
    new_list = empty_list.append(1)
    assert not new_list.is_empty
    assert new_list.head == 1
    assert new_list.tail.is_empty

def test_append_to_non_empty_list():
    initial_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    new_list = initial_list.append(4)
    assert not new_list.is_empty
    assert new_list.head == 1
    assert new_list.tail.head == 2
    assert new_list.tail.tail.head == 3
    assert new_list.tail.tail.tail.head == 4
    assert new_list.tail.tail.tail.tail.is_empty

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList_append_0_test_edge_case
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_append_0_test_edge_case.py:3:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""
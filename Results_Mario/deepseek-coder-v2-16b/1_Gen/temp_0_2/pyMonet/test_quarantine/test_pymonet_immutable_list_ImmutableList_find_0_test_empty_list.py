
from pymonet import ImmutableList
import pytest

def test_empty_list():
    empty_lst = ImmutableList()
    assert empty_lst.find(lambda x: x == 1) is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList_find_0_test_empty_list
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_find_0_test_empty_list.py:2:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""
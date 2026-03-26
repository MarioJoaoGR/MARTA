
import pytest
from pymonet import ImmutableList

def add(acc, x):
    return acc + x

@pytest.fixture
def empty_list():
    return ImmutableList()

def test_empty_list_reduce(empty_list):
    assert empty_list.reduce(add, 0) == 0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList_reduce_1_test_edge_case
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_reduce_1_test_edge_case.py:3:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""

import pytest
from pymonet import ImmutableList

def add(acc, x):
    return acc + x

@pytest.fixture
def setup():
    lst = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, is_empty=False)))
    return lst

def test_valid_input(setup):
    assert setup.reduce(add, 0) == 6  # Expected output: 6 (1 + 2 + 3)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList_reduce_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_reduce_0_test_valid_input.py:3:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""
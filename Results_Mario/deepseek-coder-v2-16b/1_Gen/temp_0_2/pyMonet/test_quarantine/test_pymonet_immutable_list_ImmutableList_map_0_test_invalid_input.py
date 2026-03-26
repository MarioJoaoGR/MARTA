
from pymonet import ImmutableList
import pytest

def test_invalid_input():
    with pytest.raises(TypeError):
        empty_list = ImmutableList.empty()
        empty_list.head = 1  # This should raise a TypeError indicating immutability

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList_map_0_test_invalid_input
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_map_0_test_invalid_input.py:2:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""
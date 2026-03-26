
from pymonet import ImmutableList

def test_empty_creation():
    empty_list = ImmutableList.empty()
    assert empty_list.is_empty is True
    assert empty_list.head is None
    assert empty_list.tail is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList_empty_0_test_empty_creation
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_empty_0_test_empty_creation.py:2:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""
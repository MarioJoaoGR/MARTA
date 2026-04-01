
from pymonet import ImmutableList

def test_valid_case():
    # Create two empty instances of ImmutableList
    list1 = ImmutableList()
    list2 = ImmutableList()
    
    # Check that they are equal
    assert list1 == list2

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList___eq___0_test_valid_case
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___eq___0_test_valid_case.py:2:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""
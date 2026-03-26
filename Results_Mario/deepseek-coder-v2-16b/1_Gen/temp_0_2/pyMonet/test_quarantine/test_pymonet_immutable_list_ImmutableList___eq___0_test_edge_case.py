
from pymonet import ImmutableList

def test_edge_case():
    # Create an empty instance of ImmutableList
    empty_list = ImmutableList.empty()
    
    # Create another empty instance of ImmutableList to compare with
    another_empty_list = ImmutableList.empty()
    
    # Check if the two empty instances are equal
    assert empty_list == another_empty_list

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList___eq___0_test_edge_case
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___eq___0_test_edge_case.py:2:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""
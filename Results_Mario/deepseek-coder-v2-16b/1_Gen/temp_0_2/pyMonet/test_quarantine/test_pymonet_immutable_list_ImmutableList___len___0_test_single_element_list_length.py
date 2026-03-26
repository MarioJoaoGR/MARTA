
from pymonet import ImmutableList

def test_single_element_list_length():
    # Create a single element list
    my_list = ImmutableList(head=1)
    
    # Check the length of the list
    assert len(my_list) == 1

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList___len___0_test_single_element_list_length
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___len___0_test_single_element_list_length.py:2:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""
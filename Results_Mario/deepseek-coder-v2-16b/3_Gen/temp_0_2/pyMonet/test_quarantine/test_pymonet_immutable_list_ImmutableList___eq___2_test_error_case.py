
import pytest
from your_module import ImmutableList  # Replace 'your_module' with the actual module name where ImmutableList is defined

def test_error_case():
    non_list = 'not a list'
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(is_empty=True)))
    
    # Test equality with a non-list object
    assert not (list1 == non_list)  # This should fail since the comparison is invalid due to type mismatch

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList___eq___2_test_error_case
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___eq___2_test_error_case.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""
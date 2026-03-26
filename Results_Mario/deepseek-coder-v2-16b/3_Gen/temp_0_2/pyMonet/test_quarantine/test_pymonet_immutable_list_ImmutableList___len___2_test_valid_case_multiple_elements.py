
import pytest
from pymonent.immutable_list import ImmutableList

def test_valid_case_multiple_elements():
    multi_element_list = ImmutableList(head=1, tail=ImmutableList(head=2))
    assert len(multi_element_list) == 2

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList___len___2_test_valid_case_multiple_elements
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___len___2_test_valid_case_multiple_elements.py:3:0: E0401: Unable to import 'pymonent.immutable_list' (import-error)


"""
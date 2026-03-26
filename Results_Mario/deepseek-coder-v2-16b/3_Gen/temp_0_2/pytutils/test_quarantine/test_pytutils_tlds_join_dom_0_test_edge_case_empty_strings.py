
import pytest
from pytutils.tlds import join_dom

def test_edge_case_empty_strings():
    # Test when both strings are empty
    assert join_dom('', '') == ''
    
    # Test when the first string is empty
    assert join_dom('example', '') == 'example'
    
    # Test when the second string is empty
    assert join_dom('', 'com') == 'com'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_tlds_join_dom_0_test_edge_case_empty_strings
pytutils/Test4DT_tests/test_pytutils_tlds_join_dom_0_test_edge_case_empty_strings.py:3:0: E0611: No name 'join_dom' in module 'pytutils.tlds' (no-name-in-module)


"""
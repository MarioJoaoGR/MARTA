
import pytest
from pytutils.tlds import join_dom

def test_valid_input():
    assert join_dom('example', 'com') == 'com.example'
    assert join_dom('co', 'uk') == 'uk.co'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_tlds_join_dom_1_test_valid_input
pytutils/Test4DT_tests/test_pytutils_tlds_join_dom_1_test_valid_input.py:3:0: E0611: No name 'join_dom' in module 'pytutils.tlds' (no-name-in-module)


"""
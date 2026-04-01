
import pytest
from pytutils.tlds import join_dom

def test_empty_string():
    with pytest.raises(ValueError):
        assert join_dom('', '') == ''

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_tlds_join_dom_1_test_empty_string
pytutils/Test4DT_tests/test_pytutils_tlds_join_dom_1_test_empty_string.py:3:0: E0611: No name 'join_dom' in module 'pytutils.tlds' (no-name-in-module)


"""

import pytest
from pytutils.memo import CachedException

def test_edge_case_none():
    with pytest.raises(TypeError):
        CachedException()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_memo_CachedException___init___1_test_edge_case_none
pytutils/Test4DT_tests/test_pytutils_memo_CachedException___init___1_test_edge_case_none.py:7:8: E1120: No value for argument 'ex' in constructor call (no-value-for-parameter)


"""
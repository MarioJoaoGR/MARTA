
import pytest
from pymonet.maybe import Maybe

def test_edge_case_none():
    maybe_none = Maybe(value=None, is_nothing=True)
    either = maybe_none.to_either()
    assert isinstance(either, Left)
    assert either.value is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_maybe_Maybe_to_either_1_test_edge_case_none
pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_either_1_test_edge_case_none.py:8:30: E0602: Undefined variable 'Left' (undefined-variable)


"""
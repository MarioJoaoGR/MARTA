
import pytest
from pymonet.maybe import Maybe

def test_empty_case():
    maybe_empty = Maybe(None, True)
    either = maybe_empty.to_either()
    
    assert isinstance(either, Left)
    assert either.value is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_maybe_Maybe_to_either_1_test_empty_case
pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_either_1_test_empty_case.py:9:30: E0602: Undefined variable 'Left' (undefined-variable)


"""
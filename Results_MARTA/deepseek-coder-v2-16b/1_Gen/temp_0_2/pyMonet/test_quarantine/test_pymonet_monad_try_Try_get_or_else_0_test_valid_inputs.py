
import pytest
from pymonet.monad_try import Try

def test_valid_inputs():
    try = Try(10, True)
    assert try.value == 10
    assert try.is_success is True
    assert try.get_or_else(0) == 10

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_monad_try_Try_get_or_else_0_test_valid_inputs
pyMonet/Test4DT_tests/test_pymonet_monad_try_Try_get_or_else_0_test_valid_inputs.py:6:9: E0001: Parsing failed: 'expected ':' (Test4DT_tests.test_pymonet_monad_try_Try_get_or_else_0_test_valid_inputs, line 6)' (syntax-error)


"""
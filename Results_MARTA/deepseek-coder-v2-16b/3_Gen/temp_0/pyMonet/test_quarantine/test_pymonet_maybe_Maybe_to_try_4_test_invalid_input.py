
import pytest
from pymonet.monad_try import Try
from pymonet.maybe import Maybe

def test_invalid_input():
    # Test with valid input
    maybe_valid = Maybe(value="Hello", is_nothing=False)
    try_valid = maybe_valid.to_try()
    assert try_valid.is_success == True
    assert try_valid.value == "Hello"
    
    # Test with invalid input (None)
    maybe_invalid = Maybe(value=None, is_nothing=False)
    try_invalid = maybe_invalid.to_try()
    assert try_invalid.is_success == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_try_4_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Test with valid input
        maybe_valid = Maybe(value="Hello", is_nothing=False)
        try_valid = maybe_valid.to_try()
        assert try_valid.is_success == True
        assert try_valid.value == "Hello"
    
        # Test with invalid input (None)
        maybe_invalid = Maybe(value=None, is_nothing=False)
        try_invalid = maybe_invalid.to_try()
>       assert try_invalid.is_success == False
E       assert True == False
E        +  where True = <pymonet.monad_try.Try object at 0x7fc4e2839fd0>.is_success

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_try_4_test_invalid_input.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_try_4_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.08s ===============================
"""
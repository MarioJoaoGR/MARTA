
import pytest
from pymonet.either import Either, Left, Right
from pymonet.monad_try import Try

def test_valid_inputs():
    # Test with a Right value
    either_right = Either(Right(42))
    try_monad_right = either_right.to_try()
    assert try_monad_right.is_success(), "Expected is_success to be True for Right"

    # Test with a Left value
    either_left = Either(Left("error message"))
    try_monad_left = either_left.to_try()
    assert not try_monad_left.is_success(), "Expected is_success to be False for Left"

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

pyMonet/Test4DT_tests/test_pymonet_either_Either_to_try_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        # Test with a Right value
        either_right = Either(Right(42))
        try_monad_right = either_right.to_try()
>       assert try_monad_right.is_success(), "Expected is_success to be True for Right"
E       TypeError: 'NoneType' object is not callable

pyMonet/Test4DT_tests/test_pymonet_either_Either_to_try_0_test_valid_inputs.py:10: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_to_try_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.09s ===============================
"""
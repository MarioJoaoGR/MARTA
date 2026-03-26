
from pymonet.either import Either, Left, Right
import pytest

def test_invalid_inputs():
    # Test with an invalid input (Left)
    either_left = Either(Left("error message"))
    try_monad_left = either_left.to_try()
    assert not try_monad_left.is_success(), "Expected failure for Left value"

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

pyMonet/Test4DT_tests/test_pymonet_either_Either_to_try_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test with an invalid input (Left)
        either_left = Either(Left("error message"))
        try_monad_left = either_left.to_try()
>       assert not try_monad_left.is_success(), "Expected failure for Left value"
E       TypeError: 'NoneType' object is not callable

pyMonet/Test4DT_tests/test_pymonet_either_Either_to_try_0_test_invalid_inputs.py:9: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_to_try_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.08s ===============================
"""

from pymonet.either import Either, Right, Left
import pytest

def test_valid_input():
    # Test with a valid value in Right
    either_right = Either(Right(42))
    try_instance = either_right.to_try()
    assert try_instance.is_success(), "Expected success for Right value"

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

pyMonet/Test4DT_tests/test_pymonet_either_Either_to_try_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Test with a valid value in Right
        either_right = Either(Right(42))
        try_instance = either_right.to_try()
>       assert try_instance.is_success(), "Expected success for Right value"
E       TypeError: 'NoneType' object is not callable

pyMonet/Test4DT_tests/test_pymonet_either_Either_to_try_0_test_valid_input.py:9: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_to_try_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.06s ===============================
"""
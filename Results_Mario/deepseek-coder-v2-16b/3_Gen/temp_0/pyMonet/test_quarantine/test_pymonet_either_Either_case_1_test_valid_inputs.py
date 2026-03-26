
import pytest
from pymonet.either import Either, Left, Right

def test_valid_inputs():
    # Test creating a Left instance with an error message
    left_value = Either(Left("error message"))
    assert isinstance(left_value, Left)

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

pyMonet/Test4DT_tests/test_pymonet_either_Either_case_1_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        # Test creating a Left instance with an error message
        left_value = Either(Left("error message"))
>       assert isinstance(left_value, Left)
E       assert False
E        +  where False = isinstance(<pymonet.either.Either object at 0x7f355e036510>, Left)

pyMonet/Test4DT_tests/test_pymonet_either_Either_case_1_test_valid_inputs.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_case_1_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.08s ===============================
"""
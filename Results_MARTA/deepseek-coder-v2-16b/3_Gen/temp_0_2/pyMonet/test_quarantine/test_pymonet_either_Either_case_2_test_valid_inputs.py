
import pytest
from pymonet.either import Either, Right

def test_valid_inputs():
    # Test with a valid Right value
    either_right = Either(Right("success message"))
    assert either_right.case(lambda x: "Error!", lambda y: f"Success: {y}") == "Success: success message"

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

pyMonet/Test4DT_tests/test_pymonet_either_Either_case_2_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        # Test with a valid Right value
        either_right = Either(Right("success message"))
>       assert either_right.case(lambda x: "Error!", lambda y: f"Success: {y}") == "Success: success message"
E       AssertionError: assert 'Error!' == 'Success: success message'
E         
E         - Success: success message
E         + Error!

pyMonet/Test4DT_tests/test_pymonet_either_Either_case_2_test_valid_inputs.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_case_2_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.09s ===============================
"""
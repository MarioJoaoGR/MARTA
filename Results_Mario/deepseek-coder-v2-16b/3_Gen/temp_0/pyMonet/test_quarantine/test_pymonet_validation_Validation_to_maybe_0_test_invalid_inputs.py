
import pytest
from pymonet.validation import Validation
from pymonet.maybe import Maybe

# Test to check if an instance of Validation with errors returns a Nothing Maybe
def test_invalid_inputs():
    val = Validation(None, ["Error occurred"])
    maybe_val = val.to_maybe()
    assert maybe_val.is_nothing(), "Expected is_nothing() to be True for invalid inputs"

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

pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_maybe_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        val = Validation(None, ["Error occurred"])
        maybe_val = val.to_maybe()
>       assert maybe_val.is_nothing(), "Expected is_nothing() to be True for invalid inputs"
E       TypeError: 'bool' object is not callable

pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_maybe_0_test_invalid_inputs.py:10: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_maybe_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.08s ===============================
"""
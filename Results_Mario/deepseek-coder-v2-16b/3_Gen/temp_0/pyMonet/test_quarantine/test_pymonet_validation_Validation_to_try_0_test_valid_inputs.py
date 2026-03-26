
import pytest
from pymonet.monad_try import Try
from pymonet.validation import Validation

def test_valid_inputs():
    val = Validation("Success", [])
    assert val.to_try().is_success() == True

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

pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_try_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        val = Validation("Success", [])
>       assert val.to_try().is_success() == True
E       TypeError: 'bool' object is not callable

pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_try_0_test_valid_inputs.py:8: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_try_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.08s ===============================
"""
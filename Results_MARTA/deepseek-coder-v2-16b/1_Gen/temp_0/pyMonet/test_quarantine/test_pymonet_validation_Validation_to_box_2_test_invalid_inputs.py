
import pytest
from pymonet.validation import Validation

def test_invalid_inputs():
    val_invalid_input = Validation('Success', 'not a list')
    
    # Check that errors are accumulated correctly
    assert len(val_invalid_input.errors) == 1
    assert isinstance(val_invalid_input.errors, list)
    assert val_invalid_input.errors[0] == "errors must be a list"
    
    # Check that the value is not changed
    assert val_invalid_input.value == 'Success'

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

pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_box_2_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        val_invalid_input = Validation('Success', 'not a list')
    
        # Check that errors are accumulated correctly
>       assert len(val_invalid_input.errors) == 1
E       AssertionError: assert 10 == 1
E        +  where 10 = len('not a list')
E        +    where 'not a list' = <pymonet.validation.Validation object at 0x7f7d37954e90>.errors

pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_box_2_test_invalid_inputs.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_box_2_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.07s ===============================
"""
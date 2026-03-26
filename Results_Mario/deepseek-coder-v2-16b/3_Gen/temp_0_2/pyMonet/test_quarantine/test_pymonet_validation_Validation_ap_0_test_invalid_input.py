
import pytest
from pymonet.validation import Validation

def test_invalid_input(capsys):
    # Create a Validation instance with an initial value and empty list of errors
    val = Validation("initial_value", [])
    
    # Define a function that returns a Validation object based on some condition (always failing in this case)
    def check_value(v):
        return Validation(None, ["Value is too high"])
    
    # Applying the function to the Validation instance should result in an error
    new_val = val.ap(check_value)
    
    # Capture the output (errors) and ensure it matches the expected error message
    captured = capsys.readouterr()
    assert "Value is too high" in captured.out
    
    # Check that the value remains unchanged and errors are accumulated correctly
    assert new_val is None
    assert val.value == "initial_value"
    assert new_val.errors == ["Value is too high"]

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

pyMonet/Test4DT_tests/test_pymonet_validation_Validation_ap_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

capsys = <_pytest.capture.CaptureFixture object at 0x7f1abe8f5750>

    def test_invalid_input(capsys):
        # Create a Validation instance with an initial value and empty list of errors
        val = Validation("initial_value", [])
    
        # Define a function that returns a Validation object based on some condition (always failing in this case)
        def check_value(v):
            return Validation(None, ["Value is too high"])
    
        # Applying the function to the Validation instance should result in an error
        new_val = val.ap(check_value)
    
        # Capture the output (errors) and ensure it matches the expected error message
        captured = capsys.readouterr()
>       assert "Value is too high" in captured.out
E       AssertionError: assert 'Value is too high' in ''
E        +  where '' = CaptureResult(out='', err='').out

pyMonet/Test4DT_tests/test_pymonet_validation_Validation_ap_0_test_invalid_input.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_validation_Validation_ap_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.09s ===============================
"""
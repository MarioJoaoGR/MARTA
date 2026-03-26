
import pytest
from pymonet.validation import Validation

def test_edge_case():
    # Create a Validation instance with an initial value and empty list of errors
    val = Validation(10, [])
    
    # Define a function that returns a Validation object based on some condition
    def check_value(v):
        if v > 5:
            return Validation(None, ["Value is too high"])
        else:
            return Validation(v, [])
    
    # Apply the function to the Validation instance
    new_val = val.ap(check_value)
    
    # Check the result after applying the function
    assert new_val.value is None  # Since value > 5 triggers an error

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

pyMonet/Test4DT_tests/test_pymonet_validation_Validation_ap_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        # Create a Validation instance with an initial value and empty list of errors
        val = Validation(10, [])
    
        # Define a function that returns a Validation object based on some condition
        def check_value(v):
            if v > 5:
                return Validation(None, ["Value is too high"])
            else:
                return Validation(v, [])
    
        # Apply the function to the Validation instance
        new_val = val.ap(check_value)
    
        # Check the result after applying the function
>       assert new_val.value is None  # Since value > 5 triggers an error
E       assert 10 is None
E        +  where 10 = <pymonet.validation.Validation object at 0x7f0ea692fa50>.value

pyMonet/Test4DT_tests/test_pymonet_validation_Validation_ap_0_test_edge_case.py:20: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_validation_Validation_ap_0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.08s ===============================
"""
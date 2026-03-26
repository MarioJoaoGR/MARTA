
import pytest
from pymonet.either import Either, Right, Left

def test_valid_input():
    # Create a valid Right instance
    right_value = Right(42)
    either_right = Either(right_value)
    
    # Define mock functions for success and error handlers
    def handle_success(value):
        return f"Success value: {value}"
    
    def handle_error(value):
        return f"Handled error: {value}"
    
    # Test the case method with a valid Right instance
    result = either_right.case(handle_error, handle_success)
    assert result == "Success value: 42"

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

pyMonet/Test4DT_tests/test_pymonet_either_Either_case_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Create a valid Right instance
        right_value = Right(42)
        either_right = Either(right_value)
    
        # Define mock functions for success and error handlers
        def handle_success(value):
            return f"Success value: {value}"
    
        def handle_error(value):
            return f"Handled error: {value}"
    
        # Test the case method with a valid Right instance
        result = either_right.case(handle_error, handle_success)
>       assert result == "Success value: 42"
E       AssertionError: assert 'Handled erro...7f1140f9cf10>' == 'Success value: 42'
E         
E         - Success value: 42
E         + Handled error: <pymonet.either.Right object at 0x7f1140f9cf10>

pyMonet/Test4DT_tests/test_pymonet_either_Either_case_0_test_valid_input.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_case_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.06s ===============================
"""
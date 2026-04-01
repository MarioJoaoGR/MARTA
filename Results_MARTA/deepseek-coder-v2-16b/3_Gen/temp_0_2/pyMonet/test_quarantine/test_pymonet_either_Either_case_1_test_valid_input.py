
import pytest
from pymonet.either import Either, Right, Left

def test_valid_input():
    # Test with a valid input that should be encapsulated in a Right
    either = Either(Right("success"))
    
    # Mock functions to handle success and error cases
    def error_handler(_):
        raise AssertionError("This should not be called")
    
    def success_handler(value):
        assert value == "success"
        return "Success!"
    
    # Call the case method with the mock handlers
    result = either.case(error_handler, success_handler)
    assert result == "Success!"

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

pyMonet/Test4DT_tests/test_pymonet_either_Either_case_1_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Test with a valid input that should be encapsulated in a Right
        either = Either(Right("success"))
    
        # Mock functions to handle success and error cases
        def error_handler(_):
            raise AssertionError("This should not be called")
    
        def success_handler(value):
            assert value == "success"
            return "Success!"
    
        # Call the case method with the mock handlers
>       result = either.case(error_handler, success_handler)

pyMonet/Test4DT_tests/test_pymonet_either_Either_case_1_test_valid_input.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pyMonet/pymonet/either.py:35: in case
    return error(self.value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

_ = <pymonet.either.Right object at 0x7fd975111fd0>

    def error_handler(_):
>       raise AssertionError("This should not be called")
E       AssertionError: This should not be called

pyMonet/Test4DT_tests/test_pymonet_either_Either_case_1_test_valid_input.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_case_1_test_valid_input.py::test_valid_input
============================== 1 failed in 0.09s ===============================
"""
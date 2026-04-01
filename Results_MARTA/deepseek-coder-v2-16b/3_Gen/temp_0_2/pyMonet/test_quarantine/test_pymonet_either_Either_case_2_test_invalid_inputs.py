
import pytest
from pymonet.either import Either, Left, Right

def test_invalid_inputs():
    # Test case where error handler is called with an invalid input
    def error_handler(value):
        return "Error!"
    
    def success_handler(value):
        return value + 10
    
    either = Either(Left("error message"))  # Creating an instance of Either with a Left value (invalid input)
    assert either.case(error_handler, success_handler) == "Error!"
    
    # Test case where success handler is called with an invalid input
    either = Either(Right("example"))  # Creating an instance of Either with a Right value (valid input)
    try:
        result = either.case(error_handler, success_handler)
        assert result == "example" + 10  # This should not raise an error and the result should be calculated correctly
    except Exception as e:
        pytest.fail(f"Unexpected exception occurred: {e}")

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

pyMonet/Test4DT_tests/test_pymonet_either_Either_case_2_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test case where error handler is called with an invalid input
        def error_handler(value):
            return "Error!"
    
        def success_handler(value):
            return value + 10
    
        either = Either(Left("error message"))  # Creating an instance of Either with a Left value (invalid input)
        assert either.case(error_handler, success_handler) == "Error!"
    
        # Test case where success handler is called with an invalid input
        either = Either(Right("example"))  # Creating an instance of Either with a Right value (valid input)
        try:
            result = either.case(error_handler, success_handler)
>           assert result == "example" + 10  # This should not raise an error and the result should be calculated correctly
E           TypeError: can only concatenate str (not "int") to str

pyMonet/Test4DT_tests/test_pymonet_either_Either_case_2_test_invalid_inputs.py:20: TypeError

During handling of the above exception, another exception occurred:

    def test_invalid_inputs():
        # Test case where error handler is called with an invalid input
        def error_handler(value):
            return "Error!"
    
        def success_handler(value):
            return value + 10
    
        either = Either(Left("error message"))  # Creating an instance of Either with a Left value (invalid input)
        assert either.case(error_handler, success_handler) == "Error!"
    
        # Test case where success handler is called with an invalid input
        either = Either(Right("example"))  # Creating an instance of Either with a Right value (valid input)
        try:
            result = either.case(error_handler, success_handler)
            assert result == "example" + 10  # This should not raise an error and the result should be calculated correctly
        except Exception as e:
>           pytest.fail(f"Unexpected exception occurred: {e}")
E           Failed: Unexpected exception occurred: can only concatenate str (not "int") to str

pyMonet/Test4DT_tests/test_pymonet_either_Either_case_2_test_invalid_inputs.py:22: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_case_2_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.09s ===============================
"""
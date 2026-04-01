
import pytest
from pymonet.either import Either, Left, Right

def test_valid_input():
    either = Either(10)  # Creating an instance of Either with a value of 10
    
    def error_handler(value): return "Error!"  # Define an error handler function
    def success_handler(value): return value + 5  # Define a success handler function
    
    assert either.case(error_handler, success_handler) == "Error!"  # Output should be the result of calling error_handler since either is Left by default
    
    right_either = Either("Hello")  # Creating an instance of Either with a string value "Hello"
    assert right_either.case(error_handler, success_handler) == "Hello" + 5  # Output should be the result of calling success_handler since either is Right now

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
        either = Either(10)  # Creating an instance of Either with a value of 10
    
        def error_handler(value): return "Error!"  # Define an error handler function
        def success_handler(value): return value + 5  # Define a success handler function
    
        assert either.case(error_handler, success_handler) == "Error!"  # Output should be the result of calling error_handler since either is Left by default
    
        right_either = Either("Hello")  # Creating an instance of Either with a string value "Hello"
>       assert right_either.case(error_handler, success_handler) == "Hello" + 5  # Output should be the result of calling success_handler since either is Right now
E       TypeError: can only concatenate str (not "int") to str

pyMonet/Test4DT_tests/test_pymonet_either_Either_case_0_test_valid_input.py:14: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_case_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.06s ===============================
"""
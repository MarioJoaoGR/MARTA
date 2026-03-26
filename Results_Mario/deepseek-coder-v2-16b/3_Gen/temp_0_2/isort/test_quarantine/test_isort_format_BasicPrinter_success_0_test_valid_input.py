
from io import StringIO
import pytest
from isort.format import BasicPrinter

def test_valid_input():
    # Create a mock for TextIO to simulate file-like object
    output = StringIO()
    
    # Initialize the BasicPrinter with success and error messages
    printer = BasicPrinter(error='An error occurred', success='Operation successful', output=output)
    
    # Call the method under test
    printer.success('Hello, world!')
    
    # Check if the message was printed correctly
    assert 'Operation successful' in output.getvalue()
    assert 'Hello, world!' in output.getvalue()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Create a mock for TextIO to simulate file-like object
        output = StringIO()
    
        # Initialize the BasicPrinter with success and error messages
        printer = BasicPrinter(error='An error occurred', success='Operation successful', output=output)
    
        # Call the method under test
        printer.success('Hello, world!')
    
        # Check if the message was printed correctly
        assert 'Operation successful' in output.getvalue()
>       assert 'Hello, world!' in output.getvalue()
E       AssertionError: assert 'Hello, world!' in 'Operation successful\n'
E        +  where 'Operation successful\n' = <built-in method getvalue of _io.StringIO object at 0x7ff197c928c0>()
E        +    where <built-in method getvalue of _io.StringIO object at 0x7ff197c928c0> = <_io.StringIO object at 0x7ff197c928c0>.getvalue

isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0_test_valid_input.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.11s ===============================
"""
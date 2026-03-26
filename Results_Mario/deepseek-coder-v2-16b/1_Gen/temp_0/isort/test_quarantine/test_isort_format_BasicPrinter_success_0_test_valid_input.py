
import sys
from io import StringIO
import pytest
from isort.format import BasicPrinter

def test_valid_input():
    # Capture the original stdout
    stdout_original = sys.stdout
    
    # Create a buffer to capture output
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Initialize the BasicPrinter with valid messages
    printer = BasicPrinter(error='ERROR', success='SUCCESS')
    printer.success('Hello, world!')
    
    # Get the value from the buffer and reset stdout
    output = captured_output.getvalue().strip()
    sys.stdout = stdout_original
    
    # Assert that the output is as expected
    assert output == 'SUCCESS: Hello, world!'

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
        # Capture the original stdout
        stdout_original = sys.stdout
    
        # Create a buffer to capture output
        captured_output = StringIO()
        sys.stdout = captured_output
    
        # Initialize the BasicPrinter with valid messages
        printer = BasicPrinter(error='ERROR', success='SUCCESS')
        printer.success('Hello, world!')
    
        # Get the value from the buffer and reset stdout
        output = captured_output.getvalue().strip()
        sys.stdout = stdout_original
    
        # Assert that the output is as expected
>       assert output == 'SUCCESS: Hello, world!'
E       AssertionError: assert 'SUCCESS' == 'SUCCESS: Hello, world!'
E         
E         - SUCCESS: Hello, world!
E         + SUCCESS

isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0_test_valid_input.py:24: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.09s ===============================
"""
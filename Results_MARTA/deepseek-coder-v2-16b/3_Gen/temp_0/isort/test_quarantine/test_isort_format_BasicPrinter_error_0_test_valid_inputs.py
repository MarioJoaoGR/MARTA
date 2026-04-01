
from io import StringIO
import sys
import pytest
from isort.format import BasicPrinter

def test_print_success():
    # Create a mock output object to capture printed content
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Instantiate the BasicPrinter with success and error messages
    printer = BasicPrinter(error='ERROR', success='SUCCESS', output=captured_output)
    
    # Call the print_success method with a sample message
    printer.print_success("Completed successfully")
    
    # Reset sys.stdout to its original state
    sys.stdout = sys.__stdout__
    
    # Check if the captured output contains the expected success message
    assert "SUCCESS: Completed successfully" in captured_output.getvalue()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_format_BasicPrinter_error_0_test_valid_inputs
isort/Test4DT_tests/test_isort_format_BasicPrinter_error_0_test_valid_inputs.py:16:4: E1101: Instance of 'BasicPrinter' has no 'print_success' member (no-member)


"""
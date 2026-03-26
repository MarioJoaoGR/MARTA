
import pytest
from io import StringIO
import sys
from isort.format import BasicPrinter

# Test default output (sys.stdout) for success and error messages
def test_basicprinter_default_output():
    # Capture the standard output
    captured_out = StringIO()
    sys.stdout = captured_out
    
    # Create a BasicPrinter instance with default templates
    printer = BasicPrinter(error="An {error}: {message}", success="Operation {success}.")
    
    # Print a success message
    printer.success("Everything went well!")
    
    # Reset the standard output to its original value
    sys.stdout = sys.__stdout__
    
    # Check if the captured output matches the expected result
    assert captured_out.getvalue() == "Operation SUCCESS.: Everything went well!\n"

# Test custom output via StringIO for success and error messages
def test_basicprinter_custom_output():
    # Create a StringIO object for in-memory file handling
    output = StringIO()
    
    # Instantiate the class with the custom output
    printer = BasicPrinter(error="An {error}: {message}", success="Operation {success}.", output=output)
    
    # Print messages to the in-memory file
    printer.success("In-memory success message")
    printer.error("In-memory error message")
    
    # Check if the in-memory file content matches the expected result
    assert output.getvalue() == "Operation SUCCESS.: In-memory success message\nAn ERROR: In-memory error message\n"

# Test default output (sys.stdout) for success and error messages without providing templates
def test_basicprinter_default_output_no_templates():
    # Capture the standard output
    captured_out = StringIO()
    sys.stdout = captured_out
    
    # Create a BasicPrinter instance without providing templates
    with pytest.raises(TypeError):  # Expecting a TypeError since templates are missing
        printer = BasicPrinter()
    
    # Reset the standard output to its original value
    sys.stdout = sys.__stdout__

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_format_BasicPrinter_success_0
isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0.py:48:18: E1120: No value for argument 'error' in constructor call (no-value-for-parameter)
isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0.py:48:18: E1120: No value for argument 'success' in constructor call (no-value-for-parameter)


"""
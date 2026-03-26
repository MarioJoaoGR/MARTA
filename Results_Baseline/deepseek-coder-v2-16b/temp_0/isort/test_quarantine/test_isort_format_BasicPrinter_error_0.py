
# Module: isort.format
import sys
from io import StringIO
import pytest
from isort.format import BasicPrinter

# Test initialization with default output (sys.stdout)
def test_basicprinter_default_init():
    printer = BasicPrinter(error="An {error}: {message}", success="Operation {success}.")
    captured_output = StringIO()
    sys.stdout = captured_output
    
    printer.print_success("Everything went well!")
    assert captured_output.getvalue().strip() == "Operation SUCCESS.: Everything went well!"
    
    captured_stderr = StringIO()
    sys.stderr = captured_stderr
    printer.error("Something went wrong")
    assert captured_stderr.getvalue().strip() == "An ERROR: Something went wrong"
    
    # Reset stdout and stderr
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__

# Test initialization with custom error and success templates
def test_basicprinter_custom_templates():
    printer = BasicPrinter(error="An {error}: {message}", success="Operation {success}.")
    captured_stderr = StringIO()
    sys.stderr = captured_stderr
    
    printer.error("Something went wrong")
    assert captured_stderr.getvalue().strip() == "An ERROR: Something went wrong"
    
    # Reset stderr
    sys.stderr = sys.__stderr__

# Test initialization with custom output stream (StringIO)
def test_basicprinter_custom_output():
    output = StringIO()
    printer = BasicPrinter(error="An {error}: {message}", success="Operation {success}.", output=output)
    
    printer.print_success("In-memory success message")
    assert output.getvalue().strip() == "Operation SUCCESS.: In-memory success message"
    
    captured_stderr = StringIO()
    sys.stderr = captured_stderr
    printer.error("In-memory error message")
    assert captured_stderr.getvalue().strip() == "An ERROR: In-memory error message"
    
    # Reset stdout and stderr
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__

# Test diff_line method
def test_basicprinter_diff_line():
    printer = BasicPrinter(error="An {error}: {message}", success="Operation {success}.")
    captured_output = StringIO()
    sys.stdout = captured_output
    
    printer.diff_line("This is a sample line of text.")
    assert captured_output.getvalue().strip() == "This is a sample line of text."
    
    # Reset stdout
    sys.stdout = sys.__stdout__

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_format_BasicPrinter_error_0
isort/Test4DT_tests/test_isort_format_BasicPrinter_error_0.py:14:4: E1101: Instance of 'BasicPrinter' has no 'print_success' member (no-member)
isort/Test4DT_tests/test_isort_format_BasicPrinter_error_0.py:43:4: E1101: Instance of 'BasicPrinter' has no 'print_success' member (no-member)


"""
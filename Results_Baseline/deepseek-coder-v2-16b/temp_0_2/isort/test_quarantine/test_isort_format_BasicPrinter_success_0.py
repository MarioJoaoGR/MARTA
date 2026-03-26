
import pytest
from io import StringIO
from sys import stdout
from isort.format import BasicPrinter

# Test initialization with default output (stdout)
def test_basicprinter_default_output():
    captured_out = StringIO()
    original_stdout = stdout
    stdout = captured_out
    
    printer = BasicPrinter(error="An error occurred: {error} - {message}", success="Operation was successful: {success} - {message}")
    printer.print_success("Everything went well!")
    assert captured_out.getvalue().strip() == "Operation was successful: SUCCESS - Everything went well!"
    
    stdout = original_stdout
    captured_out.seek(0)  # Reset the buffer to read from the beginning
    printer.print_error("Failed to connect to database")
    assert captured_out.getvalue().strip() == "An error occurred: ERROR - Failed to connect to database"

# Test initialization with custom output (file)
def test_basicprinter_custom_output():
    log_file = StringIO()
    printer = BasicPrinter(error="An error occurred: {error} - {message}", success="Operation was successful: {success} - {message}", output=log_file)
    printer.print_success("Everything went well!")
    assert log_file.getvalue().strip() == "Operation was successful: SUCCESS - Everything went well!"
    
    log_file.seek(0)  # Reset the buffer to read from the beginning
    printer.print_error("Failed to connect to database")
    assert log_file.getvalue().strip() == "An error occurred: ERROR - Failed to connect to database"

# Test using placeholders in messages
def test_basicprinter_placeholders():
    captured_out = StringIO()
    original_stdout = stdout
    stdout = captured_out
    
    printer = BasicPrinter(error="An error occurred: {error} - {message}", success="Operation was successful: {success} - {message}")
    printer.print_success("Everything went well!")
    assert captured_out.getvalue().strip() == "Operation was successful: SUCCESS - Everything went well!"
    
    stdout = original_stdout
    captured_out.seek(0)  # Reset the buffer to read from the beginning
    printer.print_error("Failed to connect to database")
    assert captured_out.getvalue().strip() == "An error occurred: ERROR - Failed to connect to database"

# Test success method with custom output
def test_basicprinter_success_method():
    log_file = StringIO()
    printer = BasicPrinter(error="An error occurred: {error} - {message}", success="Operation was successful: {success} - {message}", output=log_file)
    printer.success("Everything went well!")
    assert log_file.getvalue().strip() == "Operation was successful: SUCCESS - Everything went well!"
    
    log_file.seek(0)  # Reset the buffer to read from the beginning
    printer.print_error("Failed to connect to database")
    assert log_file.getvalue().strip() == "An error occurred: ERROR - Failed to connect to database"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_format_BasicPrinter_success_0
isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0.py:10:22: E0601: Using variable 'stdout' before assignment (used-before-assignment)
isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0.py:14:4: E1101: Instance of 'BasicPrinter' has no 'print_success' member (no-member)
isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0.py:19:4: E1101: Instance of 'BasicPrinter' has no 'print_error' member (no-member)
isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0.py:26:4: E1101: Instance of 'BasicPrinter' has no 'print_success' member (no-member)
isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0.py:30:4: E1101: Instance of 'BasicPrinter' has no 'print_error' member (no-member)
isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0.py:36:22: E0601: Using variable 'stdout' before assignment (used-before-assignment)
isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0.py:40:4: E1101: Instance of 'BasicPrinter' has no 'print_success' member (no-member)
isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0.py:45:4: E1101: Instance of 'BasicPrinter' has no 'print_error' member (no-member)
isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0.py:56:4: E1101: Instance of 'BasicPrinter' has no 'print_error' member (no-member)


"""
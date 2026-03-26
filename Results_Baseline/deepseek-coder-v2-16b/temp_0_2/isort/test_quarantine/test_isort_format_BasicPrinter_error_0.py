
# Module: isort.format
import pytest
from sys import stdout
from io import StringIO
from isort.format import BasicPrinter

# Test initialization with default output (stdout)
def test_basicprinter_init_default_output():
    printer = BasicPrinter(error="An error occurred: {error} - {message}", success="Operation was successful: {success} - {message}")
    assert printer.error_message == "An error occurred: {error} - {message}"
    assert printer.success_message == "Operation was successful: {success} - {message}"
    assert printer.output == stdout

# Test initialization with specified output (StringIO)
def test_basicprinter_init_specified_output():
    output = StringIO()
    printer = BasicPrinter(error="An error occurred: {error} - {message}", success="Operation was successful: {success} - {message}", output=output)
    assert printer.error_message == "An error occurred: {error} - {message}"
    assert printer.success_message == "Operation was successful: {success} - {message}"
    assert printer.output == output

# Test print_success method with default output (stdout)
def test_print_success(capsys):
    printer = BasicPrinter(error="An error occurred: {error} - {message}", success="Operation was successful: {success} - {message}")
    printer.print_success("Everything went well!")
    captured = capsys.readouterr()
    assert captured.out == "Operation was successful: Everything went well!\n"

# Test print_error method with default output (stdout)
def test_print_error(capsys):
    printer = BasicPrinter(error="An error occurred: {error} - {message}", success="Operation was successful: {success} - {message}")
    printer.print_error("Failed to connect to database")
    captured = capsys.readouterr()
    assert captured.err == "An error occurred: Failed to connect to database\n"

# Test print_success method with specified output (StringIO)
def test_print_success_specified_output():
    output = StringIO()
    printer = BasicPrinter(error="An error occurred: {error} - {message}", success="Operation was successful: {success} - {message}", output=output)
    printer.print_success("Everything went well!")
    assert output.getvalue() == "Operation was successful: Everything went well!\n"

# Test print_error method with specified output (StringIO)
def test_print_error_specified_output():
    output = StringIO()
    printer = BasicPrinter(error="An error occurred: {error} - {message}", success="Operation was successful: {success} - {message}", output=output)
    printer.print_error("Failed to connect to database")
    assert output.getvalue() == "An error occurred: Failed to connect to database\n"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_format_BasicPrinter_error_0
isort/Test4DT_tests/test_isort_format_BasicPrinter_error_0.py:26:4: E1101: Instance of 'BasicPrinter' has no 'print_success' member (no-member)
isort/Test4DT_tests/test_isort_format_BasicPrinter_error_0.py:33:4: E1101: Instance of 'BasicPrinter' has no 'print_error' member (no-member)
isort/Test4DT_tests/test_isort_format_BasicPrinter_error_0.py:41:4: E1101: Instance of 'BasicPrinter' has no 'print_success' member (no-member)
isort/Test4DT_tests/test_isort_format_BasicPrinter_error_0.py:48:4: E1101: Instance of 'BasicPrinter' has no 'print_error' member (no-member)


"""
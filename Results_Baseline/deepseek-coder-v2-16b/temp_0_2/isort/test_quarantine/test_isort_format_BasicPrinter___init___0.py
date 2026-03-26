
# Module: isort.format
import pytest
from io import StringIO
from isort.format import BasicPrinter

# Test cases for BasicPrinter class
def test_basic_printer_default_output():
    output = StringIO()
    printer = BasicPrinter(error="An error occurred", success="Operation successful", output=output)
    printer.print_success("Everything is fine!")
    assert output.getvalue().strip() == "Operation successful: Everything is fine!"

def test_basic_printer_custom_output():
    output = StringIO()
    printer = BasicPrinter(error="An error occurred", success="Operation successful", output=output)
    printer.print_error("Something went wrong!")
    assert output.getvalue().strip() == "An error occurred: Something went wrong!"

def test_basic_printer_default_error():
    output = StringIO()
    printer = BasicPrinter(error="Default Error", success="Operation successful", output=output)
    printer.print_success("Everything is fine!")
    assert output.getvalue().strip() == "Operation successful: Everything is fine!"

def test_basic_printer_default_success():
    output = StringIO()
    printer = BasicPrinter(error="Default Error", success="Default Success", output=output)
    printer.print_error("Something went wrong!")
    assert output.getvalue().strip() == "Default Error: Something went wrong!"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_format_BasicPrinter___init___0
isort/Test4DT_tests/test_isort_format_BasicPrinter___init___0.py:11:4: E1101: Instance of 'BasicPrinter' has no 'print_success' member (no-member)
isort/Test4DT_tests/test_isort_format_BasicPrinter___init___0.py:17:4: E1101: Instance of 'BasicPrinter' has no 'print_error' member (no-member)
isort/Test4DT_tests/test_isort_format_BasicPrinter___init___0.py:23:4: E1101: Instance of 'BasicPrinter' has no 'print_success' member (no-member)
isort/Test4DT_tests/test_isort_format_BasicPrinter___init___0.py:29:4: E1101: Instance of 'BasicPrinter' has no 'print_error' member (no-member)


"""
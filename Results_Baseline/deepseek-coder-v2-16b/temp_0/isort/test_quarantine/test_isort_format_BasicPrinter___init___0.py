
# Module: isort.format
import pytest
from io import StringIO
import sys
from isort.format import BasicPrinter

# Fixture to capture stdout
@pytest.fixture
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = new_out, new_err
    yield sys.stdout, sys.stderr
    sys.stdout, sys.stderr = old_out, old_err

def test_basic_printer_init(capsys):
    # Test initialization with default output (sys.stdout)
    printer = BasicPrinter(error='An error occurred', success='Operation successful')
    assert printer.error_message == 'An error occurred'
    assert printer.success_message == 'Operation successful'
    assert printer.output == sys.stdout

def test_basic_printer_print_success(capsys):
    # Test print_success method with a sample message
    expected_output = "Operation successful: Hello, world!\n"
    printer = BasicPrinter(error='An error occurred', success='Operation successful')
    printer.print_success('Hello, world!')
    captured = sys.stdout.getvalue().strip()
    assert captured == expected_output

def test_basic_printer_print_error(capsys):
    # Test print_error method with a sample message
    expected_output = "An error occurred: Something went wrong.\n"
    printer = BasicPrinter(error='An error occurred', success='Operation successful')
    printer.print_error('Something went wrong.')
    captured = sys.stdout.getvalue().strip()
    assert captured == expected_output

def test_basic_printer_custom_output(capsys):
    # Test initialization with a custom output (StringIO)
    output = StringIO()
    printer = BasicPrinter(error='An error occurred', success='Operation successful', output=output)
    printer.print_success('Hello, world!')
    assert output.getvalue().strip() == "Operation successful: Hello, world!\n"

def test_basic_printer_default_output(capsys):
    # Test initialization with default output (sys.stdout) and ensure it prints to stdout by default
    printer = BasicPrinter(error='An error occurred', success='Operation successful')
    printer.print_success('Hello, world!')
    captured = sys.stdout.getvalue().strip()
    assert captured == "Operation successful: Hello, world!\n"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_format_BasicPrinter___init___0
isort/Test4DT_tests/test_isort_format_BasicPrinter___init___0.py:28:4: E1101: Instance of 'BasicPrinter' has no 'print_success' member (no-member)
isort/Test4DT_tests/test_isort_format_BasicPrinter___init___0.py:36:4: E1101: Instance of 'BasicPrinter' has no 'print_error' member (no-member)
isort/Test4DT_tests/test_isort_format_BasicPrinter___init___0.py:44:4: E1101: Instance of 'BasicPrinter' has no 'print_success' member (no-member)
isort/Test4DT_tests/test_isort_format_BasicPrinter___init___0.py:50:4: E1101: Instance of 'BasicPrinter' has no 'print_success' member (no-member)


"""
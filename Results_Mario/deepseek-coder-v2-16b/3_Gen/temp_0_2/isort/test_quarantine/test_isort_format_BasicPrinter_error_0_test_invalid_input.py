
import pytest
from io import StringIO
from isort.format import BasicPrinter

@pytest.fixture
def setup_printer():
    return BasicPrinter('ERROR: {error} - {message}', 'SUCCESS: {success} - {message}')

def test_print_success(setup_printer):
    output = StringIO()
    printer = setup_printer
    printer.output = output
    message = "Hello, world!"
    printer.success(message)
    assert output.getvalue().strip() == f"SUCCESS: {message}"

def test_print_error(setup_printer):
    error_output = StringIO()
    success_output = StringIO()
    printer = setup_printer
    printer.output = success_output  # Errors should go to stdout by default
    printer.error_message = 'ERROR: {error} - {message}'
    message = "Something went wrong"
    printer.error(message)
    assert error_output.getvalue().strip() == f"ERROR: {message}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

isort/Test4DT_tests/test_isort_format_BasicPrinter_error_0_test_invalid_input.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_print_success ______________________________

setup_printer = <isort.format.BasicPrinter object at 0x7f3c3e8fff50>

    def test_print_success(setup_printer):
        output = StringIO()
        printer = setup_printer
        printer.output = output
        message = "Hello, world!"
        printer.success(message)
>       assert output.getvalue().strip() == f"SUCCESS: {message}"
E       AssertionError: assert 'SUCCESS: SUC...Hello, world!' == 'SUCCESS: Hello, world!'
E         
E         - SUCCESS: Hello, world!
E         + SUCCESS: SUCCESS - Hello, world!
E         ?          ++++++++++

isort/Test4DT_tests/test_isort_format_BasicPrinter_error_0_test_invalid_input.py:16: AssertionError
_______________________________ test_print_error _______________________________

setup_printer = <isort.format.BasicPrinter object at 0x7f3c3e3e3950>

    def test_print_error(setup_printer):
        error_output = StringIO()
        success_output = StringIO()
        printer = setup_printer
        printer.output = success_output  # Errors should go to stdout by default
        printer.error_message = 'ERROR: {error} - {message}'
        message = "Something went wrong"
        printer.error(message)
>       assert error_output.getvalue().strip() == f"ERROR: {message}"
E       AssertionError: assert '' == 'ERROR: Something went wrong'
E         
E         - ERROR: Something went wrong

isort/Test4DT_tests/test_isort_format_BasicPrinter_error_0_test_invalid_input.py:26: AssertionError
----------------------------- Captured stderr call -----------------------------
ERROR: ERROR - Something went wrong
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_format_BasicPrinter_error_0_test_invalid_input.py::test_print_success
FAILED isort/Test4DT_tests/test_isort_format_BasicPrinter_error_0_test_invalid_input.py::test_print_error
============================== 2 failed in 0.11s ===============================
"""
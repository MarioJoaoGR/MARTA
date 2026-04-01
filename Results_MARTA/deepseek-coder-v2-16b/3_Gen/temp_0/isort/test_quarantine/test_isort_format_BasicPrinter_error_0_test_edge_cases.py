
from io import StringIO
from unittest.mock import patch
import pytest
from isort.format import BasicPrinter

@pytest.fixture
def printer():
    return BasicPrinter(error='ERROR', success='SUCCESS')

def test_print_success(printer):
    output = StringIO()
    with patch('sys.stdout', new=output):
        printer.print_success('Hello, world!')
    assert output.getvalue().strip() == 'SUCCESS: Hello, world!'

def test_print_error(printer):
    error_output = StringIO()
    with patch('sys.stderr', new=error_output):
        printer.print_error('Something went wrong.')
    assert error_output.getvalue().strip() == 'ERROR: Something went wrong.'

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

isort/Test4DT_tests/test_isort_format_BasicPrinter_error_0_test_edge_cases.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_print_success ______________________________

printer = <isort.format.BasicPrinter object at 0x7fc118f7c590>

    def test_print_success(printer):
        output = StringIO()
        with patch('sys.stdout', new=output):
>           printer.print_success('Hello, world!')
E           AttributeError: 'BasicPrinter' object has no attribute 'print_success'

isort/Test4DT_tests/test_isort_format_BasicPrinter_error_0_test_edge_cases.py:14: AttributeError
_______________________________ test_print_error _______________________________

printer = <isort.format.BasicPrinter object at 0x7fc118cd4d50>

    def test_print_error(printer):
        error_output = StringIO()
        with patch('sys.stderr', new=error_output):
>           printer.print_error('Something went wrong.')
E           AttributeError: 'BasicPrinter' object has no attribute 'print_error'

isort/Test4DT_tests/test_isort_format_BasicPrinter_error_0_test_edge_cases.py:20: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_format_BasicPrinter_error_0_test_edge_cases.py::test_print_success
FAILED isort/Test4DT_tests/test_isort_format_BasicPrinter_error_0_test_edge_cases.py::test_print_error
============================== 2 failed in 0.13s ===============================
"""
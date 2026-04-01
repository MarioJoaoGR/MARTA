
import sys
from unittest.mock import patch, MagicMock
from isort.format import BasicPrinter

def test_print_success():
    printer = BasicPrinter(error='ERROR', success='SUCCESS')
    with patch('sys.stdout', new=MagicMock()) as mock_stdout:
        printer.success("Everything is fine!")
        assert mock_stdout.write.called

def test_print_error():
    printer = BasicPrinter(error='ERROR', success='SUCCESS')
    with patch('sys.stdout', new=MagicMock()) as mock_stdout:
        printer.print_error("Something went wrong.")
        assert mock_stdout.write.called

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_format_BasicPrinter_success_0_test_invalid_input
isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0_test_invalid_input.py:15:8: E1101: Instance of 'BasicPrinter' has no 'print_error' member (no-member)


"""
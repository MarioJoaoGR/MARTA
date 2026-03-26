
from unittest.mock import patch, MagicMock
import sys
from isort.format import BasicPrinter

def test_print_success():
    printer = BasicPrinter(error='ERROR', success='SUCCESS')
    with patch('sys.stdout', new=MagicMock()) as mock_stdout:
        printer.print_success("Hello, world!")
        assert mock_stdout.write.called
        assert mock_stdout.write.call_args[0][0] == "SUCCESS: Hello, world!\n"

def test_print_error():
    printer = BasicPrinter(error='ERROR', success='SUCCESS')
    with patch('sys.stderr', new=MagicMock()) as mock_stderr:
        printer.print_error("Something went wrong.")
        assert mock_stderr.write.called
        assert mock_stderr.write.call_args[0][0] == "ERROR: Something went wrong.\n"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_format_BasicPrinter_error_0_test_edge_case
isort/Test4DT_tests/test_isort_format_BasicPrinter_error_0_test_edge_case.py:9:8: E1101: Instance of 'BasicPrinter' has no 'print_success' member (no-member)
isort/Test4DT_tests/test_isort_format_BasicPrinter_error_0_test_edge_case.py:16:8: E1101: Instance of 'BasicPrinter' has no 'print_error' member (no-member)


"""

import sys
from io import StringIO
import pytest
from unittest.mock import patch
from your_module_name import BasicPrinter  # Replace 'your_module_name' with the actual module name where BasicPrinter is defined

@pytest.fixture
def setup():
    error_message = "Error occurred"
    success_message = "Operation succeeded"
    output = StringIO()
    printer = BasicPrinter(error=error_message, success=success_message, output=output)
    return printer, output

@pytest.mark.parametrize("test_input, expected", [
    ("The operation was successful!", "Operation succeeded"),
    ("Another successful operation.", "Operation succeeded")
])
def test_valid_input(setup, test_input, expected):
    printer, output = setup
    with patch('sys.stdout', new=output):
        printer.print_success(test_input)
        assert output.getvalue().strip() == f"SUCCESS: {expected}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_format_BasicPrinter_diff_line_0_test_valid_input
isort/Test4DT_tests/test_isort_format_BasicPrinter_diff_line_0_test_valid_input.py:6:0: E0401: Unable to import 'your_module_name' (import-error)


"""
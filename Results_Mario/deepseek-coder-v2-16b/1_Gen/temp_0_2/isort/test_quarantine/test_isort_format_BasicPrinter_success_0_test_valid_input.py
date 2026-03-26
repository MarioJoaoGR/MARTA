
from unittest.mock import patch
import sys
from your_module_name import BasicPrinter  # Replace 'your_module_name' with the actual module name where BasicPrinter is defined

def test_valid_input():
    error_message = "An error occurred"
    success_message = "Operation successful"
    
    with patch('sys.stdout', new=StringIO()) as mock_stdout:
        printer = BasicPrinter(error=error_message, success=success_message)
        printer.print_success("Everything is fine!")
        assert mock_stdout.getvalue().strip() == "SUCCESS: Everything is fine!"
        
        # Reset the mock output
        mock_stdout.seek(0)
        mock_stdout.truncate(0)
        
        printer.print_error("Something went wrong")
        assert mock_stdout.getvalue().strip() == "ERROR: Something went wrong"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_format_BasicPrinter_success_0_test_valid_input
isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0_test_valid_input.py:4:0: E0401: Unable to import 'your_module_name' (import-error)
isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0_test_valid_input.py:10:33: E0602: Undefined variable 'StringIO' (undefined-variable)


"""
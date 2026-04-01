
import pytest
from isort.config import Config  # Corrected import from 'isort.config'
from unittest.mock import MagicMock  # Importing mock library

def test_print_hard_fail():
    config = Config()
    message = "Test error message"
    offending_file = "test_file.py"
    
    # Mock the terminal printer to capture output
    mock_printer = MagicMock()
    def create_terminal_printer_mock(color, error, success):
        return mock_printer
    
    with pytest.raises(SystemExit):  # Expecting a hard failure which causes SystemExit
        from isort.main import _print_hard_fail  # Import the function to be tested
        
        # Replace create_terminal_printer with our mock
        original_create_terminal_printer = Config.create_terminal_printer
        Config.create_terminal_printer = create_terminal_printer_mock
        
        _print_hard_fail(config, offending_file, message)  # Call the function to be tested
        
    assert mock_printer.error.call_count == 1  # Check if error method was called with the correct message
    assert mock_printer.error.call_args[0][0] == (
        f"Unrecoverable exception thrown when parsing {offending_file}! "
        "This should NEVER happen.\n"
        "If encountered, please open an issue: https://github.com/PyCQA/isort/issues/new"
    )  # Check if the error message is correct
    
    # Restore original create_terminal_printer function
    Config.create_terminal_printer = original_create_terminal_printer

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_main__print_hard_fail_1_test_edge_cases
isort/Test4DT_tests/test_isort_main__print_hard_fail_1_test_edge_cases.py:3:0: E0401: Unable to import 'isort.config' (import-error)
isort/Test4DT_tests/test_isort_main__print_hard_fail_1_test_edge_cases.py:3:0: E0611: No name 'config' in module 'isort' (no-name-in-module)


"""
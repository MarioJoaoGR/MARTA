
import pytest
from isort.main import _print_hard_fail  # Correctly importing from 'isort.main'
from isort.config import Config  # Importing Config from 'isort.config'
from unittest.mock import MagicMock  # Mocking the terminal printer for testing

def test_valid_inputs():
    config = Config()
    config.color_output = False
    config.format_error = lambda x: print(f"Error: {x}")
    config.format_success = lambda x: print(f"Success: {x}")
    
    # Mocking the terminal printer for testing
    mock_printer = MagicMock()
    
    # Test with a specific message about an offending file
    _print_hard_fail(config, "example.py", "Critical failure occurred!")
    assert mock_printer.error.call_args[0][0] == "Error: Critical failure occurred!"
    
    # Reset the mock for the next test
    mock_printer.reset_mock()
    
    # Test with a custom error message without specifying an offending file
    _print_hard_fail(config, None, "Another critical issue!")
    assert mock_printer.error.call_args[0][0] == "Error: Another critical issue!"
    
    # Reset the mock for the next test
    mock_printer.reset_mock()
    
    # Test with the default constructed message based on the offending file
    _print_hard_fail(config)
    assert mock_printer.error.call_args[0][0] == "Error: Unrecoverable exception thrown when parsing ! This should NEVER happen.\nIf encountered, please open an issue: https://github.com/PyCQA/isort/issues/new"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_main__print_hard_fail_1_test_valid_inputs
isort/Test4DT_tests/test_isort_main__print_hard_fail_1_test_valid_inputs.py:4:0: E0401: Unable to import 'isort.config' (import-error)
isort/Test4DT_tests/test_isort_main__print_hard_fail_1_test_valid_inputs.py:4:0: E0611: No name 'config' in module 'isort' (no-name-in-module)


"""
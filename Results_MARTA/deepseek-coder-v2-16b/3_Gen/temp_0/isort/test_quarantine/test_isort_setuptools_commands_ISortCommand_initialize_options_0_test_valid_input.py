
from setuptools import Command
from isort.setuptools_commands import ISortCommand
from isort_config import DEFAULT_CONFIG
import pytest

@pytest.fixture
def isort_command():
    return ISortCommand()

def test_initialize_options(isort_command):
    # Call the initialize_options method to set up default configurations
    isort_command.initialize_options()
    
    # Check that all default settings are correctly initialized
    for key, value in vars(DEFAULT_CONFIG).items():
        assert getattr(isort_command, key) == value

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_setuptools_commands_ISortCommand_initialize_options_0_test_valid_input
isort/Test4DT_tests/test_isort_setuptools_commands_ISortCommand_initialize_options_0_test_valid_input.py:4:0: E0401: Unable to import 'isort_config' (import-error)
isort/Test4DT_tests/test_isort_setuptools_commands_ISortCommand_initialize_options_0_test_valid_input.py:9:11: E1120: No value for argument 'dist' in constructor call (no-value-for-parameter)


"""

import pytest
from your_module import FormattingPluginDoesNotExist  # Replace 'your_module' with the actual module where FormattingPluginDoesNotExist is defined

def test_valid_input():
    formatter_name = 'exampleFormatter'
    
    try:
        raise FormattingPluginDoesNotExist(formatter_name)
    except FormattingPluginDoesNotExist as e:
        assert str(e) == f"Specified formatting plugin of {formatter_name} does not exist. "

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_exceptions_FormattingPluginDoesNotExist___init___0_test_valid_input
isort/Test4DT_tests/test_isort_exceptions_FormattingPluginDoesNotExist___init___0_test_valid_input.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""
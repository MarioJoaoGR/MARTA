
import pytest
from flutes.log import _get_console_logging_function

# Assuming mock_log_fn is a predefined mock for the logging function
@pytest.fixture(autouse=True)
def mock_log_fn():
    return functools.partial(print, flush=True)

def test_valid_input():
    # Call the function under test
    result = _get_console_logging_function()
    
    # Assert that the returned value is the same as the mocked function
    assert result == mock_log_fn

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_log__get_console_logging_function_0_test_valid_input
flutes/Test4DT_tests/test_flutes_log__get_console_logging_function_0_test_valid_input.py:8:11: E0602: Undefined variable 'functools' (undefined-variable)


"""
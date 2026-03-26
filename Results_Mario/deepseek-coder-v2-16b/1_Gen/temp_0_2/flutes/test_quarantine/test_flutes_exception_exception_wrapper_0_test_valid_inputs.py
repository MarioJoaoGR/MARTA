
import pytest
from flutes.exception import exception_wrapper

# Define a mock handler function for testing
def mock_handler_fn(e, one, two=None):
    pass

# Define a wrapped method that will be tested
@exception_wrapper(mock_handler_fn)
def wrapped_method(one, two, three=None):
    if one == 'error':
        raise ValueError("Test error")
    return {one: two}

# Test valid inputs
def test_valid_inputs():
    # Valid call with no exception
    result = wrapped_method(1, 2)
    assert result == {1: 2}
    
    # Valid call with an error condition that should be caught by the wrapper
    with pytest.raises(ValueError):
        wrapped_method('error', 'value')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests/test_flutes_exception_exception_wrapper_0_test_valid_inputs.py _
flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_0_test_valid_inputs.py:10: in <module>
    @exception_wrapper(mock_handler_fn)
flutes/flutes/exception.py:124: in decorator
    raise ValueError(f"Argument '{name}' matches wrapped method argument, thus "
E   ValueError: Argument 'two' matches wrapped method argument, thus cannot have default values
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_0_test_valid_inputs.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.15s ===============================
"""
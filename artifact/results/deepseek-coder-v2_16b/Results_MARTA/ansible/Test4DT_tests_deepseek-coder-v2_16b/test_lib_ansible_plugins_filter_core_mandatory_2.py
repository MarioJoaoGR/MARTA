
import pytest
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.core import mandatory

# Scenario 1: Test valid input where variable is not undefined
def test_valid_input():
    defined_var = 'I am defined.'
    result = mandatory(defined_var)
    assert result == defined_var, f"Expected {defined_var}, but got {result}"

# Scenario 2: Test scenario where the variable is undefined and no custom message is provided
def test_missing_variable():
    with pytest.raises(AnsibleFilterError) as excinfo:
        undefined_var = None  # Simulate an undefined variable
        mandatory(undefined_var)
    assert str(excinfo.value) == "Mandatory variable 'None' not defined.", f"Expected error message to include 'None', but got {str(excinfo.value)}"

# Scenario 3: Test scenario where the variable is undefined but a custom error message is provided
def test_custom_error_message():
    msg = "Custom error message: 'undefined_var' must be defined."
    with pytest.raises(AnsibleFilterError) as excinfo:
        undefined_var = None  # Simulate an undefined variable
        mandatory(undefined_var, msg=msg)
    assert str(excinfo.value) == msg, f"Expected error message to be '{msg}', but got {str(excinfo.value)}"

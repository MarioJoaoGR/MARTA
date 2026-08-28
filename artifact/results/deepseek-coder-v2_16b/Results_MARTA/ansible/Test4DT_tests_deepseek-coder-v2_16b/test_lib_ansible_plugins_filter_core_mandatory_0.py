
import pytest
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.core import mandatory
from jinja2.runtime import Undefined


def test_defined_variable():
    defined_var = "I am defined."
    result = mandatory(defined_var)
    assert result == defined_var, f"Expected the value of a defined variable to be returned, but got {result}"

def test_missing_variable_with_custom_message():
    undefined_var = Undefined()
    custom_msg = "Custom error message: 'undefined_var' must be defined."
    with pytest.raises(AnsibleFilterError) as exc_info:
        mandatory(undefined_var, msg=custom_msg)
    assert str(exc_info.value) == custom_msg, f"Expected error message to include the custom message, but got {str(exc_info.value)}"
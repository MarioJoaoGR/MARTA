
import pytest
from jinja2.runtime import Undefined
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.core import mandatory

# Test cases for the mandatory function
def test_mandatory_undefined_without_msg():
    undefined_var = Undefined()
    with pytest.raises(AnsibleFilterError) as excinfo:
        mandatory(undefined_var)
    assert "Mandatory variable not defined." in str(excinfo.value)

def test_mandatory_undefined_with_custom_msg():
    undefined_var = Undefined()
    custom_msg = "Custom message for undefined variable"
    with pytest.raises(AnsibleFilterError) as excinfo:
        mandatory(undefined_var, msg=custom_msg)
    assert custom_msg in str(excinfo.value)

def test_mandatory_defined():
    defined_var = "some value"
    result = mandatory(defined_var)
    assert result == defined_var

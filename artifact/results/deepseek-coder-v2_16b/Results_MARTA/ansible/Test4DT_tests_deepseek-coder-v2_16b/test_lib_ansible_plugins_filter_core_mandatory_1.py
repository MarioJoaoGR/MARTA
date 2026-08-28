
import pytest
from ansible.errors import AnsibleFilterError
from jinja2.runtime import Undefined
from ansible.plugins.filter.core import mandatory



def test_defined_variable():
    defined_var = "I am defined."
    result = mandatory(defined_var)
    assert result == defined_var
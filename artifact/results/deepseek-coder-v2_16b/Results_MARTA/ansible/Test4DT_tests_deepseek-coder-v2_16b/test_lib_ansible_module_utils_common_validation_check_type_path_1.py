
import pytest
from ansible.module_utils.common.validation import check_type_str, check_type_path
import os



def test_valid_string_input():
    value = "~/mydir"
    expected_output = os.path.expanduser(os.path.expandvars("~/mydir"))
    assert check_type_path(value) == expected_output

def test_environment_variable_input():
    value = "/var/%USERNAME%"
    expected_output = os.path.expanduser(os.path.expandvars("/var/%USERNAME%"))
    assert check_type_path(value) == expected_output
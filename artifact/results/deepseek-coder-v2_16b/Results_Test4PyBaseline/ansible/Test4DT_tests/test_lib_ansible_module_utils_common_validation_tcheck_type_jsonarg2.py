
# Module: ansible.module_utils.common.validation
from ansible.module_utils.common.validation import check_type_jsonarg
import pytest
import json

# Test cases for check_type_jsonarg function
def test_check_type_jsonarg_string():
    assert check_type_jsonarg("example") == "example"
    assert check_type_jsonarg(" example ") == "example"

def test_check_type_jsonarg_text_type():
    # Assuming text_type is a type alias for str in Python 3, and binary_type does not exist in Python 3
    value = "example"
    assert check_type_jsonarg(value) == value.strip()

def test_check_type_jsonarg_list():
    value = [1, 2, 3]
    expected = json.dumps(value)
    assert check_type_jsonarg(value) == expected

def test_check_type_jsonarg_tuple():
    value = (1, 2, 3)
    expected = json.dumps(list(value))
    assert check_type_jsonarg(value) == expected

def test_check_type_jsonarg_dict():
    value = {"key": "value"}
    expected = json.dumps(value)
    assert check_type_jsonarg(value) == expected

def test_check_type_jsonarg_unsupported_type():
    with pytest.raises(TypeError):
        check_type_jsonarg(None)

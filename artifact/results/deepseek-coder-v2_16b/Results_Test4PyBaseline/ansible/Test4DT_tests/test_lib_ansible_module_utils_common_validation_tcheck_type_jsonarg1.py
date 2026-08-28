
# Module: ansible.module_utils.common.validation
from ansible.module_utils.common.validation import check_type_jsonarg
import pytest
import json

# Test cases for check_type_jsonarg function
def test_check_type_jsonarg_string():
    assert check_type_jsonarg("example") == "example"
    assert check_type_jsonarg(" example ") == "example"

@pytest.mark.xfail(reason="Expected to raise TypeError due to leading/trailing spaces")
def test_check_type_jsonarg_stripped_spaces():
    with pytest.raises(TypeError):
        check_type_jsonarg(" example ")

def test_check_type_jsonarg_list():
    assert check_type_jsonarg([1, 2, 3]) == json.dumps([1, 2, 3])

def test_check_type_jsonarg_tuple():
    assert check_type_jsonarg((1, 2, 3)) == json.dumps([1, 2, 3])

def test_check_type_jsonarg_dict():
    assert check_type_jsonarg({"key": "value"}) == json.dumps({"key": "value"})

def test_check_type_jsonarg_unsupported_type():
    with pytest.raises(TypeError):
        check_type_jsonarg(None)

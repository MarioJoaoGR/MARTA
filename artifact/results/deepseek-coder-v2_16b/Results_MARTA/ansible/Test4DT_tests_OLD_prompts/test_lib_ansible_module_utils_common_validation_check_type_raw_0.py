
import pytest
from ansible.module_utils.common.validation import check_type_raw

def test_valid_input():
    assert check_type_raw(42) == 42
    assert check_type_raw("hello") == "hello"
    assert check_type_raw([1, 2, 3]) == [1, 2, 3]
    assert check_type_raw({"key": "value"}) == {"key": "value"}
    assert check_type_raw(None) is None

def test_invalid_inputs():
    with pytest.raises(TypeError):
        check_type_raw()  # Missing argument
    with pytest.raises(TypeError):
        check_type_raw(1, "extra")  # Too many arguments

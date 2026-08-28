
import pytest
from ctypes import *
from ansible.module_utils.compat.selinux import _to_char_p

# Test valid string input
def test_valid_string_input():
    converter = _to_char_p()
    str_value = "Hello, World!"
    c_str_value = converter.from_param(str_value)
    assert isinstance(c_str_value, bytes)
    assert c_str_value == b'Hello, World!'

# Test None input
def test_none_input():
    converter = _to_char_p()
    str_value = None
    c_str_value = converter.from_param(str_value)
    assert c_str_value is None

# Test invalid type input
def test_invalid_type_input():
    converter = _to_char_p()
    with pytest.raises(TypeError):
        str_value = 12345
        converter.from_param(str_value)

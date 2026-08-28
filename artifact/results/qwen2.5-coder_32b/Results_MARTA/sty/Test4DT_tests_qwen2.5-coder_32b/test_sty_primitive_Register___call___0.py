
import pytest
from sty.primitive import Register



def test_valid_input_single_integer():
    register = Register()
    result = register(42)
    assert result == 42

def test_valid_input_rgb_values():
    register = Register()
    result = register(102, 49, 42)
    assert result == (102, 49, 42)

def test_muted_register_single_integer():
    register = Register()
    register.is_muted = True
    result = register(42)
    assert result == ""

def test_muted_register_rgb_values():
    register = Register()
    register.is_muted = True
    result = register(102, 49, 42)
    assert result == ""

def test_custom_eightbit_call():
    register = Register()
    register.eightbit_call = lambda x: f"8-bit color code: {x}"
    result = register(42)
    assert result == "8-bit color code: 42"

def test_custom_rgb_call():
    register = Register()
    register.rgb_call = lambda r, g, b: f"RGB color: ({r}, {g}, {b})"
    result = register(102, 49, 42)
    assert result == "RGB color: (102, 49, 42)"

def test_named_attribute():
    register = Register()
    register.red = "some_value"
    result = register('red')
    assert result == "some_value"

def test_invalid_input_string_not_attribute():
    register = Register()
    with pytest.raises(AttributeError):
        register('non_existent_attribute')
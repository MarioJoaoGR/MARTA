
import pytest
from sty.primitive import Register, Style



def test_register_setattr_with_non_style_value():
    register = Register()
    value = "some_string"
    register.some_attribute = value
    assert register.some_attribute == value

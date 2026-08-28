
import pytest
from sty.primitive import Register

def test_mute_happy_path():
    my_register = Register()
    assert not my_register.is_muted
    my_register.mute()
    assert my_register.is_muted

def test_mute_with_no_styles():
    my_register = Register()
    my_register.renderfuncs = {'example': lambda x: x}
    assert not my_register.is_muted
    my_register.mute()
    assert my_register.is_muted

def test_mute_with_invalid_attributes():
    my_register = Register()
    my_register.invalid_attr = 'not a style'
    assert not my_register.is_muted
    my_register.mute()
    assert my_register.is_muted


import pytest
from sty.primitive import Register

def test_register_init():
    register = Register()
    assert isinstance(register, Register)
    assert register.renderfuncs == {}
    assert not register.is_muted
    assert register.eightbit_call("test") == "test"
    assert register.rgb_call(255, 0, 0) == (255, 0, 0)

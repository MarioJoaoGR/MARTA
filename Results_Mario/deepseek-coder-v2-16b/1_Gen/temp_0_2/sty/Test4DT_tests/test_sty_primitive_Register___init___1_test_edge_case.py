
from sty import Register
import pytest

def test_Register_init():
    reg = Register()
    assert isinstance(reg.renderfuncs, dict)
    assert reg.renderfuncs == {}
    assert not reg.is_muted
    assert callable(reg.eightbit_call)
    assert reg.eightbit_call(100) == 100
    assert callable(reg.rgb_call)
    r, g, b = reg.rgb_call(50, 60, 70)
    assert (r, g, b) == (50, 60, 70)

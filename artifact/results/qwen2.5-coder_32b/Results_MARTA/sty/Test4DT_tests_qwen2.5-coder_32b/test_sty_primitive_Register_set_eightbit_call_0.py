
import pytest
from sty.primitive import Register, RenderType

class ColorRender(RenderType):
    def render(self, value):
        return f"\033[38;5;{value}m"

def test_set_eightbit_call_valid():
    register = Register()
    register.renderfuncs[ColorRender] = lambda x: f"rendered_{x}"
    register.set_eightbit_call(ColorRender)
    assert register.eightbit_call(144) == "rendered_144"

def test_set_eightbit_call_edge_none():
    register = Register()
    with pytest.raises(KeyError):
        register.set_eightbit_call(None)

def test_set_eightbit_call_invalid_type():
    register = Register()
    with pytest.raises(KeyError):
        register.set_eightbit_call(123)

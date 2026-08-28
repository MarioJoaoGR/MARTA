# Module: sty.primitive
import pytest
from sty.primitive import Register

def test_register_initialization():
    register = Register()
    assert isinstance(register.renderfuncs, dict) and not register.renderfuncs, "renderfuncs should be an empty dictionary"
    assert not register.is_muted, "is_muted should default to False"
    assert callable(register.eightbit_call), "eightbit_call should be a callable"
    assert callable(register.rgb_call), "rgb_call should be a callable"
    assert register.eightbit_call(5) == 5, "eightbit_call should return the input unchanged by default"
    assert register.rgb_call(10, 20, 30) == (10, 20, 30), "rgb_call should return the RGB values as a tuple by default"

def test_set_rgb_call():
    class MockRenderType:
        pass

    def mock_render_func(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    register = Register()
    register.renderfuncs[MockRenderType] = mock_render_func
    register.set_rgb_call(MockRenderType)
    assert register.rgb_call(10, 20, 30) == "\033[38;2;10;20;30m", "rgb_call should be set to the provided render function"

def test_set_rgb_call_with_invalid_rendertype():
    class MockRenderType:
        pass

    register = Register()
    with pytest.raises(KeyError):
        register.set_rgb_call(MockRenderType), "set_rgb_call should raise KeyError if rendertype is not in renderfuncs"


import pytest
from sty.primitive import Register

def test_set_rgb_call_with_valid_rendertype():
    class CustomRgbRenderType:
        def render(self, r, g, b):
            return f"\033[38;2;{r};{g};{b}m"

    my_register = Register()
    my_register.renderfuncs[CustomRgbRenderType] = CustomRgbRenderType().render
    my_register.set_rgb_call(CustomRgbRenderType)
    
    assert my_register.rgb_call(10, 42, 255) == "\033[38;2;10;42;255m"

def test_set_rgb_call_with_none_rendertype():
    my_register = Register()
    with pytest.raises(KeyError):
        my_register.set_rgb_call(None)

def test_initial_rgb_call_behavior():
    my_register = Register()
    
    assert my_register.rgb_call(10, 42, 255) == (10, 42, 255)

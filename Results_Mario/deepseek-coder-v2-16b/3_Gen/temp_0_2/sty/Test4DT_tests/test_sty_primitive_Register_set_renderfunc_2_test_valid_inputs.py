
import pytest
from sty import primitive

class Register:
    def __init__(self):
        self.renderfuncs = {}
        self.is_muted = False
        self.eightbit_call = lambda x: x
        self.rgb_call = lambda r, g, b: (r, g, b)

    def set_renderfunc(self, rendertype: type, func: callable) -> None:
        self.renderfuncs[rendertype] = func
        for attr_name in dir(self):
            val = getattr(self, attr_name)
            if isinstance(val, primitive.Style):
                setattr(self, attr_name, val)

def test_valid_inputs():
    custom_register = Register()
    
    # Mock a render function from sty.primitive
    def mock_render_func(x):
        return x

    # Set the new render function for a valid rendertype
    custom_register.set_renderfunc(type(mock_render_func), mock_render_func)
    
    # Check if the render function is correctly set
    assert len(custom_register.renderfuncs) == 1
    assert custom_register.renderfuncs[type(mock_render_func)] == mock_render_func

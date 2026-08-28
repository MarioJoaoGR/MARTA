
import pytest
from sty.primitive import Style

class Register:
    def __init__(self):
        self.renderfuncs = {}
        self.is_muted = False
        self.eightbit_call = lambda x: x
        self.rgb_call = lambda r, g, b: (r, g, b)

    def unmute(self) -> None:
        """
        Use this method to unmute a previously muted register object.
        """
        self.is_muted = False

        for attr_name in dir(self):
            val = getattr(self, attr_name)
            if isinstance(val, Style):
                setattr(self, attr_name, val)

def test_unmute_happy_path():
    reg = Register()
    reg.is_muted = True
    reg.my_style = Style("test")
    reg.unmute()
    assert not reg.is_muted
    assert reg.my_style == Style("test")

def test_unmute_edge_case_no_styles():
    reg = Register()
    reg.unmute()
    assert not reg.is_muted

def test_unmute_invalid_input():
    reg = Register()
    with pytest.raises(TypeError):
        reg.unmute(123)

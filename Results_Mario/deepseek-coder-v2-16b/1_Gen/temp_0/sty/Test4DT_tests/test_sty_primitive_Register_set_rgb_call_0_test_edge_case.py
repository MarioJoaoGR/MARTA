
import pytest
from unittest.mock import MagicMock
from sty import primitive

class Register:
    def __init__(self):
        self.renderfuncs = {}
        self.is_muted = False
        self.eightbit_call = lambda x: x
        self.rgb_call = lambda r, g, b: (r, g, b)

    def set_rgb_call(self, rendertype: type) -> None:
        func = self.renderfuncs[rendertype]
        self.rgb_call = func

def test_set_rgb_call_with_none():
    reg = Register()
    with pytest.raises(KeyError):
        reg.set_rgb_call(None)


import pytest
from sty import primitive as sp

class Register:
    """
    This is the base Register class. All default registers (fg, bg, ef, rs) are created from this class. You can use it to create your own custom registers.
    
    Attributes:
        renderfuncs (Renderfuncs): A dictionary containing rendering functions for various formats.
        is_muted (bool): Indicates whether the register is muted, meaning its formatting is disabled.
        eightbit_call (lambda): A lambda function to handle 8-bit color values.
        rgb_call (lambda): A lambda function to handle RGB color values.
    
    Methods:
        mute(): Sometimes it is useful to disable the formatting for a register-object. You can do so by invoking this method. When muted, all attributes that are instances of Style will be set to their default values.
    
    Example:
        reg = Register()
        # Create a custom register and use its methods as needed.
        
        # To mute the register:
        reg.mute()
    """
    def __init__(self):
        self.renderfuncs = {}
        self.is_muted = False
        self.eightbit_call = lambda x: x
        self.rgb_call = lambda r, g, b: (r, g, b)

    def mute(self) -> None:
        """
        Sometimes it is useful to disable the formatting for a register-object. You can
        do so by invoking this method.
        """
        self.is_muted = True

        for attr_name in dir(self):
            val = getattr(self, attr_name)
            if isinstance(val, sp.Style):
                setattr(self, attr_name, val.reset())

def test_mute_with_style_attributes():
    reg = Register()
    
    # Check initial state
    assert not reg.is_muted
    for attr_name in dir(reg):
        val = getattr(reg, attr_name)
        if isinstance(val, sp.Style):
            assert val != val.reset()
    
    # Mute the register
    reg.mute()
    
    # Check muted state
    assert reg.is_muted
    
    # Check all style attributes are reset to default values
    for attr_name in dir(reg):
        val = getattr(reg, attr_name)
        if isinstance(val, sp.Style):
            assert val == val.reset()

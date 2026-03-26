
import pytest
from sty import primitive

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
    
    Example usage:
    ```python
    # Creating an instance of Register
    reg = Register()
    
    # Muting the register
    reg.mute()
    print(reg.is_muted)  # Output: True
    
    # Unmuting the register (if needed, though this is not shown in the example)
    reg.is_muted = False
    ```
    
    Implementation Perspective:
    The `mute` method sets the `is_muted` attribute of the Register instance to True and ensures that all attributes of type Style are reset to their default values when muted. This is achieved by iterating over the attributes of the instance and applying the same treatment if they are instances of Style.
    
    Requirement Perspective:
    Mutes the formatting for a register-object by setting its `is_muted` attribute to True and applying the same treatment to all attributes of type Style.

    Parameters:
        None

    Returns:
        None
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
            if isinstance(val, primitive.Style):
                setattr(self, attr_name, val.__class__())

# Test function to test the mute method with valid input
def test_valid_input():
    reg = Register()
    assert not reg.is_muted  # Initial state should be unmuted
    
    # Muting the register
    reg.mute()
    assert reg.is_muted  # After muting, it should be muted
    
    # Checking if all Style attributes are reset to their default values
    for attr_name in dir(reg):
        val = getattr(reg, attr_name)
        if isinstance(val, primitive.Style):
            assert val == reg.__class__().__getattribute__(attr_name)

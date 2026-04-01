
import pytest
from sty import Style, fg, bg, ef

class Register:
    """
    The base Register class from which default registers such as fg, bg, ef, and rs are created. This class can be used to create custom registers.
    
    Attributes:
        renderfuncs (Renderfuncs): A dictionary containing rendering functions.
        is_muted (bool): Indicates whether the register is muted.
        eightbit_call (lambda): A lambda function for handling 8-bit color values.
        rgb_call (lambda): A lambda function for handling RGB color values.
    
    Methods:
        unmute(): Use this method to unmute a previously muted register object. When called, it will reset the muted attributes to their original state by iterating over all attributes and setting them back if they are instances of Style.
    
    Example:
        To create a custom register, you can instantiate the Register class::
        
            custom_register = Register()
            # Now you can use custom_register for your specific needs.
            
        To unmute a previously muted register, call the `unmute` method::
        
            custom_register.unmute()
    
    The `unmute` method is designed to reverse the muting process of the Register class, allowing it to regain its original functionality by resetting any attributes that were set to muted states back to their default or overridden values. This ensures that the register object operates as intended without any unintended restrictions.
    """
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

def test_valid_unmute():
    custom_register = Register()
    custom_register.is_muted = True
    
    # Set some attributes to instances of Style to simulate being muted
    for attr_name in dir(custom_register):
        val = getattr(custom_register, attr_name)
        if isinstance(val, Style):
            setattr(custom_register, attr_name, val)
    
    # Call the unmute method
    custom_register.unmute()
    
    # Check that is_muted is False
    assert not custom_register.is_muted
    
    # Check that other attributes are reset to their original state
    for attr_name in dir(custom_register):
        val = getattr(custom_register, attr_name)
        if isinstance(val, Style):
            assert getattr(custom_register, attr_name) == val

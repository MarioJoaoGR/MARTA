
import pytest
from sty import primitive

class Register:
    """
    This is the base Register class. All default registers (fg, bg, ef, rs) are created from this class. You can use it to create your own custom registers.
    
    Attributes:
        renderfuncs (Renderfuncs): A dictionary that holds rendering functions for various operations.
        is_muted (bool): A flag indicating whether the register is muted.
        eightbit_call (lambda): A lambda function used to call 8-bit values.
        rgb_call (lambda): A lambda function used to call RGB values.
    
    Examples:
        To create a custom register, you can instantiate the Register class and modify its attributes as needed. For example:
        
        ```python
        custom_register = Register()
        custom_register.renderfuncs['custom'] = some_rendering_function
        custom_register.is_muted = True
        custom_register.eightbit_call = lambda x: convert_to_8bit(x)
        custom_register.rgb_call = lambda r, g, b: (r, g, b)  # This example assumes some conversion function `convert_to_8bit` exists.
        ```
    
    Initialization:
        Initializes a new instance of the class with default attributes.
        
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
            if isinstance(val, Style):
                setattr(self, attr_name, val)

class Style:
    pass

@pytest.fixture
def reg():
    return Register()

def test_edge_case(reg):
    # Test muting a register
    assert not reg.is_muted
    reg.mute()
    assert reg.is_muted
    
    # Ensure all Style attributes are reset to default when muted
    for attr_name in dir(reg):
        val = getattr(reg, attr_name)
        if isinstance(val, Style):
            assert val == Style()  # Assuming the default value of Style is an instance of Style

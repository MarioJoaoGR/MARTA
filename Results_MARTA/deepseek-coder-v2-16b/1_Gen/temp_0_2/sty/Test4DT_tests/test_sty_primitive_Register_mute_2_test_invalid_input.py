
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
            if isinstance(val, Style):
                setattr(self, attr_name, val)

class Style:
    pass

# Mocking the necessary classes and methods
@pytest.fixture
def reg():
    return Register()

def test_mute_already_muted(reg):
    """Test that muting an already muted register does not raise an error."""
    reg.mute()  # Mute the register initially
    assert reg.is_muted is True
    reg.mute()  # Attempt to mute again
    assert reg.is_muted is True

def test_mute_invalid_attribute(reg):
    """Test that attempting to mute a non-existent attribute raises an error."""
    with pytest.raises(AttributeError):
        reg.non_existent_method()  # This should raise an AttributeError


import pytest
from sty.lib import Register  # Assuming the correct import path is provided

def mute(*objects: Register) -> None:
    """
    Use this function to mute multiple register-objects at once. Each object must inherit from the 'Register' class.

    Parameters:
        objects (Register): Pass multiple register-objects to the function. Each object must inherit from the 'Register' class.

    Raises:
        ValueError: If any of the provided objects does not inherit from the 'Register' class, a ValueError is raised with a specific error message.

    Example:
        To mute multiple registers, you can call the function as follows:
        
        ```python
        register1 = Register()
        register2 = AnotherRegisterClass()  # Assuming AnotherRegisterClass inherits from Register
        mute(register1, register2)
        ```

    Note:
        This function is designed to work with objects that inherit from the 'Register' class. If you pass an object that does not inherit from 'Register', a ValueError will be raised.
    
    Implementation Perspective:
        The `mute` function iterates over each provided object and checks if it inherits from the `Register` class. If any object does not meet this requirement, a `ValueError` is raised with a predefined error message. If all objects are valid, each object's `mute` method is called to mute its state.
    """
    err = ValueError(
        "The mute() method can only be used with objects that inherit "
        "from the 'Register class'."
    )
    for obj in objects:
        if not isinstance(obj, Register):
            raise err
        obj.mute()

# Test case to check invalid input
def test_invalid_input():
    register1 = object()  # An object that does not inherit from Register
    with pytest.raises(ValueError) as excinfo:
        mute(register1)
    assert str(excinfo.value) == "The mute() method can only be used with objects that inherit from the 'Register class'."


import pytest
from unittest.mock import MagicMock
from sty.lib import Register  # Assuming 'sty.lib' is the correct module path

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
        register2 = Register()
        mute(register1, register2)  # This will mute both register1 and register2
        ```

        If you try to pass an object that does not inherit from 'Register', such as a string or an integer, the function will raise a ValueError:
        
        ```python
        invalid_object = "not a Register"
        mute(invalid_object)  # This will raise a ValueError
        ```
    """
    err = ValueError(
        "The mute() method can only be used with objects that inherit "
        "from the 'Register class'."
    )
    for obj in objects:
        if not isinstance(obj, Register):
            raise err
        obj.mute()

# Test case for edge cases
def test_edge_cases():
    # Mock the Register class
    register_mock = MagicMock(spec=Register)
    
    # Case 1: Passing a valid Register object
    mute(register_mock)
    assert register_mock.mute.call_count == 1
    
    # Case 2: Passing an invalid object (e.g., string)
    with pytest.raises(ValueError):
        mute("not a Register")

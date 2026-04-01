
import pytest
from sty.lib import Register

def unmute(*objects: Register) -> None:
    """
    Use this function to unmute multiple register-objects at once. Each object must inherit from the 'Register' class.

    Parameters:
        objects (Register): Pass multiple register-objects to the function. Each object must inherit from the 'Register' class.

    Raises:
        ValueError: If any of the provided objects does not inherit from the 'Register' class, a ValueError is raised with a specific error message.

    Example:
        To unmute multiple register-objects, you can call the function as follows:
        
        ```python
        obj1 = Register()
        obj2 = AnotherRegisterSubclass()  # Ensure this subclass implements the 'unmute' method
        unmute(obj1, obj2)
        ```
    """
    err = ValueError(
        "The unmute() method can only be used with objects that inherit "
        "from the 'Register class'."
    )
    for obj in objects:
        if not isinstance(obj, Register):
            raise err
        obj.unmute()

def test_edge_case():
    # Test with None inputs to check error handling
    with pytest.raises(ValueError) as excinfo:
        unmute(None, Register())
    assert str(excinfo.value) == "The unmute() method can only be used with objects that inherit from the 'Register class'."

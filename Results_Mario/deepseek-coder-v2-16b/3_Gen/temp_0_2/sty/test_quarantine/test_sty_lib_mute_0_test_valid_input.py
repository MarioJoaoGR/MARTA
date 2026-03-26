
from unittest.mock import patch
import pytest
from sty.lib import Register

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

def test_valid_input():
    register1 = Register()
    register2 = Register()
    
    with patch('builtins.print') as mock_print:
        mute(register1, register2)
        assert register1.muted == True
        assert register2.muted == True
        mock_print.assert_called_with("The mute() method can only be used with objects that inherit from the 'Register class'.")

    # Test raising ValueError for invalid input
    invalid_object = "not a Register"
    with pytest.raises(ValueError):
        mute(invalid_object)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_lib_mute_0_test_valid_input
sty/Test4DT_tests/test_sty_lib_mute_0_test_valid_input.py:47:15: E1101: Instance of 'Register' has no 'muted' member; maybe 'mute'? (no-member)
sty/Test4DT_tests/test_sty_lib_mute_0_test_valid_input.py:48:15: E1101: Instance of 'Register' has no 'muted' member; maybe 'mute'? (no-member)


"""
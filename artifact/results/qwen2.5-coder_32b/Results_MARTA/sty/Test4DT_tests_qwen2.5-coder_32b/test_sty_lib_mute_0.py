
import pytest

# Define a simple Register class for demonstration purposes
class Register:
    def __init__(self):
        self.is_muted = False

    def mute(self):
        self.is_muted = True

# Define subclasses of Register
class MyRegister(Register):
    pass

class AnotherRegister(Register):
    pass

class NonRegisterClass:
    pass

def mute(*objects: Register) -> None:
    """
    Use this function to mute multiple register-objects at once.

    :param objects: Pass multiple register-objects to the function.
    """
    err = ValueError(
        "The mute() method can only be used with objects that inherit "
        "from the 'Register class'."
    )
    for obj in objects:
        if not isinstance(obj, Register):
            raise err
        obj.mute()

# Test file

def test_valid_case():
    reg1 = MyRegister()
    reg2 = AnotherRegister()
    mute(reg1, reg2)
    assert reg1.is_muted is True
    assert reg2.is_muted is True

def test_edge_cases():
    with pytest.raises(ValueError):
        mute(None)
    
    with pytest.raises(ValueError):
        mute([])
    
    reg1 = MyRegister()
    mute(reg1)
    assert reg1.is_muted is True

def test_invalid_case():
    invalid_obj = NonRegisterClass()
    reg1 = MyRegister()
    with pytest.raises(ValueError):
        mute(invalid_obj, reg1)

    # Ensure that valid object is not muted if an exception occurs
    assert reg1.is_muted is False

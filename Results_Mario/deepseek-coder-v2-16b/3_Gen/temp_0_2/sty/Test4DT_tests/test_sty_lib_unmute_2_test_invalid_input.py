
import pytest
from sty.lib import Register, unmute

def test_invalid_input():
    class InvalidRegister:
        pass
    
    with pytest.raises(ValueError) as excinfo:
        obj1 = Register()
        obj2 = InvalidRegister()  # This object does not inherit from Register
        unmute(obj1, obj2)
    
    assert str(excinfo.value) == "The unmute() method can only be used with objects that inherit from the 'Register class'."

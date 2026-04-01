
import pytest
from sty.lib import Register, unmute

def test_invalid_input():
    # Test that an error is raised when passing invalid objects
    class InvalidRegister:
        pass
    
    with pytest.raises(ValueError) as excinfo:
        unmute(InvalidRegister(), Register())
    
    assert str(excinfo.value) == "The unmute() method can only be used with objects that inherit from the 'Register class'."

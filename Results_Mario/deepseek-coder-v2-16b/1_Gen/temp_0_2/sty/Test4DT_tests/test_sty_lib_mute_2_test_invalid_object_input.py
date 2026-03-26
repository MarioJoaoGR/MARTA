
import pytest
from sty.lib import Register, mute

class MockNonRegister: pass

def test_invalid_object_input():
    non_register = MockNonRegister()
    with pytest.raises(ValueError) as excinfo:
        mute(non_register)
    assert str(excinfo.value) == "The mute() method can only be used with objects that inherit from the 'Register class'."

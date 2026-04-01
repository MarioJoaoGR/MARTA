
import pytest
from sty.lib import Register, unmute

class MockNonRegister: pass

def test_invalid_inputs():
    obj1 = MockNonRegister()
    obj2 = MockNonRegister()
    
    with pytest.raises(ValueError) as excinfo:
        unmute(obj1, obj2)
    
    assert str(excinfo.value) == "The unmute() method can only be used with objects that inherit from the 'Register class'."

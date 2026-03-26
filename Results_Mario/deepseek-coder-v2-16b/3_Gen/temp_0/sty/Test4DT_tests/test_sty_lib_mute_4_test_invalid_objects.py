
import pytest
from sty.lib import Register, mute

class MockNonRegister: pass

def test_invalid_objects():
    mock1 = MockNonRegister()
    mock2 = MockNonRegister()
    
    with pytest.raises(ValueError) as excinfo:
        mute(mock1, mock2)
    
    assert str(excinfo.value) == "The mute() method can only be used with objects that inherit from the 'Register class'."

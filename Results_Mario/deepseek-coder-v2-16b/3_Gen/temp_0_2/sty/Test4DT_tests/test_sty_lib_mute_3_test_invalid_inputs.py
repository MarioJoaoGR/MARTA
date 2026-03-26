
import pytest
from sty.lib import Register, mute

class MockNonRegister: pass

def test_invalid_inputs():
    mock_obj = MockNonRegister()
    with pytest.raises(ValueError) as excinfo:
        mute(mock_obj)
    assert str(excinfo.value) == "The mute() method can only be used with objects that inherit from the 'Register class'."

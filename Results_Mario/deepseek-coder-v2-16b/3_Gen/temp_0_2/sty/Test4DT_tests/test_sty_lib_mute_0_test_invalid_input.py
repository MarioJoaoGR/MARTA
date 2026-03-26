
import pytest
from unittest.mock import MagicMock
from sty.lib import Register, mute

class MockNonRegister: pass

def test_invalid_input():
    mock_non_register = MockNonRegister()
    register1 = MagicMock(spec=Register)
    register2 = MagicMock(spec=Register)
    
    with pytest.raises(ValueError, match="The mute\(\) method can only be used with objects that inherit from the 'Register class'."):
        mute(mock_non_register, register1, register2)


import pytest
from sty import Register

def test_valid_input():
    # Arrange
    register = Register()
    
    # Act
    register.mute()
    
    # Assert
    assert register.is_muted == True
    assert isinstance(register.eightbit_call, type(lambda x: x))
    assert isinstance(register.rgb_call, type(lambda r, g, b: (r, g, b)))

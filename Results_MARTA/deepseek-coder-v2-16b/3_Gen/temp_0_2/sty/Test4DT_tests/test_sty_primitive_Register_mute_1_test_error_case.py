
import pytest
from sty import Register

def test_mute():
    # Arrange
    reg = Register()
    
    # Act
    reg.mute()
    
    # Assert
    assert reg.is_muted == True

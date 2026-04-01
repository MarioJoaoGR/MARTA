
import pytest
from sty import primitive  # Assuming 'sty.primitive' is the correct module path

def test_invalid_input():
    reg = primitive.Register()
    
    # Test mute method with invalid input (should not raise an error)
    reg.mute()
    
    # Assert that the register is muted
    assert reg.is_muted == True

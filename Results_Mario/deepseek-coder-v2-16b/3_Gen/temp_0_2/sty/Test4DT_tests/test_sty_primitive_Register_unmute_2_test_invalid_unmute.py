
import pytest
from sty import Register

def test_invalid_unmute():
    # Create a Register instance
    register = Register()
    
    # Ensure the register is muted initially
    assert register.is_muted == False
    
    # Call unmute method (it should not raise an error and does nothing)
    register.unmute()
    
    # Check that the register remains muted after calling unmute
    assert register.is_muted == False

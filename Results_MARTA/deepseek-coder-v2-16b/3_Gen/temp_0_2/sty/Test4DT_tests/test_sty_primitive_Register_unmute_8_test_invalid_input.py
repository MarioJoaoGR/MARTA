
import pytest
from sty import Register

def test_invalid_input():
    # Create an instance of Register
    register = Register()
    
    # Ensure the register starts as not muted
    assert not register.is_muted, "Register should start as not muted"
    
    # Call unmute method (should do nothing since it's already not muted)
    register.unmute()
    
    # Verify that is_muted remains False after calling unmute
    assert not register.is_muted, "Unmuting a non-muted register should leave it unchanged"


# Import the Register class correctly from the sty.primitive module
from sty.primitive import Register

def test_mute():
    # Create an instance of the Register class
    reg = Register()
    
    # Check that the register is not muted initially
    assert not reg.is_muted, "Register should not be muted initially"
    
    # Mute the register
    reg.mute()
    
    # Check that the register is now muted
    assert reg.is_muted, "Register should be muted after calling mute()"

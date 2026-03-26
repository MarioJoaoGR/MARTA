
# Importing necessary components from the module 'sty.primitive'
from sty import primitive

def test_invalid_input():
    # Create an instance of the Register class
    reg = primitive.Register()
    
    # Attempt to mute the register, which should not raise any errors for invalid input
    reg.mute()
    
    # Check if the register is muted
    assert reg.is_muted == True

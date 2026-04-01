
from sty.primitive import Register

def test_edge_case():
    custom_register = Register()
    assert not custom_register.is_muted  # Ensure the register is initially unmuted
    
    custom_register.unmute()  # Attempt to unmute an already unmuted register
    assert not custom_register.is_muted  # Check that it remains unmuted after attempting to unmute again

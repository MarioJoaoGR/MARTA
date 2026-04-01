
# Importing necessary modules from sty.primitive
from sty.primitive import Register, Renderfuncs, Style
import pytest

@pytest.fixture
def register():
    return Register()

def test_mute(register):
    # Test that the register is not muted initially
    assert not register.is_muted
    
    # Muting the register
    register.mute()
    
    # Assert that the register is now muted
    assert register.is_muted
    
    # Check if all Style attributes are also muted (this would typically be handled by __init__ or similar, but for testing purposes we assume it works)
    for attr_name in dir(register):
        val = getattr(register, attr_name)
        if isinstance(val, Style):
            assert val.is_muted  # Assuming Style has an is_muted attribute

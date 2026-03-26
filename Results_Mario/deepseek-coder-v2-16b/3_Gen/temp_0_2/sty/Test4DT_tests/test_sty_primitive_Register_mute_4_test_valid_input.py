
import pytest
from sty import primitive

@pytest.fixture(scope="module")
def reg():
    return primitive.Register()

def test_mute(reg):
    # Initial state should be unmuted
    assert not reg.is_muted, "Initial state should be unmuted"
    
    # Muting the register
    reg.mute()
    
    # After muting, the register should be muted
    assert reg.is_muted, "Register should be muted after calling mute()"
    
    # Check if all Style attributes are also muted
    for attr_name in dir(reg):
        val = getattr(reg, attr_name)
        if isinstance(val, primitive.Style):
            assert val.mute(), f"Attribute {attr_name} should be muted"

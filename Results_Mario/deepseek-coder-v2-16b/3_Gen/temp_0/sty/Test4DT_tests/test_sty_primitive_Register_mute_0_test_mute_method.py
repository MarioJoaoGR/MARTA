
import pytest
from sty import primitive

@pytest.fixture
def create_register():
    return primitive.Register()

def test_mute_method(create_register):
    reg = create_register
    
    # Ensure that the register is not muted initially
    assert not reg.is_muted
    
    # Mute the register and check if it gets muted
    reg.mute()
    assert reg.is_muted
    
    # Check if all style attributes are reset to their default values
    for attr_name in dir(reg):
        val = getattr(reg, attr_name)
        if isinstance(val, primitive.Style):
            assert val == val.default()

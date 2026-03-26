
# Module: sty.primitive
# test_register.py
from sty.primitive import Register, RenderType
import pytest

@pytest.fixture
def custom_register():
    return Register()

def test_initialization(custom_register):
    assert isinstance(custom_register.renderfuncs, dict)
    assert not custom_register.is_muted
    assert callable(custom_register.eightbit_call)
    assert callable(custom_register.rgb_call)

def test_mute_unmute(custom_register):
    custom_register.mute()
    assert custom_register.is_muted is True
    
    custom_register.unmute()
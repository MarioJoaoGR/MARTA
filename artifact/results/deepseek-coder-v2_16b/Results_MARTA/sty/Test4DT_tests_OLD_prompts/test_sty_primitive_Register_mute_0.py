
import pytest
from sty.primitive import Register, Style

@pytest.fixture
def setup():
    register = Register()
    yield register
    # Teardown if needed

def test_mute_method(setup):
    register = setup
    assert not register.is_muted
    register.mute()
    assert register.is_muted

def test_unmute_method(setup):
    register = setup
    register.mute()
    assert register.is_muted
    register.unmute()
    assert not register.is_muted

def test_mute_with_style_attributes(setup):
    register = setup
    assert not register.is_muted
    register.mute()
    for attr_name in dir(register):
        val = getattr(register, attr_name)
        if isinstance(val, Style):
            assert val.is_muted

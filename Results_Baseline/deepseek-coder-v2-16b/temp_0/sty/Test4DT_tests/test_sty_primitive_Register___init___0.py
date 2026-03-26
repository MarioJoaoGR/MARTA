
# Module: sty.primitive
# test_register.py
from sty.primitive import Register
import pytest

@pytest.fixture
def default_register():
    return Register()

def test_default_register(default_register):
    assert not default_register.is_muted, "Default register should not be muted"

def test_mute_register(default_register):
    default_register.mute()
    assert default_register.is_muted, "Register should be muted after calling mute()"

def test_unmute_register(default_register):
    default_register.mute()
    default_register.unmute()
    assert not default_register.is_muted, "Register should not be muted after calling unmute()"

def test_export_as_dict(default_register):
    dict_repr = default_register.as_dict()
    assert isinstance(dict_repr, dict), "The result of as_dict() should be a dictionary"
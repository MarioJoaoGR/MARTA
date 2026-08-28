
import pytest
from sty.primitive import Register

def test_default_is_muted():
    register = Register()
    assert register.is_muted is False, "Expected is_muted to be False by default"

def test_mute_register():
    register = Register()
    register.mute()
    assert register.is_muted is True, "Expected is_muted to be True after calling mute()"

def test_unmute_register():
    register = Register()
    register.unmute()
    assert register.is_muted is False, "Expected is_muted to be False after calling unmute()"



import pytest
from unittest.mock import patch
from sty.primitive import Register, Style

@pytest.fixture
def setup():
    register = Register()
    yield register

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



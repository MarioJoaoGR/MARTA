
import pytest
from sty.primitive import Register, Style

def test_valid_input():
    custom_register = Register()
    assert not custom_register.is_muted  # Initially muted

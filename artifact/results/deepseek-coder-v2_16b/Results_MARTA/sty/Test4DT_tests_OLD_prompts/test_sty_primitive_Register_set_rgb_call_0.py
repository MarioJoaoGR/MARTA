
import pytest
from unittest.mock import patch
from sty.primitive import Register, RenderType

def test_set_rgb_call():
    custom_register = Register()
    with pytest.raises(KeyError):
        custom_register.set_rgb_call(None)


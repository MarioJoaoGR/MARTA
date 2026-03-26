
import pytest
from sty import Register, Style

def test_invalid_input():
    non_register = None
    with pytest.raises(AttributeError):
        non_register.unmute()

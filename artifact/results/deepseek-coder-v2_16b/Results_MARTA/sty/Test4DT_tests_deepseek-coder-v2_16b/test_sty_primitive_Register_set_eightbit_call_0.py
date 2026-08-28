
import pytest
from sty.primitive import Register



def test_invalid_input():
    register = Register()
    with pytest.raises(KeyError):
        register.set_eightbit_call("invalid_type")
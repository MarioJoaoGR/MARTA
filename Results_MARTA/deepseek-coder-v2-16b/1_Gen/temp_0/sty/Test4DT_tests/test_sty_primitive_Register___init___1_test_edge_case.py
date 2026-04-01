
import pytest
from sty.primitive import Register

@pytest.mark.parametrize("test_input, expected", [
    ({"renderfuncs": {}, "is_muted": False, "eightbit_call": lambda x: x, "rgb_call": lambda r, g, b: (r, g, b)}, {"renderfuncs": {}})
])
def test_sty_primitive_Register___init___(test_input, expected):
    register = Register()
    assert register.renderfuncs == expected["renderfuncs"]

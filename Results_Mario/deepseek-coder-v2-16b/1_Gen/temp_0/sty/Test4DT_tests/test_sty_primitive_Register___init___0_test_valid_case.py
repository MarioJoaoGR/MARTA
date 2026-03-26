
import pytest
from sty import primitive

@pytest.mark.parametrize("valid_case", [{}])  # Assuming valid_case is a dictionary or any other type that can be passed to the Register constructor
def test_valid_case(valid_case):
    register = primitive.Register()
    assert isinstance(register.renderfuncs, dict)
    assert register.is_muted is False
    assert callable(register.eightbit_call)
    assert callable(register.rgb_call)

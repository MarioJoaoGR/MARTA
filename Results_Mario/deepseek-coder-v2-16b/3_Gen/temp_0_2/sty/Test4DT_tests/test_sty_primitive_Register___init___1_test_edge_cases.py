
import pytest
from sty import primitive  # Assuming 'primitive' is the module containing Register class

def test_edge_cases():
    # Test initialization of the Register class
    register = primitive.Register()
    
    # Check default values
    assert isinstance(register.renderfuncs, dict)
    assert register.renderfuncs == {}
    assert not register.is_muted
    assert register.eightbit_call(10) == 10
    assert register.rgb_call(255, 255, 255) == (255, 255, 255)

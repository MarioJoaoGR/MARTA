
import pytest
from sty.primitive import Register

def test_edge_cases():
    custom_register = Register()
    
    # Test None input
    with pytest.raises(TypeError):
        assert custom_register(None)
    
    # Test empty list input
    with pytest.raises(TypeError):
        assert custom_register([])
    
    # Test invalid color code (non-integer for 8-bit call)
    with pytest.raises(AttributeError):
        assert custom_register('invalid')

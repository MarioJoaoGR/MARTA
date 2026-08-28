
import pytest
from sty.primitive import Register

# Test creating a custom register and modifying its attributes
def test_create_custom_register():
    custom_register = Register()
    assert isinstance(custom_register.renderfuncs, dict)
    assert not custom_register.is_muted
    assert callable(custom_register.eightbit_call)
    assert callable(custom_register.rgb_call)
    
    # Modify attributes
    custom_register.is_muted = True
    assert custom_register.is_muted
    
    def some_function():
        pass
    custom_register.renderfuncs['new_func'] = some_function
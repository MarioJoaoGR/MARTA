
import pytest
from copy import deepcopy
from sty.primitive import Register

# Test initialization of the Register class
def test_register_initialization():
    reg = Register()
    assert isinstance(reg.renderfuncs, dict), "Expected renderfuncs to be a dictionary"
    assert not reg.is_muted, "Expected is_muted to be False initially"
    assert callable(reg.eightbit_call) and reg.eightbit_call("test") == "test", "Expected eightbit_call to be a lambda function that returns its input"
    assert callable(reg.rgb_call) and reg.rgb_call(255, 0, 0) == (255, 0, 0), "Expected rgb_call to be a lambda function that returns the RGB values"

# Test setting custom attributes after initialization
def test_register_customization():
    reg = Register()
    reg.is_muted = True
    assert reg.is_muted, "Expected is_muted to be set to True"
    
    # Add a new rendering function
    def some_function(x):
        return f"Custom {x}"
    reg.renderfuncs['new_func'] = some_function
    assert callable(reg.renderfuncs['new_func']), "Expected renderfuncs to contain the custom function"
    
# Test copying a Register instance
def test_register_copy():
    original_reg = Register()
    copied_reg = deepcopy(original_reg)
    
    # Check if the copy is a deepcopy of the original
    assert isinstance(copied_reg, Register), "Expected copied object to be an instance of Register"
    assert copied_reg.renderfuncs == original_reg.renderfuncs, "Expected renderfuncs to be deeply copied"
    assert copied_reg.is_muted == original_reg.is_muted, "Expected is_muted to be deeply copied"
    assert callable(copied_reg.eightbit_call) and copied_reg.eightbit_call("test") == original_reg.eightbit_call("test"), "Expected eightbit_call to be deeply copied"
    assert callable(copied_reg.rgb_call) and copied_reg.rgb_call(255, 0, 0) == original_reg.rgb_call(255, 0, 0), "Expected rgb_call to be deeply copied"

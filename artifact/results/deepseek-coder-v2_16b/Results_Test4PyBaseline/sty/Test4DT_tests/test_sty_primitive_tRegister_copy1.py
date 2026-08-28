
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
    
# Test deepcopy of Register object
def test_register_deepcopy():
    reg = Register()
    copied_reg = deepcopy(reg)
    # Check if the copy is a deep copy by modifying original and checking if copy reflects changes
    assert isinstance(copied_reg, Register), "Expected deepcopy to return an instance of Register"
    assert reg.is_muted == copied_reg.is_muted, "Expected is_muted to be False in the copied object"
    assert reg.renderfuncs == copied_reg.renderfuncs, "Expected renderfuncs to be a shallow copy"
    
    # Modify original and check if it affects the copy
    reg.is_muted = True
    assert reg.is_muted != copied_reg.is_muted, "Expected modification of original object not to affect the copy"
    
    # Add a new function to renderfuncs in the original and check if it is reflected in the copy
    def another_function(x):
        return f"Another {x}"
    reg.renderfuncs['another_func'] = another_function
    assert 'another_func' not in copied_reg.renderfuncs, "Expected addition to original renderfuncs not to affect the copy"
    
# Test deepcopy of a customized Register object
def test_customized_register_deepcopy():
    reg = Register()
    reg.is_muted = True
    def some_function(x):
        return f"Custom {x}"
    reg.renderfuncs['some_func'] = some_function
    
    copied_reg = deepcopy(reg)
    assert isinstance(copied_reg, Register), "Expected deepcopy to return an instance of Register"
    assert reg.is_muted == copied_reg.is_muted, "Expected is_muted to be True in the copied object after modification"
    assert callable(copied_reg.eightbit_call) and copied_reg.eightbit_call("test") == "test", "Expected eightbit_call to remain unchanged in the copy"
    assert callable(copied_reg.rgb_call) and copied_reg.rgb_call(255, 0, 0) == (255, 0, 0), "Expected rgb_call to remain unchanged in the copy"
    
    # Add a new function to renderfuncs in the original and check if it is reflected in the copy
    def another_function(x):
        return f"Another {x}"
    reg.renderfuncs['another_func'] = another_function
    assert 'another_func' not in copied_reg.renderfuncs, "Expected addition to original renderfuncs not to affect the copy"


import pytest
from sty.primitive import Register
from typing import Type, Callable, List, Dict

# Test initialization of the Register class
def test_register_initialization():
    register = Register()
    assert isinstance(register.renderfuncs, dict), "Expected renderfuncs to be a dictionary"
    assert not register.is_muted, "Expected is_muted to be False"

# Test set_renderfunc method with new render type and function
def test_set_renderfunc():
    register = Register()
    rendertype = List[int]  # Example render type
    func = lambda: None      # Example render function
    
    register.set_renderfunc(rendertype, func)
    assert rendertype in register.renderfuncs, f"Expected {rendertype} to be in renderfuncs"
    assert register.renderfuncs[rendertype] == func, "Expected the function to be correctly set"

# Test set_renderfunc method with existing render type and replacing it with a new function
def test_set_renderfunc_replace():
    register = Register()
    rendertype = Dict[str, Callable]  # Existing render type in the example
    func1 = lambda: None              # Initial function for this type
    func2 = lambda x: x + 1          # New function to replace it with
    
    register.set_renderfunc(rendertype, func1)
    assert register.renderfuncs[rendertype] == func1, "Expected the initial function to be in renderfuncs"
    
    register.set_renderfunc(rendertype, func2)
    assert register.renderfuncs[rendertype] == func2, "Expected the new function to replace the old one"

# Test __setattr__ method with Style instance
def test_setattr_with_style():
    class Style: pass  # Placeholder for actual Style class definition
    
    register = Register()
    style = Style()
    
    setattr(register, 'test_attr', style)
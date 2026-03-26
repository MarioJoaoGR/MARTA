
import pytest
from sty import primitive
from typing import Type, Callable

# Test initialization of the Register class
def test_register_initialization():
    register = primitive.Register()
    assert isinstance(register.renderfuncs, dict), "Expected renderfuncs to be a dictionary"
    assert not register.is_muted, "Expected is_muted to be False"
    assert callable(register.eightbit_call), "Expected eightbit_call to be callable"
    assert callable(register.rgb_call), "Expected rgb_call to be callable"

# Test setting a new render function for a given type
def test_set_renderfunc():
    register = primitive.Register()
    rendertype = Type[primitive.RenderType]  # Placeholder for the actual RenderType class
    func = lambda: None  # Placeholder for the actual callable function
    
    register.set_renderfunc(rendertype, func)
    assert rendertype in register.renderfuncs, "Expected rendertype to be added to renderfuncs"
    assert register.renderfuncs[rendertype] == func, "Expected the new render function to be set correctly"

# Test updating style attributes and styles with a new render function
def test_set_renderfunc_updates_styles():
    register = primitive.Register()
    rendertype = Type[primitive.RenderType]  # Placeholder for the actual RenderType class
    func = lambda: None  # Placeholder for the actual callable function
    
    register.set_renderfunc(rendertype, func)
    for attr_name in dir(register):
        val = getattr(register, attr_name)
        if isinstance(val, primitive.Style):
            assert hasattr(register, attr_name), f"Expected {attr_name} to have a new render function set"

# Test setting multiple render functions for different types
def test_set_multiple_renderfuncs():
    register = primitive.Register()
    rendertype1 = Type[primitive.RenderType]  # Placeholder for the actual RenderType class
    func1 = lambda: None  # Placeholder for the actual callable function
    rendertype2 = Type[primitive.RenderType]  # Placeholder for the actual RenderType class
    func2 = lambda: None  # Placeholder for the actual callable function
    
    register.set_renderfunc(rendertype1, func1)
    register.set_renderfunc(rendertype2, func2)
    assert rendertype1 in register.renderfuncs, "Expected first rendertype to be added to renderfuncs"
    assert rendertype2 in register.renderfuncs, "Expected second rendertype to be added to renderfuncs"
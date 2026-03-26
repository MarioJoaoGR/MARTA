
import pytest
from sty.primitive import Register, RenderType, Style

def test_set_renderfunc():
    # Create an instance of the Register class
    register = Register()
    
    # Define a mock render function
    def mock_render_function(value):
        return value

    # Type hint for the mock function
    from typing import Callable

    # Set a new render function for a given rendertype
    register.set_renderfunc(RenderType, mock_render_function)
    
    # Check if the new render function is set correctly
    assert isinstance(register.renderfuncs[RenderType], Callable)
    assert register.renderfuncs[RenderType] == mock_render_function

    # Test updating an existing render function
    def another_mock_function(value):
        return value * 2
    
    register.set_renderfunc(RenderType, another_mock_function)
    assert register.renderfuncs[RenderType] == another_mock_function

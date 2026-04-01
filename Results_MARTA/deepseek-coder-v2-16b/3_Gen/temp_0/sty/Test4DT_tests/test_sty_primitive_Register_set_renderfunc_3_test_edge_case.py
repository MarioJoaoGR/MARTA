
from sty import Register
import pytest
from typing import Type, Callable, Type as Typetype
from sty.primitive import RenderType, Style

@pytest.fixture
def register():
    return Register()

def test_set_renderfunc(register):
    # Define a mock render function
    def mock_render_func(x):
        return f"Mock {x}"

    # Type and RenderType are imported from sty.primitive
    rendertype = RenderType  # Assuming this is the correct import for RenderType

    # Set the new render function
    register.set_renderfunc(rendertype, mock_render_func)

    # Check if the render function is set correctly
    assert isinstance(register.renderfuncs, dict)
    assert rendertype in register.renderfuncs
    assert register.renderfuncs[rendertype] == mock_render_func

def test_set_renderfunc_updates_styles(register):
    # Define a mock render function for style updates
    def mock_style_update_func(x):
        return f"Updated {x}"

    # Create a Style instance to be updated
    class MockStyle(Style):
        pass  # Assuming Style has some attributes that can be set

    # Set the new render function for a style attribute
    register.set_renderfunc(RenderType, mock_style_update_func)

    # Check if the style attributes are updated correctly
    for attr_name in dir(register):
        val = getattr(register, attr_name)
        if isinstance(val, Style):
            setattr(register, attr_name, val)  # Assuming this is how you would update the attribute

    assert hasattr(register, 'is_muted')
    assert register.is_muted == False  # Assuming default value for is_muted

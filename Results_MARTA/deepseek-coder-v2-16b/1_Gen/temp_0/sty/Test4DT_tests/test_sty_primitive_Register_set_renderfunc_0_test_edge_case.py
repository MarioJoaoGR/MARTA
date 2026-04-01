
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

def test_set_renderfunc_update(register):
    # Define a mock render function
    def mock_render_func1(x):
        return f"Mock {x}"

    def mock_render_func2(y):
        return f"New Mock {y}"

    rendertype1 = RenderType  # Assuming this is the correct import for RenderType
    rendertype2 = type('RenderType2', (RenderType,), {})  # Example of a new RenderType

    # Set the first render function
    register.set_renderfunc(rendertype1, mock_render_func1)

    # Set the second render function which should update the existing one
    register.set_renderfunc(rendertype2, mock_render_func2)

    # Check if the render functions are set correctly
    assert isinstance(register.renderfuncs, dict)
    assert rendertype1 in register.renderfuncs
    assert register.renderfuncs[rendertype1] == mock_render_func1
    assert rendertype2 in register.renderfuncs
    assert register.renderfuncs[rendertype2] == mock_render_func2

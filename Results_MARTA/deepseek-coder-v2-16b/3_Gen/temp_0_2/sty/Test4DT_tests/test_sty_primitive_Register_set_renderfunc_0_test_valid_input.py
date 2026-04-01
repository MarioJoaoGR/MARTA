
import pytest
from sty import primitive
from unittest.mock import MagicMock

@pytest.fixture
def register():
    return primitive.Register()

def test_set_renderfunc(register):
    # Create a mock render function
    mock_func = MagicMock()
    
    # Set the render function for a given type
    rendertype = type('RenderType', (object,), {})
    register.set_renderfunc(rendertype, mock_func)
    
    # Check if the render function is set correctly
    assert isinstance(register.renderfuncs, dict)
    assert len(register.renderfuncs) == 1
    assert register.renderfuncs[rendertype] == mock_func

def test_set_renderfunc_updates_style_attributes(register):
    # Create a mock style object
    class MockStyle:
        pass
    
    # Set up the register to have a style attribute
    setattr(register, 'fg', MockStyle())
    
    # Create a mock render function
    mock_func = MagicMock()
    
    # Set the render function for a given type
    rendertype = type('RenderType', (object,), {})
    register.set_renderfunc(rendertype, mock_func)
    
    # Check if the style attributes are updated correctly
    assert isinstance(getattr(register, 'fg'), MockStyle)

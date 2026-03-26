
import pytest
from sty import primitive

@pytest.fixture
def register():
    return primitive.Register()

def test_valid_input(register):
    # Define a mock render function
    def mock_render_func(x):
        return f"Mock {x}"
    
    # Type of the render type to be set
    RenderType = type('RenderType', (object,), {})
    
    # Set the render function for a valid render type
    register.set_renderfunc(RenderType, mock_render_func)
    
    # Check if the render function is correctly set
    assert len(register.renderfuncs) == 1
    assert isinstance(register.renderfuncs[RenderType], type(mock_render_func))

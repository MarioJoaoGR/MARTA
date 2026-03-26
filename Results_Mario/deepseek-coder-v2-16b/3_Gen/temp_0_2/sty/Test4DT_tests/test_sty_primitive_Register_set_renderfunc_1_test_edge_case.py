
import pytest
from sty import primitive

@pytest.fixture
def register():
    return primitive.Register()

def test_set_renderfunc(register):
    # Define a mock render function
    def mock_render_func(arg):
        return arg

    # Set the render function for a given type
    rendertype = type('RenderType', (object,), {})
    register.set_renderfunc(rendertype, mock_render_func)

    # Check if the render function is set correctly
    assert isinstance(register.renderfuncs[rendertype], type(mock_render_func))

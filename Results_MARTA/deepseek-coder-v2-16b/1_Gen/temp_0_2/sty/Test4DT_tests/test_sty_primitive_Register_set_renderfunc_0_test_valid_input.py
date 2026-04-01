
import pytest
from sty import Register, Style

@pytest.fixture
def custom_register():
    return Register()

def test_valid_input(custom_register):
    # Define a mock render function
    def mock_render_func(x):
        return f"Rendered {x}"
    
    # Add the mock render function to the register
    custom_register.set_renderfunc(Style, mock_render_func)
    
    # Check if the mock render function is added correctly
    assert len(custom_register.renderfuncs) == 1
    assert custom_register.renderfuncs[Style] == mock_render_func

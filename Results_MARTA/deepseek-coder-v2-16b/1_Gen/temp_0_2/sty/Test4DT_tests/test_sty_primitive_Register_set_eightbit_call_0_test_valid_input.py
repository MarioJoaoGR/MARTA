
import pytest
from sty import Register, RenderType

def test_valid_input():
    custom_register = Register()
    # Define a mock render function
    def mock_render_func(x):
        return x
    
    # Assign the mock function to a new RenderType in renderfuncs
    class MockRenderType:
        pass
    MockRenderType.name = "mock"
    
    custom_register.renderfuncs[MockRenderType] = mock_render_func
    
    # Set the eightbit_call with the valid MockRenderType
    custom_register.set_eightbit_call(MockRenderType)
    
    # Check if the eightbit_call is set to the mock function
    assert custom_register.eightbit_call == mock_render_func
